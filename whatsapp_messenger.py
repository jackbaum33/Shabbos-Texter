import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDWait
from selenium.common.exceptions import TimeoutException


class WhatsappMessenger():
    def __init__(self):
        self.driver = None
        try:
            self.options = Options()
            self.options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
            self.options.add_experimental_option("useAutomationExtension", False)


        except Exception as e:
            print("Error setting up options")

        try:
            self.driver = webdriver.Chrome(options=self.options)
            
        except Exception as e:
            print("Error creating webdriver instance")

        self.url = 'https://web.whatsapp.com/'
        self.driver.get("https://web.whatsapp.com")




    def wait_for_qr_scan(self):
        """ waits until the whatsapp QR code to login is visible, and scans it to sync 
            the instance of whatsapp on chrome with the user's credentials
        """
        try:
            WDWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[2]'))
        )
        except TimeoutException:
            print("TimeoutException: QR code not scanned in time or WhatsApp Web not loaded properly.")
            self.driver.quit()
    
    def send_text(self, body: str = None, name: str = None, phone_number: str = None, **kwargs) -> None: 
        time.sleep(1)
        try:
            new_message_xpath = '//div[@title="New chat"]'
            WDWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, new_message_xpath))
            ).click()
        except TimeoutException:
            print("Error: New chat button not found.")
            return

        try:
            search_box_xpath ='//*[@id="app"]/div/div[3]/div/div[2]/div[1]/span/div/span/div/div[1]/div[2]/div[2]/div/div/p'
            search_box = WDWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, search_box_xpath))
            )
            search_box.clear()
            self.driver.execute_script("arguments[0].focus();", search_box)
            time.sleep(1)
            for char in phone_number:
                search_box.send_keys(char)
                time.sleep(0.08)
            #time.sleep(2)
        except TimeoutException:
            print("Error: Search box not found or not interactable.")
            return
        time.sleep(2)
        
        try:
            input_box_xpath = '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p'
            input_box = WDWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, input_box_xpath))
            )
            self.driver.execute_script("arguments[0].focus();", input_box)
            input_box.clear()
            input_box.send_keys(body)
            input_box.send_keys(Keys.ENTER)
        except TimeoutException:
            print(f"Error: Could not send message to {name}.")
            return