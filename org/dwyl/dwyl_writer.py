#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
author:
    raja

source: (if any)
   https://stackoverflow.com/questions/3277503/in-python-how-do-i-read-a-file-line-by-line-into-a-list 
'''

import requests
import db_util as dbu
import MySQLdb

def print_file(filename):

    db = dbu.get_db()

    with open(filename) as f:
        content = f.readlines()
        
    counter = 0

    # you may also want to remove whitespace characters like `\n` at the end of each line
    for x in content:

        counter = counter + 1

        if(len(x.strip()) == 0):
            continue

        items = x.split(" ")

        #if(counter > 5):
        #    break

        #print(len(items))

        if(len(items) != 5):
            continue

        g_link = 'https://github.com' + items[2]       
        #print(g_link)
        hit_n_code = items[3].strip()
        hit_code = items[4].strip()
        

        print('----------')
        print(g_link)
        print(hit_code)
        print(hit_n_code)

        # db, github_link, hit_code, hit_n_code
        try:
            dbu.add_dwyl(db, g_link, hit_code, hit_n_code)
        except MySQLdb.IntegrityError:
            print('Duplicate Entry, so skipping')
        except MySQLdb.OperationalError:
            print('OperationalError error')            
        

        #print(x)    
    
    print('\n\nDone!')

def is_page_alive(url):
    r = requests.get(url)
    #print(r.status_code)

    if(r.status_code == 200):
        return True
    else:
        return False    
            
if __name__ == '__main__':    
    print_file("public_projects_from_hits_dwyl.txt")
    #dbu.test()
