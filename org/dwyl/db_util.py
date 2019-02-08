'''
Created on Apr 20, 2017

@author: raja

source:
    https://www.w3schools.com/python/python_mysql_insert.asp
'''

#!/usr/bin/python
import base64
import sys
import codecs
import MySQLdb

def test():
    print('tst 123')

def get_db():
    db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="test",         # your username
                     passwd="test",  # your password
                     db="test")        # name of the data base
    
    return db
    
def get_db_cursor():
    db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="test",         # your username
                     passwd="test",  # your password
                     db="test")        # name of the data base    

    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    return db.cursor()


'''
    Add City
'''
def add_dwyl(db, github_link, hit_code, hit_n_code):
    
    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()
    
    #
    sql = "INSERT INTO DWLY_HITS (GITHUB_LINK, HIT_CODE, HIT_N_CODE, ADDED_DATE) VALUES (%s, %s, %s, now())"
    values = (github_link, hit_code, hit_n_code)

    # Use all the SQL you like
    cur.execute(sql, values)

    db.commit()

    print('Done : '+str(cur.rowcount)+" inserted") 
    
    
'''
    Update City
'''    
def update_city(db, name, state, country, id):
    
    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()
    
    #
    sql = "UPDATE CITY SET NAME = %s, STATE = %s, COUNTRY = %s WHERE ID = %s"
    values = (name, state, country, id)

    # Use all the SQL you like
    cur.execute(sql, values)

    db.commit()

    print('Done : '+str(cur.rowcount)+" updated") 


'''
    Delete City
'''    
def delete_city(db, id):
    
    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()
    
    #
    sql = "DELETE FROM CITY WHERE ID = %s"
    values = (id, )

    # Use all the SQL you like
    cur.execute(sql, values)

    db.commit()
    
    if(cur.rowcount == 0):
        raise Exception("Item Not Available to Delete")
    
    if(cur.rowcount > 1):
        raise Exception("More than one item deleted")

    print('Done : '+str(cur.rowcount)+" deleted")            


'''
    Read City
'''
def read_city(db):
    
    cur = db.cursor()
    
    # Use all the SQL you like
    cur.execute("SELECT * FROM city")

    # print all the first cell of all the rows
    counter = 0;
    for row in cur.fetchall():
        try:
            counter = counter + 1
        
            pid = str(row[0])
            name = str(row[1])
            state = str(row[2])
            country = str(row[3])
        
            print(pid + " - " +  name + " - " + state + " - "+country)
        except ValueError as error:
            print('Error', format(error))

    

def main():
    
    
    db = get_db()
    
    # C - add city
    add_dwyl(db, 'Theni', 'TA', 'India')
    
    # R - read city
    read_city(db)
    
    # U - update city
    #update_city(db, 'Thennai', 'TA', 'India', 5)
    
    # D - delete city
    try:
        delete_city(db, 10)
    except Exception as er:
        print("Error : ", format(er))
    
    # close DB
    db.close()
    

if __name__ == '__main__':
    #main()
    pass