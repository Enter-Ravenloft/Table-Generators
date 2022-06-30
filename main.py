'''                                                               UPLOAD BUTTON ↗
READ ME, please :)

The following instructions require that you have
saved a formatted sheet as a .csv file and renamed
it to a file named "Shop Sheet.txt"

Instructions: 
1. You will need to return back to this tab "main.py" after the next step.
    If you look straight up from the start of this line, you will see it.
2. Click on the 📤 button in the top right corner of the left pane to upload the 
    .txt file 
3. Select the text file.
4. Click the ⊘ button in the top right corner of the right pane.
5. Click the ▶ button in the top bar.
6. Respond to the prompt with "y"
  

If you have difficulties with this, ping Quincy on discord
or ask in #Helpers
''' 


from marketTables import *

# BEGINING TESTING
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
# END TESTING


## main()
print("\nClick 'Run' to make another set of tables")

#  You can ignore the line below unless troubleshooting
#  Built from commit d71dee8f2d0112524bdcfc0d042f3e83ae5dcaaa
