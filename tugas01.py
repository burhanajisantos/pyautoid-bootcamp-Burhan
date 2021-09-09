from selenium import webdriver
driver = webdriver.Chrome(executable_path='D:\Python39\Scripts\chromedriver.exe')
link = ["https://noobtest.id","https://erzaf.com","https://orangsiber.com","https://demoqa.com","https://automatetheboringstuff.com"]
for x in link:
    driver.get(x)
    print(driver.title)
driver.minimize_window()
driver.close()