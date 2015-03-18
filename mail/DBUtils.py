# encoding: utf-8
# !/usr/bin/python

import sqlite3
import DataObject


def init_database():
    connect = sqlite3.connect("messageDB.sqlite3")
    connect.text_factory = str

    conn = connect.cursor()
    #init message table
    conn.execute('''CREATE TABLE IF NOT EXISTS EMAIL
      (INTERNALID 	  TEXT PRIMARY KEY     NOT NULL,
                 SENDER	      TEXT  NOT NULL,
                 SENDTIME       TEXT   NOT NULL,
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
      PRIMARY KEY(SENDERID,RECEIVERID,INTERNALID));''')

    return conn


def insertAMail(newMail):
    # """
    # :type newMail: DataObject.mailMeta
    # """
    # newMail = DataObject.mailMeta(mail)
    newMail.SenderHostName = "xxx"
    connect = init_database()
    action = 0
    reason = 0
    connect.execute('INSERT INTO EMAIL Values (?,?,?,?,?,?,?,?)', [newMail.MailId, newMail.Sender,
                                                                    newMail.Timestamp, newMail.SenderIP,
                                                                    newMail.SenderHostName, newMail.Subject,
                                                                    action, reason])