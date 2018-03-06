from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://www.bible.com/zh-TW/bible/46/EPH.2.CUNP')

target=driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div/div/div/div[3]/span[2]/span[3]/span')
print(target.text)

driver.quit()