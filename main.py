# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from itertools import count
import string


def read_file_content(filename):
    # [assignment] Add your code here
    with open('story.txt', 'r') as f:
        each_lines = f.read()
    return each_lines


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    new_text = text.translate(str.maketrans('', '', string.punctuation))
    words = new_text.split(' ')
    count = {}

    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count  

print(count_words())

