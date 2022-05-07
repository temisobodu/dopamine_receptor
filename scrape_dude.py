import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import List
import argparse

def find_download_links(driver, target: str, retries: int = 2):
    download_links = driver.find_elements_by_xpath('//a')
    dl_follow = None
    for dl_link in download_links:
        if dl_link.text == target:
            dl_follow = dl_link
    if not dl_follow and retries > 0:
        time.sleep(2)
        return find_download_links(driver, retries-1)
    else:
        return dl_follow


def scrape_dude(email: str, smiles: List) -> str:
    url = 'http://dude.docking.org/generate'
    driver = webdriver.Chrome()
    driver.get(url)

    email_field = driver.find_element_by_id('email')
    email_field.send_keys(email)

    human_test = driver.find_element_by_id('turing')
    human_test.send_keys("I am human")
    

    smiles_field = driver.find_element_by_id('smiles')
    smiles_field.send_keys(smiles)
    submit_btn = driver.find_element_by_xpath("//input[@type='submit']")
    submit_btn.click()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--email', help='Your email')
    parser.add_argument('--smiles_file', help='Your email')

