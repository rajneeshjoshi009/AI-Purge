# ui_effects.py - Handles text-based glitches, delays, and immersion effects

import time
import sys
import random

def glitch_text(text, glitch_rate=0.2):
    """
    Simulates glitchy AI output by randomly replacing characters.
    """
    glitched_output = ""
    for char in text:
        if random.random() < glitch_rate:
            glitched_output += random.choice(["#", "%", "&", "*", "?", "!"])
        else:
            glitched_output += char
        sys.stdout.write("\r" + glitched_output)
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n")

def redacted_text(text):
    """
    Simulates redacted text where parts of the message are hidden.
    """
    words = text.split()
    for i in range(len(words)):
        if random.random() < 0.3:  # 30% of words are redacted
            words[i] = "[REDACTED]"
    return " ".join(words)

def fake_time_lapse():
    """
    Creates an artificial delay to simulate AI processing.
    """
    print("Processing...")
    time.sleep(random.uniform(1.5, 3.0))
    print("...data inconsistencies detected...")
    time.sleep(random.uniform(1.0, 2.5))

def type_effect(text, delay=0.05):
    """
    Simulates a typing effect for AI responses.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print("\n")
