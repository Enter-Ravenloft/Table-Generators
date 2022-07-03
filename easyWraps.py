from textwrap import wrap
from math import ceil


def longestWord(text):
    if len(text) == 0:
        return "0"
    wordList = text.split()
    longest = max(wordList, key=len)
    return longest


def simpleWrap(text, width, whole_words=False):
    return wrap(text, width, break_long_words=whole_words)


def loosestWrap(text, width):
    minimum = len(longestWord(text))
    for i in range(len(text)):
        wrapCap = ceil(len(text) / (i + 2))
        if wrapCap < minimum:
            return 0
        results = simpleWrap(text, wrapCap)
        longestLine = 0
        for line in results:
            if longestLine < len(line):
                longestLine = len(line)
        if longestLine <= width:
            return wrapCap


def evenWrap(text, width):
    wrapCap = loosestWrap(text, width)
    if wrapCap > 0:
        return simpleWrap(text, wrapCap)
    else:
        return [text]


def shortestWrap(text, width):
    even = evenWrap(text, width)
    simple = simpleWrap(text, width)
    if (len(simple) < len(even)) or (even[0] == text):
        return simple
    else:
        return even
