#!/bin/bash
for arg in $@; do
	echo "Acum prelucram " $arg
	if [ -x $arg ]; then
		echo "Acesta este executabil: " $arg
	fi
done
