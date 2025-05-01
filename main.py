from stats import get_word_count  # Import the function from stats.py

def main():
    word_count = get_word_count("books/frankenstein.txt")  # Call the function
    print(f"{word_count} words found in the document")  # Print the result

main()

