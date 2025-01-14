def main():
    FILE_PATH = "books/frankenstein.txt" 
    with open(FILE_PATH) as f:
        file_contents = f.read()
        file_words = count_words(file_contents)
        file_characters = count_characters(file_contents)
        file_characters_sorted = sort_characters_dict(file_characters)
        
        # Printing Report
        print(f"--- Begin report of {FILE_PATH} ---")
        print(f"{file_words} words found in the document\n")
        for ch in file_characters_sorted:
            print(f"The '{ch["character"]} character was found {ch["count"]} times")
        print("--- End report ---")

def sort_on(dict):
    return dict["count"]

def sort_characters_dict(dict):
    characters_list = []
    for ch, count in dict.items():
        characters_list.append({ "character": ch, "count": count })
    characters_list.sort(reverse=True, key=sort_on)
    return characters_list

def count_characters(text):
    character_count = {}
    for word in text.split():
        for ch in list(word):
            character = ch.lower()
            if character.isalpha() == False:
                continue
            if character in character_count:
                character_count[character] += 1
            else:
                character_count[character] = 1
    return character_count

def count_words(text):
    return len(text.split())

main()
