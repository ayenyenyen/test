__author__ = 'Lemmeister'


# Exercise 10.1
def nested_sum(a_list):
    new_list = []
    for l in a_list:
        total = 0
        for i in l:
            total += i
        new_list.append(total)
    print('Exercise 10.1: %s' % new_list)

nested_list = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
#nested_sum(nested_list)


# Exercise 10.2
def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res


def capitalize_nested(a_list):
    new_nested_list = []
    for i in a_list:
        new_nested_list.append(capitalize_all(i))
    return new_nested_list


nested_list = [['l', 'e', 'm', 'u', 'e', 'l']]
#print('Exercise 10.2: %s' % capitalize_nested(nested_list))


# Exercise 10.3
def summation(a_list):
    sums = []
    total = 0
    for i in a_list:
        total += i
        sums.append(total)
    return sums

numbers = [1, 2, 3, 4, 5]
#print('Exercise 10.3: %s' % summation(numbers))


# Exercise 10.4
def middle(a_list):
    return a_list[1:-1]

numbers = [1, 2, 3, 4]
#print('Exercise 10.4: %s' % middle(numbers))


# Exercise 10.5
def chop(a_list):
    del a_list[0]
    del a_list[-1]
    print('Exercise 10.5: %s' % a_list)
    return None

numbers = [1, 2, 3, 4]
#chop(numbers)


# Exercise 10.6
def is_sorted(a_list):
    index = 0
    for i in a_list:
        if a_list[index] > a_list[index+1]:
            return False
        else:
            if index == len(a_list)-2:
                return True
            else:
                index += 1
    return True

my_list = [1, 2, 3, 4, -1]
#print('Exercise 10.6: %s' % is_sorted(my_list))


# Exercise 10.7
def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

str1 = 'gwapoko'
str2 = 'kogwapo'
#print('Exercise 10.7: %s' % is_anagram(str1, str2))


# Exercise 10.8 Problem 1
def has_duplicates(a_list):
    for i in a_list:
        count = 0
        for l in a_list:
            if l == i:
                count += 1
                if count == 2:
                    return True
    return False

a_list = [1, 1, 2, 3, 4, 5]
#print('Exercise 10.8 Problem 1: %s' % has_duplicates(a_list))


# Exercise 10.8 Problem 2
import random

NUMBER_OF_STUDENTS = 23
TRIALS = 100


def generate_random_birthdays():
    return [random.randint(1, 365) for student in range(NUMBER_OF_STUDENTS)]


def stats(TRIALS):
    duplicate_count = 0
    for i in range(TRIALS):
        if has_duplicates(generate_random_birthdays()):
            duplicate_count += 1
    print('Exercise 10.8 Problem 2: ' + "In %d classrooms with %d students, %.1f%% had students\
 with duplicate birthdays." % (TRIALS, NUMBER_OF_STUDENTS, (float(duplicate_count) / TRIALS) * 100))

#stats(TRIALS)


# Exercise 10.9
def remove_duplicates(a_list):
    return list(set(a_list))

a_list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
#print('Exercise 10.9: %s' % remove_duplicates(a_list))


# Exercise 10.10 Version 1
with open('words.txt') as fd:
    words = fd.read().split()


def read_words_v1(words):
    word_list = []
    for line in words:
        line = line.strip()
        word_list.append(line)
    return word_list

#print('Exercise 10.10 Version 1: %s' % type(read_words_v1(words)))


# Exercise 10.10 Version 2
def read_words_v2(words):
    word_list = []
    for line in words:
        line = line.strip()
        word_list += [line]
    return word_list

#print('Exercise 10.10 Version2: %s' % type(read_words_v2(words)))


# Exercise 10.11
with open('words.txt') as fd:
    word_list = fd.read().splitlines()


def bisect(myWord, myList):
    original = myList
    while True:
        middle = int(len(myList) / 2)
        if myWord > myList[middle]:
            myList = myList[middle:]
        elif myWord < myList[middle]:
            myList = myList[:middle]
        elif myWord == myList[middle]:
            return original.index(myWord)

        if len(myList) == 1:
            if myWord != myList[:]:
                return None
            else:
                return original.index(myWord)


#print('Exercise 10.11: %s' % bisect("danger", word_list))


# Exercise 10.12
with open('words.txt') as fd:
    word_list = fd.read().splitlines()

word_dict = {word: None for word in word_list}

def find_rev_pairs(word_dict):
    for word in word_dict:
        if word[::-1] in word_dict:
            print(word, word[::-1])

#print('Exercise 10.12:')
#find_rev_pairs(word_dict)


# Exercise 10.13
with open('words.txt') as fd:
    word_list = fd.read().splitlines()

word_dict = {word: None for word in word_list}


def split_word(word):
    word1 = word[::2]
    word2 = word[1::2]
    return word1, word2


def find_interlocked():
    for word in word_dict:
        split0 = split_word(word)[0]
        split1 = split_word(word)[1]
        if split0 in word_dict and split1 in word_dict:
                print(word, split0, split1)


def split_word2(word, i):
    split0 = word[i::3]
    split1 = word[i + 1::3]
    split2 = word[i + 2::3]
    return split0, split1, split2


def find_3way():
    answer = []
    for word in word_dict:
        for i in range(0, 3):
            split_ = split_word2(word, i)
            if (split_[0] in word_dict and
                split_[1] in word_dict and
                split_[2] in word_dict):
                    answer.append((word,
                           split_[0],
                           split_[1],
                           split_[2]))
    return answer

