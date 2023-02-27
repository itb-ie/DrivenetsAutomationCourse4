import requests

# suppose you want to see which author has a wider vocabulary
frankenstein = "https://www.gutenberg.org/cache/epub/84/pg84.txt"
dracula = "https://www.gutenberg.org/cache/epub/345/pg345.txt"


def save_local_copy(book_url, book_name):
    """
    Save a local copy of the book, so I do not download it every time I run the code
    :param book_name: The name that I want to use for the local copy of the book
    :param book_url: The url where the book is located
    :return: None
    """
    r = requests.get(book_url)
    f = open(book_name, "wb")
    f.write(r.content)
    f.close()


# save_local_copy(frankenstein, "frankenstein.txt")

def count_unique_words(book):
    """
    Count the unique words inside the book
    :param book: Local filename for the book
    :return: The number of unique words, total words
    """
    unique_words = set()
    punctuation = ".,;'?!_-:\">=<"
    total_words_count = 0
    f = open(book)
    for line in f:
        line = line.lower()
        for p in punctuation:
            line = line.replace(p, " ")
        words = line.split()
        # only count words greater than 5 characters
        words = [word for word in words if len(word) > 5]
        total_words_count += len(words)
        unique_words_in_line = set(words)  # this makes a set of all the words in the line (so only unique words)
        unique_words = unique_words.union(unique_words_in_line)
    return len(unique_words), total_words_count


dracula_words, dracula_total_words = count_unique_words("dracula.txt")
frakenstein_words, frankenstein_total_words = count_unique_words("frankenstein.txt")
print(f"Dracula has {dracula_words} unique words vs Frankenstein that has {frakenstein_words} unique words")
print(f"Dracula has {dracula_total_words} total words vs Frankenstein that has {frankenstein_total_words} total words")
print(f"Dracula fraction: {dracula_words/dracula_total_words} vs Frankenstein fraction: {frakenstein_words/frankenstein_total_words}")

