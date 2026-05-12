# campus_data.py — REAL DSCE Campus Locations & Paths

LOCATIONS = {
    0:  "Main Gate",
    1:  "Admin Block",
    2:  "CS/IS Block",
    3:  "ECE/TC Block",
    4:  "ME/CV Block",
    5:  "EEE/AE Block",
    6:  "Central Library",
    7:  "Lab Complex",
    8:  "NRI Canteen",
    9:  "Boys Hostel",
    10: "Girls Hostel",
    11: "CPA Auditorium",
    12: "Sports Ground",
    13: "Medical Center",
    14: "Parking Lot",
    15: "Bus Stop"
}

# Edges: (from, to, distance_meters) — estimated from 30-acre campus layout
EDGES = [
    (0,  14, 40),    # Main Gate ↔ Parking Lot
    (0,  15, 30),    # Main Gate ↔ Bus Stop
    (0,  1,  120),   # Main Gate ↔ Admin Block
    (1,  2,  80),    # Admin Block ↔ CS/IS Block
    (1,  6,  100),   # Admin Block ↔ Central Library
    (1,  11, 90),    # Admin Block ↔ CPA Auditorium
    (2,  3,  70),    # CS/IS Block ↔ ECE/TC Block
    (2,  7,  60),    # CS/IS Block ↔ Lab Complex
    (3,  5,  80),    # ECE/TC Block ↔ EEE/AE Block
    (3,  7,  65),    # ECE/TC Block ↔ Lab Complex
    (4,  5,  75),    # ME/CV Block ↔ EEE/AE Block
    (4,  12, 100),   # ME/CV Block ↔ Sports Ground
    (5,  7,  90),    # EEE/AE Block ↔ Lab Complex
    (6,  7,  110),   # Central Library ↔ Lab Complex
    (6,  11, 80),    # Central Library ↔ CPA Auditorium
    (7,  8,  120),   # Lab Complex ↔ NRI Canteen
    (8,  9,  90),    # NRI Canteen ↔ Boys Hostel
    (8,  10, 85),    # NRI Canteen ↔ Girls Hostel
    (8,  13, 70),    # NRI Canteen ↔ Medical Center
    (9,  10, 60),    # Boys Hostel ↔ Girls Hostel
    (9,  13, 80),    # Boys Hostel ↔ Medical Center
    (10, 12, 130),   # Girls Hostel ↔ Sports Ground
    (11, 12, 150),   # CPA Auditorium ↔ Sports Ground
    (12, 14, 200),   # Sports Ground ↔ Parking Lot
]

def get_location_name(node_id):
    return LOCATIONS.get(node_id, f"Unknown({node_id})")

def get_all_locations():
    return LOCATIONS