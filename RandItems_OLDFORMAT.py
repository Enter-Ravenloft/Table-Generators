# TODO: Implement random.org http get

from random import*
from ItemsMasterList import*


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


makeFileOLD_FORMAT()
