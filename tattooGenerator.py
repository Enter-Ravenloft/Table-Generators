#  https://github.com/ItsQc/Ravenloft-Tables
#  If you have issue with this, ping Quincy on Discord
#  Lotsa Spaghetti


from math import *
from textwrap import wrap
from time import *
from random import *
from secrets import *
from time import *




seed(time_ns() * random() + thread_time_ns() * int(token_hex(), 16) * process_time_ns() + int(token_hex(), 16))
seedList = sample(range(randint(9001, int(1000000 * (100 * random())))), 9000)
shuffle(seedList)
seed(seedList[(randint(0, len(seedList)))])


Potions = [{"name": "Perfume of Bewitching", "price": "75 gp", "page": "XGE 138", "rarity": "Common"}, {"name": "Potion of Climbing", "price": "30 gp", "page": "DMG 187", "rarity": "Common"}, {"name": "Potion of Healing (Common)", "price": "50 gp", "page": "DMG 187-188", "rarity": "Common"}, {"name": "Bottled Breath", "price": "350 gp", "page": "PA 222", "rarity": "Uncommon"}, {"name": "Oil of Slipperiness", "price": "250 gp", "page": "DMG 184", "rarity": "Uncommon"}, {"name": "Philter of Love", "price": "150 gp", "page": "DMG 184", "rarity": "Uncommon"}, {"name": "Potion of Animal Friendship", "price": "200 gp", "page": "DMG 187", "rarity": "Uncommon"}, {"name": "Potion of Fire Breath", "price": "350 gp", "page": "DMG 187", "rarity": "Uncommon"}, {"name": "Potion of Advantage", "price": "300 gp", "page": "TWBtW 212", "rarity": "Uncommon"}, {"name": "Potion of Giant Strength (Hill)", "price": "350 gp", "page": "DMG 187", "rarity": "Uncommon"}, {"name": "Potion of Growth", "price": "300 gp", "page": "DMG 187", "rarity": "Uncommon"}, {"name": "Potion of Healing (Uncommon)", "price": "300 gp", "page": "DMG 187-188", "rarity": "Uncommon"}, {"name": "Potion of Poison", "price": "500 gp", "page": "DMG 188", "rarity": "Uncommon"}, {"name": "Potion of Resistance", "price": "500 gp", "page": "DMG 188", "rarity": "Uncommon"}, {"name": "Potion of Waterbreathing", "price": "400 gp", "page": "DMG 188", "rarity": "Uncommon"}, {"name": "Elixir of Health", "price": "2,000 gp", "page": "DMG 168", "rarity": "Rare"}, {"name": "Oil of Etherealness", "price": "2,000 gp", "page": "DMG 183", "rarity": "Rare"}, {"name": "Potion of Aqueous Form", "price": "1,000 gp", "page": "MOT 197", "rarity": "Rare"}, {"name": "Potion of Clairvoyance", "price": "900 gp", "page": "DMG 187", "rarity": "Rare"}, {"name": "Potion of Diminution", "price": "500 gp", "page": "DMG 187", "rarity": "Rare"}, {"name": "Potion of Gaseous Form", "price": "1,500 gp", "page": "DMG 187", "rarity": "Rare"}, {"name": "Potion of Giant Strength (Frost/Stone)", "price": "650 gp", "page": "DMG 187", "rarity": "Rare"}, {"name": "Potion of Giant Strength (Fire)", "price": "1,200 gp", "page": "DMG 187", "rarity": "Rare"}, {"name": "Potion of Healing (Rare)", "price": "750 gp", "page": "DMG 187-188", "rarity": "Rare"}, {"name": "Potion of Heroism", "price": "800 gp", "page": "DMG 188", "rarity": "Rare"}, {"name": "Potion of Invulnerability", "price": "1,500 gp", "page": "DMG 188", "rarity": "Rare"}, {"name": "Potion of Maximum Power", "price": "2,000 gp", "page": "EGW 268", "rarity": "Rare"}, {"name": "Potion of Mind Control (beast)", "price": "1,600 gp", "page": "TYP 229", "rarity": "Rare"}, {"name": "Potion of Mind Control (humanoid)", "price": "2,500 gp", "page": "TYP 229", "rarity": "Rare"}, {"name": "Potion of Mind Reading", "price": "1,100 gp", "page": "DMG 188", "rarity": "Rare"}, {"name": "Oil of Sharpness", "price": "2,200 gp*", "page": "DMG 184", "rarity": "Very Rare"}, {"name": "Potion of Flying", "price": "2,500 gp", "page": "DMG 187", "rarity": "Very Rare"}, {"name": "Potion of Giant Strength (Cloud)", "price": "1,800 gp*", "page": "DMG 187", "rarity": "Very Rare"}, {"name": "Potion of Healing (Very Rare)", "price": "1,500 gp*", "page": "DMG 187-188", "rarity": "Very Rare"}, {"name": "Potion of Invisibility", "price": "2,000 gp*", "page": "DMG 188", "rarity": "Very Rare"}, {"name": "Potion of Longevity", "price": "3,000 gp", "page": "DMG 188", "rarity": "Very Rare"}, {"name": "Potion of Mind Control (monster)", "price": "6,000 gp", "page": "TYP 229", "rarity": "Very Rare"}, {"name": "Potion of Possibility", "price": "1,900 gp*", "page": "EGW 268", "rarity": "Very Rare"}, {"name": "Potion of Speed", "price": "2,000 gp*", "page": "DMG 188", "rarity": "Very Rare"}, {"name": "Potion of Vitality", "price": "1,800 gp*", "page": "DMG 188", "rarity": "Very Rare"}, {"name": "Potion of Giant Size", "price": "11,000 gp*", "page": "SKT 236", "rarity": "Legendary"}, {"name": "Potion of Giant Strength (Storm)", "price": "8,000 gp*", "page": "DMG 187", "rarity": "Legendary"}]
OldScrolls = [{"name": "Spell Scroll or Tattoo (Cantrip)", "price": "15 gp", "page": "DMG 200; TCE 135", "rarity": "Common"}, {"name": "Spell Scroll or Tattoo (1st Level)", "price": "25 gp", "page": "DMG 200; TCE 135", "rarity": "Common"}, {"name": "Spell Scroll or Tattoo (2nd Level)", "price": "150 gp", "page": "DMG 200; TCE 135", "rarity": "Uncommon"}, {"name": "Spell Scroll or Tattoo (3rd Level)", "price": "400 gp", "page": "DMG 200; TCE 135", "rarity": "Uncommon"}, {"name": "Spell Scroll or Tattoo (4th Level)", "price": "800 gp", "page": "DMG 200; TCE 135", "rarity": "Rare"}, {"name": "Spell Scroll or Tattoo (5th Level)", "price": "1,500 gp", "page": "DMG 200; TCE 135", "rarity": "Rare"}, {"name": "Scroll of Protection", "price": "3,500 gp", "page": "DMG 199", "rarity": "Rare"}, {"name": "Spell Scroll (6th Level)", "price": "2,000 gp*", "page": "DMG 200", "rarity": "Very Rare"}, {"name": "Spell Scroll (7th Level)", "price": "3,500 gp", "page": "DMG 200", "rarity": "Very Rare"}, {"name": "Spell Scroll (8th Level)", "price": "5,000 gp", "page": "DMG 200", "rarity": "Very Rare"}, {"name": "Spell Scroll (9th Level)", "price": "20,000 gp*", "page": "DMG 200", "rarity": "Legendary"}, {"name": "Scroll of Tarrasque Summoning", "price": "150,000 gp", "page": "IDRF 315", "rarity": "Legendary"}, {"name": "Scroll of the Comet", "price": "250,000 gp", "page": "IDRF 315-316", "rarity": "Legendary"}]

