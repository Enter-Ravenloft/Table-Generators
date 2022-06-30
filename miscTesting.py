from marketTables import *

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

annoyingItemNames = ["Adamantine Armor (medium or heavy, but not hide)",
                     "Molten Bronze Skin (breastplate, half plate, or plate)",  "Vicious Weapon (any weapon)",
                     "Amulet of Protection from Turning",  "Amulet of Proof Against Detection and Location",
                     "Instrument of the Bards (Fochlucan Bandore)",
                     "Dan's Item with a Really Long Ass Name, then he kept goin and goin without any end in sight"]

miniTest(annoyingItemNames)
# END TESTING"""
WrapSheet = []

def refreshWrapSheet():
    stepCount = 0
    for namedItem in range(len(WrapSheet)):
        for rowAddress in range(len(WrapSheet[namedItem])):
            WrapSheet[namedItem][rowAddress] = stepCount
            stepCount += 1

def addWraps(item, wraps):
    for address in range(wraps):
        WrapSheet[item].append([address])
    refreshWrapSheet()

moldList = [0,1,1,1,1,2,1,5,12,54,78]

for i in range(len(moldList)):
    WrapSheet.append([i])
refreshWrapSheet()

print(len(moldList))
print(len(WrapSheet))
print(WrapSheet)
addWraps(6, 4)
print(WrapSheet)
