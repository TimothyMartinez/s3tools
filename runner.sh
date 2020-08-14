#!/bin/bash

bucket=$1
resource=$2
function handledir() {
    echo "Uploading files to the $1 folder"
    if [ `ps | grep python | wc -l` -gt 20 ]; then
        wait
    fi
    for file in "$1"*; do
        if [ -f "$file" ]; then
            addfiles.py $bucket "$file" &
        elif [ -d "$file" ]; then
            handledir "$file/"
        fi
    done
}

if validator.py $1 2>&1 >/dev/null; then
    echo $resource
    if [ -d "$resource" ]; then
        handledir "$resource"
        wait
    elif [ -f "$resource" ]; then
        addfiles.py $bucket $resource
    fi
else
    echo "Bucket name mispelled or does not exist"
fi