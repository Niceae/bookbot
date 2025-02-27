def get_book_text(): 
    with open("books/frankenstein.txt") as f: # do something with f (the file) here
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
        if character not in character_dict:
            character_dict[character] = 1
        else:
             character_dict[character] += 1
    return character_dict
def main():
    text = get_book_text()
    count = count_words(text)
    print (f"word count: {count}")
    char_counts = count_characters(text)
    print(char_counts)
main()