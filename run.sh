#! /bin/sh
: '
echo Run set1
start1=$(date +%s.%N)
python regressor.py -t set1.txt < in1.txt > res1.txt
end1=$(date +%s.%N)    
runtime1=$(python -c "print(${end1} - ${start1})")
echo "Runtime was $runtime1"
python evaluate.py 1
echo Finish set1
echo

echo Run set2
start2=$(date +%s.%N)
python regressor.py -t set2.txt < in2.txt > res2.txt
end2=$(date +%s.%N)    
runtime2=$(python -c "print(${end2} - ${start2})")
echo "Runtime was $runtime2"
python evaluate.py 2
echo Finish set2
echo

echo Run set3
start3=$(date +%s.%N)
python regressor.py -t set3.txt < in3.txt > res3.txt
end3=$(date +%s.%N)    
runtime3=$(python -c "print(${end3} - ${start3})")
echo "Runtime was $runtime3"
python evaluate.py 3
echo Finish set3
echo
'
echo Run set4
start4=$(date +%s.%N)
python regressor.py -t set4.txt < in4.txt > res4.txt
end4=$(date +%s.%N)    
runtime4=$(python -c "print(${end4} - ${start4})")
echo "Runtime was $runtime4"
python evaluate.py 4
echo Finish set4
echo
'
read -p "Press any key to finish... " -n1 -s