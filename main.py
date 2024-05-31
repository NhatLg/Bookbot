def main() -> None:
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        wordcount = count_word(file_contents)
        print(wordcount)

def count_word(text:str) -> int:
    words = text.split()
    return len(words)

if __name__ == "__main__":
    main()
