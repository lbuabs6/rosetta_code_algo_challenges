package main

func getFinalOpenedDoors(numDoors int) []int {
	var doors []bool = make([]bool, numDoors)
	var open_doors []int

	for i := 0; i < numDoors; i++ {
		doors[i] = false
	}

	var tracker int = 1
	for tracker <= numDoors {
		for i := tracker - 1; i < numDoors; i += tracker {
			doors[i] = !doors[i]
		}
		tracker += 1
	}

	for i := 0; i < numDoors; i++ {
		if doors[i] {
			open_doors = append(open_doors, i+1)
		}
	}
	return open_doors

}
