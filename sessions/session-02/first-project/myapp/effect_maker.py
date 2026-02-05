import time 
from myapp.utils.print_effect import print_word_by_word    


def wait_for_oracle():
    """ Mostly just for dramatic effect. Consider adding more interactive elements here."""
    steps = [
        "Today, I shall assist you in receiving the Oracle of the Day...",
        "First, you must focus your mind and channel your energy... somewhere.",
        "Honestly, I have no idea where ~~ but please, just focus.",
        "Focus harder...",
        "Even harder...",
        "Are you actually focusing right now?",
        "I dont...",
        "Anyway, the universe is clearing its throat.",
    ]


    for step in steps:
        print_word_by_word(step)
        time.sleep(0.8)  # Pause for dramatic effect

    time.sleep(1)
    input("\nPress Enter when you are ready to hear the oracle's wisdom...")