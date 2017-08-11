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

select_box = browser.find_element_by_name('yy')
options = [ x for x in select_box.find_elements_by_tag_name('option')]
values = [value.get_attribute("value") for value in options]

for value in values:
    browser.find_element_by_xpath('//select/option[@value=' + str(value) +']').click()

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
