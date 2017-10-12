import requests;
from bs4 import BeautifulSoup;
from datetime import date;

base_url = 'https://www.baseball-reference.com/leagues/MLB/';
# MLB_first_year = 1903;
# current_year = date.today().year;
MLB_first_year = 2016;
current_year = date.today().year;


while MLB_first_year <= current_year:
    url = base_url + str(current_year) + '.shtml';
    MLB_requesets = requests.get(url);
    MLB_soup = BeautifulSoup(MLB_requesets.text, 'html.parser');
    Batting =  MLB_soup.find('div', {'id' : 'all_teams_standard_batting'});
    Batting_title = Batting.findAll('h2')[0].text;
    thead = Batting.find('thead').findAll('tr')[0].text.replace('\n',"  ");
    tbody = Batting.find('tbody').findAll('td')[0].text
    print(tbody);
    # print(thead + '\n');
    MLB_first_year += 1
    # Pitching =  MLB_soup.find('div', {'id' : 'all_teams_standard_pitching'}).findAll('h2')[0].text;
    # MLB_first_year += 1
    # print(str(current_year) + "\t" + Batting_title);
    # print(str(current_year) + "\t" + Pitching);