#print('Exercise 10.13: ')
#print(find_3way())


# Exercise 11.1
import uuid

with open('words.txt') as fd:
    words = fd.read().splitlines()

result = dict()


def dictionary():
    for line in words:
        result[line] = uuid.uuid4()
    return result

#print('Exercise 11.1:')
#print(dictionary())


# Exercise 11.2
def histogram(word):
    dictionary = dict()
    for character in word:
        dictionary[character] = 1 + dictionary.get(character, 0)
    return dictionary

#print('Exercise 11.2: %s' % histogram('lemuel jay vallinas'))


# Exercise 11.3
def print_hist(histogram):
    histoList = histogram.keys()
    for letter in sorted(histoList):
        print(letter, histogram[letter])

h = histogram('lemuel jay vallinas gwapo')
#print('Exercise 11.3:')
#print_hist(h)

# Exercise 11.4
def reverse_lookup(dictionary, value):
    results = []
    for key in dictionary:
        if dictionary[key] == value:
            results.append(key)
    return results


def histogram(word):
    dictionary = dict()
    for letter in word:
        dictionary[letter] = 1 + dictionary.get(letter, 0)
    return dictionary

h = histogram('lemuel jay vallinas')
k = reverse_lookup(h, 4)
#print('Exercise 11.4: %s' % k)


# Exercise 11.5
def histogram(word):
    dictionary = dict()
    for letter in word:
        dictionary[letter] = 1 + dictionary.get(letter, 0)
    return dictionary


def invert_dict(d):
    inv = dict()
    for key in d:
        val = d[key]
        inv.setdefault(val, [])
        inv[val].append(key)
    return inv

hist = histogram('lemuel jay vallinas')
inv = invert_dict(hist)
#print('Exercise 11.5: %s' % inv)


# Exercise 11.6
known = {0: 0, 1: 1}


def fibonacci_given(n):
    if n in known:
        return known[n]
    else:
        res = fibonacci_given(n - 1) + fibonacci_given(n - 2)
    known[n] = res
    return res


def fibonacci_original(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_original(n - 1) + fibonacci_original(n - 2)


# Exercise 11.7
cache = {}


def ackermann(m, n):
    """
        Credits to the owner:
        http://thinkpython.com/code/ackermann_memo.py
    """
    """
    :param m:
    :param n:
    :return:
    """
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)
    try:
        return cache[m, n]
    except KeyError:
        cache[m, n] = ackermann(m-1, ackermann(m, n-1))
        return cache[m, n]

#print('Exercise 11.7:')
#print(ackermann(3, 4))
#print(ackermann(3, 6))


# Exercise 11.9
def has_dups(myList):
    dictionary = {}
    for item in myList:
        dictionary[item] = 1 + dictionary.get(item, 0)
        if dictionary[item] > 1:
            return True
    return False

#listOne = [1, 2, 3, 4, 5, 5]
#print(has_dups(listOne))


# Exercise 11.10
def normalize(x):
    if x > 122:
        while x > 122:
            x -= 26
    elif x < 97:
        while x < 97:
            x += 26
    return x


def rotate_word(word, amount):
    new_word = ''
    for letter in word:
        letter = letter.lower()
        if ord(letter) + amount > 122:
            new_word += chr(normalize(ord(letter) + amount))
        elif ord(letter) + amount < 97:
            new_word += chr(normalize(ord(letter) + amount))
        else:
            new_word += chr(ord(letter) + amount)
    return new_word

with open('words.txt') as fd:
    word_list = fd.read().splitlines()

word_dict = {word: None for word in word_list}


def find_rot_pairs():
    final_list = []
    for word in word_dict:
        for i in range(1, 26):
            if rotate_word(word, i) in word_dict:
                final_list.append((word, i, rotate_word(word, i)))
    final_list.sort()
    for pair in final_list:
        print(pair)

#print('Exercise 11.10:')
#find_rot_pairs()


# Exercise 11.11
def read_dictionary(filename):

    d = dict()
    fin = open(filename)
    for line in fin:

        # skip over the comments
        if line[0] == '#': continue

        t = line.split()
        word = t[0].lower()
        pron = ' '.join(t[1:])
        d[word] = pron

    return d


def make_word_dict():
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = word

    return d


def homophones(a, b, phonetic):
    if a not in phonetic or b not in phonetic:
        return False

    return phonetic[a] == phonetic[b]


def check_word(word, word_dict, phonetic):
    word1 = word[1:]
    if word1 not in word_dict:
        return False
    if not homophones(word, word1, phonetic):
        return False

    word2 = word[0] + word[2:]
    if word2 not in word_dict:
        return False
    if not homophones(word, word2, phonetic):
        return False

    return True

phonetic = read_dictionary('words.txt')
word_dict = make_word_dict()
#print('Exercise 11.11:')
#for word in word_dict:
#    if check_word(word, word_dict, phonetic):
#        print(word, word[1:], word[0] + word[2:])


# Exercise 12.1
def sum_all(*args):
    return sum(args)

#print('Exercise 12.1:')
#print(sum_all(1, 2, 3))
#print(sum_all(1, 2, 3, 4, 5))
#print(sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# Exercise 12.2
import random


def sort_by_length(words):
    t = []
    for word in words:
       t.append((len(word), word))

    t.sort(reverse=True)

    res = []
    for length, word in t:
        res.append(word)
    return res