zerothLevel = ["Acid Splash", "Blade Ward", "Booming Blade", "Chill Touch", "Control Flames", "Create Bonfire", "Dancing Lights", "Druidcraft", "Eldritch Blast", "Fire Bolt", "Friends", "Frostbite", "Green-Flame Blade", "Guidance", "Gust", "Infestation", "Light", "Lightning Lure", "Mage Hand", "Magic Stone", "Mending", "Message", "Minor Illusion", "Mold earth", "Poison Spray", "Prestidigitation", "Primal Savagery", "Produce Flame", "Ray of Frost", "Resistance", "Sacred Flame", "Shape Water", "Shillelagh", "Shocking Grasp", "Spare the Dying", "Sword Burst", "Thaumaturgy", "Thorn Whip", "Thunderclap", "Toll the Dead", "True Strike", "Vicious Mockery", "Word of Radiance"]
firstLevel = ["Absorb Elements", "Alarm", "Animal Friendship", "Armor of Agathys", "Arms of Hadar", "Bane", "Beast Bond", "Bless", "Burning Hands", "Catapult", "Cause Fear", "Ceremony", "Chaos Bolt", "Charm Person", "Chromatic Orb", "Color Spray", "Command", "Compelled Duel", "Comprehend Languages", "Create or Destroy Water", "Cure Wounds", "Detect Evil and Good", "Detect Magic", "Detect Poison and Disease", "Disguise Self", "Dissonant Whispers", "Divine Favor", "Earth Tremor", "Ensnaring Strike", "Entangle", "Expeditious Retreat", "Faerie Fire", "False Life", "Feather Fall", "Find Familiar", "Fog Cloud", "Goodberry", "Grease", "Guiding Bolt", "Hail of Thorns", "Healing Word", "Hellish Rebuke", "Heroism", "Hex", "Hunter's Mark", "Ice Knife", "Identify", "Illusory Script", "Inflict Wounds", "Jump", "Longstrider", "Mage Armor", "Magic Missile", "Protection from Evil and Good", "Purify Food and Drink", "Ray of Sickness", "Sanctuary", "Searing Smite", "Shield", "Shield of Faith", "Silent Image", "Sleep", "Snare", "Speak with Animals", "Tasha's Hideous Laughter", "Tenser's Floating Disk", "Thunderous Smite", "Thunderwave", "Unseen Servant", "Witch Bolt", "Wrathful Smite", "Zephyr Strike"]
secondLevel = ["Aganazzar's Scorcher", "Aid", "Alter Self", "Animal Messenger", "Arcane Lock", "Augury", "Barkskin", "Beast Sense", "Blindness/Deafness", "Blur", "Branding Smite", "Calm Emotions", "Cloud of Daggers", "Continual Flame", "Cordon of Arrows", "Crown of Madness", "Darkness", "Darkvision", "Detect Thoughts", "Dragon' Breath", "Dust Devil", "Earthbind", "Enhance Ability", "Enlarge/Reduce", "Enthrall", "Find Steed", "Find Traps", "Flame Blade", "Flaming Sphere", "Gentle Repose", "Gust of Wind", "Healing Spirit", "Heat Metal", "Hold Person", "Invisibility", "Knock", "Lesser Restoration", "Levitate", "Locate Animals or Plants", "Locate Object", "Magic Mouth", "Magic Weapon", "Maximilian's Earthen Grasp", "Melf's Acid Arrow", "Mind Spike", "Mirror Image", "Misty Step", "Moonbeam", "Nystul's Magic Aura", "Pass Without Trace", "Phantasmal Force", "Prayer of Healing", "Protection from Poison", "Pyrotechnics", "Ray of Enfeeblement", "Rope Trick", "Scorching Ray", "See invisibility", "Shadow Blade", "Shatter", "Silence", "Skywrite", "Snilloc's Snowball Swarm", "Spider Climb", "Spike Growth", "Spiritual Weapon", "Suggestion", "Warding Bond", "Warding Wind", "Web", "Zone of Truth"]
thirdLevel = ["Animate Dead", "Aura of Vitality", "Beacon of Hope", "Bestow Curse", "Blinding Smite", "Blink", "Call Lightning", "Catnap", "Clairvoyance", "Conjure Animals", "Conjure Barrage", "Counterspell", "Create Food and Water", "Crusader's Mantle", "Daylight", "Dispel Magic", "Elemental Weapon", "Enemies abound", "Erupting Earth", "Fear", "Feign Death", "Fireball", "Flame Arrows", "Fly", "Gaseous Form", "Glyph of Warding", "Haste", "Hunger of Hadar", "Hypnotic Pattern", "Leomund's Tiny Hut", "Life Transference", "Lightning Arrow", "Lightning Bolt", "Magic Circle", "Major Image", "Mass Healing Word", "Meld into Stone", "Melf's Minute Meteors", "Nondetection", "Phantom Steed", "Plant Growth", "Protection from Energy", "Remove Curse", "Revivify", "Sending", "Sleet Storm", "Slow", "Speak with Dead", "Speak with Plants", "Spirit Guardians", "Stinking Cloud", "Summon Lesser Demons", "Thunder Step", "Tidal Wave", "Tiny Servant", "Tongues", "Vampiric Touch", "Wall of Sand", "Wall of Water", "Water Breathing", "Water Walk", "Wind Wall"]
fourthLevel = ["Arcane Eye", "Aura of Life", "Aura of Purity", "Banishment", "Blight", "Charm Monster", "Compulsion", "Confusion", "Conjure Minor Elementals", "Conjure Woodland Beings", "Control Water", "Death Ward", "Dimension Door", "Divination", "Dominate Beast", "Elemental Bane", "Evard's Black Tentacles", "Fabricate", "Find Greater Steed", "Fire Shield", "Freedom of Movement", "Giant Insect", "Grasping Vine", "Greater Invisibility", "Guardian of Faith", "Guardian of Nature", "Hallucinatory Terrain", "Ice Storm", "Leomund's Secret Chest", "Locate Creature", "Mordenkainen's Faithful Hound", "Mordenkainen's Private Sanctum", "Otiluke's Resilient Sphere", "Phantasmal Killer", "Polymorph", "Shadow of Moil", "Sickening Radiance", "Staggering Smite", "Stone Shape", "Stoneskin", "Storm Sphere", "Summon Greater Demon", "Vitriolic Sphere", "Wall of Fire", "Watery Sphere"]
fifthLevel = ["Animate Objects", "Antilife Shell", "Awaken", "Banishing Smite", "Bigby's Hand", "Circle of Power", "Cloudkill", "Commune", "Commune with Nature", "Cone of Cold", "Conjure Elemental", "Conjure Volley", "Contact Other Plane", "Contagion", "Control Winds", "Creation", "Danse Macabre", "Dawn", "Destructive Wave", "Dispel Evil and Good", "Dominate Person", "Dream", "Enervation", "Far Step", "Flame Strike", "Geas", "Greater Restoration", "Hallow", "Hold Monster", "Holy Weapon", "Immolation", "Infernal Calling", "Insect Plague", "Legend Lore", "Maelstrom", "Mass Cure Wounds", "Mislead", "Modify Memory", "Negative Energy Flood", "Passwall", "Planar Binding", "Raise Dead", "Rary's Telepathic Bond", "Reincarnate", "Scrying", "Seeming", "Skill Empowerment", "Steel Wind Strike", "Swift Quiver", "Synaptic Static", "Telekinesis", "Teleportation Circle", "Transmute Rock", "Tree Stride", "Wall of Force", "Wall of Light", "Wall of Stone", "Wrath of Nature"]
sixthLevel = ["Arcane Gate", "Blade Barrier", "Bones of the Earth", "Chain Lightning", "Circle of Death", "Conjure Fey", "Contingency", "Create Homunculus", "Create Undead", "Disintegrate", "Drawmij's Instant Summons", "Druid Grove", "Eyebite", "Find the Path", "Flesh to Stone", "Forbiddance", "Globe of Invulnerability", "Guards and Wards", "Harm", "Heal", "Heroes' Feast", "Investiture of Flame", "Investiture of Ice", "Investiture of Stone", "Investiture of Wind", "Magic Jar", "Mass Suggestion", "Mental Prison", "Move Earth", "Otiluke's Freezing Sphere", "Otto's Irresistible Dance", "Planar Ally", "Primordial Ward", "Primordial Ward", "Programmed Illusion", "Scatter", "Soul Cage", "Sunbeam", "Tenser's Transformation", "Transport via Plants", "True Seeing", "Wall of Ice", "Wall of Thorns", "Wind Walk", "Word of Recall"]
seventhLevel = ["Conjure Celestial", "Crown of Stars", "Delayed Blast Fireball", "Divine Word", "Etherealness", "Finger of Death", "Fire Storm", "Forcecage", "Mirage Arcane", "Mordenkainen's Magnificent Mansion", "Mordenkainen's Sword", "Plane Shift", "Power Word Pain", "Prismatic Spray", "Project Image", "Regenerate", "Resurrection", "Reverse Gravity", "Sequester", "Simulacrum", "Symbol", "Teleport", "Temple of the Gods", "Whirlwind"]
eighthLevel = ["Abi-Dalzim's Horrid Wilting", "Animal Shapes", "Antimagic Field", "Antipathy/ Sympathy", "Clone", "Control Weather", "Demiplane", "Dominate Monster", "Earthquake", "Feeblemind", "Glibness", "Holy Aura", "Illusory Dragon", "Incendiary Cloud", "Maddening Darkness", "Maze", "Mighty Fortress", "Mind Blank", "Power Word Stun", "Sunburst", "Telepathy", "Trap the Soul", "Tsunami"]

