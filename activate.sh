#!/bin/bash

export DOTFILES="$PWD"
export DOTFILESMACHINES="$PWD/settings/machines.json"
export DOTFILESSETTINGS="$PWD/settings/dsettings.json"
export DOTFILESKEYS="$PWD/keys"

function source_files_under_dir () {
    sd="$1"
    refiles="$2"
    echo "making it !"
    for f in $DOTFILES/.$sd/.$refiles
    do
        echo "FOUND FILE $f"
        if [ -f "$f" ]; then
            echo "[INFO] ... Sourcing $f"
            # take action on each file. $f store current file name
            . $f
            echo "[INFO] ... Completed."
        fi
    done
}

target=$1

if [ "$target" = "--functions" ]; then
    source_files_under_dir "functions" "*"
fi
