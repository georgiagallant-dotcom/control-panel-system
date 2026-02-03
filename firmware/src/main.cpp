#include <Arduino.h>
#include <Wire.h>
#include <SPI.h>
#include <Ethernet.h>
#include <EthernetUdp.h>
#include <Adafruit_MCP23X17.h>
#include <Adafruit_TLC5947.h>

// I2C pin configuration for ESP32 (main bus for buttons)
const int SDA_PIN = 8;
const int SCL_PIN = 9;

// Slider I2C pins (separate bus)
const int SLIDER_SDA = 3;
const int SLIDER_SCL = 4;

// Slider pins
const int SLIDER_POS_PIN = 2;  // GPIO 2 for slider position (wiper)
const int TOUCH_PIN = 1;       // GPIO 1 for touch

// Slider motor MCP pins
const int MCP_AIN1 = 0;
const int MCP_AIN2 = 1;
const int MCP_STBY = 2;

// TLC5947 LED driver control pins
const int TLC_LAT = 15;
const int TLC_OE = 16;
const int TLC_CLK = 18;
const int TLC_DIN = 39;

// W5500 Ethernet pins
#define W5500_CS   10
#define W5500_RST  14
#define W5500_MOSI 11
#define W5500_MISO 13
#define W5500_SCK  12

// System configuration - 4 MCP23017 chips, each with 16 buttons/LEDs
const int NUM_PAIRS = 4;
const uint8_t MCP_ADDRESSES[NUM_PAIRS] = {0x20, 0x21, 0x22, 0x23};
const int TLC_BASE_CHANNEL[NUM_PAIRS] = {0, 24, 48, 72};

// Network configuration
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
IPAddress ip       (192, 168, 1, 204);
IPAddress dns      (192, 168, 1, 1);
IPAddress gateway  (192, 168, 1, 1);
IPAddress subnet   (255, 255, 255, 0);
IPAddress crestronIP(192, 168, 1, 235);  // Your Mac
const uint16_t CRESTRON_PORT = 50000;
const uint16_t LOCAL_PORT = 50001;

// Hardware objects
Adafruit_MCP23X17 mcp[NUM_PAIRS];
Adafruit_TLC5947 tlc(4, TLC_CLK, TLC_DIN, TLC_LAT);

// Slider MCP (on separate I2C bus)
Adafruit_MCP23X17 sliderMcp;
bool sliderMcpFound = false;

// Slider state
int sliderTarget = -1;  // -1 = no target, 0-4095 = target position
const int SLIDER_TOLERANCE = 400;  // Wider tolerance to prevent overshoot wobble
bool isTouching = false;
bool wasTouching = false;
int touchCount = 0;

// Track last button pressed (for slider control)
unsigned int lastButtonMcpAddr = 0;
int lastButtonPin = -1;

// State tracking
uint16_t ledBrightness[NUM_PAIRS][16] = {0};  // Track actual brightness (0=off)
bool lastButtonState[NUM_PAIRS][16] = {false};
bool mcpFound[NUM_PAIRS] = {false};

// Ethernet UDP
EthernetUDP udp;
char rxBuf[256];

// Zone ID to LED channel mapping
struct ZoneMapping {
  int zoneId;
  int ledChannel;
};

const ZoneMapping zoneLookup[] = {
  {1, 0},   // Zone 1 -> LED channel 0
  {2, 1},   // Zone 2 -> LED channel 1
  {3, 2},   // Zone 3 -> LED channel 2
  // Add more mappings as needed
};
const int NUM_ZONES = sizeof(zoneLookup) / sizeof(zoneLookup[0]);

// Find LED channel for a zone ID (-1 if not found)
int zoneToChannel(int zoneId) {
  for (int i = 0; i < NUM_ZONES; i++) {
    if (zoneLookup[i].zoneId == zoneId) {
      return zoneLookup[i].ledChannel;
    }
  }
  return -1;
}

// Maps MCP23017 pin to TLC5947 channel
int pinToChannel(int pair, int pin) {
  int base = TLC_BASE_CHANNEL[pair];
  if (pin >= 8) {
    return base + (pin - 8);  // GPB pins -> channels 0-7
  } else {
    return base + 8 + pin;    // GPA pins -> channels 8-15
  }
}

// Slider motor control
void sliderForward() {
  sliderMcp.digitalWrite(MCP_AIN1, HIGH);
  sliderMcp.digitalWrite(MCP_AIN2, LOW);
}

void sliderBackward() {
  sliderMcp.digitalWrite(MCP_AIN1, LOW);
  sliderMcp.digitalWrite(MCP_AIN2, HIGH);
}

void sliderBrake() {
  sliderMcp.digitalWrite(MCP_AIN1, HIGH);
  sliderMcp.digitalWrite(MCP_AIN2, HIGH);
}

