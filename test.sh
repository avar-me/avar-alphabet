#!/bin/bash

diff <(head -n 30 words.txt) <(head -n 30 words.txt | cut -d: -f1 | ./transliterate.py)
