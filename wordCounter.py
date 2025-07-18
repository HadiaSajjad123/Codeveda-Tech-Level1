def wordCounter(filename):
    try:
        with open(filename, "r") as file:
            text = file.read()
            words = text.split()
            num_words = len(words)
            print("Number of words:", num_words)
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("Error:", e) 

def count_alphabet(filename):
    try:
        with open(filename, "r") as file:
            text = file.read()
            alphabet_count = 0
            for word in text.split():
                for char in word:
                    if char.isalpha():
                        alphabet_count += 1
            print("Number of alphabet characters:", alphabet_count)
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("Error:", e)

wordCounter('random_words.txt')
count_alphabet('random_words.txt')