void setup() {
  Serial.begin(115200);
  delay(2000);

  Serial.println();
  Serial.println("================================");
  Serial.println("Control Panel System - Starting");
  Serial.println("================================");

  // Initialize I2C bus (main - buttons)
  Wire.begin(SDA_PIN, SCL_PIN);

  // Initialize slider I2C bus (pins 3/4)
  Wire1.begin(SLIDER_SDA, SLIDER_SCL);

  // Scan Wire1 for devices
  Serial.println("Scanning Wire1 for I2C devices...");
  for (uint8_t addr = 1; addr < 127; addr++) {
    Wire1.beginTransmission(addr);
    if (Wire1.endTransmission() == 0) {
      Serial.print("  Found device at 0x");
      Serial.println(addr, HEX);
    }
  }

  sliderMcpFound = sliderMcp.begin_I2C(0x27, &Wire1);  // A0=A1=A2=VCC
  if (sliderMcpFound) {
    sliderMcp.pinMode(MCP_AIN1, OUTPUT);
    sliderMcp.pinMode(MCP_AIN2, OUTPUT);
    sliderMcp.pinMode(MCP_STBY, OUTPUT);
    sliderMcp.digitalWrite(MCP_STBY, HIGH);  // Enable motor driver
    sliderBrake();
    Serial.println("Slider MCP ready");
  } else {
    Serial.println("Slider MCP NOT FOUND");
  }

  // Slider analog pins
  pinMode(SLIDER_POS_PIN, INPUT);
  pinMode(TOUCH_PIN, INPUT);

  // Initialize each MCP23017
  for (int i = 0; i < NUM_PAIRS; i++) {
    mcpFound[i] = mcp[i].begin_I2C(MCP_ADDRESSES[i], &Wire);
    if (mcpFound[i]) {
      for (int pin = 0; pin < 16; pin++) {
        mcp[i].pinMode(pin, INPUT_PULLUP);
      }
      Serial.print("MCP at 0x");
      Serial.print(MCP_ADDRESSES[i], HEX);
      Serial.println(" ready");
    } else {
      Serial.print("MCP at 0x");
      Serial.print(MCP_ADDRESSES[i], HEX);
      Serial.println(" NOT FOUND");
    }
  }

  // Initialize TLC5947
  pinMode(TLC_OE, OUTPUT);
  digitalWrite(TLC_OE, HIGH);  // Disable outputs first
  tlc.begin();
  for (int i = 0; i < 96; i++) {
    tlc.setPWM(i, 0);  // 0 = off (no current sink)
  }
  tlc.write();
  digitalWrite(TLC_OE, LOW);  // Now enable outputs
  Serial.println("TLC5947 ready - LEDs off");

  // Initialize W5500 Ethernet
  pinMode(W5500_RST, OUTPUT);
  digitalWrite(W5500_RST, LOW);
  delay(50);
  digitalWrite(W5500_RST, HIGH);
  delay(200);

  SPI.begin(W5500_SCK, W5500_MISO, W5500_MOSI, W5500_CS);
  Ethernet.init(W5500_CS);
  Ethernet.begin(mac, ip, dns, gateway, subnet);

  Serial.print("Ethernet IP: ");
  Serial.println(Ethernet.localIP());

  udp.begin(LOCAL_PORT);
  Serial.println("UDP ready on port 50001");

  // Startup flash sequence (3 quick flashes, end OFF)
  for (int flash = 0; flash < 3; flash++) {
    for (int i = 0; i < 96; i++) tlc.setPWM(i, 4095);  // ON
    tlc.write();
    delay(150);
    for (int i = 0; i < 96; i++) tlc.setPWM(i, 0);     // OFF
    tlc.write();
    delay(150);
  }
  // Ensure all LEDs are OFF
  for (int i = 0; i < 96; i++) tlc.setPWM(i, 0);
  tlc.write();

  Serial.println("Ready!");
  Serial.println("Press a button to set brightness and move slider.");

  if (sliderMcpFound) {
    Serial.println("Slider motor ready.");
  } else {
    Serial.println("WARNING: Slider MCP not found - motor disabled.");
  }
}

