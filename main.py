from stats import count_words, count_characters, sort_dictionary
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    number_of_words = count_words(text)
    characters = count_characters(text)
    sorted_characters = sort_dictionary(characters)
    print_results(filepath, number_of_words, sorted_characters)
    



def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
    
def print_results(filepath, words, character_counts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for character in character_counts:
        if character["char"].isalpha():
            print(f"{character["char"]}: {character["num"]}")
    print("============= END ===============")

    
main()
    
    
    
    
    
