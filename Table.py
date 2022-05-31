class Table:
    def __init__(self):
        self.Cell = []
        self.RowInfo = [{}]
        self.widestLeftColumn = 0
        self.widestRightColumn = 0
        self.widestRow = 0
        self.widthAllowance = 28 - 7
        self.WrapsForRow = []
        self.DoesWrap = False
        self.numRowsWrapped = 0
        self.MERGE_MARKER = "MERGE"
        self.SECTION_MARKER = "ENDSECTION"
        self.BoxCharacter = {"Left":
                             {"Corner":
                                  {"single": '┌',
                                   "double": '╔'},
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
                         "Center":
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
                                  {"single": '┐',
                                   "double": '╗'},
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

    def clearMeasurements(self):
        self.widestLeftColumn = 0
        self.widestRightColumn = 0
        self.widestRow = 0
        self.widthAllowance = 28 - 7
        self.WrapsForRow = []
        self.DoesWrap = False
        self.numRowsWrapped = 0

    def clearRowInfo(self):
        self.RowInfo = [{}]

    def build(self, valuesList):
        self.fillCells(valuesList)
        self.measureDimensions()
        self.updateRowInfo()

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

            if self.Cell[row][left] == self.SECTION_MARKER:
                if leftValueLength > self.widestLeftColumn:
                    self.widestLeftColumn = leftValueLength
                if rightValueLength > self.widestRightColumn:
                    if self.Cell[row][right] != self.MERGE_MARKER:
                        self.widestRightColumn = rightValueLength
                    else:
                        rightValueLength = 0

                if self.widthAllowance < (leftValueLength + rightValueLength):
                    self.widestRow = leftValueLength + rightValueLength
                    self.WrapsForRow.append(row)
                    self.numRowsWrapped = self.numRowsWrapped + 1
                else:
                    self.WrapsForRow.append(0)

        if self.numRowsWrapped > 0:
            self.DoesWrap = True

    def updateRowInfo(self):
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

    def printUnicodeTable(self):
        print("```")
        print("TODO: printUnicodeTable")
        print("```")
