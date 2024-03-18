import datetime
import re

def main():

    pathToBuffer = "./exampleInput.md"
    readBuffer = ""
    testInput = ["CLOCK: [2024-03-11 Mon 07:53:20]--[2024-03-11 Mon 08:06:20]", "CLOCK: [2024-03-11 Mon 08:06:28]--[2024-03-11 Mon 08:54:26]", "CLOCK: [2023-07-05 Wed 16:06:44]--[2023-07-05 Wed 16:31:40]"]
    #read file into variable
    # with open(pathToBuffer, 'rb') as inp:
    #     readBuffer = inp
    #TODO:
    # - [ ] find and extract :logbook: ... :end: drawers with parent indentation (i.e.: the tasks name) from input
    # - [ ] strip it down to its components and store it in an object?
    # - [ ] get regex that returns everything between :LOGBOOK: & :END:
    #   - possible solutions:
    #   > (?s):LOGBOOK:(.*?):END: <- Returns :LOGBOOK: and :END: as well
    #   > (?s)^.*?:LOGBOOK:(.*?):END: <- Returns :LOGBOOK: and :END: + the line above :LOGBOOK:

    with open(pathToBuffer, 'r') as buffer:

        input = buffer.read()
        getLogbooks(input)


    pLbArray = parseLogbook(testInput) #returns a list of ParsedLbEntry objects

    for x in pLbArray:
        print(x)

##### END OF MAIN ####


def getLogbooks(buffer):
    thisRegEx = re.compile("(?s)^.*?:LOGBOOK:(.*?):END:", re.M)
    # Use it with (aka Py RegEx helpful snippets):
    # matches = thisRegEx.match(buffer) <- Store matches in an array
    # location = matches[0].span() <- Return the start and ending(+1) position (in the input) of the 0th match
    #--- LEFT OFF HERE LAST TIME ---
    # Writing a func that extracts every logbook from the input (a var named "buffer" in this case)
    # Potential faliure points:
    # - You might have to store the position of the matches in the input so you can append/update those lines later with the elapsed time.
    rawLogbooks = re.findall(thisRegEx, buffer)
    print("#############################")
    print(rawLogbooks)
    print("+++++++++++++++++++++++++++++")


def parseLogbook(logbook):
    parsedLogbook = []
    for x in logbook:
        x = x.replace("CLOCK: ", "").replace("[", "").replace("]", "").split("--")

        tempSplit = x[0].split(" ")
        x[0] = f"{tempSplit[0]} {tempSplit[2]}"
        tempSplit = x[1].split(" ")
        x[1] = f"{tempSplit[0]} {tempSplit[2]}"

        st = datetime.datetime.strptime(x[0], "%Y-%m-%d %H:%M:%S")
        et = datetime.datetime.strptime(x[1], "%Y-%m-%d %H:%M:%S")
        lbObj = ParsedLbEntry(st, et)

        parsedLogbook.append(lbObj)

    return parsedLogbook


class ParsedLbEntry:
    def __init__(self, st, et):
        self.st = st
        self.et = et

    def __str__(self):
        return f"start time: {self.st} | end time: {self.et}"

if __name__ == '__main__':
    main()
