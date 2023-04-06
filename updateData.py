from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time
import datetime
import pandas as pd
import random
# đọc file excel 
df=pd.read_excel('info.xlsx') # Enter excel file name
data_list=df.iloc[1:68,5].values.tolist()

with open("info.json", "w") as f:
    json.dump([], f)
browser=webdriver.Chrome('chromedriver.exe') #đây là địa chỉ của driver, phải đảm bảo phiên bản của trình duyệt phải là 111
browser.get('https://www.linkedin.com/home')
browser.maximize_window()
time.sleep(3)
input_username=browser.find_element(By.ID,'session_key')
input_username.send_keys ("")# enter username
input_pass= browser.find_element(By.ID,'session_password')
input_pass.send_keys("")# enter password
button= browser.find_element(By.XPATH,'//*[@id="main-content"]/section[1]/div/div/form[1]/div[2]/button').click()
time.sleep(3)
n=len(data_list)
def write_json(new_data, filename=None):
    with open(filename,'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data.append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 10)
def updateData():
    for i in range(n): 
        try: 
            browser.get(f'{data_list[i]}')
            val = random.randint(3, 8 )
            time.sleep(val)
            try:
                name= browser.find_element(By.TAG_NAME,'h1').text
            except:
                name=""
            try:
                job_type=browser.find_element(By.CLASS_NAME,'text-body-medium').text
            except:
                job_type=""
            try:
                location=browser.find_element(By.XPATH,'//*[@id="ember27"]/div[2]/div[2]/div[2]/span[1]').text
            except:
                location=""
            try:
                company=browser.find_element(By.XPATH,'//*[@id="ember27"]/div[2]/div[2]/ul/li[1]/button/span/div')
                company=company.get_attribute('textContent').replace('"', '').strip()
            except:
                company=""
            now =str(datetime.datetime.now())
            print(f"name: {name}")
            print('\n')
            write_json({
                "link":data_list[i],
                "fullname":name,
                "headline":job_type,
                "locality":location,
                "company":company,
                "dateupdate":now
            },filename='info.json')
        except:
            continue
    # convert file json to excel
    with open("info.json") as f:
        data= pd.read_json(f)
    data.to_excel('filename.xlsx',index=False)
if __name__ == '__main__': 
    updateData()

    
