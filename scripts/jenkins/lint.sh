#!/usr/bin/env bash

set -ex

shopt -s globstar
PY_FILES=back-api/**/*.py

pylint $PY_FILES \
    -j 0 \
    --output-format=parseable \
    --reports=no \
    --exit-zero \
    --rcfile back-api/pylintrc \
    > back-api/pylint.log

pycodestyle $PY_FILES \
    --config=back-api/pylintrc \
    > back-api/pycodestyle.log \
    || true
