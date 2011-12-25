#!/bin/sh
SELFDIR=`dirname $0`
cd ${SELFDIR}
python bootstrap.py
bin/buildout
