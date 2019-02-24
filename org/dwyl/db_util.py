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
    Add DWYL
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
    Read DWYL
'''
def read_dwyl(db):
    
    cur = db.cursor()
    
    # Use all the SQL you like
    cur.execute("SELECT * FROM DWLY_HITS")

    # print all the first cell of all the rows
    counter = 0;
    for row in cur.fetchall():
        try:
            counter = counter + 1
        
            dhid = str(row[0])
            github_link = str(row[1])
            hit_code = str(row[2])
            hit_n_code = str(row[3])
        
            #print(dhid + " - " +  github_link + " - " + hit_code + " - "+hit_n_code)

            print(github_link)
        except ValueError as error:
            print('Error', format(error))


def get_gihub_account(url):

    url = url.replace('https://github.com/', '')

    if('/' in url):
        url = url[0: url.index('/')]

    return 'https://github.com/'+url

'''
    Collect Gihub users
'''
def collect_github_users(db):
    
    cur = db.cursor()
    
    # Use all the SQL you like
    cur.execute("SELECT * FROM DWLY_HITS")

    github_user_list = []

    # print all the first cell of all the rows
    counter = 0;
    for row in cur.fetchall():
        try:
            counter = counter + 1
        
            dhid = str(row[0])
            github_link = str(row[1])
            hit_code = str(row[2])
            hit_n_code = str(row[3])
        
            #print(dhid + " - " +  github_link + " - " + hit_code + " - "+hit_n_code)

            #print(github_link)

            github_link = get_gihub_account(github_link)

            if(github_link not in github_user_list):
                github_user_list.append(github_link)

        except ValueError as error:
            print('Error', format(error))

    myfile = open("P:/test/test.txt", "a")
    for item in github_user_list:
        print(item)
        myfile.write(str(item))
        myfile.write('\n\n')

    print('Done!')

def main():
    
    
    db = get_db()
    
    # C - add city
    #add_dwyl(db, 'Theni', 'TA', 'India')
    
    # R - read city
    #read_dwyl(db)

    collect_github_users(db)
    
    # U - update city
    #update_city(db, 'Thennai', 'TA', 'India', 5)
    
    '''
    # D - delete city
    try:
        delete_city(db, 10)
    except Exception as er:
        print("Error : ", format(er))
    '''
    
    # close DB
    db.close()
    

if __name__ == '__main__':
    main()
    pass