##https://adventofcode.com/2025/day/2

##1227775554 Result of sample

def checkValidId(id:int):bool



invalidIds = []
idSum = 0
file_path = 'path/to/file/InputFile.txt'
with open(file_path) as file_object:
    for line in file_object:
        lineStr = line.strip()
        for range in lineStr.split(','):
            rangeArr = range.split('-')
            i = int(rangeArr[0])
            max = int(rangeArr[1])
            while i <= max:
                if not checkValidId(i):
                    invalidIds.append(i)
if len(invalidIds) > 0:
    for id in invalidIds:
        print(f"")
