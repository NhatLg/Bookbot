def main() -> None:
    book_path = "books/frankenstein.txt"
    text = get_text_from_book(book_path)
    wordcount = count_word(text)
    freq_char = generate_char_freq_dict(text.lower())
    freq_char_list = dict_to_list(freq_char)
    freq_char_list.sort(reverse=True, key=sort_on)
    print_report(wordcount, freq_char_list)

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

def sort_on(dict):
    return dict["num"]

def dict_to_list(my_dict:dict) -> list:
    resulted_list = []
    for i in my_dict:
        resulted_list.append({"name": i, "num": my_dict[i]})
    return resulted_list

def print_report(wordcount:int, freq_char_list:list) -> None:
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{wordcount} words found in the document\n")
    for char_dict in freq_char_list:
        if char_dict["name"].isalpha():
            print(f"The '{char_dict["name"]}' character was found {char_dict["num"]} times")
    print("--- End report ---")

if __name__ == "__main__":
    main()
    