def sort_by_length_random(words):
    t = []
    for word in words:
       t.append((len(word), random.random(), word))

    t.sort(reverse=True)

    res = []
    for length, _, word in t:
        res.append(word)
    return res

words = ['Lemuel', 'Jay', 'Zoemar', 'Vince', 'George', 'Georges']

t = sort_by_length_random(words)
#print('Exercise 12.3.:')
#for x in t:
#    print(x)

# Exercise 12.3
text = 'The rain in Spain falls mainly on the plains!!!!'


def make_dict(x):
    dictionary = {}
    for letter in x:
        dictionary[letter] = 1 + dictionary.get(letter, 0)
    return dictionary


def most_frequent(text):
    letters = [letter.lower() for letter in text if letter.isalpha()]
    dictionary = make_dict(letters)
    result = []
    for key in dictionary:
        result.append((dictionary[key], key))
    result.sort(reverse=True)
    for count, letter in result:
        print(letter, count)

#print('Exercise 12.3:')
#most_frequent(text)


# Exercise 12.4
with open('words.txt', 'r') as fd:
    words = fd.read().splitlines()

def make_anagram_dict(word_list):
    '''Take a list of words, return a dict with a fingerprint as the key
    and the anagrams made from that fingerprint as the value.'''
    anagrams = dict()
    for word in word_list:
        fp = ''.join(sorted(word))
        anagrams[fp] = anagrams.get(fp, [])
        anagrams[fp].append(word)

    anagrams = {fp: anagrams[fp] for fp in anagrams if len(anagrams[fp]) > 1}
    return anagrams

anagrams = make_anagram_dict(words)

def print_anagrams(anagrams):
    '''Uses a generator to call and print 5 items from mydict'''
    fp = (fp for fp in anagrams)

    print "Sample from anagram dict:"
    for i in range(1, 6):
        # call once, print twice
        fp_next = fp.next()
        print "%s) %s:" % (i, fp_next), anagrams[fp_next]

    print "..."
    print "\n"


print_anagrams(anagrams)


def sort_anagrams(anagrams):
    '''Returns a list of lists containing all anagram matches. The longest list
     (most anagrams) is at the top'''
    anagrams_lists = []
    for fp in anagrams:
        anagrams_lists.append(anagrams[fp])
    anagrams_lists.sort(key=len, reverse=True)

    print "Most anagrams:"
    for i in range(0, 5):
        print "%s) %d" % ((i + 1), len(anagrams_lists[i])), anagrams_lists[i]
    print "..."
    print "\n"


sort_anagrams(anagrams)


def find_bingos(anagrams):
    '''Filters mydict for keys of length 8. Sorts a list of the values
     (lists) and sorts by length in reverse order'''
    candidates = [anagrams[key] for key in anagrams if len(key) == 8]
    candidates.sort(key=len, reverse=True)

    print "Top Bingos:"
    for i in range(0, 5):
        fp = ''.join(sorted(candidates[i][0]))
        print "%s) %d: %s" % ((i + 1), len(candidates[i]), fp), candidates[i]

    print "..."
    print "\n"

find_bingos(anagrams)


def is_metathesis(reference, test):
    '''If two anagrams mismatch exactly twice they are metathesis pairs.
     Caution: This function assumes strings of equal length'''
    i = 0
    count = 0
    while i <= (len(reference) - 1):
        if reference[i] != test[i]:
            count += 1
        i += 1
    if count == 2:
        return True
    return False


def find_metathesis(anagrams):
    '''mydict values are lists, we use index 0 as a reference and check the
     rest of the list (1 to end of list) against that reference word.'''
    answer = []
    for fp in anagrams:
        reference = anagrams[fp][0]
        for i in range(1, (len(anagrams[fp]) - 1)):
            test = anagrams[fp][i]
            if is_metathesis(reference, test):
                answer.append([reference, test])

    print("Sample of metathesis pairs:")
    for i in range(0, 5):
        print("%s)" % (i + 1), answer[i])
    print("...")

find_metathesis(anagrams)


# Exercise 12.6
def make_word_dict():
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = word

    # have to add single letter words to the word list;
    # also, the empty string is considered a word.
    for letter in ['a', 'i', '']:
        d[letter] = letter
    return d

memo = {}
memo[''] = ['']


def is_reducible(word, word_dict):
    if word in memo:
        return memo[word]

    # check each of the children and make a list of the reducible ones
    res = []
    for child in children(word, word_dict):
        t = is_reducible(child, word_dict)
        if t:
            res.append(child)

    # memoize and return the result
    memo[word] = res
    return res


def children(word, word_dict):
    res = []
    for i in range(len(word)):
        child = word[:i] + word[i+1:]
        if child in word_dict:
            res.append(child)
    return res


def all_reducible(word_dict):
    res = []
    for word in word_dict:
        t = is_reducible(word, word_dict)
        if t != []:
            res.append(word)
    return res


def print_trail(word):
    if len(word) == 0:
        return
    print(word)
    t = is_reducible(word, word_dict)
    print_trail(t[0])


def print_longest_words(word_dict):
    words = all_reducible(word_dict)

    # use DSU to sort by word length
    t = []
    for word in words:
        t.append((len(word), word))
    t.sort(reverse=True)

    # print the longest 5 words
    for length, word in t[0:5]:
        print_trail(word)
        print('\n')

