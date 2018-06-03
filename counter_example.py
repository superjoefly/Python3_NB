"""Word Frequency Counter"""

# Import Modules:
from collections import Counter

def main():
    """Word Frequency Counter"""

    # Assign sentence
    sentence = "The momentous change licenses the rain. The current " \
    "debugs the record. The son reinforces the start. The invincible " \
    "mist relates the fear. The maniacal insurance resolves the " \
    "son."

    # Split into list of words
    words = sentence.split()

    counter = Counter(words)

    top_three = counter.most_common(3)

    print(top_three)



main()
