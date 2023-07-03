#!/bin/bash

echo "Date,UniqueID" > submit-data.csv

for i in {1..20}; do
dateOutput=`date '+%Y-%m-%d %H:%M:%S'`
uuidgenOutput=`uuidgen | awk '{print(tolower($0))}'`
echo "${dateOutput},${uuidgenOutput}" >> submit-data.csv
done
