# !/usr/bin/evn python
# -*- coding: utf8 -*-
import psycopg2

class Postgres():

    # initial object
    def __init__(self, host, db_name, user, passwd, charset):
        self.host = host
        self.db_name = db_name
        self.user = user
        self.passwd = passwd
        self.charset = charset
        self.connectdb()

    # connect to database
    # will create a Cursor object which can execute all the quries you need.
    def connectdb(self):
        #Define our connection string
        conn_string = "host='" + self.host + "'dbname='" + self.dbname + "'user'" + self.user  + "'password='" + self.passwd + "'"

        # get a connection, if a connect cannot be made an exception will be raised here
        conn = psycopg2.connect(conn_string)

        # conn.cursor will return a cursor object, you can use this cursor to perform queries
        cursor = conn.cursor()	

    # execute sql statment
    def exeSQL(self, sql ):
        try:
            self.cursor.execute( sql )
            self.db.commit()
        except:
            self.db.rollback()

    def createTable( self, table_name, key_list ):
        sql = "CREATE TABLE IF NOT EXISTS " + table_name + "(" + key_list[0] + " char(32)"
        for i in range( 1, len(key_list) ):
            sql += "," + key_list[i] + " char(32)"
        sql += ");"
        print sql	
        self.exeSQL( sql )

    def insertData( self, table_name, key_list, data_list ):

        sql = "INSERT INTO " + table_name + "( " + key_list[0]

        for i in range( 1, len(key_list) ):
            sql += "," + key_list[i]

        sql += ") VALUES ("

        for i in range( 0, len(data_list) ):
            if data_list[i]:	
                try: 
                    sql += "'"+ data_list[i] + "',"
                except TypeError:	
                    sql += "'"+ str(data_list[i]) + "',"
            else:
                sql += "' ',"

        sql = sql[0: len(sql) -1 ] + ");"

        self.exeSQL(sql)

