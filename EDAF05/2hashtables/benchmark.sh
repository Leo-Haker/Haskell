#!/bin/bash

RUNS=100
total1=0
total2=0

for i in $(seq 1 $RUNS); do
    t=$( { time ./check_solution.sh python3 testReference.py > /dev/null 2>&1; } 2>&1 | grep real | awk '{print $2}' | sed 's/m/:/g' | sed 's/s//g')
    min=$(echo $t | cut -d: -f1)
    sec=$(echo $t | cut -d: -f2)
    ms=$(echo "$min * 60 + $sec" | bc)
    total1=$(echo "$total1 + $ms" | bc)

    t=$( { time ./check_solution.sh python3 test1Reference.py > /dev/null 2>&1; } 2>&1 | grep real | awk '{print $2}' | sed 's/m/:/g' | sed 's/s//g')
    min=$(echo $t | cut -d: -f1)
    sec=$(echo $t | cut -d: -f2)
    ms=$(echo "$min * 60 + $sec" | bc)
    total2=$(echo "$total2 + $ms" | bc)

    echo "Run $i done"
done

avg1=$(echo "scale=3; $total1 / $RUNS" | bc)
avg2=$(echo "scale=3; $total2 / $RUNS" | bc)

echo "testReference.py   avg: ${avg1}s"
echo "test1Reference.py  avg: ${avg2}s"