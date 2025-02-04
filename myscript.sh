#!/bin/bash
mv myscript.sh SoftDev
read filename
touch $filename
git add myscript.sh
git add $filename
read commit
git commit -am $commit
git push
