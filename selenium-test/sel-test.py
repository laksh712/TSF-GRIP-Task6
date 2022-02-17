#importing required libraries

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#choosing chrome as a webdriver
driver = webdriver.Chrome(r"C:\Users\Uday\TSF-GRIP-TASK6-selenium-test\Browsers\chromedriver.exe")

#opening browser window with sparks foundation website
driver.get("https://www.thesparksfoundationsingapore.org/")

# Page 1 test 1 : checking weather navbar exist or not
print("Test 1 running...")
try:
    navbar = driver.find_element(By.TAG_NAME, "nav").is_displayed()
    print("Test results: The Navbar is present in www.thesparksfoundationsingapore.org")
except:
    print("Test results: The navbar is not present in www.thesparksfoundationsingapore.org")
print("Test case no. 1 successfully completed")
time.sleep(3)


# Page 1 test 2 : checking weather footer exist or not
print("Test 2 running...")
try:
    navbar = driver.find_element(By.TAG_NAME, "footer").is_displayed()
    print("Test results: The Footer tag is present in www.thesparksfoundationsingapore.org")
except:
    print("Test results: The Footer tag is not present in www.thesparksfoundationsingapore.org")
print("Test case no. 2 successfully completed")
time.sleep(3)


# Page 1 test 3 : checking weather how many times "The Sparks Foundation" is repeated
print("Test 3 running...")
size = driver.find_elements(By.XPATH, '//*[text()="The Sparks Foundation"]')
print("Test results: The text 'The Sparks Foundation' is repeated '", len(size), "' times")
try:
    size = driver.find_elements(By.XPATH, '//*[text()="The Sparks Foundation"]')
    print("Test results: The text 'The Sparks Foundation' is repeated '", len(size), "' times")
except:
    print("Test results: The text 'The Sparks Foundation' is not repeated")
print("Test case no. 3 successfully completed")
time.sleep(3)


# Page 2 test 4 : navigating to about us / Mission and Vision Statement page
print("Test 4 running...")
try:
    button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/a')
    button.click()
    print("Test results: success fully navigated to www.thesparksfoundationsingapore.org/about/vision-mission-and-values/ page")
except:
    print("Test results: button not found")
print("Test case no. 4 successfully completed")
time.sleep(3)


# Page 2 test 5 : checking weather logo exist or not
print("Test 5 running...")
try:
    logo = driver.find_element(By.XPATH, '//*[@id="home"]/div/div[1]/h1/a/img').is_displayed()
    print("Test results: Logo is Present in /about/vision-mission-and-values/ page")
except:
    print("Test results: Logo not found")
print("Test case no. 5 successfully completed")
time.sleep(3)
driver.back()


# Page 3 test 6 : navigating to /join-us/why-join-us/ page
print("Test 6 running...")
try:
    button = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/a')
    button.click()
    print("Test results: Successfully navigated to https://www.thesparksfoundationsingapore.org/join-us/why-join-us/ Page")
except:
    print("Test results: Page not found")
print("Test case no. 6 successfully completed")
time.sleep(3)


# Page 3 test 7 : testing weather h5 elements are present on the page or not
print("Test 7 running...")
try:
    driver.find_element(By.TAG_NAME, 'h5')
    print("Test results: h5 elements are present on the page")
except:
    print("Test results: No h5 elements are present on the page")
print("Test case no. 7 successfully completed")
time.sleep(3)
driver.back()


# Page 4 test 8 : navigating to /join-us/internship-positions/ and checking wheather images present?
print("Test 8 running...")
try:
    driver.get("https://www.thesparksfoundationsingapore.org/join-us/internship-positions/")
    print("Test results: successfully navigated to https://www.thesparksfoundationsingapore.org/join-us/internship-positions/")
    try:
        driver.find_element(By.TAG_NAME,"img")
        print("Test results: images exists")
    except:
        print("Test results: images not found")
except:
    print("Test results: Page not found")
print("Test case no. 8 successfully completed")
time.sleep(3)
driver.back()


# Page 5 test 9 : navigating to /join-us/internship-positions/ and checking wheather images present?
print("Test 9 running...")
try:
    driver.get("https://www.thesparksfoundationsingapore.org/contact-us/")
    print("Test results: successfully navigated to https://www.thesparksfoundationsingapore.org/contact-us/")
    try:
        driver.find_element(By.TAG_NAME,"span")
        print("Test results: Span tag exists")
    except:
        print("Test results: Span tag not found")
except:
    print("Test results: page not found")
print("Test case no. 9 successfully completed")
time.sleep(3)


# Page 6 test 10 : checking weather the page have a iframe tag
print("Test 10 running...")
try:
    driver.find_element(By.TAG_NAME, "iframe")
    print("Test results: iframe tag exist in the page")
except:
    print("Test results: iframe tag not found")
print("Test case no. 10 successfully completed")
time.sleep(3)



time.sleep(5)
driver.close()