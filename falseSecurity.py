lettersToMorse = {
        "A" : ".-",
        "B" : "-...",
        "C" : "-.-.",
        "D" : "-..",
        "E" : ".",
        "F" : "..-.",
        "G" : "--.",
        "H" : "....",
        "I" : "..",
        "J" : ".---",
        "K" : "-.-",
        "L" : ".-..",
        "M" : "--",
        "N" : "-.",
        "O" : "---",
        "P" : ".--.",
        "Q" : "--.-",
        "R" : ".-.",
        "S" : "...",
        "T" : "-",
        "U" : "..-",
        "V" : "...-",
        "W" : ".--",
        "X" : "-..-",
        "Y" : "-.--",
        "Z" : "--..",
        "?" : "----",
        "_" : "..--",
        "." : "---.",
        "," : ".-.-"}
morseToLetters = {}
for i in lettersToMorse.keys():
    val = lettersToMorse[i]
    morseToLetters[val] = i
stringToLenMorseString = {}
for i in lettersToMorse.keys():
    stringToLenMorseString[i] = str(len(lettersToMorse[i]))

def convertToWords(string):
    morse = ''
    lengthString = ''
    for i in string:
        morse += lettersToMorse[i]
        lengthString += stringToLenMorseString[i]
    lengthString = list(reversed(lengthString))
    counter = 0
    crackedCode = ''
    for i in lengthString:
        i = int(i)
        crackedCode += morseToLetters[morse[counter:counter+i]]
        counter += i
    print(crackedCode)

try:
    while True:
        code = input()
        convertToWords(code)
except:
    pass