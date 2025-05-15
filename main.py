from stats import get_word_count  # Import the function from stats.py
from stats import count_characters  # Import the function from stats.py
from stats import get_text  # Import the function from stats.py

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    word_count = get_word_count("books/frankenstein.txt")  # Call the function
    print(f"Found {word_count} total words")  # Print the result
    print("----------- Character Count -----------")
    chars = count_characters(get_text("books/frankenstein.txt"))  # Call the function
    for char, count in sorted(chars.items()): # Iterate over the dictionary alphabetically
        print (f"{char}: {count}")  # Print the result

main()
