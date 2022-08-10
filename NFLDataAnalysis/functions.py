from email import header
from turtle import pen
from bs4 import BeautifulSoup
import requests


def get_site(input_link):
    req = requests.get(input_link)
    req_text = req.text
    soup = BeautifulSoup(req_text, 'html.parser')
    return soup


def get_names(bs):
    table = bs.find("table", {"class": "Table"})
    names_list = []

    for row in table.find_all("tr"):
        row_text = row.text
        if row_text == " ":
            pass
        elif row_text == "RKName":
            pass
        else:
            names_list.append(row_text)
    return names_list

def get_headers(bs):
    headers = bs.find_all("thead", {"class": "Table__THEAD"})
    headers_two = headers[1]
    header_list = ["Name"]
    for item in headers_two.find_all("th"):
        header_list.append(item.text)
    return header_list


def get_stats(bs, num_of_headers, names):
    tables = bs.find_all("table", {"class" : "Table"})
    stats_table = tables[1]
    stats_list = []
    placeholder_list = []
    for data in stats_table.find_all("td"):
        data_text = data.text
        if "," in data_text:
            cleaned_data_text = data_text.replace(",", "")
        else:
            cleaned_data_text = data_text

        if cleaned_data_text == "QB" or cleaned_data_text == "TE" or cleaned_data_text == "WR" or cleaned_data_text == "RB":
            placeholder_list.append(str(cleaned_data_text))
        else:
            placeholder_list.append(float(cleaned_data_text))
        
        # Appending stats list with an individuals 
        if len(placeholder_list) % (num_of_headers - 1) == 0:
            print(len(placeholder_list))
            print(num_of_headers)
            # Append the name to the stats list first
            placeholder_list.insert(0, names[int(len(stats_list))])

            # Append the row to the stats list
            stats_list.append(placeholder_list)

            # Clear placeholder
            placeholder_list = []

    return stats_list


def setup_for_pandas(names_list, header_list, stats_list):
    player_data = []
    master_data = []
    for t in range(1, len(names_list)):
        player_data.append(names_list[t])
        counter = (((t - 1) * (len(header_list) - 1)))
        if t == 1:
            for i in range(0, len(header_list) - 1):
                player_data.append((stats_list[i]))
        else:
            for i in range(0, len(header_list) - 1):
                player_data.append((stats_list[i + counter]))

        master_data.append(player_data)
        player_data = []
    return master_data