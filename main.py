def main():
    book_path = "books/frankenstein.txt"
    content = get_book_content(book_path)
    word_count = get_word_count(content)
    letter_counts = get_letter_count(content)
    display_results(word_count, letter_counts,book_path)

def get_book_content(book_path):
    with open(book_path) as f:
        content = f.read()
    return content

def get_word_count(book_contents):
    return len(book_contents.split())

def get_letter_count(book_contents):
    content_lowered = book_contents.lower()
    
    word_list = content_lowered.split()
    
    letter_counts = {}
    
    for word in word_list:
        for letter in word:
            if letter.isalpha():
                if letter not in letter_counts:
                    letter_counts[letter] = 1
                else:
                    letter_counts[letter] += 1
    
    return letter_counts

def display_results(word_count, letter_counts,book_path):
    print(f"--- Report of {book_path} --- \n")
    print(f"{word_count} words were found in the text.\n")
    
    letter_counts = [x[::-1] for x in letter_counts.items()]
    letter_counts.sort(reverse=True)
    
    for num,letter in letter_counts:
        print(f"The letter {letter} was found {num} times.")
    print("--- End report --- \n")
main()