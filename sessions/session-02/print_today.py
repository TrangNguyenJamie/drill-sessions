from datetime import date

def print_today() -> str:
    today = date.today().isoformat()
    print(today)



if __name__ == "__main__":
    print_today()
