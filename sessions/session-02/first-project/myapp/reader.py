from myapp.utils.print_effect import print_word_by_word
import random
from pathlib import Path
import requests

default_fallback = ("""Apparently, the universe forgot to deploy. Your fate in your hands!""")

def get_random_oracle(filepath: str | Path = 'assets/oracle.txt') -> str:
    try:
        path = Path(filepath)
    except TypeError:
        raise TypeError("filepath must be str or Path")
    
    if not path.exists():
        print("Bad. No oracle warehouse found in this universe.")
        return default_fallback
    with path.open('r',  encoding="utf-8") as file:
        content = file.read() 
    
    # Keep the oracles that are not empty after stripping whitespace
    oracles = [oracle.strip() for oracle in content.split(",") if oracle.strip()]

    # Error catch: if no valid oracles found, return default fallback
    if not oracles:
        print("This universe is vacant of oracles.")
        return default_fallback
    
    return random.choice(oracles)

def build_quote_message() -> str:
    try:
        resp = requests.get("https://api.quotable.io/random", timeout=3)
        resp.raise_for_status()
        alt_oracle = resp.json().get("content")
        return alt_oracle
    except TimeoutError:
        print_word_by_word("Time-out. The parallel universe is not responding.")
    except ConnectionError:
        print_word_by_word("Connection error. Cannot reach the parallel universe.")
    except Exception:
        print_word_by_word("An unexpected error occurred while fetching the boring quote.")
    


