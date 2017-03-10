""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string
import pickle

input_file = open('austen.pickle', 'rb')
book = pickle.load(input_file)

def get_word_list(book):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    #strips the header
    start = book.index('***START OF THE PROJECT GUTENBERG EBOOK PRIDE AND PREJUDICE***') + len('***START OF THE PROJECT GUTENBERG EBOOK PRIDE AND PREJUDICE***')
    book = book[start:len(book)]
    book = book.lower()
    word_list = book.split()
    return word_list


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """
    d = dict()
    for w in word_list:
        d[w] = d.get(w, 0) + 1
    ordered_by_frequency = sorted(d, key=d.get, reverse=True)
    return ordered_by_frequency[0:n]

if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    word_list = get_word_list(book)
    print(get_top_n_words(word_list, 100))
