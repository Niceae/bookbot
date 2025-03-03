import sys
def get_book_text(path): 
    with open(path) as f: # do something with f (the file) here
        # f is a file object
        file_contents = f.read()
    return file_contents
def count_words(text):
        words = text.split()
        word_count = len(words)
        return word_count
def count_characters(text):
    character_dict = {}
    characters=text.lower()
    for character in characters:
        if character.isalpha():
            if character not in character_dict:
                character_dict[character] = 1
            else:
                character_dict[character] += 1
    return character_dict
def sort_on(character_dict):
    character_tuples= [(char, count) for char, count in character_dict.items()]
    character_tuples.sort(reverse=True, key=lambda x: x[1])
    return character_tuples
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    
    # File being analyzed
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    
    # Word count
    word_count = count_words(text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    
    # Character count
    char_counts = count_characters(text)
    sorted_chars = sort_on(char_counts)
    print("--------- Character Count -------")
    for char, count in sorted_chars:
        print(f"{char}: {count}")
    
    # End of report
main()