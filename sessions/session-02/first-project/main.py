from myapp.reader import get_random_oracle
from myapp.effect_maker import wait_for_oracle

def main():
    oracle = get_random_oracle()
    wait_for_oracle()
    print(oracle)



if __name__ == "__main__":
    main()
