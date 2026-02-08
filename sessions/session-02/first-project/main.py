from myapp.reader import build_quote_message, default_fallback, get_random_oracle
from myapp.effect_maker import wait_for_oracle, print_word_by_word

def main():
    
    wait_for_oracle()
    oracle = get_random_oracle()

    if oracle == default_fallback:
        answer = input("Want a boring quote instead? (y/n): ").strip().lower()
        if not answer.startswith("y"):
            print("Bye bye!")
            return
        quote = build_quote_message()
        print_word_by_word(quote or default_fallback)
        return

    print(oracle)



if __name__ == "__main__":
    main()
