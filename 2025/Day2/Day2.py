##https://adventofcode.com/2025/day/2

##1227775554 Result of sample
invalidIds = []
refinedInvalidIds = []
def checkValidIdsInRange(startId, endId):
    for i in range(startId,endId+1):
        strId = str(i)
        ##print(f"Evaluating: {i}")
        if strId[0] == "0" or len(strId) == 1 or len(strId)%2 != 0:
            ##print(f"Skipping Item [{i}]")
            continue
        indexSplit = int(len(strId)/2)
        item1 = strId[0:indexSplit]
        item2 = strId[indexSplit:]
        #print(f"Item 1 [{item1}] Item2 [{item2}]")
        if  item1 == item2:
            print(f"Item [{i}] is invalid. Adding to list")
            invalidIds.append(i)
            continue
        ##print(f"Item [{i}] is valid. Ignoring")

def checkValidIdsInRangeRefined(startId, endId):
    for i in range(startId,endId+1):
        strId = str(i)
        ##print(f"Evaluating: {i}")
        if strId[0] == "0" or len(strId) == 1 or len(strId)%2 != 0:
            ##print(f"Skipping Item [{i}]")
            continue
        indexSplit = int(len(strId)/2)
        item1 = strId[0:indexSplit]
        item2 = strId[indexSplit:]
        #print(f"Item 1 [{item1}] Item2 [{item2}]")
        if  item1 == item2:
            print(f"Item [{i}] is invalid. Adding to list")
            refinedInvalidIds.append(i)
            continue
        ##print(f"Item [{i}] is valid. Ignoring")   

file_path = ''
with open(file_path) as file_object:
    for line in file_object:
        lineStr = line.strip()
        for rangeStr in lineStr.split(','):
            print(f"Splitting range [{rangeStr}]")
            rangeArr = rangeStr.split('-')
            i = int(rangeArr[0])
            max = int(rangeArr[1])
            
            checkValidIdsInRange(i,max)
if len(invalidIds) > 0:
    idSum = 0
    for id in invalidIds:
        idSum = idSum + id
print(f"Sum of InvalidIds: {idSum}")

if len(refinedInvalidIds) > 0:
    idSum = 0
    for id in invalidIds:
        idSum = idSum + id
print(f"Sum of InvalidIds: {idSum}")
##1760591196115662 Sum of all ids