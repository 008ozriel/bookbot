def get_word_count(path_to_file):
     # Reads a file and returns the number of words in it
    with open(path_to_file) as f:
        file_contents = f.read()
    return len(file_contents.split())  # Count the words

def get_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents
    
def count_characters(text):
    chars = {}
    for char in text:
        char = char.lower()
        if char in chars:
            chars[char] += 1 
        else:
            chars[char] = 1
    
    return chars
    
