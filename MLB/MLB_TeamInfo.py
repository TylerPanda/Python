import requests;
from bs4 import BeautifulSoup;
from datetime import date;

base_url = 'https://www.baseball-reference.com/leagues/MLB/';
# MLB_first_year = 1903;
# current_year = date.today().year;
MLB_first_year = 2016;
current_year = date.today().year;

i = 0;
while MLB_first_year <= current_year:
    url = base_url + str(MLB_first_year) + '.shtml';
    MLB_requesets = requests.get(url);
    MLB_soup = BeautifulSoup(MLB_requesets.text, 'html.parser');
    Batting =  MLB_soup.find('div', {'id' : 'all_teams_standard_batting'});
    Batting_title = Batting.findAll('h2')[0].text;
    thead = Batting.find('thead').findAll('tr')[0].text.replace('\n',"  ");
    tbody = Batting.find('tbody');
    trs = tbody.findAll('tr');
    tr_len = len(trs);
    # print(tr_len);
    # print(trs);
    for tr in trs:
        print(tr.text)
        print(i)
        i += 1;
        # ths = tr.find('th');
        # tds = tr.find('td');
        # for th in ths:
        #     print(th);
    MLB_first_year += 1
    # print(tbody);
    # print(thead + '\n');
    # MLB_first_year += 1
    # Pitching =  MLB_soup.find('div', {'id' : 'all_teams_standard_pitching'}).findAll('h2')[0].text;
    # MLB_first_year += 1
    # print(str(current_year) + "\t" + Batting_title);
    # print(str(current_year) + "\t" + Pitching);
