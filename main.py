from pyoxigraph import *
import xlsxwriter
import os


def parseFile():
    directory = input("Enter directory:")
    print('Directory is: ' + directory)

    for filename in os.listdir(directory):
        file = os.path.join(directory, filename)
        if os.path.isfile(file) and file.endswith("ttl"):
            result = list(parse(file, "text/turtle"))
            print(result)


if __name__ == '__main__':
    parseFile()