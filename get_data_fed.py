#Imports
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.webdriver.chrome.options import Options
import pandas as pd
#Objetivo: get effective rate from the FED.
def dowload_data_fed():

    #=== HTML ===#

    # Configuring Chrome options to run in "headless" mode (no browser UI)
    chrome_options = Options()
    chrome_options.add_argument('--headless')

    #Open Google Chrome with a URL and wait 10 seconds.
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://fred.stlouisfed.org/series/FEDFUNDS')
    wait = WebDriverWait(driver, 10)

    #Get button "dowload"
    button = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div/div/button")))

    #Click button "dowload" to display the dowload options
    button.click()

    #Get option "csv download"
    a_csv = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div/div/ul/li[1]/a")))

    #get "href" from "<a>CSV(data)</a>"
    href = a_csv.get_attribute('href')

    #=== DOWNLOAD DATA ===#

    #get currect folder
    current_folder = os.path.dirname(os.path.abspath(__file__))
    
    #name file with format
    nombre_archivo = 'fed-funds.csv'

    #With request download file
    response = requests.get(href, verify=False)
    save_folder = os.path.join(current_folder, nombre_archivo)

    with open(save_folder, 'wb') as file:
        file.write(response.content)


    
    #=== RETURN DATA ===#

    #use save path
    df = pd.read_csv(save_folder)

    return df


