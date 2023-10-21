#!/usr/bin/env bash

set -ex

shopt -s globstar
PY_FILES=src-api/**/*.py

pylint $PY_FILES \
    -j 0 \
    --output-format=parseable \
    --reports=no \
    --exit-zero \
    --rcfile src-api/pylintrc \
    > src-api/pylint.log

pycodestyle $PY_FILES \
    --config=src-api/pylintrc \
    > src-api/pycodestyle.log \
    || true
