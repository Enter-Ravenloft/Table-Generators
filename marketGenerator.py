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
firstLevel = ["Absorb Elements", "Alarm", "Animal Friendship", "Armor of Agathys", "Arms of Hadar", "Bane", "Beast Bond", "Bless", "Burning Hands", "Catapult", "Cause Fear", "Ceremony +25 gp", "Chaos Bolt", "Charm Person", "Chromatic Orb +50gp", "Color Spray", "Command", "Compelled Duel", "Comprehend Languages", "Create or Destroy Water", "Cure Wounds", "Detect Evil and Good", "Detect Magic", "Detect Poison and Disease", "Disguise Self", "Dissonant Whispers", "Divine Favor", "Earth Tremor", "Ensnaring Strike", "Entangle", "Expeditious Retreat", "Faerie Fire", "False Life", "Feather Fall", "Find Familiar +10gp", "Fog Cloud", "Goodberry", "Grease", "Guiding Bolt", "Hail of Thorns", "Healing Word", "Hellish Rebuke", "Heroism", "Hex", "Hunter's Mark", "Ice Knife", "Identify +100gp", "Illusory Script +10gp", "Inflict Wounds", "Jump", "Longstrider", "Mage Armor", "Magic Missile", "Protection from Evil and Good", "Purify Food and Drink", "Ray of Sickness", "Sanctuary", "Searing Smite", "Shield", "Shield of Faith", "Silent Image", "Sleep", "Snare", "Speak with Animals", "Tasha's Hideous Laughter", "Tenser's Floating Disk", "Thunderous Smite", "Thunderwave", "Unseen Servant", "Witch Bolt", "Wrathful Smite", "Zephyr Strike"]
secondLevel = ["Aganazzar's Scorcher", "Aid", "Alter Self", "Animal Messenger", "Arcane Lock +25gp", "Augury +25gp", "Barkskin", "Beast Sense", "Blindness/Deafness", "Blur", "Branding Smite", "Calm Emotions", "Cloud of Daggers", "Continual Flame +50gp", "Cordon of Arrows", "Crown of Madness", "Darkness", "Darkvision", "Detect Thoughts", "Dragon' Breath", "Dust Devil", "Earthbind", "Enhance Ability", "Enlarge/Reduce", "Enthrall", "Find Steed", "Find Traps", "Flame Blade", "Flaming Sphere", "Gentle Repose", "Gust of Wind", "Healing Spirit", "Heat Metal", "Hold Person", "Invisibility", "Knock", "Lesser Restoration", "Levitate", "Locate Animals or Plants", "Locate Object", "Magic Mouth +10gp", "Magic Weapon", "Maximilian's Earthen Grasp", "Melf's Acid Arrow", "Mind Spike", "Mirror Image", "Misty Step", "Moonbeam", "Nystul's Magic Aura", "Pass Without Trace", "Phantasmal Force", "Prayer of Healing", "Protection from Poison", "Pyrotechnics", "Ray of Enfeeblement", "Rope Trick", "Scorching Ray", "See invisibility", "Shadow Blade", "Shatter", "Silence", "Skywrite", "Snilloc's Snowball Swarm", "Spider Climb", "Spike Growth", "Spiritual Weapon", "Suggestion", "Warding Bond +100gp", "Warding Wind", "Web", "Zone of Truth"]
thirdLevel = ["Animate Dead", "Aura of Vitality", "Beacon of Hope", "Bestow Curse", "Blinding Smite", "Blink", "Call Lightning", "Catnap", "Clairvoyance +100gp", "Conjure Animals", "Conjure Barrage", "Counterspell", "Create Food and Water", "Crusader's Mantle", "Daylight", "Dispel Magic", "Elemental Weapon", "Enemies abound", "Erupting Earth", "Fear", "Feign Death", "Fireball", "Flame Arrows", "Fly", "Gaseous Form", "Glyph of Warding +200gp", "Haste", "Hunger of Hadar", "Hypnotic Pattern", "Leomund's Tiny Hut", "Life Transference", "Lightning Arrow", "Lightning Bolt", "Magic Circle +100gp", "Major Image", "Mass Healing Word", "Meld into Stone", "Melf's Minute Meteors", "Nondetection", "Phantom Steed", "Plant Growth", "Protection from Energy", "Remove Curse", "Revivify +300gp", "Sending", "Sleet Storm", "Slow", "Speak with Dead", "Speak with Plants", "Spirit Guardians", "Stinking Cloud", "Summon Lesser Demons", "Thunder Step", "Tidal Wave", "Tiny Servant", "Tongues", "Vampiric Touch", "Wall of Sand", "Wall of Water", "Water Breathing", "Water Walk", "Wind Wall"]
fourthLevel = ["Arcane Eye", "Aura of Life", "Aura of Purity", "Banishment", "Blight", "Charm Monster", "Compulsion", "Confusion", "Conjure Minor Elementals", "Conjure Woodland Beings", "Control Water", "Death Ward", "Dimension Door", "Divination", "Dominate Beast", "Elemental Bane", "Evard's Black Tentacles", "Fabricate", "Find Greater Steed", "Fire Shield", "Freedom of Movement", "Giant Insect", "Grasping Vine", "Greater Invisibility", "Guardian of Faith", "Guardian of Nature", "Hallucinatory Terrain", "Ice Storm", "Leomund's Secret Chest", "Locate Creature", "Mordenkainen's Faithful Hound", "Mordenkainen's Private Sanctum", "Otiluke's Resilient Sphere", "Phantasmal Killer", "Polymorph", "Shadow of Moil", "Sickening Radiance", "Staggering Smite", "Stone Shape", "Stoneskin", "Storm Sphere", "Summon Greater Demon", "Vitriolic Sphere", "Wall of Fire", "Watery Sphere"]
fifthLevel = ["Animate Objects", "Antilife Shell", "Awaken", "Banishing Smite", "Bigby's Hand", "Circle of Power", "Cloudkill", "Commune", "Commune with Nature", "Cone of Cold", "Conjure Elemental", "Conjure Volley", "Contact Other Plane", "Contagion", "Control Winds", "Creation", "Danse Macabre", "Dawn", "Destructive Wave", "Dispel Evil and Good", "Dominate Person", "Dream", "Enervation", "Far Step", "Flame Strike", "Geas", "Greater Restoration", "Hallow", "Hold Monster", "Holy Weapon", "Immolation", "Infernal Calling", "Insect Plague", "Legend Lore", "Maelstrom", "Mass Cure Wounds", "Mislead", "Modify Memory", "Negative Energy Flood", "Passwall", "Planar Binding", "Raise Dead", "Rary's Telepathic Bond", "Reincarnate", "Scrying", "Seeming", "Skill Empowerment", "Steel Wind Strike", "Swift Quiver", "Synaptic Static", "Telekinesis", "Teleportation Circle", "Transmute Rock", "Tree Stride", "Wall of Force", "Wall of Light", "Wall of Stone", "Wrath of Nature"]
sixthLevel = ["Arcane Gate", "Blade Barrier", "Bones of the Earth", "Chain Lightning", "Circle of Death", "Conjure Fey", "Contingency", "Create Homunculus", "Create Undead", "Disintegrate", "Drawmij's Instant Summons", "Druid Grove", "Eyebite", "Find the Path", "Flesh to Stone", "Forbiddance", "Globe of Invulnerability", "Guards and Wards", "Harm", "Heal", "Heroes' Feast", "Investiture of Flame", "Investiture of Ice", "Investiture of Stone", "Investiture of Wind", "Magic Jar", "Mass Suggestion", "Mental Prison", "Move Earth", "Otiluke's Freezing Sphere", "Otto's Irresistible Dance", "Planar Ally", "Primordial Ward", "Primordial Ward", "Programmed Illusion", "Scatter", "Soul Cage", "Sunbeam", "Tenser's Transformation", "Transport via Plants", "True Seeing", "Wall of Ice", "Wall of Thorns", "Wind Walk", "Word of Recall"]
seventhLevel = ["Conjure Celestial", "Crown of Stars", "Delayed Blast Fireball", "Divine Word", "Etherealness", "Finger of Death", "Fire Storm", "Forcecage", "Mirage Arcane", "Mordenkainen's Magnificent Mansion", "Mordenkainen's Sword", "Plane Shift", "Power Word Pain", "Prismatic Spray", "Project Image", "Regenerate", "Resurrection", "Reverse Gravity", "Sequester", "Simulacrum", "Symbol", "Teleport", "Temple of the Gods", "Whirlwind"]
eighthLevel = ["Abi-Dalzim's Horrid Wilting", "Animal Shapes", "Antimagic Field", "Antipathy/ Sympathy", "Clone", "Control Weather", "Demiplane", "Dominate Monster", "Earthquake", "Feeblemind", "Glibness", "Holy Aura", "Illusory Dragon", "Incendiary Cloud", "Maddening Darkness", "Maze", "Mighty Fortress", "Mind Blank", "Power Word Stun", "Sunburst", "Telepathy", "Trap the Soul", "Tsunami"]

AllSpells = [zerothLevel, firstLevel, secondLevel, thirdLevel, fourthLevel, fifthLevel, sixthLevel, seventhLevel, eighthLevel]
AllowedSpells = AllSpells[0:4]