word_dict = make_word_dict()
#print('Exercise 12.6:')
#print_longest_words(word_dict)


# Exercise 13.1
from string import punctuation, whitespace

book = 'words.txt'

with open(book, 'r') as fd:
    words = fd.read().split()


def clean(word):
    cleansed = ''
    for char in word:
        if ((char in punctuation) or (char in whitespace)):
            pass
        else:
            cleansed += char.lower()
    return cleansed

#print("{} has {} 'words'".format(book, len([clean(word) for word in words])))

# Exercise 13.2
origin = 'origin.txt'
huck = 'huck.txt'
frank = 'frank.txt'
great = 'great.txt'
meta = 'meta.txt'
sherlock = 'sherlock.txt'
tale = 'tale.txt'


def words(book):
    list_ = []
    flag = False
    signal = "*** START OF"
    for line in book:
        if flag == True:
            for word in line.split():
                list_.append(word)
        elif (signal in line) and (flag == False):
            flag = True
        else:
            pass
    return list_


def clean(word):
    result = ''
    for letter in word:
        if (letter in whitespace) or (letter in punctuation):
            pass
        else:
            result += letter.lower()
    return result


def histogram(data):
    hist = {}
    for word in data:
        hist[word] = hist.get(word, 0) + 1
    return hist

books = [origin, huck, frank, great, meta, sherlock, tale]


def stats():
    for book in books:
        book = open(book, 'r')
        print("Stats for %s:" % book.name)
        data = [clean(word) for word in words(book)]
        book.close()
        print("  Total: %s" % len(data))
        print("  Unique: %s" % len(histogram(data)))

#stats()


# Exercise 13.3
origin = 'origin.txt'
huck = 'huck.txt'
frank = 'frank.txt'
great = 'great.txt'
meta = 'meta.txt'
sherlock = 'sherlock.txt'
tale = 'tale.txt'

books = [origin, huck, frank, great, meta, sherlock, tale]


def words(book):
    list_ = []
    flag = False
    signal = "*** START OF"
    op = open(book, 'r')
    for line in op:
        if flag == True:
            for word in line.split():
                list_.append(word)
        elif (signal in line) and (flag == False):
            flag = True
        else:
            pass
    op.close()
    return list_


def clean(word):
     result = ''
     for char in word:
         if (char in whitespace) or (char in punctuation):
             pass
         else:
             result += char.lower()
     return result

def histogram(data):
     hist = {}
     for word in data:
         if word == '':
             pass
         else:
             hist[word] = hist.get(word, 0) + 1
     return hist

#print('Exercise 13.3')
#for book in books:
#    data = [clean(word) for word in words(book)]
#    print("Stats for %s:" % book)
#    hist = histogram(data)
#    top20 = []
#    for key in hist:
#        top20.append([hist[key], key])
#    top20.sort(reverse=True)
#    for i in range(0, 20):
#        print("  %s) %s %s" % (i + 1, top20[i][1], top20[i][0]))
#        print("\n")


# Exercise 13.4
origin = 'origin.txt' # Origin of Species, 1859
huck = 'huck.txt' # Huck Finn, 1884
don = 'don.txt' # Don Quixote, 1605
great = 'great.txt' # Expectations, 1860
meta = 'meta.txt' # morphisis, 1915
sherlock = 'sherlock.txt' # 1887
divine = 'divine.txt' # Comedy, 1308
journey = 'journey.txt'  # to the center of the earth, 1864

word_file = 'words.txt'
books = [origin, huck, don, great, meta, sherlock, divine, journey]


def words(book):
    list_ = []
    flag = False
    signal = "*** START OF"
    for line in book:
        if flag == True:
            for word in line.split():
                list_.append(word)
        elif (signal in line) and (flag == False):
            flag = True
        else:
            pass
    return list_


def clean(word):
    result = ''
    for char in word:
        if (char in whitespace) or (char in punctuation):
            pass
        elif not char.isalpha():
            pass
        else:
            result += char.lower()
    return result


def stats():
    for book in books:
        book_words = set([clean(word) for word in words(open(book, 'r'))])
        words_ = set([word for word in open(word_file, 'r')])
        print("Stats for %s" % open(book, 'r').name)
        print("  There are %s non-listed words." % len(book_words - words_))

#print('Exercise 13.4')
#stats()
#print("\n\nThe words not in the word list for origin.txt:")
#print(set([clean(word) for word in words(open(origin, 'r'))]) -
#      set([word for word in open(word_file, 'r')]))



# Exercise 13.5
import random

t = ['a', 'a', 'b']

def hist(x):
    hist = {}
    for item in x:
        hist[item] = hist.get(item, 0) + 1
    return hist

hist = hist(t)

def choose_from_hist(hist):
    list_ = []
    for key in hist:
        for i in range(0, hist[key]):
            list_.append(key)
    return random.choice(list_)

def stats():
    a = 0
    b = 0
    for i in range(0, 10000):
        if choose_from_hist(hist) == 'a':
            a += 1
        else:
            b += 1
    print("a: %.5f" % (a / 10000.0), "b: %.5f" % (b / 10000.0))

print('Exercise 13.5:')
stats()

# Exercise 13.6
import string
import random

from analyze_book import *


def subtract(d1, d2):
    """Returns a set of all keys that appear in d1 but not d2.

    d1, d2: dictionaries
    """
    return set(d1) - set(d2)


