#import
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#setting up
driver = webdriver.Chrome()

driver.get('https://www.linkedin.com')
time.sleep(3)

linkedin_link = driver.find_element("xpath", "/html/body/main[@id='main-content']/section[@class='section min-h-[560px] flex-nowrap pt-[40px] babybear:flex-col babybear:min-h-[0] babybear:px-mobile-container-padding babybear:pt-[24px]']/div[@class='self-start relative flex-shrink-0 w-[55%] pr-[42px] babybear:w-full babybear:pr-[0px]']/a[@class='sign-in-form__join-cta btn-md btn-secondary w-column babybear:w-full block mb-3']")
linkedin_link.click()
time.sleep(3)

#verify page
assert "Sign Up | LinkedIn" in driver.title

#Fill Registration
email_address = driver.find_element("name","email-address")
password = driver.find_element("name","password")
email_address.send_keys("peterobi76768@gmail.com")
password.send_keys("obiisaboy")
time.sleep(3)

#submit
email_submit = driver.find_element("id","join-form-submit")
email_submit.click()
time.sleep(3)

firstname = driver.find_element("id","first-name")
lastname = driver.find_element("id","last-name")
firstname.send_keys("Peter")
lastname.send_keys("Obi")

name_submit = driver.find_element("id","join-form-submit")
name_submit.click()
time.sleep(3)

driver.close()






