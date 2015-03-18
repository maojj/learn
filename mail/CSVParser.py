# -*- coding: utf-8 -*-
# !/usr/bin/python

import csv
import DBUtils
import DataObject

def parseFile(file_name):
    with open(file_name) as csvFile:
        reader = csv.DictReader(csvFile)
        conn = DBUtils.init_database()
        for row in reader:
            print 'get row%s' % row
            aMail = DataObject.mailMeta(row)
            ret = DBUtils.insertAMail(aMail)
            print "ret %s" % ret
            break

parseFile("5.csv")





