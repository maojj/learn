# -*- coding: utf-8 -*-
# !/usr/bin/python

import csv
import init_database
import mailmeta

def parse_file(file_name):
    with open(file_name) as csvfile:
        reader = csv.DictReader(csvfile)
        conn = init_database.init_database()
        for row in reader:
           amail = mailmeta(row);

def parse_row(row,conn):
    sender = row['Sender']
    Timestamp = row['TimeStamp']





