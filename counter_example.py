"""Word Frequency Counter"""

# Import Modules:
from collections import Counter

# Define main:
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


# Define word_count:
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
