#!/bin/bash
for arg in $@; do
	ok=0
	if [ -f $arg ]; then
		ok=$(($ok+1))
		#echo "DA"
	fi
	if [ -d $arg ]; then
		ok=$(($ok+1))
		#echo "da"
	fi
	if [ $ok -eq 0 ]; then
			echo $ok
	fi
done
