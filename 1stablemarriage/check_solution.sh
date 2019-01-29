#!/bin/bash
# make exacutable: chmod +x check_solution.sh
# run: ./check_solution.sh pypy A.py
# or
# ./check_solution.sh java solution
# ./check_solution.sh ./a.out
folder_sample=data/sample
for f in $folder_sample/*.in; do
    echo $f
    pre=${f%.in}
    out=$pre.out
    verdict=$pre.verd
    $* < $f > $out
    python3 output_validator/output_validator.py $f < $out > $verdict
    if grep -Fxq "success" $verdict
    then 
        echo Correct!
    else
        echo $f Incorrect!
        exit 1
    fi
done
folder_secret=data/secret
for f in $folder_secret/*.in; do
    echo $f
    pre=${f%.in}
    out=$pre.out
    verdict=$pre.verd
    $* < $f > $out
    python3 output_validator/output_validator.py $f < $out > $verdict
    if grep -Fxq "success" $verdict
    then 
        echo Correct!
    else
        echo $f Incorrect!
        exit 1
    fi
done
