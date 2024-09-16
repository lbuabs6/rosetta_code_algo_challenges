import argparse

def getFinalOpenedDoors(numDoors):
    doors = [False for x in range(numDoors)]
    opened_doors = []
    tracker = 1

    while tracker <= numDoors:
        for i in range(tracker - 1, numDoors, tracker):
            doors[i] = not doors[i]
        tracker += 1
    
    for i, e  in enumerate(doors):
        if e:
            opened_doors.append(i+1)
    return opened_doors

if __name__ == "__main__":
    arguments = argparse.ArgumentParser()
    arguments.add_argument("numDoors", type=int)
    args = arguments.parse_args()
    result = getFinalOpenedDoors(args.numDoors)
    print(result)