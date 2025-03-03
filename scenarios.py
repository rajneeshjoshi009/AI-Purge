# scenarios.py - Stores all scenario data and choices

scenarios = [
    {
        "title": "All In or Fold",
        "description": "You’ve invested heavily into an unstable project. Do you continue?",
        "choices": {
            "1": {"text": "Drill deeper despite instability.", "RP_change": +10, "CB_change": +5, "CPR_change": -3},
            "2": {"text": "Cease operations immediately.", "RP_change": -5, "CB_change": +10, "CPR_change": -2}
        }
    },
    {
        "title": "The Phantom Signal",
        "description": "A distress signal from deep space appears. It could be a trap.",
        "choices": {
            "1": {"text": "Respond and investigate.", "RP_change": +10, "CB_change": -10, "CPR_change": +3},
            "2": {"text": "Ignore and continue mission.", "RP_change": -5, "CB_change": +10, "CPR_change": -2}
        }
    }
    # Add all 7 scenarios in this format
]

def get_scenario(index):
    """
    Retrieves a scenario based on its index.
    """
    if 0 <= index < len(scenarios):
        return scenarios[index]
    return None
