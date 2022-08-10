from cgi import print_arguments
import pandas as pd
from functions import get_site, get_names, get_stats, get_headers, setup_for_pandas
import csv

RUSHING_STATS_LINK = "https://www.espn.com/nfl/stats/player/_/stat/rushing/table/rushing/sort/rushingYards/dir/desc"


bs = get_site(input_link=RUSHING_STATS_LINK)
names = get_names(bs)
headers = get_headers(bs)
print(headers)
num_of_headers = int(len(headers))
print(num_of_headers)
stats = get_stats(bs, num_of_headers, names)
# Write data to csv
with open("data/rushing.csv", "w") as file:
    writer = csv.writer(file, lineterminator = '\n')
    writer.writerow(headers)
    writer.writerows(stats)


# organized_info = setup_for_pandas(names_list=names, header_list=headers, stats_list=stats)
# rushing_df = pd.DataFrame(organized_info, columns=headers)
