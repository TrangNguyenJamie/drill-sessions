import random
from pathlib import Path
import requests


# Lấy 1 quote online làm fallback
try:
    resp = requests.get("https://api.quotable.io/random", timeout=3)
    alt_oracle = resp.json().get("content")
except Exception:
    alt_oracle = "Arg, you arent even deserved a boring quote... Embrace the uncertainty!"

default_fallback = (f"Oracle Warehouse cannot be found. Apparently, the universe forgot to deploy. Your fate in your hands! Here's an random boring quote for you:\n\n{alt_oracle}")


def get_random_oracle(filepath: str | Path = 'assets/oracle.txt') -> str:
    path = Path(filepath)

    if not path.exists():
        return default_fallback
    with path.open('r',  encoding="utf-8") as file:
        content = file.read() 
    
    # Keep the oracles that are not empty after stripping whitespace
    oracles = [oracle.strip() for oracle in content.split(",") if oracle.strip()]

    # Error catch: if no valid oracles found, return default fallback
    if not oracles:
        return default_fallback
    
    return random.choice(oracles)