AllSpells = [zerothLevel, firstLevel, secondLevel, thirdLevel, fourthLevel, fifthLevel, sixthLevel, seventhLevel, eighthLevel]
AllowedSpells = AllSpells[0:4]

SpellGems = [{"name": "Spell Gem (Cantrip)", "price": "150 gp", "page": "OA 223", "rarity": "Uncommon"}, {"name": "Spell Gem (1st Level)", "price": "350 gp", "page": "OA 223", "rarity": "Uncommon"}, {"name": "Spell Gem (2nd Level)", "price": "1,500 gp", "page": "OA 223", "rarity": "Rare"}, {"name": "Spell Gem (3rd Level)", "price": "4,000 gp", "page": "OA 223", "rarity": "Rare"}, {"name": "Spell Gem (4th Level)", "price": "8,000 gp", "page": "OA 223", "rarity": "Very Rare"}, {"name": "Spell Gem (5th Level)", "price": "15,000 gp", "page": "OA 223", "rarity": "Very Rare"}, {"name": "Spell Gem (6th Level)", "price": "20,000 gp", "page": "OA 223", "rarity": "Very Rare"}, {"name": "Spell Gem (7th Level)", "price": "35,000 gp", "page": "OA 223", "rarity": "Legendary"}, {"name": "Spell Gem (8th Level)", "price": "51,000 gp", "page": "OA 223", "rarity": "Legendary"}, {"name": "Spell Gem (9th Level)", "price": "78,000 gp", "page": "OA 223", "rarity": "Legendary"}]

