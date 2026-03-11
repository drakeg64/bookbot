import sys
from stats import get_num_words, get_num_char, sort_by_count

def get_book_text(path):
    with open(path) as f:
        return f.read()

    

def main():
    if (len(sys.argv)) != 2:
         print("Usage: python3 main.py <path_to_book>")
         sys.exit(1)
    book = get_book_text(sys.argv[1])
    num_words = get_num_words(book)
    num_char = get_num_char(book)
    sorted_char = sort_by_count(num_char)
    
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for item in sorted_char:
        if item["char"].isalpha():
                print(f"{item["char"]}: {item["num"]}")
        else:
            continue



main()