#!/bin/bash
i=0
s=0
for arg in $@; do
	i=$(($i+1))
	if [ $(($i%3)) -eq 0 ]; then
		s=$(($s+$arg))
	fi
done
echo "Suma nr de pe poz m3 este: " $s
