def get_word_count(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_word_count("books/frankenstein.txt")
    word_count = len(text.split())
    print(f"{word_count} words found in the document")

main()