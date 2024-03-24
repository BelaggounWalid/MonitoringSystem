#!/bin/sh

# Loop through each user in the file "allusr.txt"
for user in $(cat allusr.txt); do
    # Use the "ps" command to get the total RSS (Resident Set Size) for each user
    # The RSS represents the non-swapped physical memory that a task has used
    # The "-U" option specifies the user
    # The "-o" option specifies the format of the output
    # The "rss" parameter extracts the RSS value
    rss=$(ps -U "$user" -o rss | awk 'NR>1 { sum += $1 } END { print sum }')

    # Output the username and the calculated RAM usage in KB
    echo "$user $rss"
done

