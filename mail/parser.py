# -*- coding: utf-8 -*-
#!/usr/bin/python

import csv

with open('bj5_IpResolved.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	index = 0
	for row in reader:
		index += 1
		if index > 100:
			break
		print(row['Sender'], row['Recipient(s)'],row['Timestamp'], row['Subject'],row['SenderIP'], row['SenderHostName'],row['Mail'])

