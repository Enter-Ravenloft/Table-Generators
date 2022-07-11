# TODO: Implement random.org http get

from random import*
from ItemsMasterList import*

def getScrolls(num_scrolls=1, max_level=1, min_level=-1):
    if min_level > max_level:
        min_level = max_level
    # TODO add checks for valid arguments

    scrolls = []
    for i in range(num_scrolls):
        attempts = 0
        while True:
            attempts = attempts + 1
            level = randint(min_level, max_level)
            randNum = randint(0, len(MasterList[level]))
            newScroll = AllSpells[level][randNum]
            if newScroll not in scrolls:
                break
            elif attempts > 100:
                # TESTING STATEMENT
                scrolls.append(["Exceeded maximum attempts for this scroll", str(attempts)])
                break
        scrolls.append(newScroll)

    return scrolls


def getItems(tableName="Items", numItems=1, rarity="Uncommon"):
    TableList = ["Potions", "Scrolls", "SpellGems", "Items", "SpecialMaterials"]
    RaritiesList = ["Common", "Uncommon", "Rare", "Very Rare", "Legendary"]
    results = []

    if tableName in TableList or rarity not in RaritiesList:
        table = TableList.index(tableName)
        key_name = "name"
        key_price = "price"
        key_rarity = "rarity"

        if numItems < len(MasterList[table]):
            for i in range(numItems):
                attempts = 0
                while True:
                    attempts = attempts + 1
                    randNum = randint(0, len(MasterList[table]))
                    pricedItem = [MasterList[table][randNum][key_name], MasterList[table][randNum][key_price]]
                    if (pricedItem not in results) and (rarity == MasterList[table][randNum][key_rarity]):
                        break
                    elif attempts > 100:
                        results.append(["Exceeded maximum attempts for this item", str(attempts)])
                        break
                results.append(pricedItem)
        else:
            results.append(["Number of items requested too high.", str(numItems)])
    else:
        results.append(["Table or rarity not in initial list.", tableName])

    return results


def OLD_FORMAT_TEST():
    requestTable = "Items"
    tableSize = 3

    availableItems = getItems(requestTable, tableSize)
    print(availableItems)
    print()

    for item in range(tableSize):
        print(availableItems[item][0], availableItems[item][1])


def makeFileOLD_FORMAT():
    printList = ["Potions", "Items", "SpecialMaterials"]
    repetitions = 3

    tableResults = []
    for i in range(len(printList)):
        tableResults.append(getItems(printList[i], repetitions))

    filename = "oldie.txt"
    try:
        outputFile = open(filename, 'w')
        isFileOpen = True
    except OSError:
        print("\nError: No input file uploaded.")
        isFileOpen = False

    if outputFile.writable():
        for category in tableResults:
            for item in range(len(category)):
                line = str(category[item][0]) + "\t|\t" + str(category[item][1]) + '\n'
                outputFile.write(line)

        outputFile.close()
        print("File written successfully")

    else:
        print("Unable to open file")

def getVistaniItems():
    marketList = ["Items", "Scrolls", "SpecialMaterials"]
    spellLevelAndCost = ["Cantrip: 15gp", "1st: 25gp", "2nd: 150gp", "3rd: 400gp"]
    raritiesList = ["Common", "Uncommon", "Rare"]

    itemList = []
    maxItemsPerSubcategory = 3
    for i in range(len(raritiesList)):
        itemList.append(raritiesList[i])
        for j in range(maxItemsPerSubcategory - i):
            itemList.append(getItems(marketList[0], 1, raritiesList[i]))

    for i in range(len(spellLevelAndCost) // 2):
        lesserScrollLevel = i * 2
        greaterScrollLevel = lesserScrollLevel + 1
        itemList.append(spellLevelAndCost[lesserScrollLevel])
        itemList.append(spellLevelAndCost[greaterScrollLevel])

        weakerScrolls = getScrolls(maxItemsPerSubcategory, lesserScrollLevel)
        strongerScrolls = getScrolls(maxItemsPerSubcategory, greaterScrollLevel)

        for j in range(maxItemsPerSubcategory):
            itemList.append(weakerScrolls[j])
            itemList.append(strongerScrolls[j])

    return itemList


def makeSnakeboxItems():
    TableList = ["Potions", "Scrolls", "SpellGems", "Items", "SpecialMaterials"]
    printList = ["Potions", "Items", "SpecialMaterials"]
    repetitions = 3

    tableResults = []
    for i in range(len(printList)):
        tableResults.append(getItems(printList[i], repetitions))

    tableInput = ""
    for category in tableResults:
        for item in range(len(category)):
            line = str(category[item][0]) + '\n' + str(category[item][1])
            tableInput = tableInput + line
            if item < (len(category) - 1):
                tableInput = tableInput + '\n'

    filename = "snakeboxString.txt"
    try:
        outputFile = open(filename, 'w')
        isFileOpen = True
    except OSError:
        print("\nError: No input file uploaded.")
        isFileOpen = False

    if outputFile.writable():
        outputFile.write(tableInput)
        outputFile.close()
        print("File written successfully")

    else:
        print("Unable to open file")

    return tableInput


makeFileOLD_FORMAT()
makeSnakeboxItems()
