"""Word Frequency Counter"""


# Description: The following program takes a sentence from the user
# and determines the word frequency using the Counter module:


# Import Modules:
from collections import Counter


# Gets a sentence and a level from the user to determine
# the frequency of word occurence:
def main():
    """The main function"""

    print()

    # Get sentence for word frequency count:
    sentence = input("Enter a sentence for the word frequency count: ")

    print()

    # Define level of frequency:
    level = int(input("Enter a non-negative integer for the level of " \
    "frequency. For example, enter '3' to get the top 3 words: "))

    print()

    # Get frequent words:
    frequent_words = word_frequency(sentence, level)

    # Display frequent words:
    print(frequent_words)


# Takes a sentence and a level and returns the frequency
# of words depending on the level:
def word_frequency(sentence, level):
    """Count word frequency"""

    # Split into list of words:
    words = sentence.split()

    # Create Counter object:
    counter = Counter(words)

    # Get top three most common words:
    result = counter.most_common(level)

    # Display top three most common words:
    return result


# Call main:
main()
