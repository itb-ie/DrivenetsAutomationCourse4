# find the 10 most used words in Dracula!
def word_frequency(book, len_words=0):
    """
    Construct a dictionary with all the words frequencies in the book
    :param len_words: the minimum size of the word
    :param book: the local filename
    :return: a dict where the key is the unique word, value is the number of times it shows up in the book
    """
    f = open(book)
    punctuation = ".,;'?!_-:\">=<"
    freq = {}
    for line in f:
        line = line.lower()
        for p in punctuation:
            line = line.replace(p, " ")
        words = line.split()
        for word in words:
            if len_words and len(word) < len_words:
                continue
            # there are 3 ways to do it, choose one!

            # if word in freq:
            #     freq[word] = freq[word] + 1
            # else:
            #     freq[word] = 1
            freq[word] = freq.get(word, 0) + 1
            # freq[word] = freq.setdefault(word, 0) + 1
    return freq


def get_max(freq: dict, top: int = 30):
    """
    return a list of tuples that are key, values with the most common frequencies
    :param freq: a dictionary of key, value, where the values are frequencies
    :param top: how many items to return
    :return: list of tuples containing they top (key, value)
    """
    result_list = []
    top_freq = list(freq.values())
    top_freq.sort(reverse=True)
    top_freq = top_freq[:top]

    # now we just need to match the keys to these values!! This will not be sorted!!
    # for k, v in freq.items():
    #     if v in top_freq:
    #         result_list.append((k, v))  # add the word/freq tuple in the result list
    #         continue

    for f in top_freq:
        for k, v in freq.items():
            if v == f:
                result_list.append((k, v))  # add the word/freq tuple in the result list
                del freq[k]
                break

    return result_list


freq = word_frequency("dracula.txt", 6)
print(get_max(freq, 10))
freq = word_frequency("frankenstein.txt", 6)
print(get_max(freq, 10))
