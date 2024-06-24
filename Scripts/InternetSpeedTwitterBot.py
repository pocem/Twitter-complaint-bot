import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')
NAME = os.getenv('NAME')
DOWNLOAD = os.getenv('DOWNLOAD')
UPLOAD = os.getenv('UPLOAD')
class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.email = EMAIL
        self.password = PASSWORD
        self.promised_download = int(DOWNLOAD)
        self.promised_upload = int(UPLOAD)
        self.download_speed = 0
        self.upload_speed = 0

    def get_internet_speed(self):

        self.driver.get("https://www.speedtest.net")
        try:
            cookies_button = WebDriverWait(self.driver, 50).until(
                EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
            )
            cookies_button.click()
        except NoSuchElementException:
            print("Cookies button not found on the page.")
        except Exception as e:
            print(f"An error occurred: {e}")

        try:
            go_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "start-button"))
            )
            go_button.click()
        except NoSuchElementException:
            print("Start button not found on the page.")
        except Exception as e:
            print(f"An error occurred: {e}")

        time.sleep(80)

        try:
            self.download_speed = WebDriverWait(self.driver, 80).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]'))
            ).text
            self.upload_speed = WebDriverWait(self.driver, 80).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]'))
            ).text

            print(f"Download speed: {self.download_speed} Mbps")
            print(f"Upload speed: {self.upload_speed} Mbps")
        except NoSuchElementException:
            print("Speed test results not found on the page.")
        except Exception as e:
            print(f"An error occurred in scraping internet speed: {e}")




    def tweet_at_provider(self):

        if self.download_speed < self.promised_download or self.upload_speed < self.promised_upload:

            self.driver.get("https://x.com/login=")

            try:
                cookies_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '// *[ @ id = "layers"] / div / div[3] / div / div / div / div[2] / button[1]'))
                )
                cookies_button.click()
            except NoSuchElementException:
                print("Cookies button not found on the page.")
            except Exception as e:
                print(f"An error occurred trying to accept cookies: {e}")

            try:
                login_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/a/div'))
                )
                login_button.click()
            except NoSuchElementException:
                print("Login button not found on the page.")
            except Exception as e:
                print(f"An error occurred trying to press login button: {e}")

            try:
                email_input = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'))
                )
                email_input.send_keys(EMAIL)
                email_input.send_keys(Keys.ENTER)
            except NoSuchElementException:
                print("email input not found on the page.")
            except Exception as e:
                print(f"An error occurred trying to enter email: {e}")

            try:
                name_input = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input'))
                )
                name_input.send_keys(NAME)
                name_input.send_keys(Keys.ENTER)
            except NoSuchElementException:
                print("name input not found on the page.")
            except Exception as e:
                print(f"An error occurred trying to enter name: {e}")

            try:
                password_input = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'))
                )
                password_input.send_keys(PASSWORD)
                password_input.send_keys(Keys.ENTER)
            except NoSuchElementException:
                print("Cookies button not found on the page.")
            except Exception as e:
                print(f"An error occurred trying to enter email: {e}")

            time.sleep(10)

            try:
                home_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[1]/div'))
                )
                home_button.click()
            except NoSuchElementException:
                print("Home button not found on the page.")
            except Exception as e:
                print(f"An error occurred trying to press home button: {e}")

            ###message for the internet provider###
            message = (f"Dear internet provider, you advertise your product as follows: down speed {DOWNLOAD}Mb/s and up speed {UPLOAD}Mb/s, however, what I am getting from"
             f"you is: {self.download_speed} Mbps as download speed and {self.upload_speed} Mbps as upload speed. Gimme my money back or fix the issue please and thank you."  )

            try:
                post_input = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div'))
                )
                post_input.send_keys(message)
            except NoSuchElementException:
                print("Post input not found on the page.")
            except Exception as e:
                print(f"An error occurred trying to make a twitter post: {e}")

            try:
                post_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span'))
                )
                post_button.click()
            except NoSuchElementException:
                print("Post button not found on the page.")
            except Exception as e:
                print(f"An error occurred trying to press post button: {e}")

            time.sleep(30)

            self.driver.quit()

        else:
            pass



