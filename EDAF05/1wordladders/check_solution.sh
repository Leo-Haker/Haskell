#!/bin/bash
# make executable: chmod +x check_solution.sh
# run: ./check_solution.sh pypy A.py
# or
# ./check_solution.sh java solution
# ./check_solution.sh ./a.out

for f in data/**/*.in; do
    echo "---------------------------"
    echo "Testing: $f"
    
    pre=${f%.in}
    out=$pre.out
    ans=$pre.ans
    
    # Använd 'time' för att mäta körningen. 
    # -p ger ett standardformat (real, user, sys)
    # Vi kör själva programmet ($*) med input
    START_TIME=$(date +%s%3N) # Starttid i millisekunder
    
    $* < $f > $out
    
    END_TIME=$(date +%s%3N) # Sluttid i millisekunder
    ELAPSED=$((END_TIME - START_TIME))
    
    DIFF=$(diff -w $ans $out)
    
    if [ "$DIFF" == "" ]
    then 
        echo "Status: Correct!"
        echo "Time: ${ELAPSED}ms"
    else
        echo "Status: $f Incorrect!"
        # Visa skillnaden om du vill se vad som blev fel:
        # diff -u $ans $out
        exit 1
    fi
done
