def get_word_count(path_to_file):
     # Reads a file and returns the number of words in it
    with open(path_to_file) as f:
        file_contents = f.read()
    return len(file_contents.split())  # Count the words