from ItemsMasterList import*
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
    seed = (time_ns())

print("Seed: %d" % seed)

rng = np.random.default_rng(seed)

def getScrolls(num_scrolls=1, max_level=1, min_level=-1):
    if min_level > max_level:
        min_level = max_level
    # TODO add checks for valid arguments

    scrolls = []
    for i in range(num_scrolls):
        attempts = 0
        while True:
            attempts = attempts + 1
            level = rng.integers(low=min_level, high=max_level)
            randNum = rng.integers(low=0, high=len(AllSpells[level]) - 1)
            newScroll = AllSpells[level][randNum]
            if newScroll not in scrolls:
                break
            elif attempts > 100:
                # TESTING STATEMENT
                scrolls.append(["Exceeded maximum attempts for this item", str(attempts)])
                break
        scrolls.append(newScroll)

    return scrolls


def getMaterials(requested_type, num_materials=1):
    typesOfMaterials = ["Cloth", "Organic", "Metal", "Mineral"]
    key_name = "name"
    key_price = "price"

    materialType = typesOfMaterials.index(requested_type)


    materials = []
    for i in range(num_materials):
        attempts = 0
        while True:
            attempts = attempts + 1

            randNum = rng.integers(low=0, high=len(SpecialMaterials[materialType]) - 1)
            newScroll = [SpecialMaterials[materialType][randNum][key_name], SpecialMaterials[materialType][randNum][key_price]]
            if newScroll not in materials:
                break
            elif attempts > 100:
                # TESTING STATEMENT
                materials.append(["Exceeded maximum attempts for this item", str(attempts)])
                break
        materials.append(newScroll[0])
        materials.append(newScroll[1])

    return materials


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
                searchComplete = False
                while not searchComplete:
                    attempts = attempts + 1
                    randNum = rng.integers(low=0, high=len(MasterList[table]) - 1)
                    left = MasterList[table][randNum][key_name]
                    right = MasterList[table][randNum][key_price]
                    pricedItem = [left, right]
                    if (pricedItem not in results) and (rarity == MasterList[table][randNum][key_rarity]):
                        searchComplete = True
                        results.append(left)
                        results.append(right)
                    elif attempts > 100:
                        searchComplete = True
                        results.append(["Exceeded maximum attempts for this item", str(attempts)])
        else:
            results.append(["Number of items requested too high.", str(numItems)])
    else:
        results.append(["Table or rarity not in initial list.", tableName])

    return results


def getVistaniItems():
    marketList = ["Items"]
    spellLevelAndCost = ["Cantrip: 15gp", "1st: 25gp", "2nd: 150gp", "3rd: 400gp"]
    raritiesList = ["Common", "Uncommon", "Rare"]
    materialTypes = ["Cloth", "Organic", "Metal", "Mineral"]
    endTableMarker = "ENDTABLE"
    sectionMarker = "ENDSECTION"
    mergeMarker = "MERGE"

    itemList = []
    maxItemsPerSubcategory = 3
    for i in range(len(raritiesList)):
        itemList.append(raritiesList[i])
        itemList.append(mergeMarker)
        itemList.append(sectionMarker)
        itemList.append(sectionMarker)
        for j in range(maxItemsPerSubcategory - i):
            newItem = getItems(marketList[0], 1, raritiesList[i])
            itemList.append(newItem[0])
            itemList.append(newItem[1])
    itemList.append(endTableMarker)

    for i in range(len(spellLevelAndCost) // 2):
        lesserScrollLevel = i * 2
        greaterScrollLevel = lesserScrollLevel + 1
        itemList.append(spellLevelAndCost[lesserScrollLevel])
        itemList.append(spellLevelAndCost[greaterScrollLevel])
        itemList.append(sectionMarker)
        itemList.append(sectionMarker)

        weakerScrolls = getScrolls(maxItemsPerSubcategory, lesserScrollLevel)
        strongerScrolls = getScrolls(maxItemsPerSubcategory, greaterScrollLevel)

        for j in range(maxItemsPerSubcategory):
            itemList.append(weakerScrolls[j])
            itemList.append(strongerScrolls[j])

    itemList.append(endTableMarker)

    for i in range(len(materialTypes) // 2):
        firstType = i * 2
        secondType = firstType + 1

        itemList.append(materialTypes[firstType])
        itemList.append(materialTypes[secondType])
        itemList.append(sectionMarker)
        itemList.append(sectionMarker)

        firstMaterial = getMaterials(materialTypes[firstType])
        secondMaterial = getMaterials(materialTypes[secondType])

        # append names
        itemList.append(firstMaterial[0])
        itemList.append(secondMaterial[0])

        # append prices
        itemList.append(firstMaterial[1])
        itemList.append(secondMaterial[1])

    return itemList
