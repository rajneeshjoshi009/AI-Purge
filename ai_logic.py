# ai_logic.py - Handles AI Responses and Judgment System

from stats import RP, CB, CPR

def immediate_response(RP_change, CB_change):
    """
    Generates an immediate AI response based on RP & CB changes.
    """
    if RP_change > 0:
        return "Risk appetite detected. Calculating volatility impact."
    elif RP_change < 0:
        return "Caution protocol registered. Predictability increasing."
    
    if CB_change > 0:
        return "Cognitive bias reinforcement detected."
    elif CB_change < 0:
        return "Bias disruption noted. Unpredictability increasing."

    return "Behavioral data updated."

def cpr_based_response():
    """
    Generates a response based on long-term CPR trends.
    """
    if CPR <= 3:
        return "Patterns stable. Behavior fixed. Minimal deviation detected. Possible Purge Candidate."
    elif CPR >= 7:
        return "Patterns unstable. Subject resists classification. Anomaly detected."
    return "Adaptation present. Evaluation ongoing."

def final_AI_judgment():
    """
    Determines the player's final classification.
    """
    if CPR <= 3:
        return "Predictable. Minimal deviation detected. RESULT: PURGED."
    elif CPR >= 7:
        return "Unstable behavior. Subject cannot be controlled. RESULT: PURGED."
    return "Behavior patterns consistent. Adaptation present, but controlled. RESULT: PRESERVED—for now."