Tattoos = [{"name": "Illuminator's Tattoo", "price": "65 gp", "page": "TCE 129", "rarity": "Common"}, {"name": "Masquerade Tattoo", "price": "75 gp", "page": "TCE 131", "rarity": "Common"}, {"name": "Barrier Tattoo (Uncommon)", "price": "200 gp", "page": "TCE 122", "rarity": "Uncommon"}, {"name": "Coiling Grasp Tattoo", "price": "500 gp", "page": "TCE 123", "rarity": "Uncommon"}, {"name": "Eldritch Claw Tattoo", "price": "750 gp", "page": "TCE 126-127", "rarity": "Uncommon"}, {"name": "Barrier Tattoo (Rare)", "price": "1,500 gp", "page": "TCE 122", "rarity": "Rare"}, {"name": "Shadowfell Brand Tattoo", "price": "1,100 gp", "page": "TCE 134-135", "rarity": "Rare"}, {"name": "Absorbing Tattoo", "price": "8,000 gp", "page": "TCE 119", "rarity": "Very Rare"}, {"name": "Barrier Tattoo (Very Rare)", "price": "6,000 gp", "page": "TCE 122", "rarity": "Very Rare"}, {"name": "Ghost Step Tattoo", "price": "9,000 gp", "page": "TCE 128", "rarity": "Very Rare"}, {"name": "Lifewell Tattoo", "price": "5,100 gp", "page": "TCE 129", "rarity": "Very Rare"}, {"name": "Blood Fury Tattoo", "price": "32,000 gp*", "page": "TCE 122", "rarity": "Legendary"}]

Cloth = [{'name': 'Infernal Leather', 'price': '750 gp', 'page': 'Special Materials', 'rarity': 'Uncommon', 'type': 'Cloth'}, {'name': 'Shadowfell Linen', 'price': '750 gp', 'page': 'Special Materials', 'rarity': 'Uncommon', 'type': 'Cloth'}]
Organic = [{'name': 'Asmorch Wood', 'price': '500 gp', 'page': 'Special Materials', 'rarity': 'Uncommon', 'type': 'Organic'}, {'name': 'Coral', 'price': '100 gp', 'page': 'Special Materials', 'rarity': 'Uncommon', 'type': 'Organic'}, {'name': 'Plague wood', 'price': '250 gp', 'page': 'Special Materials', 'rarity': 'Uncommon', 'type': 'Organic'}, {'name': 'Spiritual Wood', 'price': '800 gp', 'page': 'Special Materials', 'rarity': 'Uncommon', 'type': 'Organic'}]
Metal = [{'name': 'Cold Iron', 'price': '100 gp', 'page': 'Special Materials', 'rarity': 'Uncommon', 'type': 'Metal'}, {'name': 'Adamantine', 'price': '300 gp', 'page': 'Special Materials', 'rarity': 'Uncommon', 'type': 'Metal'}, {'name': 'Darksteel', 'price': '600 gp', 'page': 'Special Materials', 'rarity': 'Uncommon', 'type': 'Metal'}, {'name': 'Flametouched Iron', 'price': '500 gp', 'page': 'Special Materials', 'rarity': 'Uncommon', 'type': 'Metal'}, {'name': 'Orichalcum', 'price': '650 gp', 'page': 'Special Materials', 'rarity': 'Uncommon', 'type': 'Metal'}, {'name': 'Infernal Steel', 'price': '750 gp', 'page': 'Special Materials', 'rarity': 'Uncommon', 'type': 'Metal'}, {'name': 'Osmodium', 'price': '760 gp', 'page': 'Special Materials', 'rarity': 'Uncommon', 'type': 'Metal'}, {'name': 'Stellar Iron', 'price': '850 gp', 'page': 'Special Materials', 'rarity': 'Uncommon', 'type': 'Metal'}]
Mineral = [{'name': 'Aerocrystal', 'price': '750 gp', 'page': 'Special Materials', 'rarity': 'Uncommon', 'type': 'Mineral'}, {'name': 'Dwarvenstone', 'price': '300 gp', 'page': 'Special Materials', 'rarity': 'Uncommon', 'type': 'Mineral'}, {'name': 'Eternal Ice', 'price': '600 gp', 'page': 'Special Materials', 'rarity': 'Uncommon', 'type': 'Mineral'}, {'name': 'Ignium', 'price': '100 gp', 'page': 'Special Materials', 'rarity': 'Uncommon', 'type': 'Mineral'}, {'name': 'Obsidian', 'price': '500 gp', 'page': 'Special Materials', 'rarity': 'Uncommon', 'type': 'Mineral'}]

SpecialMaterials = [Cloth, Organic, Metal, Mineral]

MasterList = [Potions, AllSpells, SpellGems, SpecialMaterials]


def getScrolls(num_scrolls=1, max_level=1, min_level=-1):
    if min_level > max_level or min_level < 0:
        min_level = max_level

    scrolls = []
    for i in range(num_scrolls):
        attempts = 0
        while True:
            attempts = attempts + 1
            if min_level != max_level:
                level = randint(min_level, max_level)
            else:
                level = max_level
            randNum = randint(0, len(AllowedSpells[level]) - 1)
            newScroll = AllowedSpells[level][randNum]
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

            randNum = randint(0, len(SpecialMaterials[materialType]) - 1)
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
    TableList = ["Tattoos"]
    RaritiesList = ["Common", "Uncommon", "Rare", "Very Rare", "Legendary"]
    results = []

    if (tableName in TableList) and (rarity in RaritiesList):
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
                    randNum = randint(0, len(MasterList[table]) - 1)
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

def getTattoo(max_rarity="Common", min_rarity=""):
    TableList = ["Tattoos"]
    RaritiesList = ["Common", "Uncommon", "Rare", "Very Rare", "Legendary"]
    tattoo = {"name": "Tattoo Not Found", "price": "Not Found"}

    if len(min_rarity) == 0:
        min_rarity = max_rarity

    if (min_rarity in RaritiesList) and (max_rarity in RaritiesList):
        if min_rarity == max_rarity:
            rarity = RaritiesList.index(max_rarity)

        else:
            if (RaritiesList.index(min_rarity) > RaritiesList.index(max_rarity)):
                temp = min_rarity
                min_rarity = max_rarity
                max_rarity = temp

            rarity = randint(RaritiesList.index(min_rarity), RaritiesList.index(max_rarity))

        attempts = 0
        searchComplete = False
        while (not searchComplete) and (attempts < 100):
            attempts = attempts + 1
            randomTattoo = Tattoos[randint(0, len(Tattoos) - 1)]
            if randomTattoo["rarity"] == RaritiesList[rarity]:
                searchComplete = True
                tattoo = randomTattoo

    return tattoo

