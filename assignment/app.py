from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import os
import csv

def write_csv(csv_path,scraped_dict,header):

    f = csv.DictWriter(open(csv_path,'a'),fieldnames=header)

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.ec2pricing.net/")
driver.maximize_window()

totalprice=[]

for i in range(1,10):
    instance_type= driver.find_element(By.XPATH,f'/html/body/div/div/table/tbody/tr[{i}]/td[1]').text

    totalprice.append(instance_type)
   
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(totalprice)
print(instance_type)