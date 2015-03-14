# encoding: utf-8
#!/usr/bin/python

import sqlite3

def initDataBase():
	conn = sqlite3.connect("messageDB.sqlite3");

	#init message table
	conn.execute('''CREATE TABLE IF NOT EXISTS EMAIL
	       (INTERNALID 	  TEXT PRIMARY KEY     NOT NULL,
	       SENDER	      TEXT  NOT NULL,
	       SENDTIME       INT64   NOT NULL, 
	       SENDERIP       TEXT  NOT NULL,
	       SENDERHOSTNAME TEXT,  
	       SUBJECT        TEXT,
	       ACTION		  INT,
	       HITPOLICY      INT);''')


	#init user table

	conn.execute('''CREATE TABLE IF NOT EXISTS USER
		(USERID INT PRIMARY KEY NOT NULL,
		EMAIL 	TEXT NOT NULL,
		DOMAIN	TEXT);''');


	#init Send table

	conn.execute('''CREATE TABLE IF NOT EXISTS SEND
		(SENDERID INT NOT NULL,
			RECEIVERID INT NOT NULL,
			INTERNALID TEXT NOT NULL,
			PRIMARY KEY(SENDERID,RECEIVERID,INTERNALID));''');

	conn.close()
return

def parse():
	
return;

def function():

return;