if __name__ == '__main__':
    hist = process_file('emma.txt', skip_header=True)
    print('Total number of words:', total_words(hist))
    print('Number of different words:', different_words(hist))

    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[0:20]:
        print(word, '\t', freq)

    words = process_file('words.txt', skip_header=False)

    diff = subtract(hist, words)
    print("The words in the book that aren't in the word list are:")
    for word in diff:
        print(word)

    print("\n\nHere are some random words from the book")
    for i in range(100):
        print(random_word(hist))

# Exercise 13.7
import string
import random

from bisect import bisect

from analyze_book import *


def random_word(hist):
    """Chooses a random word from a histogram.

    The probability of each word is proportional to its frequency.

    This could be made faster by computing the cumulative frequencies
    once and reusing them.
    """
    words = []
    freqs = []
    total_freq = 0

    # make a list of words and a list of cumulative frequencies
    for word, freq in hist.items():
        total_freq += freq
        words.append(word)
        freqs.append(total_freq)

    # choose a random value and find its location in the cumulative list
    x = random.randint(0, total_freq-1)
    index = bisect(freqs, x)
    return words[index]


if __name__ == '__main__':
    hist = process_file('emma.txt', skip_header=True)
    print('Total number of words:', total_words(hist))
    print('Number of different words:', different_words(hist))

    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[0:20]:
        print(word, '\t', freq)

    words = process_file('words.txt', skip_header=False)

    diff = subtract(hist, words)
    print("The words in the book that aren't in the word list are:")
    for word in diff:
        print(word)

    print "\n\nHere are some random words from the book"
    for i in range(100):
        print(random_word(hist))

# Exercise 13.8
import sys
import string
import random

# global variables
suffix_map = {}        # map from prefixes to a list of suffixes
prefix = ()            # current tuple of words


def process_file(filename, order=2):
    """Reads a file and performs Markov analysis.

    filename: string
    order: integer number of words in the prefix

    Returns: map from prefix to list of possible suffixes.
    """
    fp = open(filename)
    skip_gutenberg_header(fp)

    for line in fp:
        for word in line.rstrip().split():
            process_word(word, order)


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*END*THE SMALL PRINT!'):
            break


def process_word(word, order=2):
    """Processes each word.

    word: string
    order: integer

    During the first few iterations, all we do is store up the words;
    after that we start adding entries to the dictionary.
    """
    global prefix
    if len(prefix) < order:
        prefix += (word,)
        return

    try:
        suffix_map[prefix].append(word)
    except KeyError:
        # if there is no entry for this prefix, make one
        suffix_map[prefix] = [word]

    prefix = shift(prefix, word)


def random_text(n=100):
    """Generates random wordsfrom the analyzed text.

    Starts with a random prefix from the dictionary.

    n: number of words to generate
    """
    # choose a random prefix (not weighted by frequency)
    start = random.choice(suffix_map.keys())

    for i in range(n):
        suffixes = suffix_map.get(start, None)
        if suffixes == None:
            # if the start isn't in map, we got to the end of the
            # original text, so we have to start again.
            random_text(n-i)
            return

        # choose a random suffix
        word = random.choice(suffixes)
        print word,
        start = shift(start, word)


def shift(t, word):
    """Forms a new tuple by removing the head and adding word to the tail.

    t: tuple of strings
    word: string

    Returns: tuple of strings
    """
    return t[1:] + (word,)


def main(name, filename='', n=100, order=2, *args):
    try:
        n = int(n)
        order = int(order)
    except:
        print 'Usage: randomtext.py filename [# of words] [prefix length]'
    else:
        process_file(filename, order)
        random_text(n)


if __name__ == '__main__':
    main(*sys.argv)

# Exercise 13.9
import sys
import string

import matplotlib.pyplot as pyplot

from analyze_book import *


def rank_freq(hist):
    """Returns a list of tuples where each tuple is a rank
    and the number of times the item with that rank appeared.
    """
    # sort the list of frequencies in decreasing order
    freqs = hist.values()
    freqs.sort(reverse=True)

    # enumerate the ranks and frequencies
    rf = [(r+1, f) for r, f in enumerate(freqs)]
    return rf


def print_ranks(hist):
    """Prints the rank vs. frequency data."""
    for r, f in rank_freq(hist):
        print(r, f)


def plot_ranks(hist, scale='log'):
    """Plots frequency vs. rank."""
    t = rank_freq(hist)
    rs, fs = zip(*t)

    pyplot.clf()
    pyplot.xscale(scale)
    pyplot.yscale(scale)
    pyplot.title('Zipf plot')
    pyplot.xlabel('rank')
    pyplot.ylabel('frequency')
    pyplot.plot(rs, fs, 'r-')
    pyplot.show()


def main(name, filename='emma.txt', flag='plot', *args):
    hist = process_file(filename, skip_header=True)

    # either print the results or plot them
    if flag == 'print':
        print_ranks(hist)
    elif flag == 'plot':
        plot_ranks(hist)
    else:
        print('Usage: zipf.py filename [print|plot]')


if __name__ == '__main__':
    main(*sys.argv)

# Exercise 14.1
import os


def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print(path)
        else:
            walk(path)


def walk2(dirname):
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            print(os.path.join(root, filename))

#print('Exercise 14.1:')
#walk('.')
#walk2('.')


# Exercise 14.2
import sys


