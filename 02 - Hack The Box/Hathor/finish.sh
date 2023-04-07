#!/bin/bash
name=$(echo "{PWD##*/}")
git add ../$name/*
git commit -m "Finished $name."
git push