SpellGems = [{"name": "Spell Gem (Cantrip)", "price": "150 gp", "page": "OA 223", "rarity": "Uncommon"}, {"name": "Spell Gem (1st Level)", "price": "350 gp", "page": "OA 223", "rarity": "Uncommon"}, {"name": "Spell Gem (2nd Level)", "price": "1,500 gp", "page": "OA 223", "rarity": "Rare"}, {"name": "Spell Gem (3rd Level)", "price": "4,000 gp", "page": "OA 223", "rarity": "Rare"}, {"name": "Spell Gem (4th Level)", "price": "8,000 gp", "page": "OA 223", "rarity": "Very Rare"}, {"name": "Spell Gem (5th Level)", "price": "15,000 gp", "page": "OA 223", "rarity": "Very Rare"}, {"name": "Spell Gem (6th Level)", "price": "20,000 gp", "page": "OA 223", "rarity": "Very Rare"}, {"name": "Spell Gem (7th Level)", "price": "35,000 gp", "page": "OA 223", "rarity": "Legendary"}, {"name": "Spell Gem (8th Level)", "price": "51,000 gp", "page": "OA 223", "rarity": "Legendary"}, {"name": "Spell Gem (9th Level)", "price": "78,000 gp", "page": "OA 223", "rarity": "Legendary"}]

Tattoos = [{"name": "Illuminator's Tattoo", "price": "65 gp", "page": "TCE 129", "rarity": "Common"}, {"name": "Masquerade Tattoo", "price": "75 gp", "page": "TCE 131", "rarity": "Common"}, {"name": "Barrier Tattoo (Uncommon)", "price": "200 gp", "page": "TCE 122", "rarity": "Uncommon"}, {"name": "Coiling Grasp Tattoo", "price": "500 gp", "page": "TCE 123", "rarity": "Uncommon"}, {"name": "Eldritch Claw Tattoo", "price": "750 gp", "page": "TCE 126-127", "rarity": "Uncommon"}, {"name": "Barrier Tattoo (Rare)", "price": "1,500 gp", "page": "TCE 122", "rarity": "Rare"}, {"name": "Shadowfell Brand Tattoo", "price": "1,100 gp", "page": "TCE 134-135", "rarity": "Rare"}, {"name": "Absorbing Tattoo", "price": "8,000 gp", "page": "TCE 119", "rarity": "Very Rare"}, {"name": "Barrier Tattoo (Very Rare)", "price": "6,000 gp", "page": "TCE 122", "rarity": "Very Rare"}, {"name": "Ghost Step Tattoo", "price": "9,000 gp", "page": "TCE 128", "rarity": "Very Rare"}, {"name": "Lifewell Tattoo", "price": "5,100 gp", "page": "TCE 129", "rarity": "Very Rare"}, {"name": "Blood Fury Tattoo", "price": "32,000 gp*", "page": "TCE 122", "rarity": "Legendary"}]

