"""
Orient House - Lutron Integration Device Data
Extracted from Integration Report 20260116.pdf

This file contains all zone, button, and shade IDs from the Lutron system.
"""

# Zones (Lights/Circuits) - /zone/[id]/[level] where level is 0-65535
ZONES = {
    # Exterior
    435: {"name": "Exterior\\ZE-001", "level": 0},
    580: {"name": "Exterior\\ZE-004", "level": 0},
    559: {"name": "Exterior\\ZE-005", "level": 0},
    635: {"name": "Exterior\\ZE-110", "level": 0},
    644: {"name": "Exterior\\ZE-104", "level": 0},
    722: {"name": "Exterior\\ZE-111", "level": 0},
    803: {"name": "Exterior\\ZE-114", "level": 0},
    812: {"name": "Exterior\\ZE-113", "level": 0},
    821: {"name": "Exterior\\ZE-115", "level": 0},
    830: {"name": "Exterior\\ZE-119", "level": 0},
    839: {"name": "Exterior\\ZE-120", "level": 0},
    848: {"name": "Exterior\\ZE-121", "level": 0},
    871: {"name": "Exterior\\ZE-118", "level": 0},
    1868: {"name": "Exterior\\ZE-116", "level": 0},
    1877: {"name": "Exterior\\ZE-117", "level": 0},
    3044: {"name": "Exterior\\Light Well ZE-122", "level": 0},
    10577: {"name": "Exterior\\ZE-113A", "level": 0},

    # Lower Level - Garage 001
    2281: {"name": "Lower Level\\Garage 001\\LS-PL03", "level": 0},
    2310: {"name": "Lower Level\\Garage 001\\ZE-001", "level": 0},
    2338: {"name": "Lower Level\\Garage 001\\LS-WS02", "level": 0},

    # Lower Level - Trash 002
    2567: {"name": "Lower Level\\Trash 002\\LS-PL01", "level": 0},

    # Lower Level - Stor 003
    2444: {"name": "Lower Level\\Stor 003\\ZB-003", "level": 0},
    2472: {"name": "Lower Level\\Stor 003\\ZB-103", "level": 0},
    2605: {"name": "Lower Level\\Stor 003\\ZB-101", "level": 0},
    2707: {"name": "Lower Level\\Stor 003\\ZB-001", "level": 0},

    # Lower Level - Mech Room 004
    2677: {"name": "Lower Level\\Mech Room 004\\LS-PL01", "level": 0},

    # Lower Level - Pantry Storage 004A
    2647: {"name": "Lower Level\\Pantry Storage 004A\\LS-PL01", "level": 0},

    # Lower Level - Hall 005
    2908: {"name": "Lower Level\\Hall 005\\ZB-004 ZB-002", "level": 0},
    2936: {"name": "Lower Level\\Hall 005\\ZB-007", "level": 0},
    3016: {"name": "Lower Level\\Hall 005\\ZB-104", "level": 0},

    # Lower Level - Elec Room 006
    2754: {"name": "Lower Level\\Elec Room 006\\LS-PL01", "level": 0},

    # Lower Level - Storage 006A
    9210: {"name": "Lower Level\\Storage 006A\\LS-PL01", "level": 0},

    # Lower Level - Gym 007
    533: {"name": "Lower Level\\Gym 007\\ZB-005", "level": 0},
    3153: {"name": "Lower Level\\Gym 007\\ZB-006", "level": 0},

    # Lower Level - Bath 008
    3200: {"name": "Lower Level\\Bath 008\\ZB-102", "level": 0},
    10843: {"name": "Lower Level\\Bath 008\\Zone 02", "level": 0},

    # Lower Level - Unfinished Storage 010
    3347: {"name": "Lower Level\\Unfinished Storage 010\\LS-PL01", "level": 0},

    # Lower Level - Storage 012
    3305: {"name": "Lower Level\\Storage 012\\LS-PL01", "level": 0},

    # Lower Level - New Mech Near Garage
    10809: {"name": "Lower Level\\New Mech Near Garage\\Zone 01", "level": 0},

    # First Floor - Entry 101
    2087: {"name": "First Floor\\Entry 101\\Z-001", "level": 0},
    2096: {"name": "First Floor\\Entry 101\\Z1-002", "level": 0},

    # First Floor - Living/Dining Room 102
    665: {"name": "First Floor\\Living/Dining Room 102\\Z1-004", "level": 0},
    674: {"name": "First Floor\\Living/Dining Room 102\\Z1-003 INT", "level": 0},
    683: {"name": "First Floor\\Living/Dining Room 102\\Z1-003 CCT", "level": 0},
    1079: {"name": "First Floor\\Living/Dining Room 102\\Z1-011", "level": 0},
    4376: {"name": "First Floor\\Living/Dining Room 102\\Z1-102", "level": 0},
    4404: {"name": "First Floor\\Living/Dining Room 102\\Z1-107", "level": 0},
    4432: {"name": "First Floor\\Living/Dining Room 102\\Z1-005", "level": 0},

    # First Floor - Kitchen 104
    4127: {"name": "First Floor\\Kitchen 104\\ZE-101 ZE-102", "level": 0},
    4207: {"name": "First Floor\\Kitchen 104\\Z1-006", "level": 0},
    9164: {"name": "First Floor\\Kitchen 104\\Z1-106A", "level": 0},

    # First Floor - Utility Pantry 105
    3801: {"name": "First Floor\\Utility Pantry 105\\Z1-010", "level": 0},
    10918: {"name": "First Floor\\Utility Pantry 105\\Zone 02", "level": 0},

    # First Floor - Breakfast Room 106
    3507: {"name": "First Floor\\Breakfast Room 106\\Z1-014", "level": 0},
    3535: {"name": "First Floor\\Breakfast Room 106\\ZE-007", "level": 0},
    3621: {"name": "First Floor\\Breakfast Room 106\\Z1-008 Z1-007", "level": 0},
    3649: {"name": "First Floor\\Breakfast Room 106\\Z1-009", "level": 0},
    3679: {"name": "First Floor\\Breakfast Room 106\\Z1-106", "level": 0},
    3759: {"name": "First Floor\\Breakfast Room 106\\ZE-105", "level": 0},
    3831: {"name": "First Floor\\Breakfast Room 106\\Z1-105", "level": 0},
    10961: {"name": "First Floor\\Breakfast Room 106\\Zone 03", "level": 0},
    10993: {"name": "First Floor\\Breakfast Room 106\\Zone 04", "level": 0},

    # First Floor - Rear Stairs
    4007: {"name": "First Floor\\Rear Stairs\\Z1-013A", "level": 0},
    4035: {"name": "First Floor\\Rear Stairs\\Z1-013", "level": 0},

    # First Floor - Mudroom 107
    3953: {"name": "First Floor\\Mudroom 107\\Z1-012", "level": 0},

    # First Floor - Coat Closet 108
    4665: {"name": "First Floor\\Coat Closet 108\\ZE-103", "level": 0},
    4698: {"name": "First Floor\\Coat Closet 108\\Z1-017", "level": 0},

    # First Floor - Powder Room 109
    9684: {"name": "First Floor\\Powder Room 109\\WS05LD", "level": 0},
    9703: {"name": "First Floor\\Powder Room 109\\Z1-108", "level": 0},

    # First Floor - Den 110
    4790: {"name": "First Floor\\Den 110\\ZE-109", "level": 0},
    4818: {"name": "First Floor\\Den 110\\ZE-002 ZE-003", "level": 0},
    4846: {"name": "First Floor\\Den 110\\ZE-107", "level": 0},
    4876: {"name": "First Floor\\Den 110\\Z1-110", "level": 0},
    4904: {"name": "First Floor\\Den 110\\Z1-015", "level": 0},
    4932: {"name": "First Floor\\Den 110\\Z1-019", "level": 0},
    4960: {"name": "First Floor\\Den 110\\Z1-109", "level": 0},
    5090: {"name": "First Floor\\Den 110\\Z1-111 table Lamps", "level": 0},

    # First Floor - Main Stairs 111
    704: {"name": "First Floor\\Main Stairs 111\\Z1-018", "level": 0},
    713: {"name": "First Floor\\Main Stairs 111\\Z1-112", "level": 0},
    731: {"name": "First Floor\\Main Stairs 111\\Z2-005 INT", "level": 0},
    740: {"name": "First Floor\\Main Stairs 111\\Z2-005 CCT", "level": 0},
    2115: {"name": "First Floor\\Main Stairs 111\\Z2-002", "level": 0},
    5120: {"name": "First Floor\\Main Stairs 111\\Z1-016", "level": 0},

    # First Floor - Hallway 112
    5358: {"name": "First Floor\\Hallway 112\\Z1-020", "level": 0},
    5386: {"name": "First Floor\\Hallway 112\\ZE-108", "level": 0},
    5414: {"name": "First Floor\\Hallway 112\\Z1-114", "level": 0},

    # First Floor - Bedroom 1 113
    5564: {"name": "First Floor\\Bedroom 1 113\\Z1-119", "level": 0},
    5594: {"name": "First Floor\\Bedroom 1 113\\Z-118A", "level": 0},
    5624: {"name": "First Floor\\Bedroom 1 113\\Z1-118B", "level": 0},

    # First Floor - Bathroom 1 114
    5718: {"name": "First Floor\\Bathroom 1 114\\Z1-120", "level": 0},
    5746: {"name": "First Floor\\Bathroom 1 114\\Z1-023", "level": 0},
    11071: {"name": "First Floor\\Bathroom 1 114\\Zone 03", "level": 0},

    # First Floor - Laundry Room 115
    6122: {"name": "First Floor\\Launry Room 115\\LS-PL01", "level": 0},

    # First Floor - Bedroom 2 116
    5866: {"name": "First Floor\\Bedroom 2 116\\Z1-116", "level": 0},
    5896: {"name": "First Floor\\Bedroom 2 116\\Z1-117B", "level": 0},
    5930: {"name": "First Floor\\Bedroom 2 116\\Z1-117A", "level": 0},
    9460: {"name": "First Floor\\Bedroom 2 116\\LS-PL01", "level": 0},

    # First Floor - Bathroom 2 117
    6052: {"name": "First Floor\\Bathroom 2 117\\Z1-115", "level": 0},
    6080: {"name": "First Floor\\Bathroom 2 117\\Z1-021", "level": 0},
    11123: {"name": "First Floor\\Bathroom 2 117\\Zone 01", "level": 0},

    # First Floor - Storage Closet
    5264: {"name": "First Floor\\Storage Closet\\LS-PL01", "level": 0},

    # Second Floor - Primary Bedroom 201
    773: {"name": "Second Floor\\Primary Bedroom 201\\Z2-107", "level": 0},
    6203: {"name": "Second Floor\\Primary Bedroom 201\\Z2-119", "level": 0},
    6231: {"name": "Second Floor\\Primary Bedroom 201\\ZE-009", "level": 0},
    6259: {"name": "Second Floor\\Primary Bedroom 201\\Z2-009", "level": 0},
    6289: {"name": "Second Floor\\Primary Bedroom 201\\Z2-xxx.", "level": 0},
    6317: {"name": "Second Floor\\Primary Bedroom 201\\Z2-105A", "level": 0},
    6447: {"name": "Second Floor\\Primary Bedroom 201\\Z2-xxx", "level": 0},
    6475: {"name": "Second Floor\\Primary Bedroom 201\\Z2-105B", "level": 0},

    # Second Floor - Dressing Room 202
    6567: {"name": "Second Floor\\Dressing Room 202\\Z2-011A", "level": 0},
    6597: {"name": "Second Floor\\Dressing Room 202\\Z2-011", "level": 0},

    # Second Floor - Primary Bathroom 203
    6677: {"name": "Second Floor\\Primary Bathroom 203\\Z2-108", "level": 0},
    6705: {"name": "Second Floor\\Primary Bathroom 203\\Z2-012", "level": 0},
    6733: {"name": "Second Floor\\Primary Bathroom 203\\Z2-013", "level": 0},
    6843: {"name": "Second Floor\\Primary Bathroom 203\\Z2-109", "level": 0},
    11283: {"name": "Second Floor\\Primary Bathroom 203\\Zone 04", "level": 0},
    11313: {"name": "Second Floor\\Primary Bathroom 203\\Zone 07", "level": 0},

    # Second Floor - Study 204
    6951: {"name": "Second Floor\\Study 204\\Z2-115", "level": 0},
    6979: {"name": "Second Floor\\Study 204\\Z2-014", "level": 0},

    # Second Floor - Bedroom 207
    7587: {"name": "Second Floor\\Bedroom 207\\Z2-118", "level": 0},
    7617: {"name": "Second Floor\\Bedroom 207\\Z2-104A", "level": 0},
    7647: {"name": "Second Floor\\Bedroom 207\\Z2-104B", "level": 0},

    # Second Floor - Bathroom 208
    7689: {"name": "Second Floor\\Bathroom 208\\Z2-103", "level": 0},
    7717: {"name": "Second Floor\\Bathroom 208\\Z2-008", "level": 0},
    11179: {"name": "Second Floor\\Bathroom 208\\Zone 03", "level": 0},

    # Second Floor - Laundry 209
    9506: {"name": "Second Floor\\Laundry 209\\LS-PL01", "level": 0},

    # Second Floor - Bedroom 210
    7841: {"name": "Second Floor\\Bedroom 210\\Z2-117", "level": 0},
    7871: {"name": "Second Floor\\Bedroom 210\\Z2-101B", "level": 0},
    7901: {"name": "Second Floor\\Bedroom 210\\Z2-101A", "level": 0},

    # Second Floor - Hallway 211
    7123: {"name": "Second Floor\\Hallway 211\\Z2-003", "level": 0},
    7151: {"name": "Second Floor\\Hallway 211\\Z2-001", "level": 0},
    7233: {"name": "Second Floor\\Hallway 211\\ZE-008", "level": 0},
    7261: {"name": "Second Floor\\Hallway 211\\ZE-112", "level": 0},
    7317: {"name": "Second Floor\\Hallway 211\\Z2-116", "level": 0},

    # Second Floor - Closet 212
    8047: {"name": "Second Floor\\Closet 212\\Z2-007", "level": 0},

    # Second Floor - Bathroom 213
    7943: {"name": "Second Floor\\Bathroom 213\\Z2-102", "level": 0},
    7971: {"name": "Second Floor\\Bathroom 213\\Z2-006", "level": 0},
    11231: {"name": "Second Floor\\Bathroom 213\\Zone 03", "level": 0},

    # Second Floor - Storage
    7463: {"name": "Second Floor\\Storage\\LS-PL01", "level": 0},

    # Control Panel
    9087: {"name": "Control panel\\Zone 06", "level": 0},
}

