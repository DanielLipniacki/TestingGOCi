import re
import xml.etree.ElementTree as ET

def findAndPrintTestCoverage(text: str):
    matches = re.findall('(?<=">TestingGOCi)(.*)(?=<\/option>)', text)
    print('## Test Coverage\\n | File        | Coverage           |\\n | :-------------: |:-------------:|\\n', end="")
    for match in matches:
        line = match.split(" ")
        print("| " + line[0]+ " | " + line[1][1:-1] + " |\\n", end="")


def parseUnitTestXml(fileName: str):
    total : int = 0
    failures: int = 0
    mytree = ET.parse(fileName)
    myroot = mytree.getroot()
    for testSuite in myroot.findall("testsuite"):
        total += int(testSuite.get("tests"))
        failures += int(testSuite.get("failures"))
    
    print(f"## Unit Tests\\n Total: {total}, failures: {failures}\\n", end="")

def main():
    coverFile = open("cover.html")
    text = coverFile.read()
    coverFile.close()
    print('{"body":" ', end="")
    findAndPrintTestCoverage(text)
    parseUnitTestXml("unit-tests.xml")
    print('"}', end="")

main()
