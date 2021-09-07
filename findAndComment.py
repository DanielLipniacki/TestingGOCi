import re

def findText(text: str):
    matches = re.findall('(?<=">TestingGOCi)(.*)(?=<\/option>)', text)
    print('{"body":" ## Test Coverage\\n | File        | Coverage           |\\n | :-------------: |:-------------:|\\n', end="")
    for match in matches:
        line = match.split(" ")
        print("| " + line[0]+ " | " + line[1][1:-1] + " |\\n", end="")
    print('"}', end="")

def main():
    coverFile = open("cover.html")
    text = coverFile.read()
    coverFile.close()
    findText(text)

main()
