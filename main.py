def main() -> None:
    book_path = "books/frankenstein.txt"
    text = get_text_from_book(book_path)
    wordcount = count_word(text)
    freq_char = generate_char_freq_dict(text.lower())
    print(f"{wordcount} words found in the document")
    print(freq_char)

def count_word(text:str) -> int:
    words = text.split()
    return len(words)

def get_text_from_book(path:str) -> str:
    with open(path) as f:
        return f.read()

def generate_char_freq_dict(text:str) -> dict:
    freq_dict = {}
    for i in text:
        freq_dict[i] = freq_dict.get(i, 0) + 1
    return freq_dict


if __name__ == "__main__":
    main()