def sed(pattern, replace, source, dest):
    try:
        fin = open(source, 'r')
        fout = open(dest, 'w')

        for line in fin:
            line = line.replace(pattern, replace)
            fout.write(line)

        fin.close()
        fout.close()
    except:
        print('Something went wrong.')


def main(name):
    pattern = 'pattern'
    replace = 'replacendum'
    source = name
    dest = name + '.replaced'
    sed(pattern, replace, source, dest)

main(*sys.argv)


# Exercise 14.3
def signature(s):
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t


def all_anagrams(filename):
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)

        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d


def print_anagram_sets(d):
    for v in d.values():
        if len(v) > 1:
            print(len(v), v)


def print_anagram_sets_in_order(d):
    # make a list of (length, word pairs)
    t = []
    for v in d.values():
        if len(v) > 1:
            t.append((len(v), v))

    # sort in ascending order of length
    t.sort()

    # print the sorted list
    for x in t:
        print(x)


def filter_length(d, n):
    res = {}
    for word, anagrams in d.items():
        if len(word) == n:
            res[word] = anagrams
    return res


#print('Exercise 14.3:')
#d = all_anagrams('words.txt')
#print_anagram_sets_in_order(d)
#eight_letters = filter_length(d, 8)
#print_anagram_sets_in_order(eight_letters)


# Exercise 14.4
import os


def walk(dirname):
    names = []
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            names.append(path)
        else:
            names.extend(walk(path))
    return names


def compute_checksum(filename):
    cmd = 'md5sum ' + filename
    return pipe(cmd)


def check_diff(name1, name2):
    cmd = 'diff %s %s' % (name1, name2)
    return pipe(cmd)


def pipe(cmd):
    fp = os.popen(cmd)
    res = fp.read()
    stat = fp.close()
    assert stat is None
    return res, stat


def compute_checksums(dirname, suffix):
    names = walk(dirname)

    d = {}
    for name in names:
        if name.endswith(suffix):
            res, stat = compute_checksum(name)
            checksum, _ = res.split()

            if checksum in d:
                d[checksum].append(name)
            else:
                d[checksum] = [name]

    return d


def check_pairs(names):
    for name1 in names:
        for name2 in names:
            if name1 < name2:
                res, stat = check_diff(name1, name2)
                if res:
                    return False
    return True


def print_duplicates(d):
    for key, names in d.iteritems():
        if len(names) > 1:
            print('The following files have the same checksum:')
            for name in names:
                print(name)

            if check_pairs(names):
                print('And they are identical.')



# Exercise 15.1
import math


class Point(object):
    """Represents a point in 2d space."""

point_one = Point()
point_two = Point()

point_one.x, point_one.y = 6.0, 1.0
point_two.x, point_two.y = 2.0, 6.0


def distance(p1, p2):
    """Returns the distance between two points in 2d space."""
    delta_x = p2.x - p1.x
    delta_y = p2.y - p1.y
    return math.sqrt(delta_x ** 2 + delta_y ** 2)

print("The distance between point one at (%g,%g)" % (point_one.x, point_one.y))
print("and point two at (%g,%g)" % (point_two.x, point_two.y))
print("is %.3f" % distance(point_one, point_two))

# Exercise 15.2
class Point(object):
    """Represents a point in 2d space"""


class Rectangle(object):
    """Represents a rectangle in 2d space"""

rectangle = Rectangle()

bottom_left = Point()
bottom_left.x = 3.0
bottom_left.y = 5.0

top_right = Point()
top_right.x = 5.0
top_right.y = 10.0

rectangle.corner1 = bottom_left
rectangle.corner2 = top_right

dx = 5.0
dy = 12.0


def move_rectangle(rectangle, dx, dy):
    """Takes a rectangle and moves it to the values of dx and dy."""
    print ("The rectangle started with bottom left corner at (%g,%g)"
           % (rectangle.corner1.x, rectangle.corner1.y)),
    print ("and top right corner at (%g,%g)."
           % (rectangle.corner2.x, rectangle.corner2.y)),
    print "dx is %g and dy is %g" % (dx, dy)
    rectangle.corner1.x = rectangle.corner1.x + dx
    rectangle.corner2.x = rectangle.corner2.x + dx
    rectangle.corner1.y = rectangle.corner1.y + dy
    rectangle.corner2.y = rectangle.corner2.y + dy
    print ("It ended with a bottom left corner at (%g,%g)"
           % (rectangle.corner1.x, rectangle.corner1.y)),
    print ("and a top right corner at (%g,%g)"
           % (rectangle.corner2.x, rectangle.corner2.y))

move_rectangle(rectangle, dx, dy)

# Exercise 15.3
import copy


class Point(object):
    """Represents a point in 2d space"""


class Rectangle(object):
    """Represents a rectangle in 2d space"""

rectangle = Rectangle()

bottom_left = Point()
bottom_left.x = 3.0
bottom_left.y = 5.0

top_right = Point()
top_right.x = 5.0
top_right.y = 10.0

rectangle.corner1 = bottom_left
rectangle.corner2 = top_right

dx = 5.0
dy = 12.0


