def main() -> None:
    book_path = "books/frankenstein.txt"
    text = get_text_from_book(book_path)
    wordcount = count_word(text)
    print(f"{wordcount} words found in the document")

def count_word(text:str) -> int:
    words = text.split()
    return len(words)

def get_text_from_book(path:str) -> str:
    with open(path) as f:
        return f.read()

if __name__ == "__main__":
    main()
