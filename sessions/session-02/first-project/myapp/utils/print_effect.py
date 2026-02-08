import time

def print_word_by_word(text:str, delay:float=0.2):
    words = text.split()
    for word in words:
        print(word, end=" ", flush=True)
        time.sleep(delay)
    print()  # Enter after finishing the sentence