def move_rectangle(rectangle, dx, dy):
    """Moves a trangle to the values of dx and dy using deepcopy to create
    a new rectangle object and not modify the original rectangle."""
    new_rectangle = copy.deepcopy(rectangle)
    print ("Original: (%g,%g)" % (rectangle.corner1.x, rectangle.corner1.y)),
    print ("(%g,%g)" % (rectangle.corner2.x, rectangle.corner2.y))
    new_rectangle.corner1.x = new_rectangle.corner1.x + dx
    new_rectangle.corner2.x = new_rectangle.corner2.x + dx
    new_rectangle.corner1.y = new_rectangle.corner1.y + dy
    new_rectangle.corner2.y = new_rectangle.corner2.y + dy
    print ("New: (%g,%g)" % (new_rectangle.corner1.x,
           new_rectangle.corner1.y)),
    ("(%g,%g)" % (new_rectangle.corner2.x, new_rectangle.corner2.y))

move_rectangle(rectangle, dx, dy)

# Exercise 16.1
class Time(object):
    """ represents the time of day.
    attributes: hour, minute, second"""

time = Time()
time.hour = 11
time.minute = 59
time.second = 30


def print_time(time):
    print("%.2d:%.2d:%.2d" % (time.hour, time.minute, time.second))

print_time(time)

# Exercise 16.2
import time
import datetime


class Time(object):
    """Time object based on datetime.datetime describes time in 24hr format"""
    def __init__(self, year=2000, month=1, day=1, hour=12, minute=0, sec=0):
        self.date = datetime.datetime(year, month, day, hour, minute, sec)

    def mktime(self):
        return time.mktime(self.date.timetuple())


t1 = Time(2013, 1, 3, 15)
t2 = Time(2013, 1, 3, 1)

def is_after(time1, time2):
    return time1.mktime() > time2.mktime()

print(is_after(t1, t2))

# Exercise 16.3
class Time(object):
    """ represents the time of day.
    attributes: hour, minute, second"""

time = Time()
time.hour = 11
time.minute = 59
time.second = 30


def increment(time, seconds):
    print ("Original time was: %.2d:%.2d:%.2d"
          % (time.hour, time.minute, time.second))

    time.second += seconds
    if time.second > 59:
        quotient, remainder = divmod(time.second, 60)
        time.minute += quotient
        time.second = remainder
    if time.minute > 59:
        quotient, remainder = divmod(time.minute, 60)
        time.hour += quotient
        time.minute = remainder
    if time.hour > 12:
        time.hour -= 12

    print("Plus %g seconds" % (seconds))
    print("New time is: %.2d:%.2d:%.2d" % (time.hour, time.minute, time.second))

increment(time, 300)

# Exercise 16.4
import copy


class Time(object):
    """ represents the time of day.
    attributes: hour, minute, second"""

time = Time()
time.hour = 11
time.minute = 59
time.second = 30


def increment(time, seconds):
    print ("Original time was: %.2d:%.2d:%.2d"
          % (time.hour, time.minute, time.second))

    new_time = copy.deepcopy(time)
    new_time.second += seconds
    if new_time.second > 59:
        quotient, remainder = divmod(new_time.second, 60)
        new_time.minute += quotient
        new_time.second = remainder
    if new_time.minute > 59:
        quotient, remainder = divmod(new_time.minute, 60)
        new_time.hour += quotient
        new_time.minute = remainder
    if new_time.hour > 12:
        new_time.hour -= 12

    print("Plus %g seconds" % (seconds))
    print(("New time is: %.2d:%.2d:%.2d"
          % (new_time.hour, new_time.minute, new_time.second)))
    print("memory id of object 'time': ", id(time))
    print("memory id of object 'new_time': ", id(new_time))

increment(time, 300)


# Exercise 16.5
import copy


class Time(object):
    """ represents the time of day.
    attributes: hour, minute, second"""

time = Time()
time.hour = 11
time.minute = 59
time.second = 30


def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def int_to_time(seconds):
    new_time = Time()
    minutes, new_time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def increment(time, seconds):
    new_time = copy.deepcopy(time)
    new_time = time_to_int(new_time) + seconds
    new_time = int_to_time(new_time)
    print ("New time is: %.2d:%.2d:%.2d"
          % (new_time.hour, new_time.minute, new_time.second))

increment(time, 300)

# Exercise 16.6
class Time(object):
    """ represents the time of day.
    attributes: hour, minute, second"""

time = Time()
time.hour = 3
time.minute = 0
time.second = 0


def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def int_to_time(seconds):
    new_time = Time()
    minutes, new_time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def mul_time(time, multicand):
    time_int = time_to_int(time) * multicand
    new_time = int_to_time(time_int)
    if new_time.hour > 12:
        new_time.hour = new_time.hour % 12
#    print ("New time is: %.2d:%.2d:%.2d"
#    % (new_time.hour, new_time.minute, new_time.second))
    return new_time

# mul_time(time, 2)


def race_stats(time, distance):
    print(("The finish time was %.2d:%.2d:%.2d"
          % (time.hour, time.minute, time.second)))
    print("The distance was %d miles" % (distance))

    average = mul_time(time, (1.0 / distance))

    print(("The average is: %.2d:%.2d:%.2d per mile"
          % (average.hour, average.minute, average.second)))

race_stats(time, 3)

# Exercise 16.7
import copy

# month:days in month
rules = {1: 31,
         2: 28,
         3: 31,
         4: 30,
         5: 31,
         6: 30,
         7: 31,
         8: 31,
         9: 30,
         10: 31,
         11: 30,
         12: 31}

names = {1: "January",
         2: "Feburary",
         3: "March",
         4: "April",
         5: "May",
         6: "June",
         7: "July",
         8: "August",
         9: "September",
         10: "October",
         11: "November",
         12: "December"}


