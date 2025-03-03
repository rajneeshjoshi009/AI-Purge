# stats.py - Handles Player Stats (RP, CB, CPR)

# Initialize Stats
RP = 50  # Risk Propensity (1-100)
CB = 50  # Cognitive Bias (1-100)
CPR = 5  # Cognitive Pattern Recognition (1-10)

def update_stats(RP_change=0, CB_change=0, CPR_change=0):
    """
    Updates player stats while ensuring values stay within valid ranges.
    """
    global RP, CB, CPR
    RP = max(0, min(100, RP + RP_change))  # Keep RP between 0-100
    CB = max(0, min(100, CB + CB_change))  # Keep CB between 0-100
    CPR = max(1, min(10, CPR + CPR_change))  # Keep CPR between 1-10

def get_stats():
    """
    Returns the current values of RP, CB, and CPR.
    """
    return {"RP": RP, "CB": CB, "CPR": CPR}
