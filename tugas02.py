from selenium import webdriver
driver = webdriver.Chrome(executable_path='D:\Python39\Scripts\chromedriver.exe')

data_details = [
    ["Rudi","Tabuti","Rudi34@gmail.com","12","2000000","kartun"],
    ["Patrick","Star","StarPatrick@yahoo.com","18","3000000","kartun"],
    ["Monkey","Luffy","monckey@gmail.com","17","30000000","anime"]
    ]
driver.get("https://demoqa.com/webtables")
for registrasion_form in data_details:
    driver.find_element_by_id('addNewRecordButton').click()
    driver.find_element_by_id('firstName').send_keys(registrasion_form[0])
    driver.find_element_by_id('lastName').send_keys(registrasion_form[1])
    driver.find_element_by_id('userEmail').send_keys(registrasion_form[2])
    driver.find_element_by_id('age').send_keys(registrasion_form[3])
    driver.find_element_by_id('salary').send_keys(registrasion_form[4])
    driver.find_element_by_id('department').send_keys(registrasion_form[5])
    driver.find_element_by_id('submit').click()