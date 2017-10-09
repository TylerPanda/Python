import requests
from bs4 import BeautifulSoup

base_url = "https://www.yelp.com/search?find_loc=";
location = "CA";
page = 0;
while( page < 1000):
    url = base_url + location + "&start=" + str(page);
    yelp_requests = requests.get(url);
    yelp_soup = BeautifulSoup(yelp_requests.text, "html.parser");
    business = yelp_soup.findAll("div", {"class" : "biz-listing-large"});
    for biz in business:
        title = biz.findAll("a", {"class" : "biz-name js-analytics-click"})[0].text;
        first_line = "";
        second_line = "";
        try:
            address = biz.findAll("address")[0].contents
            for item in address:
                if "br" in str(item):
                    second_line += item.getText().strip(" \n\t\r");
                else:
                    first_line = item.strip(" \n\t\r");
        except:
            pass;
        # print("\n")
        try:
            phone = biz.findAll("span", {"class" : "biz-phone"})[0].getText().strip(" \n\t\r");
        except:
            phone = None;
        information = "{title}\n{address}\n{phone}\n".format(title = title, address = first_line + second_line, phone = phone);
        print(information);
    page += 10;
    # print(title);
    # address = biz.findAll("address")[0].getText().replace(" ", "");
    # print(address);
    # phone = biz.findAll("span", {"class" : "biz-phone"})[0].getText().replace(" ", "");
    # phone = phone.replace("\n", "");
    # print(phone);
    # information = "{title}{address}{phone}\n".format(title = title, address = address, phone = phone);
    # print(information);
