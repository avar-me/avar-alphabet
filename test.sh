#!/bin/bash

N=${1:-50}
diff <(head -n $N words.txt) <(head -n $N words.txt | cut -d: -f1 | ./transliterate.py)
