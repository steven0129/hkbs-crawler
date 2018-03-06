from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://www.bible.com/zh-TW/bible/46/EPH.2.CUNP')

divs = driver.find_elements_by_xpath("//div[@class='p']")
print(divs[0].text)
    
driver.quit()