# Buttons (Scenes) - /button/[id]/press -> /button/[id]/fb
BUTTONS = {
    # Exterior - Pool
    10711: {"name": "Exterior\\Pool\\Button 1", "active": False},
    10715: {"name": "Exterior\\Pool\\Button 2", "active": False},
    10719: {"name": "Exterior\\Pool\\Button 3", "active": False},
    10723: {"name": "Exterior\\Pool\\Button 4", "active": False},
    10727: {"name": "Exterior\\Pool\\Button 5", "active": False},
    10731: {"name": "Exterior\\Pool\\Button 6", "active": False},
    10735: {"name": "Exterior\\Pool\\Button 18", "active": False},
    10737: {"name": "Exterior\\Pool\\Button 19", "active": False},

    # Lower Level - Garage 001
    2272: {"name": "Lower Level\\Garage 001\\PRO-001.1 Button 0", "active": False},
    2302: {"name": "Lower Level\\Garage 001\\PRO-001.2 Button 0", "active": False},
    2330: {"name": "Lower Level\\Garage 001\\PRO-001.3 Button 0", "active": False},

    # Lower Level - Trash 002
    2558: {"name": "Lower Level\\Trash 002\\S-003.1 Button 0", "active": False},

    # Lower Level - Stor 003
    2392: {"name": "Lower Level\\Stor 003\\ST-003.2 Button 1", "active": False},
    2396: {"name": "Lower Level\\Stor 003\\ST-003.2 Button 2", "active": False},
    2400: {"name": "Lower Level\\Stor 003\\ST-003.2 Button 3", "active": False},
    2404: {"name": "Lower Level\\Stor 003\\ST-003.2 Button 4", "active": False},
    2408: {"name": "Lower Level\\Stor 003\\ST-003.2 Button 5", "active": False},
    2412: {"name": "Lower Level\\Stor 003\\ST-003.2 Button 6", "active": False},
    2416: {"name": "Lower Level\\Stor 003\\ST-003.2 Button 18", "active": False},
    2418: {"name": "Lower Level\\Stor 003\\ST-003.2 Button 19", "active": False},
    2436: {"name": "Lower Level\\Stor 003\\PRO-003.3 Button 0", "active": False},
    2464: {"name": "Lower Level\\Stor 003\\PRO-003.4 Button 0", "active": False},
    2501: {"name": "Lower Level\\Stor 003\\ST-003.1 Button 1", "active": False},
    2505: {"name": "Lower Level\\Stor 003\\ST-003.1 Button 2", "active": False},
    2509: {"name": "Lower Level\\Stor 003\\ST-003.1 Button 3", "active": False},
    2513: {"name": "Lower Level\\Stor 003\\ST-003.1 Button 4", "active": False},
    2517: {"name": "Lower Level\\Stor 003\\ST-003.1 Button 5", "active": False},
    2521: {"name": "Lower Level\\Stor 003\\ST-003.1 Button 6", "active": False},
    2525: {"name": "Lower Level\\Stor 003\\ST-003.1 Button 18", "active": False},
    2527: {"name": "Lower Level\\Stor 003\\ST-003.1 Button 19", "active": False},
    2597: {"name": "Lower Level\\Stor 003\\PRO-003.2 Button 0", "active": False},
    2699: {"name": "Lower Level\\Stor 003\\PRO-003.1 Button 0", "active": False},

    # Lower Level - Mech Room 004
    2669: {"name": "Lower Level\\Mech Room 004\\S-004.1 Button 0", "active": False},
    3823: {"name": "Lower Level\\Mech Room 004\\PRO-106.7 Button 0", "active": False},

    # Lower Level - Pantry Storage 004A
    2639: {"name": "Lower Level\\Pantry Storage 004A\\S-004A.1 Button 0", "active": False},

    # Lower Level - Hall 005
    2807: {"name": "Lower Level\\Hall 005\\ST-009.1 Button 1", "active": False},
    2811: {"name": "Lower Level\\Hall 005\\ST-009.1 Button 2", "active": False},
    2815: {"name": "Lower Level\\Hall 005\\ST-009.1 Button 3", "active": False},
    2819: {"name": "Lower Level\\Hall 005\\ST-009.1 Button 4", "active": False},
    2823: {"name": "Lower Level\\Hall 005\\ST-009.1 Button 5", "active": False},
    2827: {"name": "Lower Level\\Hall 005\\ST-009.1 Button 6", "active": False},
    2831: {"name": "Lower Level\\Hall 005\\ST-009.1 Button 18", "active": False},
    2833: {"name": "Lower Level\\Hall 005\\ST-009.1 Button 19", "active": False},
    2900: {"name": "Lower Level\\Hall 005\\PRO-009.1 Button 0", "active": False},
    2928: {"name": "Lower Level\\Hall 005\\PRO-009.2 Button 0", "active": False},
    3008: {"name": "Lower Level\\Hall 005\\PRO-009.3 Button 0", "active": False},
    3036: {"name": "Lower Level\\Hall 005\\PRO-009.4 Button 0", "active": False},
    2965: {"name": "Lower Level\\Hall 005\\ST-009.2 Button 1", "active": False},
    2969: {"name": "Lower Level\\Hall 005\\ST-009.2 Button 2", "active": False},
    2973: {"name": "Lower Level\\Hall 005\\ST-009.2 Button 3", "active": False},
    2977: {"name": "Lower Level\\Hall 005\\ST-009.2 Button 4", "active": False},
    2981: {"name": "Lower Level\\Hall 005\\ST-009.2 Button 5", "active": False},
    2985: {"name": "Lower Level\\Hall 005\\ST-009.2 Button 6", "active": False},
    2989: {"name": "Lower Level\\Hall 005\\ST-009.2 Button 18", "active": False},
    2991: {"name": "Lower Level\\Hall 005\\ST-009.2 Button 19", "active": False},
    9383: {"name": "Lower Level\\Hall 005\\ST-005.1 Button 1", "active": False},
    9387: {"name": "Lower Level\\Hall 005\\ST-005.1 Button 2", "active": False},
    9391: {"name": "Lower Level\\Hall 005\\ST-005.1 Button 3", "active": False},
    9395: {"name": "Lower Level\\Hall 005\\ST-005.1 Button 4", "active": False},
    9399: {"name": "Lower Level\\Hall 005\\ST-005.1 Button 5", "active": False},
    9403: {"name": "Lower Level\\Hall 005\\ST-005.1 Button 6", "active": False},
    9407: {"name": "Lower Level\\Hall 005\\ST-005.1 Button 18", "active": False},
    9409: {"name": "Lower Level\\Hall 005\\ST-005.1 Button 19", "active": False},

    # Lower Level - Elec Room 006
    2746: {"name": "Lower Level\\Elec Room 006\\S-006.1 Button 0", "active": False},

    # Lower Level - Storage 006A
    10595: {"name": "Lower Level\\Storage 006A\\PRO-006A.1 Button 0", "active": False},

    # Lower Level - Gym 007
    3102: {"name": "Lower Level\\Gym 007\\ST-007.1 Button 1", "active": False},
    3106: {"name": "Lower Level\\Gym 007\\ST-007.1 Button 2", "active": False},
    3110: {"name": "Lower Level\\Gym 007\\ST-007.1 Button 3", "active": False},
    3114: {"name": "Lower Level\\Gym 007\\ST-007.1 Button 4", "active": False},
    3118: {"name": "Lower Level\\Gym 007\\ST-007.1 Button 5", "active": False},
    3122: {"name": "Lower Level\\Gym 007\\ST-007.1 Button 6", "active": False},
    3126: {"name": "Lower Level\\Gym 007\\ST-007.1 Button 18", "active": False},
    3128: {"name": "Lower Level\\Gym 007\\ST-007.1 Button 19", "active": False},
    3145: {"name": "Lower Level\\Gym 007\\PRO-007.1 Button 0", "active": False},

    # Lower Level - Bath 008
    3192: {"name": "Lower Level\\Bath 008\\PRO-008.1 Button 0", "active": False},
    10835: {"name": "Lower Level\\Bath 008\\Fan Button 0", "active": False},

    # Lower Level - Unfinished Storage 010
    3339: {"name": "Lower Level\\Unfinished Storage 010\\S-011.1 Button 0", "active": False},

    # Lower Level - Storage 012
    3297: {"name": "Lower Level\\Storage 012\\S-012.1 Button 0", "active": False},

    # Lower Level - New Mech Near Garage
    10801: {"name": "Lower Level\\New Mech Near Garage\\Device 1 Button 0", "active": False},

    # First Floor - Entry 101
    4561: {"name": "First Floor\\Entry 101\\Alisse-101.1 Button 1", "active": False},
    4565: {"name": "First Floor\\Entry 101\\Alisse-101.1 Button 2", "active": False},
    11018: {"name": "First Floor\\Entry 101\\Alisse-101.1 Button 3", "active": False},
    4577: {"name": "First Floor\\Entry 101\\Alisse-101.1 Button 10", "active": False},

    # First Floor - Living/Dining Room 102
    4368: {"name": "First Floor\\Living Room 102\\PRO-102.1 Button 0", "active": False},
    4396: {"name": "First Floor\\Living Room 102\\PRO-102.2 Button 0", "active": False},
    4424: {"name": "First Floor\\Living Room 102\\PRO-102.3 Button 0", "active": False},
    4461: {"name": "First Floor\\Living Room 102\\ST-102.1 Button 1", "active": False},
    4465: {"name": "First Floor\\Living Room 102\\ST-102.1 Button 2", "active": False},
    4469: {"name": "First Floor\\Living Room 102\\ST-102.1 Button 3", "active": False},
    4473: {"name": "First Floor\\Living Room 102\\ST-102.1 Button 4", "active": False},
    4477: {"name": "First Floor\\Living Room 102\\ST-102.1 Button 5", "active": False},
    4481: {"name": "First Floor\\Living Room 102\\ST-102.1 Button 6", "active": False},
    4485: {"name": "First Floor\\Living Room 102\\ST-102.1 Button 18", "active": False},
    4487: {"name": "First Floor\\Living Room 102\\ST-102.1 Button 19", "active": False},
    4511: {"name": "First Floor\\Living Room 102\\ST-102.2 Button 1", "active": False},
    4515: {"name": "First Floor\\Living Room 102\\ST-102.2 Button 2", "active": False},
    4519: {"name": "First Floor\\Living Room 102\\ST-102.2 Button 3", "active": False},
    4523: {"name": "First Floor\\Living Room 102\\ST-102.2 Button 4", "active": False},
    4527: {"name": "First Floor\\Living Room 102\\ST-102.2 Button 5", "active": False},
    4531: {"name": "First Floor\\Living Room 102\\ST-102.2 Button 6", "active": False},
    4535: {"name": "First Floor\\Living Room 102\\ST-102.2 Button 18", "active": False},
    4537: {"name": "First Floor\\Living Room 102\\ST-102.2 Button 19", "active": False},

    # First Floor - Kitchen 104
    4119: {"name": "First Floor\\Kitchen 104\\PRO-106.9 Button 0", "active": False},
    4154: {"name": "First Floor\\Kitchen 104\\ST-106.3 Button 1", "active": False},
    4158: {"name": "First Floor\\Kitchen 104\\ST-106.3 Button 2", "active": False},
    4162: {"name": "First Floor\\Kitchen 104\\ST-106.3 Button 3", "active": False},
    4166: {"name": "First Floor\\Kitchen 104\\ST-106.3 Button 4", "active": False},
    4170: {"name": "First Floor\\Kitchen 104\\ST-106.3 Button 5", "active": False},
    4174: {"name": "First Floor\\Kitchen 104\\ST-106.3 Button 6", "active": False},
    4178: {"name": "First Floor\\Kitchen 104\\ST-106.3 Button 18", "active": False},
    4180: {"name": "First Floor\\Kitchen 104\\ST-106.3 Button 19", "active": False},
    4199: {"name": "First Floor\\Kitchen 104\\PRO-106.8 Button 0", "active": False},
    4241: {"name": "First Floor\\Kitchen 104\\Alisse-106.2 Button 1", "active": False},
    4245: {"name": "First Floor\\Kitchen 104\\Alisse-106.2 Button 2", "active": False},
    4249: {"name": "First Floor\\Kitchen 104\\Alisse-106.2 Button 3", "active": False},
    4253: {"name": "First Floor\\Kitchen 104\\Alisse-106.2 Button 4", "active": False},
    4257: {"name": "First Floor\\Kitchen 104\\Alisse-106.2 Button 5", "active": False},
    4261: {"name": "First Floor\\Kitchen 104\\Alisse-106.2 Button 6", "active": False},
    4265: {"name": "First Floor\\Kitchen 104\\Alisse-106.2 Button 7", "active": False},
    4269: {"name": "First Floor\\Kitchen 104\\Alisse-106.2 Button 8", "active": False},
    4273: {"name": "First Floor\\Kitchen 104\\Alisse-106.2 Button 9", "active": False},
    4277: {"name": "First Floor\\Kitchen 104\\Alisse-106.2 Button 10", "active": False},
    4310: {"name": "First Floor\\Kitchen 104\\Alisse-106.1 Button 1", "active": False},
    4314: {"name": "First Floor\\Kitchen 104\\Alisse-106.1 Button 2", "active": False},
    4318: {"name": "First Floor\\Kitchen 104\\Alisse-106.1 Button 3", "active": False},
    4322: {"name": "First Floor\\Kitchen 104\\Alisse-106.1 Button 4", "active": False},
    4326: {"name": "First Floor\\Kitchen 104\\Alisse-106.1 Button 5", "active": False},
    4330: {"name": "First Floor\\Kitchen 104\\Alisse-106.1 Button 6", "active": False},
    4334: {"name": "First Floor\\Kitchen 104\\Alisse-106.1 Button 7", "active": False},
    4338: {"name": "First Floor\\Kitchen 104\\Alisse-106.1 Button 8", "active": False},
    4342: {"name": "First Floor\\Kitchen 104\\Alisse-106.1 Button 9", "active": False},
    4346: {"name": "First Floor\\Kitchen 104\\Alisse-106.1 Button 10", "active": False},
    9156: {"name": "First Floor\\Kitchen 104\\Kitchen Island Lamp Button 0", "active": False},

    # First Floor - Utility Pantry 105
    3793: {"name": "First Floor\\Utility Pantry 105\\PRO-105.1 Button 0", "active": False},
    10910: {"name": "First Floor\\Utility Pantry 105\\Device 2 Button 0", "active": False},

    # First Floor - Breakfast Room 106
    3499: {"name": "First Floor\\Breakfast Room 106\\PRO-106.3 Button 0", "active": False},
    3527: {"name": "First Floor\\Breakfast Room 106\\PRO-106.2 Button 0", "active": False},
    10953: {"name": "First Floor\\Breakfast Room 106\\Device 1 Button 0", "active": False},
    10985: {"name": "First Floor\\Breakfast Room 106\\Device 2 Button 0", "active": False},
    3613: {"name": "First Floor\\Breakfast Room 106\\PRO-106.5 Button 0", "active": False},
    3641: {"name": "First Floor\\Breakfast Room 106\\PRO-106.4 Button 0", "active": False},
    3671: {"name": "First Floor\\Breakfast Room 106\\PRO-106.6 Button 0", "active": False},
    3708: {"name": "First Floor\\Breakfast Room 106\\ST-106.1 Button 1", "active": False},
    3712: {"name": "First Floor\\Breakfast Room 106\\ST-106.1 Button 2", "active": False},
    3716: {"name": "First Floor\\Breakfast Room 106\\ST-106.1 Button 3", "active": False},
    3720: {"name": "First Floor\\Breakfast Room 106\\ST-106.1 Button 4", "active": False},
    3724: {"name": "First Floor\\Breakfast Room 106\\ST-106.1 Button 5", "active": False},
    3728: {"name": "First Floor\\Breakfast Room 106\\ST-106.1 Button 6", "active": False},
    3732: {"name": "First Floor\\Breakfast Room 106\\ST-106.1 Button 18", "active": False},
    3734: {"name": "First Floor\\Breakfast Room 106\\ST-106.1 Button 19", "active": False},
    3751: {"name": "First Floor\\Breakfast Room 106\\PRO-106.11 Button 0", "active": False},
    10639: {"name": "First Floor\\Breakfast Room 106\\Mudroom Door Button 2", "active": False},
    10651: {"name": "First Floor\\Breakfast Room 106\\Mudroom Door Button 10", "active": False},

    # Crestron Test Buttons
    11783: {"name": "crestron\\Lower Level\\test1 ON", "active": False},
    11790: {"name": "crestron\\Lower Level\\test1 OFF", "active": False},
    11797: {"name": "crestron\\Lower Level\\test1 TOGGLE", "active": False},
    11804: {"name": "crestron\\Lower Level\\test1 RAISE", "active": False},
    11811: {"name": "crestron\\Lower Level\\test1 LOWER", "active": False},
}

