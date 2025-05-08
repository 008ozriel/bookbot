from stats import get_word_count  # Import the function from stats.py
from stats import count_characters  # Import the function from stats.py
from stats import get_text  # Import the function from stats.py

def main():
    word_count = get_word_count("books/frankenstein.txt")  # Call the function
    print(f"{word_count} words found in the document")  # Print the result

    chars = count_characters(get_text("books/frankenstein.txt"))  # Call the function
    for char, count in sorted(chars.items()): # Iterate over the dictionary alphabetically
        print (f"{char}: {count}")  # Print the result

main()

