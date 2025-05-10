def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters = {}
    text = text.lower()
    for char in text:
        if char not in characters:
            characters[char] = 0
        characters[char] += 1
    return characters

def sort_on(dict):
    return dict["num"]

def sort_dictionary(dict):
    sorted_list = []
    for char in dict:
        sorted_list.append({"char": char, "num": dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list