import re
import xml.etree.ElementTree as ET

def findAndPrintTestCoverage(text: str):
    matches : list = re.findall('(?<=">TestingGOCi)(.*)(?=<\/option>)', text)
    print('## Test Coverage\\n | File        | Coverage           |\\n | :-------------: |:-------------:|\\n', end="")
    for match in matches:
        line = match.split(" ")
        if line[1][1:-1] != "0.0%":
            print("| " + line[0]+ " | " + line[1][1:-1] + " |\\n", end="")


def parseUnitTestXml(fileName: str):
    total : int = 0
    failures: int = 0
    errors: str = ""
    mytree = ET.parse(fileName)
    myroot = mytree.getroot()
    for testSuite in myroot.findall("testsuite"):
        total += int(testSuite.get("tests"))
        failures += int(testSuite.get("failures"))
        if int(testSuite.get("failures")) > 0:
            for testCase in testSuite.findall("testcase"):
                for failure in testCase.findall("failure"):
                    errors += failure.text
                    errors += "\\n\\n"
    print(f"## Unit Tests\\n **Total**: {total}    **Successes**:{total-failures}    **Failures**: {failures}\\n", end="")

    if failures > 0:
        print(f" ### Errors \\n ``` \\n\\n{errors}   ```", end="")

def main():
    coverFile = open("cover.html")
    text = coverFile.read()
    coverFile.close()
    print('{"body":" ', end="")
    findAndPrintTestCoverage(text)
    parseUnitTestXml("unit-tests.xml")
    print('"}', end="")

main()
