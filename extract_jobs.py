from glassdoor_scraper import get_jobs
import pandas as pd

#url = 'https://www.glassdoor.com/Job/united-states-machine-learning-jobs-SRCH_IL.0,13_IN1_KO14,30.htm?includeNoSalaryJobs=false'

num_jobs = int( input('Enter number of jobs to extract: ') )
url = input('Enter the base url: ')
name_file = input('Enter name of csv file: ')
df = get_jobs( url, num_jobs )
df.to_csv('./data/'+name_file)
print(df)
