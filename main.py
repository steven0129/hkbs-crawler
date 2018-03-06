from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from tqdm import tqdm

options = Options()
options.add_argument('--headless')

books = ['GEN','EXO','LEV','NUM','DEU','JOS','JUG','RUT','1SA','2SA','1KI','2KI','1CH','2CH','EZR','NEH','EST','JOB','PSM','PRO','ECC','SON','ISA','JER','LAM','EZE','DAN','HOS','JOE','AMO','OBA','JON','MIC','NAH','HAB','ZEP','HAG','ZEC','MAL']
driver = webdriver.Firefox(firefox_options=options, executable_path='./geckodriver')

for book in tqdm(books):
    tqdm.write('處理中經卷:' + book)

    for i in tqdm(range(16)): # 章數
        driver.get('https://www.bible.com/zh-TW/bible/46/'+ book +'.' + str(i+1) + '.CUNP')
        divs = driver.find_elements_by_xpath("//div[@class='p']")

        for div in divs:
            verses = div.find_elements_by_class_name('verse')
            for verse in tqdm(verses): # 節數
                spans = verse.find_elements_by_class_name('add')
                for span in spans: # 虛點點文字
                    tqdm.write(verse.get_attribute('class') + ', ' + span.text)

driver.quit()