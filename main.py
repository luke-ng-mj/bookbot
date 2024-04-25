from collections import Counter

path_to_file = "books/frankenstein.txt"

def count_words(content):
    words = content.split()
    return len(words)


def count_chars(content):
    cnt = Counter()
    for c in content:
        if c and c.isalpha():
            cnt[c.lower()] += 1

    return dict(cnt)


def print_report(content):
    #print(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    num_words = count_words(content)
    print(f"{num_words} words found in the document\n")

    char_count = count_chars(content)
    sorted_dict = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))
    #print(sorted_dict)
    for char, count in sorted_dict.items():
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")


def main():
    with open(path_to_file) as f:
        file_contents = f.read()
        print_report(file_contents)

print("Running...")
main()