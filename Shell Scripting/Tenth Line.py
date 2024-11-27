# Read from the file file.txt and output the tenth line to stdout.
#cat file.txt | tail -n +10 | head -n 1
sed -n '10p' file.txt
