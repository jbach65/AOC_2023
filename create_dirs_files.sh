#!/bin/bash

# Bash script to create directories and files for days 4 through 25 because I'm lazy...

for day in {4..25}
do
    # Create the directory for the day
    mkdir -p "day_$day"

    # Create the Python files and data files inside the day's directory
    touch "day_$day/AOC_${day}_1.py"
    touch "day_$day/AOC_${day}_2.py"
    touch "day_$day/AOC_${day}_test.txt"
    touch "day_$day/AOC_${day}.txt"
done

echo "Directories and files created successfully."
