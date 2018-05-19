#!/bin/bash

# Prefer US English and use UTF-8
export LC_ALL="en_US.UTF-8"
export LANG="en_US"
export DOTFILES="$HOME/Github/dotfiles"
export DOTFILES_CONFIGURATIONS="$DOTFILES/df.configs"
export CRED_CONF="$DOTFILES_CONFIGURATIONS/cred.config.json"
#export NUCLEUS="$HOME/Nucleus"
#export NUCLEUS_BIN="$NUCLEUS/bin"

export GOPATH=~/go
export PATH=$PATH:$GOPATH/bin
export PATH=$PATH:$HOME/bin
export PATH=$PATH:$HOME/google-cloud-sdk/bin
export PATH=/usr/local/sbin:$PATH


function source_lib () {
    for f in $DOTFILES/.src/*
    do
        if [ -f "$f" ]; then
            source $f # . $f
            echo "[INFO] ... Sourced file => $(basename $f)"
        fi
    done
}

# The next line updates PATH for the Google Cloud SDK.
if [ -f '/Users/ial-ah/Desktop/google-cloud-sdk/path.bash.inc' ]; then source '/Users/ial-ah/Desktop/google-cloud-sdk/path.bash.inc'; fi

# The next line enables shell command completion for gcloud.
if [ -f '/Users/ial-ah/Desktop/google-cloud-sdk/completion.bash.inc' ]; then source '/Users/ial-ah/Desktop/google-cloud-sdk/completion.bash.inc'; fi

source_lib
