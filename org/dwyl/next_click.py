#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 

Course work: 

@author: raja

Source:
    
'''

# Import necessary modules
from selenium import webdriver 
import time

def startpy():

    url = 'https://github.com/fabiopagoti?tab=followers'
    
    driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')

    user_counter = 0
    driver.get(url)    

    time.sleep(7)

    user_list = []

    counter = 0
    while(counter < 3):

        links = driver.find_elements_by_css_selector('a[data-hovercard-type=user]')

        for link in links:
            #print(link)
            user_link = link.get_attribute("href")   

            if(user_link in user_list):
                continue

            user_list.append(user_link)

            user_counter += 1    
            #print(user_link)                    

        print('collected : ', user_counter)

        # div.paginate-container div.pagination a
        buttons = driver.find_elements_by_css_selector('div.paginate-container div.pagination a')

        for button in buttons:
            button_text = button.text

            print(button_text)

        #next_button.click()
    
        counter += 1

    #print(next_button)

if __name__ == '__main__':
    startpy()