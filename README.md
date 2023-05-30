# **Glassdoor Scraper**

This repository contains a scraper for one of the most jobs search engine ***Glassdoor**, with this scraper you can extract the jobs from this page and create some projects.

The use of data that you will extact is your resposanbility.

## **How to use this project?**

1. Clone the repository using ```git clone https://github.com/erikintech/glassdoor-scraper.git```
2. Create a virtualenv in your project folder with pip or conda, in my case I use pip. ```python -m virtualenv .venv```
3. Activate the virtualenv
4. Install selenium and pandas using ```pip install selenium pandas```
5. Download the webdriver, you can use Firefox, Chrome or your favourite browser
   * Firefox - geckodriver: [driver link](https://github.com/mozilla/geckodriver/releases)
   * Chrome - chromediver: [driver link](https://chromedriver.chromium.org/downloads)
6. Into your project folder you can create a new folder named driver, here you have to unzip your webdriver and also you should create a folder named data.
7. Review the glassdoor_scraper.py file and make the necessary changes, for example the name of the webdriver
8. Run the extract_jobs.py file  ```python extract_jobs.py```.