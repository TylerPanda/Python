import requests;
from bs4 import BeautifulSoup;
from datetime import date;

base_url = 'https://www.baseball-reference.com/leagues/MLB/';
MLB_first_year = 1903;
current_year = date.today().year;
# MLB_first_year = 2017;
# current_year = date.today().year;

TeamData = [];
while MLB_first_year <= current_year:
    url = base_url + str(MLB_first_year) + '.shtml';
    MLB_requesets = requests.get(url);
    MLB_soup = BeautifulSoup(MLB_requesets.text, 'html.parser');

    Batting =  MLB_soup.find('div', {'id' : 'all_teams_standard_batting'});
    Batting_title = Batting.findAll('h2')[0].text;
    thead = Batting.find('thead').findAll('tr')[0].text.replace('\n',"  ");
    tbody = Batting.find('tbody');
    trs = tbody.findAll('tr');
    for tr in trs:
        TeamData.append(MLB_first_year);
        TeamName = tr.findAll('th')[0].text;
        tds = tr.findAll('td');
        TeamData.append(TeamName);
        for i in range(0, len(tds)):
            TeamData.append(tds[i].text);
        print(TeamData);
        TeamData = [];
    MLB_first_year += 1
