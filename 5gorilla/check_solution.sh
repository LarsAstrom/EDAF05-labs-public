#!/bin/bash
# make exacutable: chmod +x check_solution.sh
# run: ./check_solution.sh pypy A.py
# or
# ./check_solution.sh java solution
# ./check_solution.sh ./a.out

for f in data/**/*.in; do
    echo $f
    pre=${f%.in}
    out=$pre.out
    ans=$pre.ans
    verdict=$pre.verd
    $* < $f > $out
    python3 output_validator/output_validator.py $f $out $ans > $verdict
    if grep -Fxq "success" $verdict
    then 
        echo Correct!
    else
        echo $f Incorrect!
        exit 1
    fi
done
