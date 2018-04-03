import math
import string
import sys


def read_file(filename):  # Operation 1: read a text file
    try:
        f = open(filename, 'r')
        return f.read()
    except IOError:
        print "Error opening files: ", filename
        sys.exit()


translation_table = string.maketrans(string.punctuation+string.uppercase,
                                     " "*len(string.punctuation)+string.lowercase)


def get_words_from_line_list(text):  # Operation 2: split the text lines into words
    text = text.translate(translation_table)
    word_list = text.split()
    return word_list


def count_frequency(word_list):  # Operation 3: count frequency of each word
    D = {}
    for new_word in word_list:
        if new_word in D:
            D[new_word] = D[new_word] + 1
        else:
            D[new_word] = 1
    return D


def word_frequencies_for_file(filename):
    """
    Return dictionary of (word,frequency) pairs for the given file.
    """

    line_list = read_file(filename)
    word_list = get_words_from_line_list(line_list)
    freq_mapping = count_frequency(word_list)

    print "File",filename,":",
    print len(line_list),"lines,",
    print len(word_list),"words,",
    print len(freq_mapping),"distinct words"

    return freq_mapping


def inner_product(D1, D2):
    sum = 0.0
    for key in D1:
        if key in D2:
            sum += D1[key]*D2[key]
    return sum


def vector_angle(D1, D2):
    num = inner_product(D1, D2)
    den = math.sqrt(inner_product(D1, D1)*inner_product(D2, D2))
    return math.acos(num/den)


def main():
    if len(sys.argv) != 3:
        print "Usage: docdist8.py filename_1 filename_2"
    else:
        filename1 = sys.argv[1]
        filename2 = sys.argv[2]
        sort_word_list_1 = word_frequencies_for_file(filename1)
        sort_word_list_2 = word_frequencies_for_file(filename2)
        distance = vector_angle(sort_word_list_1, sort_word_list_2)
        print "The distance between the documents is: %0.6f (radians)" % distance


if __name__ == "__main__":
    import profile
    profile.run("main()")
