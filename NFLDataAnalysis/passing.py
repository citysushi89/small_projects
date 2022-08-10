import pandas as pd
from functions import get_site, get_names, get_stats, get_headers, setup_for_pandas
import csv

PASSING_STATS_LINK = "https://www.espn.com/nfl/stats/player"


bs = get_site(PASSING_STATS_LINK)
names = get_names(bs)
headers = get_headers(bs)
num_of_headers = int(len(headers))
stats = get_stats(bs, num_of_headers, names)

# Write data to csv
with open("data/passing.csv", "w") as file:
    writer = csv.writer(file, lineterminator = '\n')
    writer.writerow(headers)
    writer.writerows(stats)


# organized_info = setup_for_pandas(names_list=names, header_list=headers, stats_list=stats)
# passing_df = pd.DataFrame(organized_info, columns=headers)

