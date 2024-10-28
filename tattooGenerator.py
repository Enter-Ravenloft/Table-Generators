#  https://github.com/ItsQc/Ravenloft-Tables
#  If you have issue with this, ping Quincy on Discord
#  Lotsa Spaghetti

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

Tattoos = [{"name": "Illuminator's Tattoo", "price": "65 gp", "page": "TCE 129", "rarity": "Common"}, {"name": "Masquerade Tattoo", "price": "75 gp", "page": "TCE 131", "rarity": "Common"}, {"name": "Barrier Tattoo (Uncommon)", "price": "200 gp", "page": "TCE 122", "rarity": "Uncommon"}, {"name": "Coiling Grasp Tattoo", "price": "500 gp", "page": "TCE 123", "rarity": "Uncommon"}, {"name": "Eldritch Claw Tattoo", "price": "750 gp", "page": "TCE 126-127", "rarity": "Uncommon"}, {"name": "Barrier Tattoo (Rare)", "price": "1,500 gp", "page": "TCE 122", "rarity": "Rare"}, {"name": "Shadowfell Brand Tattoo", "price": "1,100 gp", "page": "TCE 134-135", "rarity": "Rare"}, {"name": "Absorbing Tattoo", "price": "8,000 gp", "page": "TCE 119", "rarity": "Very Rare"}, {"name": "Barrier Tattoo (Very Rare)", "price": "6,000 gp", "page": "TCE 122", "rarity": "Very Rare"}, {"name": "Ghost Step Tattoo", "price": "9,000 gp", "page": "TCE 128", "rarity": "Very Rare"}, {"name": "Lifewell Tattoo", "price": "5,100 gp", "page": "TCE 129", "rarity": "Very Rare"}, {"name": "Blood Fury Tattoo", "price": "32,000 gp*", "page": "TCE 122", "rarity": "Legendary"}]


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


def getTattoo(max_rarity="Common", min_rarity=""):
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
    sections = ["Spellwrought Tattoos", "Permanent Tattoo"]
    RaritiesList = ["Common", "Uncommon", "Rare", "Very Rare", "Legendary"]
    spellwroughtsSpellLevel = ["Cantrip", "1st Level", "2nd Level", "3rd Level"]
    spellwroughtsPrice = ["150gp", "250gp", "1000gp", "3000gp"]

    tattooShop = []

    spellwroughts = {"title": sections[0], "sections": []}
    for i in range(len(spellwroughtsSpellLevel)):
        spellwroughts["sections"].append({"title": f'{RaritiesList[i]} ({spellwroughtsSpellLevel[i]}) {spellwroughtsPrice[i]}', "bullets": [{"item": getScrolls(1, i, i)[0], "cost": None}]})
    tattooShop.append(spellwroughts)

    permanentTattoo = getTattoo(RaritiesList[0], RaritiesList[2])
    tattooShop.append({"title": sections[1], "sections": [{"title": permanentTattoo["rarity"], "bullets": [{"item": permanentTattoo["name"], "cost": permanentTattoo["price"]}]}]})

    return tattooShop


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


def nicePrint(table=[]):
    for market in table:
        print("## __" + market["title"] + "__")
        for section in market["sections"]:
            print("### " + section["title"])
            for bullet in section["bullets"]:
                if bullet["cost"] is not None:
                    print(f'''- {bullet["item"]} | **{bullet["cost"]}**''')
                else:
                    print(f'''- {bullet["item"]}''')


def main():
    TABLE_TITLES_DEFAULTS = ["Saoirse's Tattoo Journal"]
    NUM_TABLES_DEFAULT = 1
    IsCustomTables = True
    TextWrapping = True
    WRAP_WIDTH_DEFAULT = 29
    POSIX_DAY_IN_SECONDS = 60 * 60 * 24
    MARKET_CYCLE_START_POSIX = 0 * POSIX_DAY_IN_SECONDS  # Days offset from epoch
    POSTING_HOUR_DEFAULT = 0  # Hana Den posting time
    DAYS_IN_CYCLE_DEFAULT = 3  # Hana Den market cycle length
    DAYS_TO_ADD_DEFAULT = 3  # Number of days in the future for discord time code
    FILENAME_DEFAULT = 'Shop Sheet.txt'  # Must be UTF-8 text
    MANUAL_INPUT = getTattooItems()

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
        else:
            print("# " + TABLE_TITLES_DEFAULTS[0])

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
        nicePrint(unprocessedTableInput)

        print(closingPlayersTag)


main()
