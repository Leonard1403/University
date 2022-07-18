#!/bin/bash
for arg in $@; do
	if [ $(($arg%2)) -eq 0 ]; then
		echo "Acesta este un nr par" $arg
	fi
done
