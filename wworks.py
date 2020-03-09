from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
import time
import getpass

emailAddress = input("UWaterloo email: ")
passwordUW = getpass.getpass()

driver = webdriver.Chrome()

driver.get('https://waterlooworks.uwaterloo.ca/home.htm')

loginButton = driver.find_element_by_class_name('btn--landing')
loginButton.click()

emailInput = driver.find_element_by_name('UserName')
emailInput.send_keys(emailAddress)
emailInput.send_keys(Keys.RETURN)

passwordInput = driver.find_element_by_name('Password')
passwordInput.send_keys(passwordUW)
passwordInput.send_keys(Keys.RETURN)

#searchPostings = driver.find_element_by_xpath("//*[@class='orbis-posting-actions']//*[text()='Search Postings']")
#searchPostings = driver.find_element_by_xpath("//*[contains(@href, '#searchPostings')]")
time.sleep(2)
searchPostings = driver.find_element_by_link_text('Hire Waterloo Co-op')
searchPostings.click()

time.sleep(4)
shortlist = driver.find_element_by_link_text('Shortlist')
shortlist.click()

#time.sleep(2)
#sortDeadline = driver.find_element_by_link_text('App Deadline')
#sortDeadline.click()

#nextPage = driver.find_element_by_xpath('//a[contains("loadPostingTable", "2")]')
#nextPage.click()

table = driver.find_element_by_id('postingsTable')
jobNumber = 1
appClosed = 0

def rows():
    try:
        return table.find_elements_by_xpath('.//tr')
    except StaleElementReferenceException:
        print('Exception occurred in rows()')
        pass

def cols():
    empties = []
    try:
        return row.find_elements_by_xpath('.//td')
    except StaleElementReferenceException:
        print('Exception occurred in cols()')
        return empties
        pass

for row in rows():
    try:
        print(row.text)
    except StaleElementReferenceException:
        row = table.find_elements_by_xpath('.//tr')
        print(row.text)
        print('Exception occurred in for loop')
    for td in cols():
        #print(type(td.text))
        if td.text == 'Applied':
            print('^ Unshortlisted ^')
            unshortlist = row.find_element_by_link_text('Unshortlist')
            unshortlist.click()
            appClosed += 1
            time.sleep(3)
            break
    #date_time_str = row.find_element_by_link_text('Jan')
    #print(date_time_str)
    jobNumber += 1
    
print('There are ', jobNumber, ' shortlisted jobs')
print('There are ', appClosed, ' unnecessary jobs')

time.sleep(5)

#driver.close()
