def main():
    book_path = "books/frankenstein.txt"
    text = print_text(book_path)
    letters_repeating = get_letters_repeating(text)
    word_count = get_number_of_words(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    for letter, count in letters_repeating:
        print (f"The '{letter}' character was found {count} times")
    print("--- End report ---")

def print_text(path):
    with open(path) as f:
        return f.read()
    
def get_number_of_words(text):
    words = text.split()
    return len(words)

def get_letters_repeating(text):
    counted_letters = {}
    lowered_text = text.lower()
    for letter in lowered_text:
        if letter.isalpha():
            if letter in counted_letters: 
                counted_letters[letter] += 1
            else:
                counted_letters[letter] = 1
    sorted_letters = sorted(counted_letters.items(), key=lambda x: x[1], reverse=True)
    return sorted_letters

main()