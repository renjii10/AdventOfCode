dialLocation = 50
max_value = 99
min_value = 0
timeLandedOnZero = 0
crossCtr = 0
file_path = 'path/to/file/InputFile.txt'
with open(file_path) as file_object:
    for line in file_object:
        value = line.strip()
        direction = value[:1]
        movement = int(value[1:])
        if direction == "R":
            while movement > 0:
                dialLocation = dialLocation + 1 if dialLocation != max_value else min_value
                if dialLocation == min_value:
                    crossCtr = crossCtr + 1
                movement = movement - 1                   
        else:
            print(f" CUrrent pos {dialLocation} Direction L, Movement {movement}")
            while movement > 0:
                dialLocation = dialLocation - 1 if dialLocation != min_value else max_value
                movement = movement - 1
                if dialLocation == min_value:
                    crossCtr = crossCtr + 1

        if dialLocation == 0:
            timeLandedOnZero = timeLandedOnZero + 1
            print(f"0 hit: {timeLandedOnZero}")

print(f"Final 0 hit: {timeLandedOnZero}")
print(f"Final 0 crosses: {crossCtr}")
