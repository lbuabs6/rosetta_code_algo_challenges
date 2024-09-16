function getFinalOpenedDoors(numDoors) {
  const doors = [];
  const open_doors = [];
  for (let i = 0; i < numDoors; i++){
    doors.push(false);
  }
  let tracker = 1;
  while (tracker <= numDoors){
    for (let i = tracker - 1; i < numDoors; i += tracker){
      doors[i] = !doors[i];
    }
    tracker += 1;
  }
  
  for (let i = 0; i < numDoors; i++){
    if (doors[i]){
      open_doors.push(i + 1);
    }
  }
  return open_doors;
}

if(require.main === module){
  const numDoors = parseInt(process.argv[2], 10);
  if (isNaN(numDoors)){
    console.error();
    process.exit(1);
  }
  const result = getFinalOpenedDoors(numDoors);
  console.log(result);
}