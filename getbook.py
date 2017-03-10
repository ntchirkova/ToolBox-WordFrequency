import pickle
import requests

book = requests.get('http://www.gutenberg.org/ebooks/42671.txt.utf-8')
f = open('austen.pickle', 'wb')
pickle.dump(book.text, f)
f.close()
