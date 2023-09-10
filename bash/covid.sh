#!/bin/bash
# This script downloads covid data and displays it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
NEGATIVE=$(echo $DATA | jq '.[0].negative')
DEATHS=$(echo $DATA | jq '.[0].death')
HOSPITAL=$(echo $DATA | jq '.[0].hospitalized')
PENDING=$(echo $DATA | jq '.[0].pending')
INICU=$(echo $DATA | jq '.[0].inIcuCurrently')
ONVENTILATOR=$(echo $DATA | jq '.[0].onVentilatorCurrently')
TODAY=$(date)

echo "On $TODAY, there were $POSITIVE positive cases, $NEGATIVE negative tests, $DEATHS deaths, and $HOSPITAL hospitalized. There have also been $PENDING pending test results, $INICU patients currently in the ICU, and $ONVENTILATOR patients currently on a ventilator."
