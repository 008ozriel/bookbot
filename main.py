from stats import get_word_count  # Import the function from stats.py
from stats import count_characters  # Import the function from stats.py
from stats import get_text  # Import the function from stats.py

def main():
    word_count = get_word_count("books/frankenstein.txt")  # Call the function
    print(f"{word_count} words found in the document")  # Print the result


    text = get_text("books/frankenstein.txt")  # Call the function
    chars = count_characters(text)  # Call the function
    print(chars)  # Print the result

    

main()