class Date(object):
    """Representation of a date
    attributes: month, day, year"""

date = Date()
date.month = 10
date.day = 30
date.year = 2012


def increment_date(date, inc):
    date_ = copy.deepcopy(date)

    # adjust ui for leap year
#    if (date_.year % 4 == 0):
#        print "Starting: %s %s, %s (Leap year!)" \
#        % (names[date.month], date.day, date.year)
#    else:
#        print "Starting: %s %s, %s" % (names[date.month], date.day, date.year)
#    print "Moving forward %s days" %  inc
    while True:

        # adjust feb for leap year
        rules[2] = 28
        if (date_.year % 4 == 0):
            rules[2] = 29
        elif date_.month != 2:
            pass

        days_left = rules[date_.month] - date_.day

        # set date_.day based on value of days_left and inc
        if inc <= days_left:
            date_.day += inc
            break
        elif inc == 0:
            date_.day = rules[date_.month]
            break
        elif inc < 0:
            date_.day = rules[date_.month] + inc
            break
        else:
            inc -= rules[date_.month]
            date_.month += 1

        # increment year if month counter pushes past 12
        if date_.month > 12:
            date_.year += 1
            date_.month = 1

    # final adjustment of date if previous year was a leap year
    if ((date_.year - 1) % 4 == 0) and date_.month != 2:
        date_.day -= 1

    #final ui element
#    print "Ending: %s %s, %s" % (names[date_.month], date_.day, date_.year)
    return date_

newDate = increment_date(date, 365)

print(date, "%s %s, %s" % (names[date.month], date.day, date.year))
print(newDate, "%s %s, %s" % (names[newDate.month], newDate.day, newDate.year))


# Exercise 16.8
import datetime

rules = {0: "Monday",
         1: "Tuesday",
         2: "Wednesday",
         3: "Thursday",
         4: "Friday",
         5: "Saturday",
         6: "Sunday"}


class Time(object):
    now = datetime.datetime.now()

    def __init__(self, year=1, month=1, day=1, hour=0, minute=0, second=0):
        self.date = datetime.datetime(year, month, day, hour, minute, second)

today = Time().now
birthday = Time(1953, 5, 24).date


def day_of_week():
    return "1) Today is %s" % rules[today.weekday()]


def birthday_stats(birthday):
    age = today.year - birthday.year
    if (birthday.month == today.month) and (birthday.day <= today.day):
        pass
    elif birthday.month < today.month:
        pass
    else:
        age -= 1

    birthday_ = Time(today.year, birthday.month, birthday.day).date
    till_birthday = str(birthday_ - today).split()

    if len(till_birthday) > 1:
        days = int(till_birthday[0])
        time = till_birthday[2].split(":")
    else:
        days = 365
        time = till_birthday[0].split(":")

    hours = time[0]
    mins = time[1]
    secs = time[2][:2]

    if (days < 0) and (days != 365):
        days = 365 + days
    elif (days == 365):
        days = 0
    else:
        days = abs(days)

    print ("2) You are %s years old; %sd:%sh:%sm:%ss until your next birthday."
    % (age, days, hours, mins, secs))

print(day_of_week())
birthday_stats(birthday)

# Exercise 17.1
class Time(object):
    def time_to_int(self):
        minutes = time.hour * 60 + time.minute
        seconds = minutes * 60 + time.second
        return seconds

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

print(time.time_to_int())

# Exercise 17.2
class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def print_point(self):
        print("x =", self.x, ",")
        print("y =", self.y)

#print('Exercise 17.2:')
#point = Point()
#point.print_point()
#point = Point(10)
#point.print_point()
#point = Point(20, 30)
#point.print_point()


# Exercise 17.3
class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)

#print('Exercise 17.3: ')
#point = Point()
#print(point)
#point = Point(10)
#print(point)
#point = Point(10, 15)
#print(point)


# Exercise 17.4
class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

point1 = Point(1, 3)
point2 = Point(4, 5)
#print('Exercise 17.4:')
#print(point1 + point2)

# Exercise 17.5
class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        point_ = Point()
        if isinstance(other, Point):
            point_.x += self.x + other.x
            point_.y += self.y + other.y
            return point_
        elif type(other) == tuple:
            point_.x += self.x + other[0]
            point_.y += self.y + other[1]
        return point_

    def __radd__(self, other):
        return self.__add__(other)

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

point1 = Point(1, 6)
point2 = (5, 2)
point3 = point1 + point2
point4 = point2 + point1
#print('Exercise 17.6:')
#print(point3, point4)


# Exercise 18.1
class Time(object):
    def __init__(self, hour=0, minute=0):
        self.hour = hour
        self.minute = minute

    def __lt__(self, other):
        return (self.hour, self.minute) < (other.hour, other.minute)

    def __gt__(self, other):
        return (self.hour, self.minute) > (other.hour, other.minute)

    def __eq__(self, other):
        return (self.hour, self.minute) == (other.hour, other.minute)

    def __repr__(self):
        return '{}'.format((self.hour, self.minute))

a = Time(hour=3, minute=31)
b = Time(hour=4, minute=30)

#print('Exercise 18.1:')
#print(a < b)

# Exercise 18.2
class Card(object):
    """Represents a standard playing card."""

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
              '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

class Deck(object):
  def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)
  def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)



deck = Deck()
deck.sort()