Items = [{"name": "Chronolometer","price": "12,500 gp","page":"AI 220","rarity":"Very Rare"},{"name": "Dimensional Loop","price": "6,000 gp","page":"AI 220-221","rarity":"Very Rare"},{"name": "Rotor of Return","price": "2,500 gp*","page":"AI 221","rarity":"Very Rare"},{"name": "Far Gear","price": "7,500 gp","page":"AI 221","rarity":"Very Rare"},{"name": "Timepiece of Travel","price": "8,000 gp","page":"AI 221-222","rarity":"Very Rare"},{"name": "Wheel of Stars","price": "6,500 gp","page":"AI 222","rarity":"Very Rare"},{"name": "Gauntlets of Flaming Fury","price": "2,000 gp","page":"BGDA 223","rarity":"Rare"},{"name": "Helm of Devil Command","price": "21,500 gp","page":"BGDA 223","rarity":"Very Rare"},{"name": "Hellfire Weapon (any weapon)","price": "500 gp","page":"BGDA 223","rarity":"Uncommon"},{"name": "Fane-Eater","price": "55,000 gp","page":"BGDA 223","rarity":"Legendary"},{"name": "Battle Standard of Infernal Power","price": "6,000 gp","page":"BGDA 223","rarity":"Very Rare"},{"name": "Obsidian Flint Dragon Plate","price": "27,000 gp*","page":"BGDA 224","rarity":"Legendary"},{"name": "Infernal Puzzle Box","price": "3,500 gp*","page":"BGDA 224","rarity":"Uncommon"},{"name": "Infernal Tack","price": "8,000 gp*","page":"BGDA 224","rarity":"Legendary"},{"name": "Soul Coin","price": "250 gp","page":"BGDA 225","rarity":"Uncommon"},{"name": "Shield of the Hidden Lord","price": "86,000 gp","page":"BGDA 225","rarity":"Legendary"},{"name": "Serpent Scale Armor","price": "3,500 gp","page":"Candlekeep Mysteries","rarity":"Uncommon"},{"name": "Icon of Ravenloft","price": "50,500 gp","page":"CS 222","rarity":"Legendary"},{"name": "Holy Symbol of Ravenkind","price": "51,000 gp","page":"CS 222","rarity":"Legendary"},{"name": "Adamantine Armor (medium or heavy, but not hide)","price": " +500 gp","page":"DMG 150","rarity":"Uncommon"},{"name": "Alchemy Jug","price": "100 gp","page":"DMG 150","rarity":"Uncommon"},{"name": "Amulet of Health","price": "4,000 gp","page":"DMG 150","rarity":"Rare"},{"name": "Amulet of Proof Against Detection and Location","price": "400 gp","page":"DMG 150","rarity":"Uncommon"},{"name": "Amulet of the Planes","price": "43,000 gp","page":"DMG 150","rarity":"Very Rare"},{"name": "Animated Shield","price": "6,000 gp","page":"DMG 151","rarity":"Very Rare"},{"name": "Apparatus of Kwalish","price": "90,000 gp","page":"DMG 151","rarity":"Legendary"},{"name": "Armor of Vulnerability (plate)","price": "1,500 gp","page":"DMG 152","rarity":"Rare"},{"name": "Armor of Resistance (light, medium, or heavy)","price": "3,000 gp","page":"DMG 152","rarity":"Rare"},{"name": "Armor (light, medium, or heavy), +1","price": "3,500 gp","page":"DMG 152","rarity":"Rare"},{"name": "Armor (light, medium, or heavy), +2","price": "20,000 gp","page":"DMG 152","rarity":"Very Rare"},{"name": "Armor (light, medium, or heavy), +3","price": "51,000 gp","page":"DMG 152","rarity":"Legendary"},{"name": "Armor of Invulnerability (plate)","price": "70,000 gp","page":"DMG 152","rarity":"Legendary"},{"name": "Bag of Beans","price": "4,200 gp","page":"DMG 152","rarity":"Rare"},{"name": "Arrow-Catching Shield","price": "4,500 gp","page":"DMG 152","rarity":"Rare"},{"name": "Bag of Devouring","price": "12,000 gp","page":"DMG 153","rarity":"Very Rare"},{"name": "Bag of Holding","price": "500 gp","page":"DMG 153-154","rarity":"Uncommon"},{"name": "Bead of Force","price": "3,000 gp","page":"DMG 154","rarity":"Rare"},{"name": "Bag of Tricks","price": "350 gp","page":"DMG 154","rarity":"Uncommon"},{"name": "Belt of Giant Strength (Storm)","price": "100,000 gp","page":"DMG 155","rarity":"Legendary"},{"name": "Belt of Giant Strength (Stone/Frost)","price": "12,000 gp","page":"DMG 155","rarity":"Very Rare"},{"name": "Berserker Axe (cursed)","price": "2,000 gp","page":"DMG 155","rarity":"Rare"},{"name": "Boots of Speed","price": "3,000 gp","page":"DMG 155","rarity":"Rare"},{"name": "Belt of Giant Strength (Fire)","price": "36,000 gp","page":"DMG 155","rarity":"Very Rare"},{"name": "Belt of Giant Strength (Hill)","price": "4,000 gp","page":"DMG 155","rarity":"Rare"},{"name": "Boots of Levitation","price": "4,500 gp","page":"DMG 155","rarity":"Rare"},{"name": "Boots of Elvenkind","price": "400 gp","page":"DMG 155","rarity":"Uncommon"},{"name": "Belt of Dwarvenkind","price": "5,000 gp","page":"DMG 155","rarity":"Rare"},{"name": "Belt of Giant Strength (Cloud)","price": "66,000 gp","page":"DMG 155","rarity":"Legendary"},{"name": "Boots of Striding and Springing","price": "200 gp","page":"DMG 156","rarity":"Uncommon"},{"name": "Boots of the Winterlands","price": "300 gp","page":"DMG 156","rarity":"Uncommon"},{"name": "Bracers of Archery","price": "350 gp","page":"DMG 156","rarity":"Uncommon"},{"name": "Brooch of Shielding","price": "375 gp","page":"DMG 156","rarity":"Uncommon"},{"name": "Bracers of Defense","price": "4,000 gp","page":"DMG 156","rarity":"Rare"},{"name": "Broom of Flying","price": "4,500 gp*","page":"DMG 156","rarity":"Uncommon"},{"name": "Bowl of Commanding Water Elementals","price": "4,700 gp","page":"DMG 156","rarity":"Rare"},{"name": "Brazier of Commanding Fire Elementals","price": "4,700 gp","page":"DMG 156","rarity":"Rare"},{"name": "Cape of the Mountebank","price": "3,900 gp","page":"DMG 157","rarity":"Rare"},{"name": "Carpet of Flying","price": "44,000 gp","page":"DMG 157","rarity":"Very Rare"},{"name": "Cap of Water Breathing","price": "450 gp","page":"DMG 157","rarity":"Uncommon"},{"name": "Candle of Invocation","price": "8,400 gp","page":"DMG 157","rarity":"Very Rare"},{"name": "Cloak of Arachnida","price": "14,000 gp","page":"DMG 158","rarity":"Very Rare"},{"name": "Cloak of Elvenkind","price": "250 gp","page":"DMG 158","rarity":"Uncommon"},{"name": "Chime of Opening","price": "3,000 gp","page":"DMG 158","rarity":"Rare"},{"name": "Cloak of Displacement","price": "3,600 gp","page":"DMG 158","rarity":"Rare"},{"name": "Circlet of Blasting","price": "350 gp","page":"DMG 158","rarity":"Uncommon"},{"name": "Censer of Controlling Air Elementals","price": "4,700 gp","page":"DMG 158","rarity":"Rare"},{"name": "Cloak of Invisibility","price": "54,000 gp","page":"DMG 158-159","rarity":"Legendary"},{"name": "Cloak of the Manta Ray","price": "350 gp","page":"DMG 159","rarity":"Uncommon"},{"name": "Cloak of the Bat","price": "4,600 gp","page":"DMG 159","rarity":"Rare"},{"name": "Cloak of Protection","price": "400 gp","page":"DMG 159","rarity":"Uncommon"},{"name": "Crystal Ball","price": "42,000 gp","page":"DMG 159","rarity":"Very Rare"},{"name": "Crystal Ball of Mind Reading","price": "51,000 gp","page":"DMG 159","rarity":"Legendary"},{"name": "Crystal Ball of Telepathy","price": "70,000 gp","page":"DMG 159","rarity":"Legendary"},{"name": "Crystal Ball of True Seeing","price": "80,000 gp","page":"DMG 159","rarity":"Legendary"},{"name": "Cube of Force","price": "5,000 gp","page":"DMG 159-160","rarity":"Rare"},{"name": "Cubic Gate","price": "164,000 gp","page":"DMG 160","rarity":"Legendary"},{"name": "Daern's Instant Fortress","price": "5,000 gp","page":"DMG 160-161","rarity":"Rare"},{"name": "Dagger of Venom","price": "1,500 gp","page":"DMG 161","rarity":"Rare"},{"name": "Dancing Sword (any sword)","price": "10,000 gp","page":"DMG 161","rarity":"Very Rare"},{"name": "Decanter of Endless Water","price": "300 gp","page":"DMG 161","rarity":"Uncommon"},{"name": "Deck of Illusions","price": "450 gp","page":"DMG 161-162","rarity":"Uncommon"},{"name": "Deck of Many Things","price": "200,000 gp","page":"DMG 162-164","rarity":"Legendary"},{"name": "Defender (any sword)","price": "55,000 gp","page":"DMG 164","rarity":"Legendary"},{"name": "Demon Armor (plate) (cursed)","price": "7500 gp","page":"DMG 165","rarity":"Very Rare"},{"name": "Dragon Scale Mail","price": "15000 gp","page":"DMG 165","rarity":"Very Rare"},{"name": "Dimensional Shackles","price": "2,800 gp","page":"DMG 165","rarity":"Rare"},{"name": "Driftglobe","price": "100 gp","page":"DMG 166","rarity":"Uncommon"},{"name": "Dust of Sneezing and Choking","price": "150 gp","page":"DMG 166","rarity":"Uncommon"},{"name": "Dust of Disappearance","price": "200 gp","page":"DMG 166","rarity":"Uncommon"},{"name": "Dust of Dryness","price": "350 gp","page":"DMG 166","rarity":"Uncommon"},{"name": "Dragon Slayer (any sword)","price": "4,800 gp","page":"DMG 166","rarity":"Rare"},{"name": "Dwarven Plate","price": "25,000 gp","page":"DMG 167","rarity":"Very Rare"},{"name": "Efreeti Chain (chain mail)","price": "80,000 gp","page":"DMG 167","rarity":"Legendary"},{"name": "Dwarven Thrower (warhammer)","price": "25,000 gp","page":"DMG 167","rarity":"Very Rare"},{"name": "Efreeti Bottle","price": "45,000 gp","page":"DMG 167","rarity":"Very Rare"},{"name": "Elven Chain (chain shirt)","price": "4500 gp","page":"DMG 168","rarity":"Rare"},{"name": "Eyes of Minute Seeing","price": "150 gp","page":"DMG 168","rarity":"Uncommon"},{"name": "Elemental Gem","price": "250 gp","page":"DMG 168","rarity":"Uncommon"},{"name": "Eversmoking Bottle","price": "270 gp","page":"DMG 168","rarity":"Uncommon"},{"name": "Eyes of Charming","price": "300 gp","page":"DMG 168","rarity":"Uncommon"},{"name": "Eyes of the Eagle","price": "400 gp","page":"DMG 168","rarity":"Uncommon"},{"name": "Figurine of Wondrous Power (Bronze Griffon)","price": "3,600 gp","page":"DMG 169","rarity":"Rare"},{"name": "Figurine of Wondrous Power (Ebony Fly)","price": "3,600 gp","page":"DMG 169","rarity":"Rare"},{"name": "Figurine of Wondrous Power (Golden Lions)","price": "5,000 gp","page":"DMG 169","rarity":"Rare"},{"name": "Figurine of Wondrous Power (Ivory Goats)","price": "5,000 gp","page":"DMG 169","rarity":"Rare"},{"name": "Figurine of Wondrous Power (Obsidian Steed)","price": "28,500 gp","page":"DMG 170","rarity":"Very Rare"},{"name": "Figurine of Wondrous Power (Serpentine Owl)","price": "3,000 gp","page":"DMG 170","rarity":"Rare"},{"name": "Figurine of Wondrous Power (Onyx Dog)","price": "3,200 gp","page":"DMG 170","rarity":"Rare"},{"name": "Figurine of Wondrous Power (Silver Raven)","price": "380 gp","page":"DMG 170","rarity":"Uncommon"},{"name": "Flame Tongue (any sword)","price": "5,000 gp","page":"DMG 170","rarity":"Rare"},{"name": "Figurine of Wondrous Power (Marble Elephant)","price": "5,000 gp","page":"DMG 170","rarity":"Rare"},{"name": "Folding Boat","price": "4,750 gp","page":"DMG 170-171","rarity":"Rare"},{"name": "Frost Brand (any sword)","price": "11,000 gp","page":"DMG 171","rarity":"Very Rare"},{"name": "Gem of Brightness","price": "250 gp","page":"DMG 171","rarity":"Uncommon"},{"name": "Gauntlets of Ogre Power","price": "450 gp","page":"DMG 171","rarity":"Uncommon"},{"name": "Glamoured Studded Leather","price": "4,800","page":"DMG 172","rarity":"Rare"},{"name": "Gloves of Swimming and Climbing","price": "250 gp","page":"DMG 172","rarity":"Uncommon"},{"name": "Goggles of Night","price": "300 gp","page":"DMG 172","rarity":"Uncommon"},{"name": "Gloves of Thievery","price": "300 gp","page":"DMG 172","rarity":"Uncommon"},{"name": "Gloves of Missile Snaring","price": "325 gp","page":"DMG 172","rarity":"Uncommon"},{"name": "Giant Slayer (any axe or sword)","price": "4,600 gp","page":"DMG 172","rarity":"Rare"},{"name": "Gem of Seeing","price": "5,000 gp","page":"DMG 172","rarity":"Rare"},{"name": "Helm of Comprehending Languages","price": "200 gp","page":"DMG 173","rarity":"Uncommon"},{"name": "Helm of Brilliance","price": "32,000 gp","page":"DMG 173","rarity":"Very Rare"},{"name": "Headband of Intellect","price": "450 gp","page":"DMG 173","rarity":"Uncommon"},{"name": "Hat of Disguise","price": "475 gp","page":"DMG 173","rarity":"Uncommon"},{"name": "Hammer of Thunderbolts (maul)","price": "51,000 gp","page":"DMG 173","rarity":"Legendary"},{"name": "Heward's Handy Haversack","price": "2,000 gp","page":"DMG 174","rarity":"Rare"},{"name": "Helm of Telepathy","price": "300 gp","page":"DMG 174","rarity":"Uncommon"},{"name": "Helm of Teleportation","price": "4,250 gp","page":"DMG 174","rarity":"Rare"},{"name": "Holy Avenger (any sword)","price": "65,000 gp","page":"DMG 174","rarity":"Legendary"},{"name": "Horn of Blasting","price": "2,500 gp","page":"DMG 174-175","rarity":"Rare"},{"name": "Horn of Valhalla (Bronze)","price": "20,000 gp","page":"DMG 175","rarity":"Very Rare"},{"name": "Horseshoes of Speed","price": "3,000 gp","page":"DMG 175","rarity":"Rare"},{"name": "Horn of Valhalla (Silver/Brass)","price": "5,000 gp","page":"DMG 175","rarity":"Rare"},{"name": "Horn of Valhalla (Iron)","price": "50,000 gp","page":"DMG 175","rarity":"Legendary"},{"name": "Immovable Rod","price": "500 gp","page":"DMG 175","rarity":"Uncommon"},{"name": "Horseshoes of a Zephyr","price": "6,000 gp","page":"DMG 175","rarity":"Very Rare"},{"name": "Instrument of the Bards (Anstruth Harp)","price": "17,500 gp","page":"DMG 176","rarity":"Very Rare"},{"name": "Instrument of the Bards (Doss Lute)","price": "250 gp","page":"DMG 176","rarity":"Uncommon"},{"name": "Instrument of the Bards (Canaith Mandolin)","price": "3,750 gp","page":"DMG 176","rarity":"Rare"},{"name": "Instrument of the Bards (Fochlucan Bandore)","price": "350 gp","page":"DMG 176","rarity":"Uncommon"},{"name": "Instrument of the Bards (Cli Lyre)","price": "4,250 gp","page":"DMG 176","rarity":"Rare"},{"name": "Instrument of the Bards (Mac-Fuimidh Cittern)","price": "450 gp","page":"DMG 176","rarity":"Uncommon"},{"name": "Instrument of the Bards (Ollamh Harp)","price": "51,000 gp","page":"DMG 176","rarity":"Legendary"},{"name": "Ioun Stone: Absorption","price": "20,000 gp","page":"DMG 176-177","rarity":"Very Rare"},{"name": "Ioun Stone: Sustenance","price": "3,000 gp","page":"DMG 176-177","rarity":"Rare"},{"name": "Ioun Stone: Protection","price": "3,600 gp","page":"DMG 176-177","rarity":"Rare"},{"name": "Ioun Stone: Awareness","price": "4,000 gp","page":"DMG 176-177","rarity":"Rare"},{"name": "Ioun Stone: Reserve","price": "4,500 gp","page":"DMG 176-177","rarity":"Rare"},{"name": "Ioun Stone: Regeneration","price": "55,000 gp","page":"DMG 176-177","rarity":"Legendary"},{"name": "Ioun Stone: Greater Absorption","price": "60,000 gp","page":"DMG 176-177","rarity":"Legendary"},{"name": "Ioun Stone: Mastery","price": "60,000 gp","page":"DMG 176-177","rarity":"Legendary"},{"name": "Ioun Stone: Agility","price": "8,000 gp","page":"DMG 176-177","rarity":"Very Rare"},{"name": "Ioun Stone: Fortitude","price": "8,000 gp","page":"DMG 176-177","rarity":"Very Rare"},{"name": "Ioun Stone: Insight","price": "8,000 gp","page":"DMG 176-177","rarity":"Very Rare"},{"name": "Ioun Stone: Intellect","price": "8,000 gp","page":"DMG 176-177","rarity":"Very Rare"},{"name": "Ioun Stone: Leadership","price": "8,000 gp","page":"DMG 176-177","rarity":"Very Rare"},{"name": "Ioun Stone: Strength","price": "8,000 gp","page":"DMG 176-177","rarity":"Very Rare"},{"name": "Iron Bands of Bilarro","price": "2,600 gp","page":"DMG 177","rarity":"Rare"},{"name": "Iron Flask","price": "170,000 gp","page":"DMG 178","rarity":"Legendary"},{"name": "Javelin of Lightning","price": "750 gp","page":"DMG 178","rarity":"Uncommon"},{"name": "Mace of Disruption","price": "1,750 gp","page":"DMG 179","rarity":"Rare"},{"name": "Keoghtom's Ointment","price": "1,250 gp (5 doses)","page":"DMG 179","rarity":"Uncommon"},{"name": "Mace of Smiting","price": "2,000 gp","page":"DMG 179","rarity":"Rare"},{"name": "Lantern of Revealing","price": "500 gp","page":"DMG 179","rarity":"Uncommon"},{"name": "Mace of Terror","price": "3,500 gp","page":"DMG 180","rarity":"Rare"},{"name": "Manual of Bodily Health","price": "36,000 gp","page":"DMG 180","rarity":"Very Rare"},{"name": "Manual of Gainful Exercise","price": "36,000 gp","page":"DMG 180","rarity":"Very Rare"},{"name": "Mantle of Spell Resistance","price": "4,200 gp","page":"DMG 180","rarity":"Rare"},{"name": "Manual of Golems","price": "22,000 gp","page":"DMG 180-181","rarity":"Very Rare"},{"name": "Mariner's Armor (light, medium, or heavy)","price": "+400","page":"DMG 181","rarity":"Uncommon"},{"name": "Medallion of Thoughts","price": "300 gp","page":"DMG 181","rarity":"Uncommon"},{"name": "Manual of Quickness of Action","price": "36,000 gp","page":"DMG 181","rarity":"Very Rare"},{"name": "Mirror of Life Trapping","price": "50,000 gp","page":"DMG 181-182","rarity":"Very Rare"},{"name": "Mithral Armor (medium or heavy, but not hide)","price": "+450","page":"DMG 182","rarity":"Uncommon"},{"name": "Necklace of Fireballs","price": "4,350 gp","page":"DMG 182","rarity":"Rare"},{"name": "Necklace of Adaptation","price": "450 gp","page":"DMG 182","rarity":"Uncommon"},{"name": "Necklace of Prayer Beads","price": "5,000 gp","page":"DMG 182","rarity":"Rare"},{"name": "Oathbow (longbow)","price": "13,000 gp","page":"DMG 183","rarity":"Very Rare"},{"name": "Nolzur's Marvelous Pigments","price": "16,000 gp","page":"DMG 183","rarity":"Very Rare"},{"name": "Nine Lives Stealer (any sword)","price": "36,000 gp","page":"DMG 183","rarity":"Very Rare"},{"name": "Periapt of Health","price": "250 gp","page":"DMG 184","rarity":"Uncommon"},{"name": "Periapt of Wound Closure","price": "375 gp","page":"DMG 184","rarity":"Uncommon"},{"name": "Periapt of Proof Against Poison","price": "4,700 gp","page":"DMG 184","rarity":"Rare"},{"name": "Pearl of Power","price": "400 gp","page":"DMG 184","rarity":"Uncommon"},{"name": "Plate Armor of Etherealness","price": "60,000","page":"DMG 185","rarity":"Legendary"},{"name": "Pipes of the Sewers","price": "150 gp","page":"DMG 185","rarity":"Uncommon"},{"name": "Pipes of Haunting","price": "300 gp","page":"DMG 185","rarity":"Uncommon"},{"name": "Portable Hole","price": "5,000 gp","page":"DMG 185-187","rarity":"Rare"},{"name": "Quaal's Feather Token (Anchor, Bird, Fan, Swan Boat, Tree or Whip)","price": "1,000 gp","page":"DMG 188-189","rarity":"Rare"},{"name": "Ring of Animal Influence","price": "1,000 gp","page":"DMG 189","rarity":"Rare"},{"name": "Quiver of Ehlonna","price": "250 gp","page":"DMG 189","rarity":"Uncommon"},{"name": "Ring of Djinni Summoning","price": "125,000 gp","page":"DMG 190","rarity":"Legendary"},{"name": "Ring of Elemental Command","price": "200,000 gp","page":"DMG 190","rarity":"Legendary"},{"name": "Ring of Feather Falling","price": "2,200 gp","page":"DMG 191","rarity":"Rare"},{"name": "Ring of Jumping","price": "250 gp","page":"DMG 191","rarity":"Uncommon"},{"name": "Ring of Protection","price": "3,000 gp","page":"DMG 191","rarity":"Rare"},{"name": "Ring of Free Action","price": "4,500 gp","page":"DMG 191","rarity":"Rare"},{"name": "Ring of Evasion","price": "4,900 gp","page":"DMG 191","rarity":"Rare"},{"name": "Ring of Regeneration","price": "40,000 gp","page":"DMG 191","rarity":"Very Rare"},{"name": "Ring of Mind Shielding","price": "450 gp","page":"DMG 191","rarity":"Uncommon"},{"name": "Ring of Invisibility","price": "75,000 gp","page":"DMG 191","rarity":"Legendary"},{"name": "Ring of Shooting Stars","price": "20,000 gp","page":"DMG 192","rarity":"Very Rare"},{"name": "Ring of Resistance","price": "3,500 gp","page":"DMG 192","rarity":"Rare"},{"name": "Ring of Spell Storing","price": "3,600 gp","page":"DMG 192","rarity":"Rare"},{"name": "Ring of Telekinesis","price": "25,000 gp","page":"DMG 193","rarity":"Very Rare"},{"name": "Ring of X-Ray Vision","price": "3,500 gp","page":"DMG 193","rarity":"Rare"},{"name": "Ring of Swimming","price": "300 gp","page":"DMG 193","rarity":"Uncommon"},{"name": "Ring of the Ram","price": "4,000 gp","page":"DMG 193","rarity":"Rare"},{"name": "Ring of Warmth","price": "480 gp","page":"DMG 193","rarity":"Uncommon"},{"name": "Ring of Water Walking","price": "500 gp","page":"DMG 193","rarity":"Uncommon"},{"name": "Ring of Spell Turning","price": "66,000 gp","page":"DMG 193","rarity":"Legendary"},{"name": "Ring of Three Wishes","price": "97,950 gp","page":"DMG 193","rarity":"Legendary"},{"name": "Robe of Eyes","price": "5,000 gp","page":"DMG 193-194","rarity":"Rare"},{"name": "Robe of Scintillating Colors","price": "27,000 gp","page":"DMG 194","rarity":"Very Rare"},{"name": "Robe of Stars","price": "45,000 gp","page":"DMG 194","rarity":"Very Rare"},{"name": "Robe of the Archmagi","price": "75,000 gp","page":"DMG 194","rarity":"Legendary"},{"name": "Robe of Useful Items","price": "400 gp","page":"DMG 195","rarity":"Uncommon"},{"name": "Rod of Absorption","price": "48,000 gp","page":"DMG 195","rarity":"Very Rare"},{"name": "Rod of Alertness","price": "11,000 gp","page":"DMG 196","rarity":"Very Rare"},{"name": "Rod of Lordly Might","price": "70,000 gp","page":"DMG 196","rarity":"Legendary"},{"name": "Rod of Resurrection","price": "125,000 gp","page":"DMG 197","rarity":"Legendary"},{"name": "Rod of the Pact Keeper (+3)","price": "14,000 gp","page":"DMG 197","rarity":"Very Rare"},{"name": "Rod of Rulership","price": "3,600 gp","page":"DMG 197","rarity":"Rare"},{"name": "Rope of Climbing","price": "350 gp","page":"DMG 197","rarity":"Uncommon"},{"name": "Rod of the Pact Keeper (+2)","price": "4,000 gp","page":"DMG 197","rarity":"Rare"},{"name": "Rod of the Pact Keeper (+1)","price": "400 gp","page":"DMG 197","rarity":"Uncommon"},{"name": "Rod of Security","price": "45,000 gp","page":"DMG 197","rarity":"Very Rare"},{"name": "Rope of Entanglement","price": "1,000 gp","page":"DMG 197-199","rarity":"Rare"},{"name": "Saddle of the Cavalier","price": "250 gp","page":"DMG 199","rarity":"Uncommon"},{"name": "Sentinel Shield","price": "300 gp","page":"DMG 199","rarity":"Uncommon"},{"name": "Sending Stones","price": "500 gp","page":"DMG 199","rarity":"Uncommon"},{"name": "Scarab of Protection","price": "58,000 gp","page":"DMG 199","rarity":"Legendary"},{"name": "Scimitar of Speed","price": "7,500 gp","page":"DMG 199","rarity":"Very Rare"},{"name": "Shield of Missile Attraction","price": "1,000 gp","page":"DMG 200","rarity":"Rare"},{"name": "Shield, +3","price": "22,000 gp","page":"DMG 200","rarity":"Very Rare"},{"name": "Shield, +2","price": "4,000 gp","page":"DMG 200","rarity":"Rare"},{"name": "Shield, +1","price": "450 gp","page":"DMG 200","rarity":"Uncommon"},{"name": "Sovereign Glue","price": "5,000 gp*","page":"DMG 200","rarity":"Legendary"},{"name": "Slippers of Spider Climbing","price": "500 gp","page":"DMG 200","rarity":"Uncommon"},{"name": "Staff of Fire","price": "18,000 gp","page":"DMG 201","rarity":"Very Rare"},{"name": "Sphere of Annihilation","price": "200,000 gp","page":"DMG 201","rarity":"Legendary"},{"name": "Staff of Charming","price": "3,750 gp","page":"DMG 201","rarity":"Rare"},{"name": "Spellguard Shield","price": "36,000 gp","page":"DMG 201","rarity":"Very Rare"},{"name": "Staff of Frost","price": "18,000 gp","page":"DMG 202","rarity":"Very Rare"},{"name": "Staff of Healing","price": "4,800 gp","page":"DMG 202","rarity":"Rare"},{"name": "Staff of Power","price": "46,000 gp","page":"DMG 202","rarity":"Very Rare"},{"name": "Staff of the Adder","price": "350 gp","page":"DMG 203","rarity":"Uncommon"},{"name": "Staff of Striking","price": "36,000 gp","page":"DMG 203","rarity":"Very Rare"},{"name": "Staff of Swarming Insects","price": "4,500 gp","page":"DMG 203","rarity":"Rare"},{"name": "Staff of the Magi","price": "98,000 gp","page":"DMG 203","rarity":"Legendary"},{"name": "Staff of the Python","price": "1000 gp","page":"DMG 204","rarity":"Uncommon"},{"name": "Staff of the Woodlands","price": "4,500 gp","page":"DMG 204","rarity":"Rare"},{"name": "Staff of Thunder and Lightning","price": "30,000 gp","page":"DMG 204-205","rarity":"Very Rare"},{"name": "Sun Blade (longsword)","price": "2,000 gp","page":"DMG 205","rarity":"Rare"},{"name": "Staff of Withering","price": "2,100 gp","page":"DMG 205","rarity":"Rare"},{"name": "Stone of Controlling Earth Elementals","price": "4,700 gp","page":"DMG 205","rarity":"Rare"},{"name": "Stone of Good Luck","price": "400 gp","page":"DMG 205","rarity":"Uncommon"},{"name": "Sword of Life Stealing (any sword)","price": "2,200 gp","page":"DMG 206","rarity":"Rare"},{"name": "Sword of Vengeance (any sword)","price": "400 gp","page":"DMG 206","rarity":"Uncommon"},{"name": "Sword of Sharpness (slashing swords)","price": "42,000 gp","page":"DMG 206","rarity":"Very Rare"},{"name": "Sword of Wounding (any sword)","price": "1,200 gp","page":"DMG 207","rarity":"Rare"},{"name": "Talisman of Pure Good","price": "125,000 gp","page":"DMG 207","rarity":"Legendary"},{"name": "Talisman of Ultimate Evil","price": "125,000 gp","page":"DMG 207","rarity":"Legendary"},{"name": "Talisman of the Sphere","price": "75,000 gp","page":"DMG 207","rarity":"Legendary"},{"name": "Tentacle Rod","price": "2,000 gp","page":"DMG 208","rarity":"Rare"},{"name": "Tome of Clear Thought","price": "36,000 gp","page":"DMG 208","rarity":"Very Rare"},{"name": "Tome of Leadership and Influence","price": "36,000 gp","page":"DMG 208","rarity":"Very Rare"},{"name": "Tome of the Stilled Tongue","price": "60,000 gp","page":"DMG 208","rarity":"Legendary"},{"name": "Wand of Binding","price": "2,500 gp","page":"DMG 209","rarity":"Rare"},{"name": "Trident of Fish Command","price": "300 gp","page":"DMG 209","rarity":"Uncommon"},{"name": "Tome of Understanding","price": "36,000 gp","page":"DMG 209","rarity":"Very Rare"},{"name": "Vicious Weapon (any weapon)","price": "4,000 gp","page":"DMG 209","rarity":"Rare"},{"name": "Universal Solvent","price": "5,000 gp*","page":"DMG 209","rarity":"Legendary"},{"name": "Wand of Fear","price": "3,250 gp","page":"DMG 210","rarity":"Rare"},{"name": "Wand of Enemy Detection","price": "3,750 gp","page":"DMG 210","rarity":"Rare"},{"name": "Wand of Fireballs","price": "4,800 gp","page":"DMG 210","rarity":"Rare"},{"name": "Wand of Secrets","price": "125 gp","page":"DMG 211","rarity":"Uncommon"},{"name": "Wand of Magic Detection","price": "150 gp","page":"DMG 211","rarity":"Uncommon"},{"name": "Wand of Polymorph","price": "21,000 gp","page":"DMG 211","rarity":"Very Rare"},{"name": "Wand of Magic Missiles","price": "300 gp","page":"DMG 211","rarity":"Uncommon"},{"name": "Wand of Paralysis","price": "4,250 gp","page":"DMG 211","rarity":"Rare"},{"name": "Wand of Lightning Bolts","price": "4,800 gp","page":"DMG 211","rarity":"Rare"},{"name": "Wand of the War Mage, +3","price": "14,000 gp","page":"DMG 212","rarity":"Very Rare"},{"name": "Wand of Wonder","price": "2,250 gp","page":"DMG 212","rarity":"Rare"},{"name": "Wand of Web","price": "250 gp","page":"DMG 212","rarity":"Uncommon"},{"name": "Wand of the War Mage, +2","price": "4,000 gp","page":"DMG 212","rarity":"Rare"},{"name": "Wand of the War Mage, +1","price": "400 gp","page":"DMG 212","rarity":"Uncommon"},{"name": "Weapon (any), +3","price": "15,000 gp","page":"DMG 213","rarity":"Very Rare"},{"name": "Wind Fan","price": "150 gp","page":"DMG 213","rarity":"Uncommon"},{"name": "Weapon (any), +2","price": "2,500 gp","page":"DMG 213","rarity":"Rare"},{"name": "Weapon of Warning","price": "400 gp","page":"DMG 213","rarity":"Uncommon"},{"name": "Weapon (any), +1","price": "500 gp","page":"DMG 213","rarity":"Uncommon"},{"name": "Well of Many Worlds","price": "90,000 gp","page":"DMG 213","rarity":"Legendary"},{"name": "Wings of Flying","price": "3,600 gp","page":"DMG 214","rarity":"Rare"},{"name": "Winged Boots","price": "5,000 gp*","page":"DMG 214","rarity":"Uncommon"},{"name": "Circlet of Human Perfection","price": "450 gp","page":"DotMM","rarity":"Uncommon"},{"name": "Amulet of the Drunkard","price": "500 gp","page":"EGW 265","rarity":"Uncommon"},{"name": "Arcane Cannon","price": "6,500 gp","page":"EGW 265","rarity":"Very Rare"},{"name": "Acheron Blade (any sword)","price": "900 gp","page":"EGW 265","rarity":"Rare"},{"name": "Corpse Slayer (any weapon)","price": "1,300 gp","page":"EGW 266","rarity":"Rare"},{"name": "Butcher's Bib","price": "2,750 gp","page":"EGW 266","rarity":"Rare"},{"name": "Brooch of Living Essence","price": "250 gp","page":"EGW 266","rarity":"Uncommon"},{"name": "Bloodaxe (greataxe)","price": "27,000 gp","page":"EGW 266","rarity":"Very Rare"},{"name": "Breathing Bubble","price": "50 gp","page":"EGW 266","rarity":"Common"},{"name": "Coin of Delving","price": "50 gp","page":"EGW 266","rarity":"Common"},{"name": "Dispelling Stone","price": "7,000 gp","page":"EGW 266","rarity":"Very Rare"},{"name": "Battering Shield","price": "850 gp","page":"EGW 266","rarity":"Rare"},{"name": "Duskcrusher (warhammer)","price": "8,500 gp","page":"EGW 266-267","rarity":"Very Rare"},{"name": "Dust of Deliciousness","price": "150 gp","page":"EGW 267","rarity":"Uncommon"},{"name": "Goggles of Object Reading","price": "350 gp","page":"EGW 267","rarity":"Uncommon"},{"name": "Hunter's Coat (leather)","price": "5,000 gp","page":"EGW 267","rarity":"Very Rare"},{"name": "Last Stand Armor (any armor)","price": "6,500 gp","page":"EGW 267","rarity":"Very Rare"},{"name": "Needle of Mending (dagger)","price": "1,400 gp","page":"EGW 268","rarity":"Rare"},{"name": "Reincarnation Dust","price": "3,500 gp","page":"EGW 268","rarity":"Very Rare"},{"name": "Orb of the Veil","price": "31,000 gp","page":"EGW 268","rarity":"Very Rare"},{"name": "Luxon Beacon","price": "35,000 gp*","page":"EGW 268","rarity":"Legendary"},{"name": "Nightfall Pearl","price": "51,000 gp","page":"EGW 268","rarity":"Legendary"},{"name": "Ring of Obscuring","price": "150 gp","page":"EGW 269","rarity":"Uncommon"},{"name": "Ring of Temporal Salvation","price": "2,250 gp","page":"EGW 269","rarity":"Rare"},{"name": "Rod of Retribution","price": "250 gp","page":"EGW 269","rarity":"Uncommon"},{"name": "Spell Bottle","price": "75,000 gp","page":"EGW 269","rarity":"Legendary"},{"name": "Staff of the Ivory Claw","price": "1,000 gp","page":"EGW 270","rarity":"Rare"},{"name": "Weapon of Certain Death (any weapon)","price": "1,500 gp","page":"EGW 270","rarity":"Rare"},{"name": "Vox Seeker","price": "100 gp","page":"EGW 270","rarity":"Common"},{"name": "Staff of Dunamancy","price": "27,000 gp","page":"EGW 270","rarity":"Very Rare"},{"name": "Mark of the Order, +3","price": "14,500 gp","page":"Enter Ravenloft","rarity":"Very Rare"},{"name": "Shield Arbalest","price": "250gp","page":"Enter Ravenloft","rarity":"Uncommon"},{"name": "Mark of the Order, +2","price": "4,250 gp","page":"Enter Ravenloft","rarity":"Rare"},{"name": "Mark of the Order, +1","price": "425 gp","page":"Enter Ravenloft","rarity":"Uncommon"},{"name": "Boomerang Bandolier","price": "500 gp","page":"Enter Ravenloft","rarity":"Uncommon"},{"name": "Armblade (any one-handed melee weapon)","price": "100 gp","page":"ERLW 276","rarity":"Common"},{"name": "Dyrrn's Tentacle Whip","price": "17,000 gp","page":"ERLW 276","rarity":"Very Rare"},{"name": "Docent","price": "4,500 gp","page":"ERLW 276","rarity":"Rare"},{"name": "Arcane Propulsion Arm","price": "5,100 gp","page":"ERLW 276","rarity":"Very Rare"},{"name": "Arcane Propulsion Arm","price": "5,100 gp","page":"ERLW 276","rarity":"Very Rare"},{"name": "Cleansing Stone","price": "50 gp","page":"ERLW 276","rarity":"Common"},{"name": "Belashyrra's Beholder Crown","price": "51,000 gp","page":"ERLW 276","rarity":"Legendary"},{"name": "Everbright Lantern","price": "100 gp","page":"ERLW 277","rarity":"Common"},{"name": "Glamerweave (uncommon)","price": "150 gp","page":"ERLW 277","rarity":"Uncommon"},{"name": "Earworm","price": "225 gp","page":"ERLW 277","rarity":"Uncommon"},{"name": "Feather Token (Feather Fall)","price": "25 gp","page":"ERLW 277","rarity":"Common"},{"name": "Glamerweave (common)","price": "50 gp","page":"ERLW 277","rarity":"Common"},{"name": "Keycharm","price": "50 gp","page":"ERLW 277","rarity":"Common"},{"name": "Finder's Goggles","price": "500 gp","page":"ERLW 277","rarity":"Uncommon"},{"name": "Imbued Wood Focus","price": "75 gp","page":"ERLW 277","rarity":"Common"},{"name": "Kyrzin's Ooze","price": "21,000 gp","page":"ERLW 278","rarity":"Very Rare"},{"name": "Living Gloves","price": "500 gp","page":"ERLW 278","rarity":"Uncommon"},{"name": "Orb of Shielding","price": "80 gp","page":"ERLW 278","rarity":"Common"},{"name": "Living Armor","price": "9,500 gp","page":"ERLW 278","rarity":"Very Rare"},{"name": "Scribe's Pen","price": "60 gp","page":"ERLW 278-279","rarity":"Common"},{"name": "Prosthetic Limb","price": "100 gp","page":"ERLW 278; EGW 268","rarity":"Common"},{"name": "Prosthetic Limb","price": "100 gp","page":"ERLW 278; EGW 268","rarity":"Common"},{"name": "Prosthetic Limb","price": "100 gp","page":"ERLW 278; TCE 134","rarity":"Common"},{"name": "Ventilating Lungs","price": "1,000 gp","page":"ERLW 279","rarity":"Rare"},{"name": "Shiftweave","price": "100 gp","page":"ERLW 279","rarity":"Common"},{"name": "Spellshard","price": "100 gp","page":"ERLW 279","rarity":"Common"},{"name": "Speaking Stone","price": "5,000 gp","page":"ERLW 279","rarity":"Very Rare"},{"name": "Wand Sheath","price": "75 gp","page":"ERLW 279","rarity":"Common"},{"name": "Wheel of Wind and Water","price": "350 gp","page":"ERLW 280","rarity":"Uncommon"},{"name": "Dragon Wing Bow","price": "1,500 gp","page":"FTD","rarity":"Rare"},{"name": "Wakened Dragon Vessel","price": "11,000 gp","page":"FTD","rarity":"Very Rare"},{"name": "Emerald Pen 150gp","price": "150 gp","page":"FTD","rarity":"Common"},{"name": "Amethyst Lodestone","price": "17,500 gp","page":"FTD","rarity":"Very Rare"},{"name": "Dragonhide Belt +2","price": "2,250 gp","page":"FTD","rarity":"Rare"},{"name": "Stirring Dragon's Wrath Weapon +1","price": "2,500 gp","page":"FTD","rarity":"Rare"},{"name": "Stirring Dragon-Touched Focus","price": "2,500 gp","page":"FTD","rarity":"Rare"},{"name": "Slumbering Dragon Vessel","price": "2,750 gp","page":"FTD","rarity":"Uncommon"},{"name": "Crystal Blade","price": "3,000 gp","page":"FTD","rarity":"Rare"},{"name": "Stirring Scaled Ornament","price": "3,000 gp","page":"FTD","rarity":"Rare"},{"name": "Dragonhide Belt +3","price": "4,500 gp","page":"FTD","rarity":"Very Rare"},{"name": "Dragonhide Belt +1","price": "400 gp","page":"FTD","rarity":"Uncommon"},{"name": "Slumbering Dragon's Wrath Weapon","price": "400 gp","page":"FTD","rarity":"Uncommon"},{"name": "Slumbering Dragon-Touched Focus","price": "400 gp","page":"FTD","rarity":"Uncommon"},{"name": "Slumbering Scaled Ornament","price": "400 gp","page":"FTD","rarity":"Uncommon"},{"name": "Wakened Dragon's Wrath Weapon +2","price": "5,000 gp","page":"FTD","rarity":"Very Rare"},{"name": "Wakened Dragon-Touched Focus","price": "5,000 gp","page":"FTD","rarity":"Very Rare"},{"name": "Stirring Dragon Vessel","price": "5,500 gp","page":"FTD","rarity":"Rare"},{"name": "Dracofist","price": "5000gp","page":"FTD","rarity":"Rare"},{"name": "Sapphire Buckler","price": "6,000 gp","page":"FTD","rarity":"Very Rare"},{"name": "Wakened Scaled Ornament","price": "6,000 gp","page":"FTD","rarity":"Very Rare"},{"name": "Gem Dracofist","price": "TBC","page":"FTD","rarity":"Very Rare"},{"name": "Gruul Keyrune","price": "2,800 gp","page":"GGR 177","rarity":"Rare"},{"name": "Orzhov Keyrune","price": "1,100 gp","page":"GGR 178","rarity":"Rare"},{"name": "Illusionist's Bracers","price": "13,500 gp","page":"GGR 178","rarity":"Yes (spellcaster) Very Rare"},{"name": "Mizzium Mortar","price": "2,100 gp","page":"GGR 179","rarity":"Rare"},{"name": "Pariah's Shield","price": "1,500 gp","page":"GGR 180","rarity":"Rare"},{"name": "Pyroconverger","price": "250 gp","page":"GGR 180","rarity":"Uncommon"},{"name": "Moodmark Paint","price": "50 gp","page":"GGR 180","rarity":"Common"},{"name": "Peregrine Mask","price": "6,000 gp","page":"GGR 180","rarity":"Very Rare"},{"name": "Voyager Staff","price": "10,500 gp","page":"GGR 181","rarity":"Very Rare"},{"name": "Sword of the Paruns (longsword)","price": "16,000 gp","page":"GGR 181","rarity":"Very Rare"},{"name": "Skyblinder Staff","price": "375 gp","page":"GGR 181","rarity":"Uncommon"},{"name": "Sunforger (warhammer)","price": "4,600 gp","page":"GGR 181","rarity":"Rare"},{"name": "Spies' Murmur","price": "475 gp","page":"GGR 181","rarity":"Uncommon"},{"name": "Mirrorlight Stinger","price": "1,500 gp","page":"Griffon's Saddlebag","rarity":"Rare"},{"name": "Dagger of the Ogre Mage","price": "3,500 gp","page":"Griffon's Saddlebag","rarity":"Rare"},{"name": "Camper's Respite","price": "200 gp","page":"Griffon's Saddlebag","rarity":"Uncommon"},{"name": "Death Knell Glaive","price": "3,000 gp","page":"Griffon's Saddlebag","rarity":"Rare"},{"name": "Rope Caster","price": "400 gp","page":"Griffon's Saddlebag","rarity":"Uncommon"},{"name": "Gelatinous Whip","price": "400 gp","page":"Griffon's Saddlebag","rarity":"Uncommon"},{"name": "Cleaning Cube","price": "50 gp","page":"Griffon's Saddlebag","rarity":"Common"},{"name": "Companion's Band","price": "50 gp","page":"Griffon's Saddlebag","rarity":"Common"},{"name": "Foxfire Charm","price": "50 gp","page":"Griffon's Saddlebag","rarity":"Common"},{"name": "Ambitious Medic's Box","price": "500 gp","page":"Griffon's Saddlebag","rarity":"Uncommon"},{"name": "Charm of Plant Command","price": "1,500 gp","page":"GS 229","rarity":"Rare"},{"name": "Pressure Capsule","price": "25 gp","page":"GS 229","rarity":"Common"},{"name": "Cursed Luckstone","price": "250 gp","page":"GS 229","rarity":"Uncommon"},{"name": "Pipe of Remembrance","price": "50 gp","page":"GS 229","rarity":"Common"},{"name": "Sekolahian Worshipping Statuette","price": "50 gp","page":"GS 229","rarity":"Common"},{"name": "Helm of Underwater Action","price": "500 gp","page":"GS 229","rarity":"Uncommon"},{"name": "Wand of Winter","price": "4,100 gp","page":"HDQ 94","rarity":"Rare"},{"name": "Insignia of Claws","price": "450 gp","page":"HDQ 94","rarity":"Uncommon"},{"name": "Hazirawn (greatsword)","price": "66,000 gp","page":"HDQ 94","rarity":"Legendary"},{"name": "Black Dragon Mask","price": "95,000 gp","page":"HDQ 94","rarity":"Legendary"},{"name": "Abracadadabrus","price": "2,500 gp*","page":"IDRF 314","rarity":"Very Rare"},{"name": "Cauldron of Plenty","price": "3,500 gp","page":"IDRF 314","rarity":"Rare"},{"name": "Hook of Fisher's Delight","price": "550 gp","page":"IDRF 314","rarity":"Rare"},{"name": "Lantern of Tracking","price": "75 gp","page":"IDRF 314-315","rarity":"Common"},{"name": "Professor Orb","price": "4,000 gp","page":"IDRF 315","rarity":"Rare"},{"name": "Psi Crystal","price": "500 gp","page":"IDRF 315","rarity":"Uncommon"},{"name": "Ythryn Mythallar","price": "200,000 gp","page":"IDRF 316","rarity":"Legendary"},{"name": "Thermal Cube","price": "50 gp","page":"IDRF 316","rarity":"Common"},{"name": "Spider Staff","price": "1,750 gp","page":"LMP 53","rarity":"Rare"},{"name": "Staff of Defense","price": "3,400 gp","page":"LMP 53","rarity":"Rare"},{"name": "Molten Bronze Skin (breastplate, half plate, or plate)","price": "+1300","page":"MOT 196","rarity":"Rare"},{"name": "Helm of the Gods","price": "1,200 gp","page":"MOT 196","rarity":"Rare"},{"name": "Flying Chariot","price": "4,750 gp","page":"MOT 196","rarity":"Rare"},{"name": "Pyxis of Pandemonium","price": "25,000 gp*","page":"MOT 197","rarity":"Legendary"},{"name": "Two-Birds Sling","price": "4,000 gp","page":"MOT 198","rarity":"Rare"},{"name": "Siren Song Lyre","price": "650 gp","page":"MOT 198","rarity":"Rare"},{"name": "Piwafwi of Fire Resistance","price": "1,400 gp","page":"OA 222","rarity":"Rare"},{"name": "Piwafwi (Cloak of Elvenkind)","price": "200 gp","page":"OA 222","rarity":"Uncommon"},{"name": "Dawnbringer (longsword)","price": "57,000 gp","page":"OA 222","rarity":"Legendary"},{"name": "Stonespeaker Crystal","price": "4,600 gp","page":"OA 223","rarity":"Rare"},{"name": "Wand of Viscid Globs","price": "900 gp","page":"OA 223","rarity":"Rare"},{"name": "Devastation Orb (Earth)","price": "11,000 gp","page":"PA 222","rarity":"Very Rare"},{"name": "Balloon Pack","price": "275 gp","page":"PA 222","rarity":"Uncommon"},{"name": "Claws of the Umber Hulk","price": "4,300 gp","page":"PA 222","rarity":"Rare"},{"name": "Devastation Orb (Air)","price": "8,000 gp","page":"PA 222","rarity":"Very Rare"},{"name": "Devastation Orb (Fire)","price": "9,500 gp","page":"PA 222","rarity":"Very Rare"},{"name": "Seeker Dart","price": "100 gp","page":"PA 223","rarity":"Uncommon"},{"name": "Storm Boomerang","price": "150 gp","page":"PA 223","rarity":"Uncommon"},{"name": "Weird Tank","price": "2,200 gp","page":"PA 223","rarity":"Rare"},{"name": "Wingwear","price": "300 gp","page":"PA 223","rarity":"Uncommon"},{"name": "Devastation Orb (Water)","price": "9,500 gp","page":"PA 223","rarity":"Very Rare"},{"name": "Lost Crown of Besilmer","price": "23,000 gp","page":"PA 223-224","rarity":"Legendary"},{"name": "Drown (trident)","price": "66,000 gp","page":"PA 224","rarity":"Legendary"},{"name": "Dragontooth Dagger","price": "5,000 gp","page":"RT 93","rarity":"Rare"},{"name": "Banner of the Krig Rune","price": "4,400 gp","page":"SKT 233","rarity":"Rare"},{"name": "Claw of the Wyrm Rune","price": "4,400 gp","page":"SKT 233","rarity":"Rare"},{"name": "Blod Stone","price": "6,500 gp","page":"SKT 233","rarity":"Rare"},{"name": "Conch of Teleportation","price": "1,850 gp*","page":"SKT 234","rarity":"Very Rare"},{"name": "Ingot of the Skold Rune","price": "15,000 gp","page":"SKT 234","rarity":"Very Rare"},{"name": "Skold Rune Shield","price": "2,600 gp","page":"SKT 234","rarity":"Rare"},{"name": "Gavel of the Venn Rune","price": "2,800 gp","page":"SKT 234","rarity":"Rare"},{"name": "Skold Rune Weapon (ant two-handed weapon)","price": "500 gp","page":"SKT 234","rarity":"Uncommon"},{"name": "Gurt's Greataxe","price": "67,000 gp","page":"SKT 234","rarity":"Legendary"},{"name": "Orb of the Stein Rune","price": "2,700 gp","page":"SKT 235","rarity":"Rare"},{"name": "Navigation Orb","price": "27,000 gp","page":"SKT 235","rarity":"Very Rare"},{"name": "Ild Rune Armor (light, medium, or heavy)","price": "3,000 gp","page":"SKT 235","rarity":"Rare"},{"name": "Opal of the Ild Rune","price": "3,500 gp","page":"SKT 235","rarity":"Rare"},{"name": "Stein Rune Boots","price": "350 gp","page":"SKT 235","rarity":"Uncommon"},{"name": "Stein Rune Shield","price": "4,600 gp","page":"SKT 235","rarity":"Rare"},{"name": "Ild Rune Weapon (any weapon)","price": "400 gp","page":"SKT 235","rarity":"Uncommon"},{"name": "Pennant of the Vind Rune","price": "13,000 gp","page":"SKT 235-236","rarity":"Very Rare"},{"name": "Rod of the Vonindod","price": "3,400 gp","page":"SKT 236","rarity":"Rare"},{"name": "Vind Rune Armor (light, medium, or heavy)","price": "300 gp","page":"SKT 236","rarity":"Uncommon"},{"name": "Robe of Serpents","price": "375 gp","page":"SKT 236","rarity":"Uncommon"},{"name": "Vind Rune Cloak","price": "650 gp","page":"SKT 236","rarity":"Rare"},{"name": "Vind Rune Boots","price": "650 gp","page":"SKT 236","rarity":"Rare"},{"name": "Shard of the Ise Rune","price": "9,000 gp","page":"SKT 236","rarity":"Very Rare"},{"name": "Ise Rune Cloak","price": "1,200 gp","page":"SKT 237","rarity":"Rare"},{"name": "Ise Rune Boots","price": "2,650 gp","page":"SKT 237","rarity":"Rare"},{"name": "Ghost Lantern","price": "1,750 gp","page":"TA 206","rarity":"Rare"},{"name": "Bookmark (dagger)","price": "30,000 gp*","page":"TA 206","rarity":"Legendary"},{"name": "Amulet of the Black Skull","price": "6,400 gp","page":"TA 206","rarity":"Very Rare"},{"name": "Mask of the Beast","price": "200 gp","page":"TA 207","rarity":"Uncommon"},{"name": "Scorpion Armor (plate)","price": "2,100 gp","page":"TA 208","rarity":"Rare"},{"name": "All-Purpose Tool, +1","price": "1,500 gp*","page":"TCE 119","rarity":"Uncommon"},{"name": "Amulet of the Devout, +3","price": "14,500 gp","page":"TCE 119","rarity":"Very Rare"},{"name": "All-Purpose Tool, +3","price": "16,000 gp","page":"TCE 119","rarity":"Very Rare"},{"name": "Alchemical Compendium","price": "3,000 gp","page":"TCE 119","rarity":"Rare"},{"name": "Amulet of the Devout, +2","price": "4,250 gp","page":"TCE 119","rarity":"Rare"},{"name": "All-Purpose Tool, +2","price": "4,500 gp","page":"TCE 119","rarity":"Rare"},{"name": "Amulet of the Devout, +1","price": "425 gp","page":"TCE 119","rarity":"Uncommon"},{"name": "Arcane Grimoire, +3","price": "14,500 gp","page":"TCE 120","rarity":"Very Rare"},{"name": "Astromancy Archive","price": "3,300 gp","page":"TCE 120","rarity":"Rare"},{"name": "Atlas of Endless Horizons","price": "3,750 gp","page":"TCE 120","rarity":"Rare"},{"name": "Astral Shard","price": "4,200 gp","page":"TCE 120","rarity":"Rare"},{"name": "Arcane Grimoire, +2","price": "4,250 gp","page":"TCE 120","rarity":"Rare"},{"name": "Arcane Grimoire, +1","price": "425 gp","page":"TCE 120","rarity":"Uncommon"},{"name": "Bloodwell Vial, +3","price": "14,500 gp","page":"TCE 122","rarity":"Very Rare"},{"name": "Bloodwell Vial, +2","price": "4,250 gp","page":"TCE 122","rarity":"Rare"},{"name": "Bloodwell Vial, +1","price": "425 gp","page":"TCE 122","rarity":"Uncommon"},{"name": "Bell Branch","price": "750 gp","page":"TCE 122","rarity":"Rare"},{"name": "Cauldron of Rebirth","price": "10,000 gp","page":"TCE 122-123","rarity":"Very Rare"},{"name": "Crystalline Chronicle","price": "6,500 gp","page":"TCE 124-125","rarity":"Very Rare"}]
Cloth = [{'name': 'Infernal Leather', 'price': '750 gp', 'page': 'Special Materials', 'rarity': 'Uncommon', 'type': 'Cloth'}, {'name': 'Shadowfell Linen', 'price': '750 gp', 'page': 'Special Materials', 'rarity': 'Uncommon', 'type': 'Cloth'}]
Organic = [{'name': 'Asmorch Wood', 'price': '500 gp', 'page': 'Special Materials', 'rarity': 'Uncommon', 'type': 'Organic'}, {'name': 'Coral', 'price': '100 gp', 'page': 'Special Materials', 'rarity': 'Uncommon', 'type': 'Organic'}, {'name': 'Plague wood', 'price': '250 gp', 'page': 'Special Materials', 'rarity': 'Uncommon', 'type': 'Organic'}, {'name': 'Spiritual Wood', 'price': '800 gp', 'page': 'Special Materials', 'rarity': 'Uncommon', 'type': 'Organic'}]
Metal = [{'name': 'Cold Iron', 'price': '100 gp', 'page': 'Special Materials', 'rarity': 'Uncommon', 'type': 'Metal'}, {'name': 'Adamantine', 'price': '300 gp', 'page': 'Special Materials', 'rarity': 'Uncommon', 'type': 'Metal'}, {'name': 'Darksteel', 'price': '600 gp', 'page': 'Special Materials', 'rarity': 'Uncommon', 'type': 'Metal'}, {'name': 'Flametouched Iron', 'price': '500 gp', 'page': 'Special Materials', 'rarity': 'Uncommon', 'type': 'Metal'}, {'name': 'Orichalcum', 'price': '650 gp', 'page': 'Special Materials', 'rarity': 'Uncommon', 'type': 'Metal'}, {'name': 'Infernal Steel', 'price': '750 gp', 'page': 'Special Materials', 'rarity': 'Uncommon', 'type': 'Metal'}, {'name': 'Osmodium', 'price': '760 gp', 'page': 'Special Materials', 'rarity': 'Uncommon', 'type': 'Metal'}, {'name': 'Stellar Iron', 'price': '850 gp', 'page': 'Special Materials', 'rarity': 'Uncommon', 'type': 'Metal'}]
Mineral = [{'name': 'Aerocrystal', 'price': '750 gp', 'page': 'Special Materials', 'rarity': 'Uncommon', 'type': 'Mineral'}, {'name': 'Dwarvenstone', 'price': '300 gp', 'page': 'Special Materials', 'rarity': 'Uncommon', 'type': 'Mineral'}, {'name': 'Eternal Ice', 'price': '600 gp', 'page': 'Special Materials', 'rarity': 'Uncommon', 'type': 'Mineral'}, {'name': 'Ignium', 'price': '100 gp', 'page': 'Special Materials', 'rarity': 'Uncommon', 'type': 'Mineral'}, {'name': 'Obsidian', 'price': '500 gp', 'page': 'Special Materials', 'rarity': 'Uncommon', 'type': 'Mineral'}]

