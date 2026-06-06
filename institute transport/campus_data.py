# campus_data.py
# Contains all the nodes (locations) and edges (paths) for the campus graph

LOCATIONS = {
    0: "Staff Parking lot",
    1: "Heritage block",
    2: "Main gate",
    3: "Principal parking lot",
    4: "DSI Library",
    5: "Vip Parking Lot",
    6: "CPA Auditorium/PC Sagar",
    7: "Student Parking Lot",
    8: "Mechanical block",
    9: "Civil block",
    10: "EEE Building",
    11: "Aeronautical building",
    12: "Automobile",
    13: "Dept of Management studies",
    14: "Chemical Eng",
    15: "Food Truck",
    16: "DSI Gym",
    17: "NRI hostel",
    18: "NRI Canteen",
    19: "Tennis court",
    20: "Football Ground",
    21: "Basketball court",
    22: "Rock Garden",
    23: "CD Sagar",
    24: "Sharada Girls Hostel",
    25: "Nelson Mandela girls Hostel",
    26: "ECE Dept",
    27: "CSE/ISE Dept",
    28: "AIML Dept",
    29: "Electronics and instrumentations eng",
    30: "Amphitheatre",
    31: "Dental Block",
    32: "IEM Block",
    33: "Indian boys hostel",
    34: "BB Block",
    35: "Architecture block"
}

# Temporary coordinates spread out in a grid around the center so you can drag them easily
GPS_COORDINATES = {
    0:  (12.908969, 77.566057), # Staff Parking lot
    1:  (12.908934, 77.566505), # Heritage block
    2:  (12.909406, 77.566792), # Main gate
    3:  (12.909335, 77.566990), # Principal parking lot
    4:  (12.909215, 77.567068), # DSI Library
    5:  (12.909386, 77.567049), # Vip Parking Lot
    6:  (12.909019, 77.566923), # CPA Auditorium/PC Sagar
    7:  (12.909228, 77.567690), # Student Parking Lot
    8:  (12.908512, 77.567795), # Mechanical block
    9:  (12.908354, 77.567717), # Civil block
    10:  (12.908024, 77.567704), # EEE Building
    11:  (12.908854, 77.568194), # Aeronautical building
    12:  (12.909001, 77.568216), # Automobile
    13:  (12.908525, 77.568430), # Dept of Management studies
    14:  (12.907879, 77.567859), # Chemical Eng
    15:  (12.907543, 77.567238), # Food Truck
    16:  (12.907226, 77.567612), # DSI Gym
    17:  (12.907045, 77.567454), # NRI hostel
    18:  (12.907138, 77.567511), # NRI Canteen
    19:  (12.906908, 77.567060), # Tennis court
    20:  (12.907109, 77.566695), # Football Ground
    21:  (12.907257, 77.567083), # Basketball court
    22:  (12.907887, 77.567057), # Rock Garden
    23:  (12.907918, 77.567576), # CD Sagar
    24:  (12.907637, 77.566399), # Sharada Girls Hostel
    25:  (12.908061, 77.565570), # Nelson Mandela girls Hostel
    26:  (12.907521, 77.565443), # ECE Dept
    27:  (12.907788, 77.566083), # CSE/ISE Dept
    28:  (12.907611, 77.565990), # AIML Dept
    29:  (12.908287, 77.565627), # Electronics and instrumentations eng
    30:  (12.908094, 77.566177), # Amphitheatre
    31:  (12.908596, 77.565979), # Dental Block
    32:  (12.908201, 77.567448), # IEM Block
    33:  (12.907862, 77.565488), # Indian boys hostel
    34:  (12.907100, 77.566175), # BB Block
    35:  (12.906938, 77.566188), # Architecture block
}

# Updated paths from Path Edit Mode
EDGES = [
    (2, 3, 23),
    (4, 3, 16),
    (2, 5, 28),
    (4, 6, 27),
    (6, 1, 46),
    (1, 31, 68),
    (31, 29, 51),
    (29, 25, 26),
    (25, 30, 66),
    (25, 33, 24),
    (30, 27, 36),
    (5, 7, 72),
    (7, 12, 62),
    (12, 11, 17),
    (7, 8, 80),
    (8, 9, 19),
    (9, 32, 34),
    (9, 10, 37),
    (10, 23, 18),
    (10, 14, 23),
    (23, 22, 56),
    (23, 15, 56),
    (23, 15, 56),
    (15, 22, 43),
    (15, 21, 36),
    (21, 20, 45),
    (21, 19, 39),
    (15, 17, 60),
    (17, 18, 12),
    (18, 16, 15),
    (15, 24, 92),
    (24, 28, 44),
    (28, 26, 60),
    (15, 34, 125),
    (34, 35, 18),
    (2, 0, 93),
    (33, 26, 38),
]

def get_location_name(node_id):
    return LOCATIONS.get(node_id, f"Unknown({node_id})")

def get_all_locations():
    return LOCATIONS

def get_coordinates(node_id):
    return GPS_COORDINATES.get(node_id)