def getTattooItems():
    sections = ["Spellwrought Tattoos", "Permanent (As Listed)"]
    RaritiesList = ["Common", "Uncommon", "Rare", "Very Rare", "Legendary"]
    spellwroughtsSpellLevel = ["Cantrip", "1st Level", "2nd Level", "3rd Level"]
    spellwroughtsPrice = ["150gp", "250gp", "1000gp", "3000gp"]
    sectionMarker = "ENDSECTION"
    mergeMarker = "MERGE"
    sameLineMarker = "SAMELINE"

    tattooList = []
    tattooList.append(sections[0])
    tattooList.append(mergeMarker)

    for i in range(len(spellwroughtsSpellLevel) // 2):
        lesserScrollLevel = i * 2
        greaterScrollLevel = lesserScrollLevel + 1
        tattooList.append(spellwroughtsSpellLevel[lesserScrollLevel])
        tattooList.append(spellwroughtsSpellLevel[greaterScrollLevel])

        tattooList.append(sameLineMarker)
        tattooList.append(sameLineMarker)

        tattooList.append(spellwroughtsPrice[lesserScrollLevel])
        tattooList.append(spellwroughtsPrice[greaterScrollLevel])

        weakerScrolls = getScrolls(1, lesserScrollLevel)
        strongerScrolls = getScrolls(1, greaterScrollLevel)

        tattooList.append(weakerScrolls[0])
        tattooList.append(strongerScrolls[0])

    tattooList.append(sectionMarker)
    tattooList.append(sectionMarker)

    tattooList.append(sections[1])
    tattooList.append(mergeMarker)

    permanentTattoo = getTattoo(RaritiesList[0], RaritiesList[2])
    tattooList.append(permanentTattoo["name"])
    tattooList.append(mergeMarker)
    tattooList.append(sameLineMarker)
    tattooList.append(sameLineMarker)
    tattooList.append(permanentTattoo["price"])
    tattooList.append(mergeMarker)

    return tattooList


MANUAL_INPUT = getTattooItems()


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



class Table:
    def __init__(self, valuesList=[], text_wrapping=False, max_width=-1):
        self.Cell = []
        self.RowInfo = []
        self.WrapSheet = []
        self.widestLeftColumn = 0
        self.widestRightColumn = 0
        self.widestRow = 0
        self.TOTAL_WIDTH_MINIMUM = 28  # Originally 28 -7 based on feedback from cellphone users.
        self.NON_CONTENT_WIDTH = 7
        self.userWidth = max_width
        if self.userWidth > self.TOTAL_WIDTH_MINIMUM:
            self.widthAllowance = self.userWidth
        else:
            self.widthAllowance = self.TOTAL_WIDTH_MINIMUM
        self.PerformWrapping = text_wrapping
        self.WrapsForRow = []
        self.DoesWrap = False
        self.numRowsWrapped = 0
        self.MERGE_MARKER = "MERGE"
        self.SECTION_MARKER = "ENDSECTION"
        self.COMBINE_ROW_MARKER = "SAMELINE"
        self.BoxChars = {"Left":
                             {"Corner":
                                  {"Top":
                                       {"single": '┌',
                                        "double": '╔'},
                                   "Bottom":
                                       {"single": '└',
                                        "double": '╚'}},
                              "Vertical":
                                  {"single":
                                       {"intersect":
                                            {"single": '├',
                                             "double": '╞'},
                                        "straight": '│'},
                                   "double":
                                       {"intersect":
                                            {"single": '╟',
                                             "double": '╠'},
                                        "straight": '║'}},
                              },
                         "Horizontal":
                             {"single":
                                  {"intersect":
                                       {"down":
                                            {"single": '┬',
                                             "double": '╥'},
                                        "through":
                                            {"single": '┼',
                                             "double": '╫'},
                                        "up":
                                            {"single": '┴',
                                             "double": '╨'}},
                                   "straight": '─'},
                              "double":
                                  {"intersect":
                                       {"down":
                                            {"single": '╤',
                                             "double": '╦'},
                                        "through":
                                            {"single": '╪',
                                             "double": '╬'},
                                        "up":
                                            {"single": '╧',
                                             "double": '╩'}},
                                   "straight": '═'}
                              },
                         "Right":
                             {"Corner":
                                  {"Top":
                                       {"single": '┐',
                                        "double": '╗'},
                                   "Bottom":
                                       {"single": '┘',
                                        "double": '╝'}},
                              "Vertical":
                                  {"single":
                                       {"intersect":
                                            {"single": '┤',
                                             "double": '╡'},
                                        "straight": '│'},
                                   "double":
                                       {"intersect":
                                            {"single": '╢',
                                             "double": '╣'},
                                        "straight": '║'}},
                              }
                         }
        if len(valuesList) > 0:
            self.build(valuesList)

    def clearMeasurements(self):
        self.widestLeftColumn = 0
        self.widestRightColumn = 0
        self.widestRow = 0
        if self.userWidth > self.TOTAL_WIDTH_MINIMUM:
            self.widthAllowance = self.userWidth
        else:
            self.widthAllowance = self.TOTAL_WIDTH_MINIMUM
        self.WrapsForRow = []
        self.DoesWrap = False
        self.numRowsWrapped = 0

    def clearRowInfo(self):
        self.RowInfo = []

    def getWrapItemNumber(self, wrap):
        itemNumber = -1
        for namedItem in range(len(self.WrapSheet)):
            for rowAddress in range(len(self.WrapSheet[namedItem])):
                if self.WrapSheet[namedItem][rowAddress] == wrap:
                    itemNumber = namedItem
                    break
        return itemNumber

    def refreshWrapSheet(self):
        stepCount = 0
        for namedItem in range(len(self.WrapSheet)):
            for rowAddress in range(len(self.WrapSheet[namedItem])):
                self.WrapSheet[namedItem][rowAddress] = stepCount
                stepCount += 1

    def addWraps(self, item, wraps):
        for address in range(wraps):
            self.WrapSheet[item].append([address])
        self.refreshWrapSheet()

    def columZipper(self, left_column, right_column):
        if len(left_column) > len(right_column):
            greaterColumn = left_column
            lesserColumn = right_column
            GreaterIsLeftmost = True
        else:
            greaterColumn = right_column
            lesserColumn = left_column
            GreaterIsLeftmost = False

        if len(lesserColumn) == 0 or lesserColumn[0] == self.MERGE_MARKER:
            filler = self.MERGE_MARKER
        else:
            filler = " "
        for i in range(len(greaterColumn) - len(lesserColumn)):
            lesserColumn.append(filler)

        joinedColumns = []
        if len(greaterColumn) == len(lesserColumn):
            for j in range(len(greaterColumn)):
                if GreaterIsLeftmost:
                    joinedColumns.append([greaterColumn[j], lesserColumn[j]])
                else:
                    joinedColumns.append([lesserColumn[j], greaterColumn[j]])

        return joinedColumns

    def wrapTable(self, max_length= -1):
        if self.DoesWrap:
            if max_length < 1:
                max_length = self.widthAllowance - self.NON_CONTENT_WIDTH

            itemsToWrap = []
            for i in range(len(self.WrapSheet)):
                content = self.Cell[i][0]
                if not ((content == self.COMBINE_ROW_MARKER) or (content == self.SECTION_MARKER)):
                    itemsToWrap.append(self.WrapSheet[i])
            itemsToWrap.reverse()
            for item in itemsToWrap:
                row = item[0]

                if len(self.Cell[row][0]) > len(self.Cell[row][1]):
                    smallerCell = 1
                    largerCell = 0
                    isLargerLeftmost = True
                else:
                    smallerCell = 0
                    largerCell = 1
                    isLargerLeftmost = False

                if self.Cell[row][largerCell] != self.MERGE_MARKER:
                    primaryLengthConstraint = max_length - len(self.Cell[row][smallerCell])
                    primaryCells = shortestWrap(self.Cell[row][largerCell], primaryLengthConstraint)

                    secondaryLengthConstraint = 0
                    for cell in primaryCells:
                        if len(cell) > secondaryLengthConstraint:
                            secondaryLengthConstraint = len(cell)

                    smallCellContent = self.Cell[row][smallerCell]
                    if self.Cell[row][smallerCell] != self.MERGE_MARKER:
                        secondaryCells = shortestWrap(self.Cell[row][smallerCell], (max_length - secondaryLengthConstraint))
                        sameLineMarkers = [self.COMBINE_ROW_MARKER, self.MERGE_MARKER]
                    else:
                        secondaryCells = [self.MERGE_MARKER]
                        sameLineMarkers = [self.COMBINE_ROW_MARKER, self.MERGE_MARKER]

                    if largerCell == 0:
                        newRows = self.columZipper(primaryCells, secondaryCells)
                    else:
                        newRows = self.columZipper(secondaryCells, primaryCells)

                    self.addWraps(self.getWrapItemNumber(row), len(newRows))

                    self.Cell.pop(row)
                    for i in range(len(newRows)):
                        line = newRows[i]
                        if i == 0:
                            self.Cell.insert(row, line)
                        else:
                            self.Cell.insert(previousLineIndex + 1, line)
                        if i < (len(newRows) - 1):
                            newRowIndex = self.Cell.index(line)
                            self.Cell.insert(newRowIndex + 1, sameLineMarkers)
                            previousLineIndex = self.Cell.index(sameLineMarkers, newRowIndex)


                self.getRowTraits()
                self.measureDimensions()

    def build(self, valuesList):
        self.fillCells(valuesList)
        self.measureDimensions()
        self.getRowTraits()
        for i in range(len(self.Cell)):
            self.WrapSheet.append([i])
        self.refreshWrapSheet()

        if self.PerformWrapping and self.DoesWrap:
            self.wrapTable()

    def fillCells(self, valuesList):
        self.Cell = []

        # Iterate over every line
        for i in range(len(valuesList) // 2):
            i = i * 2
            j = i + 1
            leftColumn = valuesList[i].rstrip()
            leftColumn = leftColumn.strip('"')
            rightColumn = valuesList[j].rstrip()
            rightColumn = rightColumn.strip('"')
            self.Cell.append([leftColumn, rightColumn])

    def checkToWrap(self, row):
        left = 0
        right = 1
        leftValueLength = len(self.Cell[row][left])
        rightValueLength = len(self.Cell[row][right])
        if self.Cell[row][right] == self.MERGE_MARKER:
            rightValueLength = 0

        if (self.Cell[row][left] != self.SECTION_MARKER) and (self.Cell[row][left] != self.COMBINE_ROW_MARKER):
            if leftValueLength > self.widestLeftColumn:
                self.widestLeftColumn = leftValueLength
            if rightValueLength > self.widestRightColumn:
                self.widestRightColumn = rightValueLength

    def measureDimensions(self):
        self.clearMeasurements()
        left = 0
        right = 1

        for row in range(len(self.Cell)):
            leftValueLength = len(self.Cell[row][left])
            rightValueLength = len(self.Cell[row][right])
            if self.Cell[row][right] == self.MERGE_MARKER:
                rightValueLength = 0

            if (self.Cell[row][left] != self.SECTION_MARKER) and (self.Cell[row][left] != self.COMBINE_ROW_MARKER) and \
                    (self.Cell[row][right] != self.MERGE_MARKER):
                if leftValueLength > self.widestLeftColumn:
                    self.widestLeftColumn = leftValueLength
                if rightValueLength > self.widestRightColumn:
                    self.widestRightColumn = rightValueLength

                if self.widestRow < (leftValueLength + rightValueLength):
                    self.widestRow = leftValueLength + rightValueLength
                    self.WrapsForRow.append(row)
                    self.numRowsWrapped = self.numRowsWrapped + 1

        if self.numRowsWrapped > 0:
            self.DoesWrap = True

    def getRowTraits(self):
        self.clearRowInfo()
        left = 0
        right = 1

        for row in range(len(self.Cell)):
            if self.Cell[row][right] == self.MERGE_MARKER:
                merge = True
            else:
                merge = False

            if self.Cell[row][left] == self.SECTION_MARKER:
                sectionEnd = True
            else:
                sectionEnd = False

            if self.Cell[row][left] == self.COMBINE_ROW_MARKER:
                combine = True
            else:
                combine = False

            self.RowInfo.append({self.MERGE_MARKER: merge, self.SECTION_MARKER: sectionEnd, self.COMBINE_ROW_MARKER: combine})

    def getBoxCharsForRow(self, row):
        merged = self.MERGE_MARKER
        noPrint = self.COMBINE_ROW_MARKER
        nextMerged = "Next Merged"
        sectionHead = "Section Head"
        tableHead = "Table Head"
        sectionFoot = "Section Foot"
        tableFoot = "Table Foot"
        prevMerged = "Previous Merged"
        sectionMarker = self.SECTION_MARKER
        setOfTraits = [merged, nextMerged, sectionHead, tableHead, sectionMarker, sectionFoot, sectionMarker,
                       prevMerged]

        traits = dict()
        for key in setOfTraits:
            traits[key] = False

        if self.RowInfo[row][merged]:
            traits[merged] = True
        if self.RowInfo[row][sectionMarker]:
            traits[sectionMarker] = True

        # Adjust for multi-line rows due to text wrapping
        nextPrintableRow = row
        nextFound = False
        checkRow = row + 1
        while (not nextFound) and (checkRow < (len(self.Cell) - 1)):
            if not self.RowInfo[checkRow][noPrint]:
                nextPrintableRow = checkRow
                nextFound = True
            else:
                checkRow += 1

        secondNextPrintableRow = nextPrintableRow
        for i in range(len(self.Cell) - (nextPrintableRow - 1)):
            nextFound = False
            checkRow = nextPrintableRow + 1
            while (not nextFound) and (checkRow < (len(self.Cell) - 1)):
                if not self.RowInfo[checkRow][noPrint]:
                    secondNextPrintableRow = checkRow
                    nextFound = True
                else:
                    checkRow += 1

        if row == 0:
            traits[tableHead] = True
        elif row == len(self.RowInfo):
            traits[tableFoot] = True
        elif self.RowInfo[row - 1][sectionMarker]:
            traits[sectionHead] = True
        else:
            # Check if part of a multi-line section head or table head
            previousPrintableRow = row - 1
            while self.RowInfo[previousPrintableRow][noPrint] and (previousPrintableRow > -1):
                previousPrintableRow -= 1

            if previousPrintableRow > 0:
                precedingPreviousPrintable = previousPrintableRow - 1
            else:
                precedingPreviousPrintable = 0
            if previousPrintableRow <= 0 or self.RowInfo[precedingPreviousPrintable][self.SECTION_MARKER]:
                traits[sectionHead] = True

            # Process information for next printable rows
            if self.RowInfo[nextPrintableRow][sectionMarker]:
                traits[sectionFoot] = True
                # If row is a sectionFoot then need to check row after the section marker row
                if row < len(self.RowInfo):
                    if self.RowInfo[secondNextPrintableRow][merged]:
                        traits[nextMerged] = True
            else:
                if self.RowInfo[row + 1][merged]:
                    traits[nextMerged] = True

        nextLine = []

        # Left edge and fill line
        if traits[sectionFoot] or traits[sectionHead] or traits[tableHead]:  # Next line is double
            isDoubleLine = True
            nextLine.append(self.BoxChars["Left"]["Vertical"]["double"]["intersect"]["double"])
            nextLine.append(self.BoxChars["Horizontal"]["double"]["straight"])
            nextLine.append(self.BoxChars["Right"]["Vertical"]["double"]["intersect"]["double"])
        else:  # Next line is single
            isDoubleLine = False
            nextLine.append(self.BoxChars["Left"]["Vertical"]["double"]["intersect"]["single"])
            nextLine.append(self.BoxChars["Horizontal"]["single"]["straight"])
            nextLine.append(self.BoxChars["Right"]["Vertical"]["double"]["intersect"]["single"])

        # Separator
        if traits[merged]:  # Top is flat
            if traits[nextMerged]:  # bottom flat, all flat
                if isDoubleLine:
                    nextLine.append(self.BoxChars["Horizontal"]["double"]["straight"])
                else:
                    nextLine.append(self.BoxChars["Horizontal"]["single"]["straight"])
            else:  # points down
                if isDoubleLine:
                    nextLine.append(self.BoxChars["Horizontal"]["double"]["intersect"]["down"]["single"])
                else:
                    nextLine.append(self.BoxChars["Horizontal"]["single"]["intersect"]["down"]["single"])
        else:  # Points up
            if traits[nextMerged]:  # bottom is flat
                if isDoubleLine:
                    nextLine.append(self.BoxChars["Horizontal"]["double"]["intersect"]["up"]["single"])
                else:
                    nextLine.append(self.BoxChars["Horizontal"]["single"]["intersect"]["up"]["single"])
            else:  # Points down as well
                if isDoubleLine:
                    nextLine.append(self.BoxChars["Horizontal"]["double"]["intersect"]["through"]["single"])
                else:
                    nextLine.append(self.BoxChars["Horizontal"]["single"]["intersect"]["through"]["single"])

        return nextLine

    def printUnicodeTable(self):
        self.getRowTraits()
        self.measureDimensions()
        print("```")

        left = 0
        right = 1
        widthLeft = self.widestLeftColumn
        widthRight = self.widestRightColumn

        for i in range(len(self.RowInfo)):

            if i == 0:  # Print Table Header
                lineFill = self.BoxChars["Horizontal"]["double"]["straight"]
                if self.RowInfo[i][self.MERGE_MARKER]:
                    separator = lineFill
                else:
                    separator = self.BoxChars["Horizontal"]["double"]["intersect"]["down"]["single"]

                print(self.BoxChars["Left"]["Corner"]["Top"]["double"].ljust(widthLeft + 3, lineFill), end=separator)
                print("".rjust(widthRight + 2, lineFill),
                      end=(self.BoxChars["Right"]["Corner"]["Top"]["double"] + '\n'))

            edgeLeft = self.BoxChars["Right"]["Vertical"]["double"]["straight"]
            edgeLeft = edgeLeft + ' '
            separator = self.BoxChars["Left"]["Vertical"]["single"]["straight"]
            edgeRight = self.BoxChars["Right"]["Vertical"]["double"]["straight"]
            edgeRight = ' ' + edgeRight + '\n'

            if (not self.RowInfo[i][self.COMBINE_ROW_MARKER]) and (self.Cell[i][left] != self.SECTION_MARKER):

                if self.RowInfo[i][self.MERGE_MARKER]:
                    print(edgeLeft + "%s" % self.Cell[i][left].center(widthLeft + widthRight + 3), end=edgeRight)
                else:
                    print(edgeLeft + "%s %s %s" % (self.Cell[i][left].center(widthLeft), separator,
                                                   self.Cell[i][right].center(widthRight)), end=edgeRight)

                # Print Table Footer
                if i == (len(self.RowInfo) - 1):
                    lineFill = self.BoxChars["Horizontal"]["double"]["straight"]
                    if self.RowInfo[i][self.MERGE_MARKER]:
                        separator = lineFill
                    else:
                        separator = self.BoxChars["Horizontal"]["double"]["intersect"]["up"]["single"]
                    print(self.BoxChars["Left"]["Corner"]["Bottom"]["double"].ljust(widthLeft + 3, lineFill),
                          end=separator)
                    print("".rjust(widthRight + 2, lineFill),
                          end=(self.BoxChars["Right"]["Corner"]["Bottom"]["double"] + '\n'))

                elif not self.RowInfo[i + 1][self.COMBINE_ROW_MARKER]:  # Print bottom line of row
                    characters = self.getBoxCharsForRow(i)
                    edgeLeft = characters[0]
                    lineFill = characters[1]
                    edgeRight = characters[2] + '\n'
                    separator = characters[3]

                    print(edgeLeft.ljust(widthLeft + 3, lineFill), end=separator)
                    print("".rjust(widthRight + 2, lineFill), end=edgeRight)

        print("```")


def addDaysToPOSIX(add_days=1, to_hour=-1, day_cycle=-1, cycle_start=0, start_day=-1):
    NANOSECONDS_PER_SECOND = 1000000000
    SECONDS_PER_HOUR = 60 * 60
    SECONDS_PER_DAY = SECONDS_PER_HOUR * 24

    if start_day < 0:
        currentTimeInPOSIX = time_ns() // NANOSECONDS_PER_SECOND
    else:
        currentTimeInPOSIX = start_day

    secondsAfterMidnight = currentTimeInPOSIX % SECONDS_PER_DAY
    currentTimeInPOSIX = currentTimeInPOSIX - secondsAfterMidnight

    if day_cycle > 0:
        cycleOffset = (currentTimeInPOSIX - cycle_start) % (day_cycle * SECONDS_PER_DAY)
        futureTimeInPOSIX = currentTimeInPOSIX - cycleOffset

    futureTimeInPOSIX = futureTimeInPOSIX + (add_days * SECONDS_PER_DAY)

    if to_hour > 0:
        futureTimeInPOSIX = futureTimeInPOSIX + (to_hour * SECONDS_PER_HOUR)

    return futureTimeInPOSIX


def getInputOrDefault(prompt="Enter input: ", stored_value="DEFAULT", code_for_default='x'):
    userInput = str(input(prompt))
    if userInput != code_for_default:
        stored_value = userInput

    return stored_value


def main():
    TABLE_TITLES_DEFAULTS = ["Saoirse's Tattoo Journal"]
    NUM_TABLES_DEFAULT = 1
    DELIMITER_STRING = 'ENDTABLE'
    IsCustomTables = True
    TextWrapping = True
    WRAP_WIDTH_DEFAULT = 29
    POSIX_DAY_IN_SECONDS = 60 * 60 * 24
    MARKET_CYCLE_START_POSIX = 0 * POSIX_DAY_IN_SECONDS  # Days offset from epoch
    POSTING_HOUR_DEFAULT = 0  # Hana Den posting time
    DAYS_IN_CYCLE_DEFAULT = 3  # Hana Den market cycle length
    DAYS_TO_ADD_DEFAULT = 3  # Number of days in the future for discord time code
    FILENAME_DEFAULT = 'Shop Sheet.txt'  # Must be UTF-8 text

    userInput = 'y'
    if userInput != 'n':
        IsCustomTables = False

    userFile = FILENAME_DEFAULT
    if IsCustomTables:
        prompt = "\nWhen entering a file name, include the file extension (\".txt\").\n"
        prompt = prompt + "Only enter the file name, do not add anything else.\n"
        prompt = prompt + "(Enter 'x' for default '%s') Enter file name: " % FILENAME_DEFAULT
        userFile = getInputOrDefault(prompt, FILENAME_DEFAULT)

    desiredWidth = WRAP_WIDTH_DEFAULT
    if IsCustomTables:
        desiredWidth = int(getInputOrDefault("Enter how wide you want the tables to be in number of characters."
                                             "Enter x for the default: ", WRAP_WIDTH_DEFAULT))

    if True:

        closingPlayersTag = "@Players Saoirse's Parlour closes <t:"
        endOfCLosingPlayersTag = ":R>."

        if IsCustomTables:

            unixTimeToAdjust = int(getInputOrDefault("Enter unix time stamp. Enter x for automatic calculation: ",
                                                     str(-1)))
            daysOpen = int(getInputOrDefault("Enter the number of days until the market will close. "
                                             "Enter x for the default: ", DAYS_TO_ADD_DEFAULT))
            cycleLength = int(getInputOrDefault("Enter the number of days the market is supposed ot be open. "
                                                "Enter x for the default: ", DAYS_IN_CYCLE_DEFAULT))
            hourToPost = int(getInputOrDefault("Enter the hour to post. 1 to 24 and in UTC time. "
                                               "Enter x for the default: ", POSTING_HOUR_DEFAULT))

            unixTimeStamp = addDaysToPOSIX(daysOpen, hourToPost, cycleLength, MARKET_CYCLE_START_POSIX,
                                           unixTimeToAdjust)
            closingPlayersTag = closingPlayersTag + str(unixTimeStamp)

        else:
            unixTimeStamp = addDaysToPOSIX(DAYS_TO_ADD_DEFAULT, POSTING_HOUR_DEFAULT, DAYS_IN_CYCLE_DEFAULT,
                                           MARKET_CYCLE_START_POSIX)
            closingPlayersTag = closingPlayersTag + str(unixTimeStamp)

        closingPlayersTag = closingPlayersTag + endOfCLosingPlayersTag

        numTables = NUM_TABLES_DEFAULT
        if IsCustomTables:
            prompt = "(Enter 'x' for default '%d') Enter number of tables to be made: " % NUM_TABLES_DEFAULT
            numTables = int(getInputOrDefault(prompt, str(NUM_TABLES_DEFAULT)))

        tableTitles = []
        for i in range(numTables):
            if i < len(TABLE_TITLES_DEFAULTS):
                titleDefault = TABLE_TITLES_DEFAULTS[i]
            else:
                titleDefault = "Table %d" % (i + 1)

            if IsCustomTables:
                if i < len(TABLE_TITLES_DEFAULTS):
                    titleDefault = TABLE_TITLES_DEFAULTS[i]
                else:
                    titleDefault = "Table %d" % (i + 1)
                prompt = "(Enter 'x' for default '%s') Enter table title: " % titleDefault
                titleDefault = getInputOrDefault(prompt, titleDefault)

            tableTitles.append(titleDefault)

        unprocessedTableInput = MANUAL_INPUT
        if numTables > 1:
            for i in range(numTables):

                if unprocessedTableInput.count(DELIMITER_STRING) > 0:
                    IndexOfDelimiter = unprocessedTableInput.index(DELIMITER_STRING)
                    tableItems = unprocessedTableInput[0:IndexOfDelimiter]
                    unprocessedTableInput = unprocessedTableInput[(IndexOfDelimiter + 1):]
                else:
                    tableItems = unprocessedTableInput

                print("**%s**" % tableTitles[i])
                marketTable = Table(tableItems, TextWrapping, desiredWidth)
                marketTable.printUnicodeTable()

        else:
            print("__**%s**__" % tableTitles[i])
            marketTable = Table(unprocessedTableInput, TextWrapping, desiredWidth)
            marketTable.printUnicodeTable()

        print(closingPlayersTag)


main()
