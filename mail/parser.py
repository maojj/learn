# encoding: utf-8
#!/usr/bin/python

import csv

with open('name.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print(row['first'], row['second'])

		
