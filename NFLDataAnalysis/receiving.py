import pandas as pd
from functions import get_site, get_names, get_stats, get_headers, setup_for_pandas
import csv

RECEIVING_STATS_LINK = r"https://www.espn.com/nfl/stats/player/_/stat/receiving/table/receiving/sort/receivingYards/dir/desc"


bs = get_site(RECEIVING_STATS_LINK)
names = get_names(bs)
headers = get_headers(bs)
num_of_headers = int(len(headers) - 1)
stats = get_stats(bs, num_of_headers, names)

with open("data/receiving.csv", "w") as file:
    writer = csv.writer(file, lineterminator = '\n')
    writer.writerow(headers)
    writer.writerows(stats)

# organized_info = setup_for_pandas(names_list=names, header_list=headers, stats_list=stats)
# receiving_df = pd.DataFrame(organized_info, columns=headers)

