class Table:
    def __init__(self, valuesList=[]):
        self.Cell = []
        self.RowInfo = []
        self.widestLeftColumn = 0
        self.widestRightColumn = 0
        self.widestRow = 0
        self.widthAllowance = 30  # Orignally 28 -7 based on feedback from cellphone users.
        self.WrapsForRow = []
        self.DoesWrap = False
        self.numRowsWrapped = 0
        self.MERGE_MARKER = "MERGE"
        self.SECTION_MARKER = "ENDSECTION"
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
                                       "double ":
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
                                       "double ":
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
        self.widthAllowance = 28 - 7
        self.WrapsForRow = []
        self.DoesWrap = False
        self.numRowsWrapped = 0

    def clearRowInfo(self):
        self.RowInfo = []

    def build(self, valuesList):
        self.fillCells(valuesList)
        self.measureDimensions()
        self.getRowTraits()

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

    def measureDimensions(self):
        self.clearMeasurements()
        left = 0
        right = 1

        for row in range(len(self.Cell)):
            leftValueLength = len(self.Cell[row][left])
            rightValueLength = len(self.Cell[row][right])

            if self.Cell[row][left] != self.SECTION_MARKER:
                if leftValueLength > self.widestLeftColumn:
                    self.widestLeftColumn = leftValueLength
                if rightValueLength > self.widestRightColumn:
                    if self.Cell[row][right] != self.MERGE_MARKER:
                        self.widestRightColumn = rightValueLength

                if self.widthAllowance < (leftValueLength + rightValueLength):
                    self.widestRow = leftValueLength + rightValueLength
                    self.WrapsForRow.append(row)
                    self.numRowsWrapped = self.numRowsWrapped + 1
                else:
                    self.WrapsForRow.append(0)

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

            self.RowInfo.append({self.MERGE_MARKER: merge, self.SECTION_MARKER: sectionEnd})


    def getContextRowChars(self, row):
        merged = self.MERGE_MARKER
        nextMerged = "Next Merged"
        sectionHead = "Section Head"
        tableHead = "Table Head"
        sectionFoot = "Section Foot"
        tableFoot = "Table Foot"
        sectionMarker = self.SECTION_MARKER

        traits = {merged, nextMerged, sectionHead, tableHead, tableFoot, sectionFoot,
                  sectionMarker}
        for key in traits:
            traits[key] = False


        if self.RowInfo[row][merged]:
            traits[merged] = True
        if self.RowInfo[row][sectionMarker]:
            traits[sectionMarker] = True

        # Process information on next printable row
        if row < len(self.RowInfo):
            if self.RowInfo[row + 1][sectionMarker]:
                traits[sectionFoot] = True
                # If row is a sectionFoot then need to check row after the section marker row
                if row < len(self.RowInfo):
                    if self.RowInfo[row + 2][merged]:
                        traits[nextMerged] = True

            else:
                if self.RowInfo[row + 1][merged]:
                    traits[nextMerged] = True





    def printUnicodeTable(self):
        self.getRowTraits()
        self.measureDimensions()
        print("```")

        left = 0
        right = 1
        isMerge = 0
        isSectionEnd = 1
        rowWraps = self.numRowsWrapped
        widthLeft = self.widestLeftColumn
        widthRight = self.widestRightColumn

        for i in range(len(self.RowInfo)):

            if i == 0:
                lineFill = self.BoxChars["Horizontal"]["double"]["straight"]
                if self.RowInfo[i][self.MERGE_MARKER]:
                    separator = lineFill
                else:
                    separator = self.BoxChars["Horizontal"]["double"]["intersect"]["down"]["double"]

                print(self.BoxChars["Left"]["Corner"]["Top"]["double"].ljust(widthLeft + 2, lineFill), end=separator)
                print("".rjust(widthRight + 1, lineFill), end=(self.BoxChars["Right"]["Corner"]["Top"]["double"] + '\n'))



            edgeLeft = self.BoxChars["Right"]["Vertical"]["double"]["straight"]
            lineFill = self.BoxChars["Horizontal"]["single"]["straight"]
            separator = self.BoxChars["Left"]["Vertical"]["double"]["straight"]
            edgeRight = self.BoxChars["Right"]["Vertical"]["double"]["straight"]
            edgeRight = edgeRight + '\n'

            if self.Cell[i][left] != self.SECTION_MARKER:
                ##if rowWraps < 1:
                if self.RowInfo[i][self.MERGE_MARKER]:
                    print(edgeLeft + "%s" % self.Cell[i][left].center(widthLeft + widthRight + 3), end=edgeRight)
                else:
                    print(edgeLeft + "%s %s %s" % (self.Cell[i][left].center(widthLeft), separator,
                                                   self.Cell[i][right].center(widthRight)), end=edgeRight)

                if i == (len(self.RowInfo) - 1):
                    if self.RowInfo[i][self.MERGE_MARKER]:
                        separator = self.BoxChars["Horizontal"]["double"]["straight"]
                    else:
                        separator = self.BoxChars["Horizontal"]["double"]["intersect"]["up"]["double"]
                    print(self.BoxChars["Left"]["Corner"]["Bottom"]["double"].ljust(widthLeft + 2, lineFill), end=separator)
                    print("".rjust(widthRight + 1, lineFill), end=(self.BoxChars["Right"]["Corner"]["Bottom"]["double"] + '\n'))
                else:
                    print("TODO: NICE BOXES".center(widthLeft + widthRight + 3, lineFill))

        print("```")

        print("Width: left %d, right %d, combined %d" % (widthLeft, widthRight, (widthLeft + widthRight)))
