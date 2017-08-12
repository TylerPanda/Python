import requests
from selenium import webdriver
from bs4 import BeautifulSoup


# regex = re.compile('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
url = 'http://www.twse.com.tw/zh/page/trading/indices/MI_5MINS_HIST.html'

browser = webdriver.Chrome()
browser.get(url)
# browser.maximize_window()
# html = requests.get(url)
# html.encoding = 'utf-8'
# sp = BeautifulSoup(html.text, 'html.parser')

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

        # <a href="#" class="button search">查詢</a>

browser.close()


# for value in options:
#     values = [value.get_attribute("value")]


# for value in browser.find_element_by_tag_name('option'):
#     browser.find_element_by_xpath('//select/option[@value='+ str(value) +']').click()
#     print(value)

# browser.find_element_by_id('d1').click()

# sp = BeautifulSoup(html.text, 'html.parser')
#
# table = sp.find('table')
# trs = table.find_all('tr')
# print(trs)

# browser = webdriver.Chrome()
# browser.get('https://www.google.com.tw/')
