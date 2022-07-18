#!/bin/bash
for item in $(ls "." | grep -E "\.txt$"); do
        grep -l "cat" $item
done
