from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import random
from tqdm import tqdm

options = Options()
options.add_argument('--headless')

oldBooks = ['GEN','EXO','LEV','NUM','DEU','JOS','JUG','RUT','1SA','2SA','1KI','2KI','1CH','2CH','EZR','NEH','EST','JOB','PSM','PRO','ECC','SON','ISA','JER','LAM','EZE','DAN','HOS','JOE','AMO','OBA','JON','MIC','NAH','HAB','ZEP','HAG','ZEC','MAL']
newBooks = ['MAT','MAK','LUK','JHN','ACT','ROM','1CO','2CO','GAL','EPH','PHL','COL','1TS','2TS','1TI','2TI','TIT','PHM','HEB','JAS','1PE','2PE','1JN','2JN','3JN','JUD','REV']
books = oldBooks + newBooks

driver = webdriver.Firefox(firefox_options=options, executable_path='./geckodriver')

for book in tqdm(books):
    
    driver.get('https://www.bible.com/zh-TW/bible/46/' + book)
    chapterList = driver.find_element_by_xpath("//ul[@class='chapter-list']").find_elements_by_tag_name('a')
    tqdm.write('處理中經卷: %s, 本卷書總章數: %d' % (book, len(chapterList)))

    for i in tqdm(range(len(chapterList))): # 章數
        driver.get('https://www.bible.com/zh-TW/bible/46/'+ book +'.' + str(i+1) + '.CUNP')
        divs = driver.find_elements_by_xpath("//div[@class='p']")

        for div in tqdm(divs):
            verses = div.find_elements_by_class_name('verse')
            for verse in verses: # 節數
                spans = verse.find_elements_by_class_name('add')
                for span in spans: # 虛點點文字
                    pass
                    # tqdm.write(verse.get_attribute('class') + ', ' + span.text)

driver.quit()