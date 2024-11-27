# Read from the file file.txt and output the tenth line to stdout.
#cat file.txt | tail -n +10 | head -n 1
#sed -n '10p' file.txt

#!/bin/bash
filename="file.txt"
if [ $(wc -l < "$filename") -ge 10 ]; then
    head -n 10 "$filename" | tail -n 1
fi
