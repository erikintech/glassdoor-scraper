from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import numpy as np
import pandas as pd
import time

def get_jobs(url, num_jobs):
	driver = webdriver.Firefox( executable_path="./driver/geckodriver" )
	driver.get(url)
	jobs = []

	while len(jobs) < num_jobs:
		time.sleep(10)
		job_btns = driver.find_elements(By.CLASS_NAME, 'react-job-listing' )
		for job_btn in job_btns:
			if len(jobs) >= num_jobs:
				break
			
			try:
				wait = WebDriverWait(driver, 15)
				element = wait.until(
	                EC.element_to_be_clickable((By.CLASS_NAME, 'modal_closeIcon'))
	            )
				if element:
					element.click()
			except TimeoutException:
				pass

			job_btn.click()  #You might 

			try:
				wait = WebDriverWait(driver, 15)
				element = wait.until(
	                EC.element_to_be_clickable((By.CLASS_NAME, 'modal_closeIcon'))
	            )
				if element:
					element.click()
			except TimeoutException:
				pass
			try:
				job_title = driver.find_element(By.XPATH, '//div[@data-test="jobTitle"]').text
				company = driver.find_element(By.XPATH,'//div[@data-test="employerName"]').text      
			except:
				job_title = None
				company = None
			
			try:
				location = driver.find_element(
	                By.XPATH, '//div[@data-test="location"]'
	            ).text
			except:
				location = None
			
			try:
				salary = driver.find_element(
	                By.XPATH, '//span[@data-test="detailSalary" and text()]'
	            ).text
			except:
				salary = None
	        
			try:
				description = driver.find_element(By.XPATH, "//div[@class='jobDescriptionContent desc']").text
			except:
				description = None
			
			try:
				average_salary = driver.find_element(By.XPATH, "//div[@class='salaryTab tabSection p-std']//div[2]//div[text()]").text
			except:
				average_salary = None
	        
	        # Company data
			try:
				driver.find_element(By.XPATH, '//*[@id="EmpBasicInfo"]')
				try:
					size = driver.find_element(By.XPATH, "//div[@id='EmpBasicInfo']//div//div//div[1]//span[2][text()]").text
				except:
					size = None

				try:
					founded = driver.find_element(By.XPATH, "//div[@id='EmpBasicInfo']//div//div//div[2]//span[2][text()]"  ).text
				except:
					founded = None

				try:
					company_type = driver.find_element(By.XPATH, "//div[@id='EmpBasicInfo']//div//div//div[3]//span[2][text()]" ).text
				except:
					company_type = None
				
				try:
					industry = driver.find_element(By.XPATH, "//div[@id='EmpBasicInfo']//div//div//div[4]//span[2][text()]").text
				except:
					industry = None

				try:
					sector = driver.find_element(By.XPATH, "//div[@id='EmpBasicInfo']//div//div//div[5]//span[2][text()]").text
				except:
					sector = None
				
				try:
					revenue = driver.find_element(
	                    By.XPATH, "//div[@id='EmpBasicInfo']//div//div//div[6]//span[2][text()]" ).text
				except:
					revenue = None
			
			except:
				size = None
				industry = None
				company_type = None
				sector = None
				founded = None
				revenue = None
			try:
				driver.find_element( By.XPATH, '//*[@id="JDCol"]/div/article/div/div[2]/div[1]/div[4]/div' )

				try:
					rating = driver.find_element(
	                    By.XPATH, '//*[@id="employerStats"]/div[1]/div[1]'
	                ).text
				except:
					rating = None
			except:
				rating = None

			jobs.append( {
	            'Job Title': job_title,
	            'Location': location,
	            'Salary': salary,
	            'AverageSalary': average_salary,
	            'Description': description,
	            'Company': company,
	            'CompanyType': company_type,
	            'Sector': sector,
	            'Founded': founded,
	            'Revenue': revenue,
	            'Rating': rating
	        } )

		try:
			driver.find_element(
	            By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/article/div[2]/div/div[1]/button[7]/span'
	        ).click()
		except NoSuchElementException:
			print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_jobs, len(jobs)))
			break
	
	return pd.DataFrame(jobs)
	