#!/bin/bash
i=0
sum=0
for arg in $@; do
	i=$(($i+1))
	#echo "Elementul este: " $arg
	if [ $(($i%2)) -eq 1 ]; then
		sum=$(($sum+$arg))
	fi
	#echo "Suma este: " $sum
done
echo "Suma este: " $sum
