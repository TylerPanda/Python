import lxml.html
import time
from bs4 import BeautifulSoup
from selenium import webdriver
# regex = re.compile('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
url = 'http://www.twse.com.tw/zh/page/trading/indices/MI_5MINS_HIST.html'

browser = webdriver.Chrome()
browser.get(url)
years = browser.find_element_by_name('yy')
years_options = [x for x in years.find_elements_by_tag_name('option')]
years_values = [value.get_attribute('value') for value in years_options]
months = browser.find_element_by_name('mm')
months_options = [x for x in months.find_elements_by_tag_name('option')]
months_values = [value.get_attribute('value') for value in months_options]

for value in years_values:
    browser.find_element_by_xpath('//select/option[@value=' + str(value) +']').click()
    for value in months_values:
        browser.find_element_by_xpath('//select/option[@value=' + str(value) +']').click()
        browser.find_element_by_link_text('查詢').click()
        content = 'na'
        time.sleep(2)
        html = browser.page_source
        sp = BeautifulSoup(html, 'lxml')
        trs = sp.find_all('tr')
        for tr in trs:
            tds = tr.find_all('td', attrs = {'class' : ' dt-head-center dt-body-center'})
            print(content)
            f = open('output.text', 'a')
            f.write(str(content) + '\n')
            for td in tds:
                content = tds[0].get_text().strip(), tds[1].get_text().strip(), tds[2].get_text().strip(), tds[3].get_text().strip(), tds[4].get_text().strip()
browser.close()