SpecialMaterials = [Cloth, Organic, Metal, Mineral]

MasterList = [Potions, AllSpells, SpellGems, Items, SpecialMaterials]


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
        for j in range(maxItemsPerSubcategory - i):
            newItem = getItems(marketList[0], 1, raritiesList[i])
            itemList.append(newItem[0])
            itemList.append(newItem[1])
        if i < (len(raritiesList) - 1):
            itemList.append(sectionMarker)
            itemList.append(sectionMarker)
    itemList.append(endTableMarker)

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

        if i < ((len(spellLevelAndCost) // 2) - 1):
            itemList.append(sectionMarker)
            itemList.append(sectionMarker)

    itemList.append(endTableMarker)

    for i in range(len(materialTypes) // 2):
        firstType = i * 2
        secondType = firstType + 1

        itemList.append(materialTypes[firstType])
        itemList.append(materialTypes[secondType])

        firstMaterial = getMaterials(materialTypes[firstType])
        secondMaterial = getMaterials(materialTypes[secondType])

        # append names
        itemList.append(firstMaterial[0])
        itemList.append(secondMaterial[0])

        # append same line so price and name are in same box
        itemList.append("SAMELINE")
        itemList.append("SAMELINE")

        # append prices
        itemList.append(firstMaterial[1])
        itemList.append(secondMaterial[1])

        if i < ((len(materialTypes) // 2) - 1):
            itemList.append(sectionMarker)
            itemList.append(sectionMarker)

    return itemList

MANUAL_INPUT = getVistaniItems()


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

            if previousPrintableRow == -1 or self.RowInfo[previousPrintableRow][self.SECTION_MARKER]:
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
    TABLE_TITLES_DEFAULTS = ["Magic Items", "Spell Scrolls", "Special Materials"]
    NUM_TABLES_DEFAULT = 3
    DELIMITER_STRING = 'ENDTABLE'
    IsCustomTables = True
    TextWrapping = True
    WRAP_WIDTH_DEFAULT = 29
    MARKET_CYCLE_START_POSIX = 1654387200  # June 5th at 12am UTC aka ISO 2022-06-05 00:00:00 UTC
    POSTING_HOUR_DEFAULT = 23  # Vistani Market posting time
    DAYS_IN_CYCLE_DEFAULT = 3  # Vistani Market market cycle length
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

        closingPlayersTag = "@Players the market closes <t:"
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
            print("__**Vistani Market**__\n")

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
            print("**%s**" % tableTitles[i])
            marketTable = Table(unprocessedTableInput, TextWrapping, desiredWidth)
            marketTable.printUnicodeTable()

        print(closingPlayersTag)


main()
