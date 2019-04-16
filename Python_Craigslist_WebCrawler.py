##################################
#Final Project By: Brian Diunizio
#File Name: Python_Crawler.py
#Function: This program crawls through a New York software developer jobs page and extracts the url of the job posting, its posting date, and job title. The program then outputs these datasets to a .csv file
##################################

import requests
import pandas as pd
import csv
import re
from bs4 import BeautifulSoup

url = ("https://newyork.craigslist.org/d/software-qa-dba-etc/search/sof")

req = requests.get(url)

content = (req.content)

soup = BeautifulSoup(content,"lxml")

#print(soup.prettify)

url_list = []
for i,p in enumerate(soup.find_all('p', {'class' : 'result-info'})):
     a_tag = p.find('a')
     href = a_tag.get("href")
     url_list.append(href)

jobtitle_list = []
for i,p in enumerate(soup.find_all('p', {'class' : 'result-info'})):
     job_title = p.find('a', {'class' : 'result-title hdrlnk'}).text
     jobtitle_list.append(job_title)

postingdate_list = []
for i,p in enumerate(soup.find_all('p', {'class' : 'result-info'})):
    posting_date = p.find('time', {'class' : 'result-date'}).text
    postingdate_list.append(posting_date)

##location_list = []
##for i,p in enumerate(soup.find_all('p', {'class' : 'result-info'})): 
##    locale = p.find('span', {'class' : 'result-hood'}).text
##    location_list.append(locale)
#^^^ For the life of me I cannot figure out how to negotiate the none type data types that are found in the result-hood class. So when I attempt to grab the text out I get " Traceback: none type has no attribute 'text'. Any ideas?    

data_frame = pd.DataFrame({"URL" : url_list, "Job Title" : jobtitle_list, "Posting Date" : postingdate_list})
data_frame.to_csv("NY_dev_jobs.csv")

#print (len(postingdate_list), len(location_list), len(url_list))


    






