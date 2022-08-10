from turtle import width
from matplotlib import pyplot as plt
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


# TODO Access data from CSVs (go ahead and access all data and setup for manipulation)


passing_df = pd.read_csv("data\passing.csv")
receiving_df = pd.read_csv(r"data\receiving.csv")
rushing_df = pd.read_csv(r"data\rushing.csv")
# print(passing_df.head())
print(receiving_df.head())
# print(rushing_df.head())
graph_dpi = 300








# OLD GRAPHS MADE FOR REFERENCE

# Receiving stacked bar chart

# org receiving stats into fantasy points
# Yards
receiving_points_yds_list = []
for item in receiving_df.YDS:
    receving_points_from_yds = item / 10
    receiving_points_yds_list.append(receving_points_from_yds)
# TDS
receiving_points_tds_list = []
for item in receiving_df.TD:
    receving_points_from_tds = item * 6
    receiving_points_tds_list.append(receving_points_from_tds)
# Receptions
receiving_points_receptions_list = [item for item in receiving_df.REC]

receiving_points_totals = []
for i in range(0, len(receiving_points_receptions_list)):
    total_points_for_player = receiving_points_yds_list[i] + receiving_points_tds_list[i] + receiving_points_receptions_list[i]
    receiving_points_totals.append(total_points_for_player)
print(receiving_points_totals)

# Create Chart with organized point data
receiving_split_bar = px.bar(
    x=receiving_df.Name,
    y=[receiving_points_yds_list, receiving_points_tds_list, receiving_points_receptions_list],
    # color=receiving_points_totals,
    title="Receiving points by category",
    labels={
        "variable": "Points From:",
        # "wide_variable_0": "Points From Yards",
    }
)

receiving_split_bar.update_layout(
    xaxis_title="Player",
    yaxis_title="Total Points",
    
)
receiving_split_bar.update_xaxes(ticks="outside", tickwidth=2, ticklen=10)

newnames = {'wide_variable_0':'Yards', 'wide_variable_1': 'Touchdowns', 'wide_variable_2':'Receptions'}
receiving_split_bar.for_each_trace(lambda t: t.update(name = newnames[t.name]))

receiving_split_bar.write_image("graphs/receiving_points_origin.png", width=1400, height=850)
receiving_split_bar.show()





# Receiving Scatter
# scatter = px.scatter(
#     receiving_df,
#     x="YDS",
#     y="TD",
#     color="Name",
#     size="TGTS",
#     # labels=dict(Name="Name")
# )

# scatter.update_layout(
#     xaxis_title="Passing Yards",
#     yaxis_title="Touchdowns",
# )
# scatter.write_image("graphs/receiving_yds_tds_targets_scatter.png", width=850, height=850)
# scatter.show()






# Redo of Scatter with plotly express passing
# scatter = px.scatter(
#     passing_df,
#     x="YDS",
#     y="TD",
#     color="Name"
#     # labels=dict(Name="Name")
# )

# scatter.update_layout(
#     xaxis_title="Passing Yards",
#     yaxis_title="Touchdowns"
# )
# scatter.write_image("graphs/passing_yds_tds_scatter.png")
# scatter.show()


#  Created rushing_yards_and_tds_total.png

# bar = go.Figure(
#     data=[
#         go.Bar(name="Yards", x=rushing_df.Name, y=rushing_df.YDS, yaxis='y', offsetgroup=1),
#         go.Bar(name="Touchdowns", x=rushing_df.Name, y=rushing_df.TD, yaxis='y2', offsetgroup=2)
#     ],
#     layout={
#         "yaxis": {"title": "Yards"},
#         "yaxis2": {"title": "Touchdowns", "overlaying": "y", "side": "right"}
#     }
# )
# bar.update_layout(barmode="group")
# bar.update_xaxes(ticks="outside", tickwidth=2, ticklen=15)
# bar.write_image("graphs/rushing_yards_and_tds_total.png", width=1200)
# bar.show()



# Created rushing_yards_total.png

# bar = px.bar(x=players,
#              y=yards
#              )
# bar.update_layout(xaxis_title="Player",
#                   yaxis_title="Yards"
#                   )
# bar.write_image("graphs/rushing_yards_total.png")
#
# bar.show()
