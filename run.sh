#!/usr/bin/env bash
script_dir=$(cd $(dirname ${BASH_SOURCE:-$0}); pwd)
PIPFILE=$script_dir/Pipfile
export PIPENV_PIPFILE=$(cd $(dirname $PIPFILE) && pwd)/$(basename $PIPFILE)
pipenv run fetch
