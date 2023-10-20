from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from mailjet_rest import Client
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


import time
import os

api_key = 'f1e40cee66621dca7307b4acea51a91c'
api_secret = '5766e5da4a91306e3b8a7e9faa64da31'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-setuid-sandbox")


def testDemoForm():
    global formNumber, pageUrl
    try:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=chrome_options)
        pageUrl = "https://www.tcpsoftware.com/demo";
        driver.get(pageUrl)
        time.sleep(1)

        formElement = driver.find_element(By.CLASS_NAME, "mktoForm")
        formNumber = formElement.get_attribute("id")

        firstNameField = driver.find_element(By.ID, 'FirstName')
        firstNameField.send_keys('Selenuim')

        lastNameField = driver.find_element(By.ID, 'LastName')
        lastNameField.send_keys('Test')

        emailField = driver.find_element(By.ID, 'Email')
        emailField.send_keys('error')

        orgField = driver.find_element(By.ID, 'Company')
        orgField.send_keys('TCPSoftware')

        selectCountryField = Select(driver.find_element(By.ID, 'Country'))
        selectCountryField.select_by_visible_text('United States*')

        selectStateField = Select(driver.find_element(By.ID, 'State'))
        selectStateField.select_by_visible_text('Florida')

        optInField = driver.find_element(By.ID, 'optInNewsletter')
        optInField.click()

        optInField = driver.find_element(By.ID, 'mktoOptIn')
        optInField.click()

        optInField.location_once_scrolled_into_view

        time.sleep(3)

        submitButton = driver.find_element(By.ID, 'alt-btn')
        submitButton.click()

        time.sleep(3)

        get_url = driver.current_url
        if str(get_url) == "https://go.tcpsoftware.com/TYPs_Thank-You-Page--Get-a-Demo.html":
            print("The current url is:" + str(get_url))
        else:
            # sendMail("Error submitting form on: \n" + "Page Url: " + pageUrl + "\n Form Number: " + formNumber)
            print("Redirection did not happen")

    except NoSuchElementException as ex:
        # sendMail("Error submitting form on: \n" + "Page Url: " + pageUrl + "\n Form Number: " + formNumber + "\n Exception: " + ex.msg)
        print(ex.msg)

    finally:
        driver.quit()


def testOtherForm():
    try:
        driver = webdriver.Remote(
            command_executor="http://uitest-chrome-1:4444",
            options=chrome_options
        )
        driver.get("https://www.tcpsoftware.com/demo")
        time.sleep(1)

        firstNameField = driver.find_element(By.ID, 'FirstName')
        firstNameField.send_keys('Selenuim')

        lastNameField = driver.find_element(By.ID, 'LastName')
        lastNameField.send_keys('Test')

        emailField = driver.find_element(By.ID, 'Email')
        emailField.send_keys('ajibran2@tcpsoftware.com')

        orgField = driver.find_element(By.ID, 'Company')
        orgField.send_keys('TCPSoftware')

        selectCountryField = Select(driver.find_element(By.ID, 'Country'))
        selectCountryField.select_by_visible_text('United States*')

        selectStateField = Select(driver.find_element(By.ID, 'State'))
        selectStateField.select_by_visible_text('Florida')

        optInField = driver.find_element(By.ID, 'optInNewsletter')
        optInField.click()

        optInField = driver.find_element(By.ID, 'mktoOptIn')
        optInField.click()

        optInField.location_once_scrolled_into_view

        time.sleep(3)

        optInField = driver.find_element(By.ID, 'alt-btn')
        optInField.click()

        time.sleep(3)

        get_url = driver.current_url
        if str(get_url) == "https://go.tcpsoftware.com/TYPs_Thank-You-Page--Get-a-Demo.html":
            print("The current url is:" + str(get_url))
        else:
            print("Redirection did not happen")

    except NoSuchElementException as ex:
        print(ex.msg)

    finally:
        driver.quit()


def sendMail(msg):
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
        'Messages': [
            {
                "From": {
                    "Email": "ajibran2@tcpsoftware.com",
                    "Name": "Selenium Automated Test Result "
                },
                "To": [
                    {
                        "Email": "ajibran2@tcpsoftware.com",
                        "Name": "Ali Jibran"
                    },
                    {
                        "Email": "wmubashir@tcpsoftware.com",
                        "Name": "Wajahat Mubashir"
                    },
                    {
                        "Email": "lmarini@tcpsoftware.com",
                        "Name": "Luis Marini"
                    },
                    {
                        "Email": "mmanojlovic@tcpsoftware.com",
                        "Name": "Milan Manojlovic"
                    },
                    {
                        "Email": "emthurston@tcpsoftware.com",
                        "Name": "Emily Thurston"
                    }
                ],
                "Subject": "Selenium Automated Test Error",
                "TextPart": msg,
            }
        ]
    }
    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())


if __name__ == "__main__":
    testDemoForm()
#    time.sleep(1)
#    testOtherForm()
