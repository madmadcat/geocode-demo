#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv

with open('locate.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        print row[0], row[1]

