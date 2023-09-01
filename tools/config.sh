#!/bin/bash

BASE_DIR=$(dirname "$(dirname "$(realpath "$0")")")
UI_DIR="$BASE_DIR/ui"

PYTHON_SRC_DIR="$BASE_DIR/src/downloader"
PYTHON_UI_DIR="$PYTHON_SRC_DIR/ui"


export BASE_DIR
export UI_DIR
export PYTHON_SRC_DIR
export PYTHON_UI_DIR
