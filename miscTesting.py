from marketTables import *
from math import *
from statistics import *
from ItemsMasterList import *
from RandItems_OLDFORMAT import *

"""'# BEGINING TESTING
def miniTest(input):
    for test in input:
        print("%d Characters long" % len(test))
        print(test)
        print(" " * (len(test) // 2), end="^\n")
        result = testWrapping(test, 30)
        charsPerRow = []
        for section in result:
            charsPerRow.append(len(section))
            print(section)
        print()
        print(charsPerRow, end=" Characters for each row\n")
        print("---------")





miniTest(annoyingItemNames)"""
annoyingItemNames = ["Adamantine Armor (medium or heavy, but not hide)",
                     "Molten Bronze Skin (breastplate, half plate, or plate)", "Vicious Weapon (any weapon)",
                     "Amulet of Protection from Turning", "Amulet of Proof Against Detection and Location",
                     "Instrument of the Bards (Fochlucan Bandore)",
                     "Dan's Item with a Really Long Ass Name, then he kept goin and goin without any end in sight"]

# END TESTING"""
WrapSheet = []


def longestWord(text):
    wordList = text.split()
    longest = max(wordList, key=len)
    return longest


def simpleWrap(text, width, break_words=False):
    return wrap(text, width, initial_indent='', subsequent_indent='', expand_tabs=True, replace_whitespace=True,
                fix_sentence_endings=False, break_long_words=break_words)


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


def compareWraps(tests):
    gameScores = []
    detailedScores = []
    evenTotalPoints = 0
    simpleTotalPoints = 0
    evenWinWidths = []
    simpleWinWidths = []
    comparisons = 0
    for line in tests:
        individualScores = []
        evenGamePoints = 0
        simpleGamePoints = 0
        lowerBound = len(longestWord(line)) - 1
        currentWidth = len(line) - 1
        while lowerBound < currentWidth:
            if evenWrap(sentence, currentWidth) == shortestWrap(sentence, currentWidth):
                evenGamePoints = evenGamePoints + 1
            elif simpleWrap(sentence, currentWidth) == shortestWrap(sentence, currentWidth):
                simpleGamePoints = simpleGamePoints + 1
            currentWidth = currentWidth - 1
            comparisons = comparisons + 1
            if evenGamePoints > simpleGamePoints:
                winner = "Even"
                evenWinWidths.append(currentWidth)
            elif simpleGamePoints > evenGamePoints:
                winner = "Simple"
                simpleWinWidths.append(currentWidth)
            else:
                winner = "Tie"
            individualScores.append(winner)

        if evenGamePoints > simpleGamePoints:
            winner = "Even"
        elif simpleGamePoints > evenGamePoints:
            winner = "Simple"
        else:
            winner = "Tie"
        gameScores.append(winner)
        detailedScores.append(individualScores)
        simpleTotalPoints = simpleTotalPoints + simpleGamePoints
        evenTotalPoints = evenTotalPoints + evenGamePoints

    if evenTotalPoints > simpleTotalPoints:
        winner = "Even"
    elif simpleTotalPoints > evenTotalPoints:
        winner = "Simple"
    else:
        winner = "Tie"
    print("Winner: %s" % winner)
    print("Even: %d" % evenTotalPoints)
    print("Average %d, Median %d" % (floor(mean(evenWinWidths)), median_low(evenWinWidths)))
    print("Simple: %d" % simpleTotalPoints)
    print("Average %d, Median %d" % (floor(mean(simpleWinWidths)), median_low(simpleWinWidths)))
    print(gameScores)
    print("%d comparisons made.\n\n" % comparisons)




sentence = "Dan's Item with a Really Long Ass Name, then he kept goin and goin without any end in sight"

"""
maximum = 24
print(longestWord(sentence))
print(loosestWrap(sentence, maximum))
print(evenWrap(sentence, maximum))
print(simpleWrap(sentence, maximum))
print(shortestWrap(sentence, maximum))
print('\n\n')
"""

"""compareWraps(annoyingItemNames)

print("Spell List Compare:")
spellList = []
for level in AllSpells:
    for spell in level:
        spellList.append(spell)

compareWraps(spellList)

print("Item List Compare:")
itemList = []
for item in Items:
    itemList.append(item["name"])

compareWraps(itemList)

value = False
test = wrap(sentence, maximum, initial_indent='', subsequent_indent='', expand_tabs=True, replace_whitespace=True,
            fix_sentence_endings=False, break_long_words=value)
print(test)
"""

"""
typesOfMaterials = ["Cloth", "Organic", "Metal", "Mineral"]
newList = []
for i in range(len(typesOfMaterials)):
    newList.append([])
for material in SpecialMaterials:
    if material["type"] in typesOfMaterials:
        order = typesOfMaterials.index(material["type"])
        newList[order].append(material)

for item in newList:
    print(typesOfMaterials[newList.index(item)])
    for subitem in item:
        print(subitem)
    print('\n')
"""

newList = getVistaniItems()
for i in newList:
    print(i)

print('\n\n')
import numpy as np
# Importing Necessary Modules
import requests  # to get image from the web
from time import *

# Set up the image URL and filename
REQUEST_URL = "https://www.random.org/integers/?num=1&min=1&max=9001&col=1&base=10&format=plain&rnd=new"

headers = {'User-Agent': 'Chrome/83.0.4103.116'}
s = requests.Session()
s.get('https://www.random.org', headers=headers)
r = s.get(REQUEST_URL, headers=headers)

# Check if the image was retrieved successfully
if r.status_code == 200:
    seed = int(r.text)

else:
    seed(time_ns())

print("Seed: %d" % seed)

rng = np.random.default_rng(seed)

rints = rng.integers(low=0, high=20)
print(rints)