# Shades - /shade/[id]/[position] where position is 0-65535
# Shade Groups from the Integration Report
SHADES = {
    # Lower Level - Game Room
    8112: {"name": "Lower Level\\Game Room\\Solar Shades", "position": 0},
    8175: {"name": "Lower Level\\Game Room\\Blackout Shades", "position": 0},

    # First Floor - Kitchen 104
    8239: {"name": "First Floor\\Kitchen 104\\Solar Shades", "position": 0},

    # First Floor - Den 110
    8435: {"name": "First Floor\\Den 110\\Solar Shades", "position": 0},

    # First Floor - Bedroom 1 113
    8344: {"name": "First Floor\\Bedroom 1 113\\Solar Shades", "position": 0},
    8379: {"name": "First Floor\\Bedroom 1 113\\Blackout Shades", "position": 0},

    # First Floor - Bedroom 2 116
    8400: {"name": "First Floor\\Bedroom 2 116\\Solar Shades", "position": 0},

    # Second Floor - Primary Bedroom 201
    8456: {"name": "Second Floor\\Primary Bedroom 201\\Solar Shades", "position": 0},
    8547: {"name": "Second Floor\\Primary Bedroom 201\\Drapery Tracks", "position": 0},

    # Second Floor - Primary Bathroom 203
    8736: {"name": "Second Floor\\Primary Bathroom 203\\Blackout Shade", "position": 0},

    # Second Floor - Study 204
    8659: {"name": "Second Floor\\Study 204\\Solar Shades", "position": 0},

    # Second Floor - Bedroom 207
    8582: {"name": "Second Floor\\Bedroom 207\\Solar Shades", "position": 0},
    8603: {"name": "Second Floor\\Bedroom 207\\Blackout Shades", "position": 0},

    # Second Floor - Bedroom 210
    8624: {"name": "Second Floor\\Bedroom 210\\Solar Shades", "position": 0},
}


def get_zone_ids():
    """Return a list of all zone IDs."""
    return list(ZONES.keys())


def get_button_ids():
    """Return a list of all button IDs."""
    return list(BUTTONS.keys())


def get_shade_ids():
    """Return a list of all shade IDs."""
    return list(SHADES.keys())
