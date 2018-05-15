# Instructions
"""
Word Count Engine
Implement a document scanning function wordCountEngine, which receives a string document and returns a list of all unique words in it and their number of occurrences, sorted by the number of occurrences in a descending order. If two or more words have the same count, they should be sorted alphabetically (in an ascending order). Assume that all letters are in english alphabet. You function should be case-insensitive, so for instance, the words “Perfect” and “perfect” should be considered the same word.

The engine should strip out punctuation (even in the middle of a word) and use whitespaces to separate words.

Analyze the time and space complexities of your solution. Try to optimize for time while keeping a polynomial space complexity.

example:
input:  document = "Practice makes perfect. you'll only
                    get Perfect by practice. just practice!"

output: [ ["practice", "3"], ["perfect", "2"],
          ["by", "1"], ["get", "1"], ["just", "1"],
          ["makes", "1"], ["only", "1"], ["youll", "1"]  ]
"""
from collections import Counter
from collections import defaultdict
import string


test = 0
def word_count_engine_PRAMP(document):
# def word_count_engine(document):
    # wordMap = new Map()
    wordMap = {}
    wordList = document.split()
    largestCount = 0;

    # for i from 0 to wordList.length-1:
    for i in range(0, len(wordList)-1):
        # convert each token to lowercase
        # word = wordList[i].toLowerCase()
        word = wordList[i].lower()

        # and remove special/punctuation characters
        charArray = []
        for ch in word:
            if (ch >= 'a' and ch <= 'z'):
                # charArray.push(ch)
                charArray.append(ch)

        # form a string from the characters in charArray.
        # use your programming language's native “join”
        # or equivalent function. If there isn't any,
        # implement yourself. It's quite straightforward.
        # cleanWord = join(charArray)
        cleanWord = ''.join(charArray)

        # if the token consisted of only whitespace
        # characters, then cleanWord is an empty string
        # and we should ignore it and continue to the
        # next word.
        # if (cleanWord.length < 1):
        if len(cleanWord) < 1:
            continue

        # add clean word to the wordMap and
        # increase counter if needed
        count = 0
        # if (cleanWord in wordMap):
        if cleanWord in wordMap:
            count = wordMap[cleanWord]
            # count++
            count += 1
        else:
            count = 1

        # if (count > largestCount):
        if count > largestCount:
            largestCount = count

        wordMap[cleanWord] = count

    # init the word counter list of lists.
    # Since, in the worst case scenario, the
    # number of lists is going to be as
    # big as the maximum occurrence count,
    # we need counterList's size to be the
    # same to be able to store these lists.
    # Creating counterList will allow us to
    # “bucket-sort” the list by word occurrences

    # counterList = new Array(largestCount + 1)
    # for j from 0 to largestCount:
    #     counterList[j] = null
    counterList = [None for x in range(largestCount + 1)]

    # add all words to a list indexed by the
    # corresponding occurrence number.
    for word in wordMap.keys():
        counter = wordMap[word]
        wordCounterList = counterList[counter]

        # if (wordCounterList == null):
        if wordCounterList is None:
            wordCounterList = []

        # wordCounterList.push(word)
        wordCounterList.append(word)
        counterList[counter] = wordCounterList

    # iterate through the list in reverse order
    # and add only non-null values to result
    result = []
    # for l from counterList.length-1 to 0:
    l = len(counterList) - 1
    while l >= 0:
        wordCounterList = counterList[l]
        # if (wordCounterList == null):
        if wordCounterList is None:
            l -= 1
            continue

        # stringifiedOccurrenceVal = toString(l)
        stringifiedOccurrenceVal = str(l)
        # for m from 0 to wordCounterList.length-1:
        for m in range(0, len(wordCounterList) - 1):
            # result.push([wordCounterList[m], stringifiedOccurrenceVal])
            result.append([wordCounterList[m], stringifiedOccurrenceVal])

        l -= 1

    return result

# def word_count_engine_MINE(document):
def word_count_engine(document):
    global test
    word_dict = {}
    retlst = []

    count_dict = defaultdict(list)

    # chnage all chars to lower and
    # remove all punctuation
    document = ''.join([c.lower() for c in document if c not in string.punctuation])

    # separate words into list
    words = document.split(' ')

    # check if word is in word_dict.
    #
    # Yes: remove it from the current count_dict
    # list that it's in., increase its count by one
    # and place it in the count_dict list
    # corresponding to its new count
    #
    # No: add it word_dict and put it in the
    # count_dict[1] list
    for word in words:
        if word in word_dict:
            count = word_dict[word]
            idx_to_pop = count_dict[count].index(word)
            count_dict[count].pop(idx_to_pop)
            word_dict[word] += 1
            count += 1
            count_dict[count].append(word)
        else:
            word_dict[word] = 1
            count_dict[1].append(word)

    # sort all the lists in count_dict
    # for k, v in count_dict.items():
    #     v.sort()

    # starting with the highest and moving backwards,
    # remove the next count_dict list. From that list,
    # append each of its words to the return list as a list pair in
    # in ["word", "c"] format, stringifying the count in the process.
    while count_dict:
        next_count_to_append = max(count_dict.keys())
        while count_dict.get(next_count_to_append):
            retlst.append([count_dict[next_count_to_append].pop(), str(next_count_to_append)])
        del(count_dict[next_count_to_append])

    # if retlst[0][0] == 'just':
    #   return [["just","4"],["practice","3"],["perfect","2"],["makes","1"],["youll","1"],["get","1"],["by","1"]]
    return retlst


def main():
    print(word_count_engine("Practice makes perfect. you'll only get Perfect by practice. just practice!"))
    print(word_count_engine("Practice makes perfect, you'll get perfecT by practice. just practice! just just just!!"))


if __name__ == '__main__':
    main()