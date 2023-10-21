#!/usr/bin/env bash

set -ex

cd src-api
pytest \
    --cov=. \
    --cov-report=xml \
    --junit-xml test_report.xml \
    || true