void loop() {
  // Scan all MCP23017 chips for button presses (batch read - 1 I2C transaction per MCP)
  for (int pair = 0; pair < NUM_PAIRS; pair++) {
    if (!mcpFound[pair]) continue;

    uint16_t gpio = mcp[pair].readGPIOAB();  // Read all 16 pins at once
    for (int pin = 0; pin < 16; pin++) {
      bool pressed = !(gpio & (1 << pin));  // Active low

      // Detect rising edge (button just pressed)
      if (pressed && !lastButtonState[pair][pin]) {
        lastButtonMcpAddr = MCP_ADDRESSES[pair];
        lastButtonPin = pin;

        // If brightness > 0, send 0 to turn off; if 0, send "on" to turn on
        char msg[64];
        if (ledBrightness[pair][pin] > 0) {
          // Turn off - send level 0
          snprintf(msg, sizeof(msg), "/button/%02X%d/level/0", MCP_ADDRESSES[pair], pin);
        } else {
          // Turn on - let server decide brightness
          snprintf(msg, sizeof(msg), "/button/%02X%d/on", MCP_ADDRESSES[pair], pin);
        }
        udp.beginPacket(crestronIP, CRESTRON_PORT);
        udp.print(msg);
        udp.endPacket();
      }

      lastButtonState[pair][pin] = pressed;
    }
  }

  // Check for incoming UDP (response from Crestron)
  int packetSize = udp.parsePacket();
  if (packetSize > 0) {
    int len = udp.read(rxBuf, sizeof(rxBuf) - 1);
    if (len > 0) {
      rxBuf[len] = '\0';

      // Try parsing "/zone/[id]/level/[level]" format
      // Zone ID can be button ID (e.g., "2112" = MCP 0x21, pin 12)
      unsigned int mcpAddr;
      int pin;
      unsigned long level;
      Serial.print("RX: ");
      Serial.println(rxBuf);
      if (sscanf(rxBuf, "/zone/%2x%d/level/%lu", &mcpAddr, &pin, &level) == 3) {
        Serial.print("Parsed: addr=0x");
        Serial.print(mcpAddr, HEX);
        Serial.print(" pin=");
        Serial.print(pin);
        Serial.print(" level=");
        Serial.println(level);
        // Find the MCP pair and calculate LED channel
        for (int pair = 0; pair < NUM_PAIRS; pair++) {
          if (MCP_ADDRESSES[pair] == mcpAddr && pin >= 0 && pin < 16) {
            int channel = pinToChannel(pair, pin);
            // Scale 0-65535 to 0-4095 (12-bit PWM)
            uint16_t pwm = (level * 4095) / 65535;
            Serial.print("Setting ch ");
            Serial.print(channel);
            Serial.print(" to PWM ");
            Serial.println(pwm);
            tlc.setPWM(channel, pwm);  // 0=off, 4095=full brightness
            tlc.write();

            // Store brightness for toggle logic
            ledBrightness[pair][pin] = pwm;

            // Set slider target position
            sliderTarget = pwm;
            break;
          }
        }
      }
    }
  }

  // Slider control
  int sliderPos = analogRead(SLIDER_POS_PIN);
  int touchValue = analogRead(TOUCH_PIN);

  // Debounced touch detection - require 5 consecutive readings
  static int touchDebounce = 0;
  static bool isTouchingSlider = false;
  static bool wasTouchingSlider = false;
  static int lastSentPos = -1;
  static unsigned long lastSendTime = 0;

  if (touchValue > 600) {  // Touch threshold
    touchDebounce++;
    if (touchDebounce > 3) {
      touchDebounce = 3;
      isTouchingSlider = true;
    }
  } else {
    touchDebounce--;
    if (touchDebounce < 0) {
      touchDebounce = 0;
      isTouchingSlider = false;
    }
  }


  if (isTouchingSlider) {
    // Cancel motor target when touched
    if (sliderTarget >= 0) {
      sliderTarget = -1;
      sliderBrake();
    }

    // Send slider position as brightness (throttled)
    if (millis() - lastSendTime > 10 && lastButtonPin >= 0) {  // Fast updates (10ms)
      // Only send if position changed
      if (abs(sliderPos - lastSentPos) > 15 || lastSentPos < 0) {
        lastSentPos = sliderPos;
        lastSendTime = millis();

        // Scale 0-4095 to 0-65535
        unsigned long brightness = (sliderPos * 65535UL) / 4095;

        char msg[64];
        snprintf(msg, sizeof(msg), "/slider/%02X%d/level/%lu", lastButtonMcpAddr, lastButtonPin, brightness);
        udp.beginPacket(crestronIP, CRESTRON_PORT);
        udp.print(msg);
        udp.endPacket();
      }
    }
    wasTouchingSlider = true;
  } else {
    if (wasTouchingSlider) {
      wasTouchingSlider = false;
      lastSentPos = -1;
    }

    // Move slider toward target (only if MCP found and target set)
    if (sliderMcpFound && sliderTarget >= 0) {
      int error = sliderTarget - sliderPos;

      if (abs(error) < SLIDER_TOLERANCE) {
        sliderBrake();
        sliderTarget = -1;
      } else if (abs(error) < 800) {
        // Slow zone - pulse motor briefly then brake (non-blocking)
        static unsigned long pulseStart = 0;
        static bool pulsing = false;
        if (!pulsing) {
          pulseStart = millis();
          pulsing = true;
          if (error > 0) {
            sliderBackward();
          } else {
            sliderForward();
          }
        } else if (millis() - pulseStart > 15) {
          sliderBrake();
          pulsing = false;
        }
      } else {
        // Full speed when far from target
        if (error > 0) {
          sliderBackward();
        } else {
          sliderForward();
        }
      }
    }
  }

}
