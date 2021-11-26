import datacommons_pandas
import pandas as pd
import plotly.express as px

# Unemployment rate by-year in United States
dc: pd.DataFrame = datacommons_pandas.build_time_series("country/USA", "UnemploymentRate_Person")

newData = {}
oldData = dc.to_dict()

# Get the max UR% for each year
for k in oldData:
    year = int(k.split("-")[0])
    if year in newData.keys():
        newData[year] = max(newData[year], oldData[k])
    else:
        newData[year] = oldData[k]

finalData = pd.DataFrame(sorted(newData.items()), columns=["Year", "MaxUnemployment"])

# Writing to CSV
finalData.to_csv("outputs/output.csv")

# Output bar graph
fig = px.bar(finalData, x="Year", y="MaxUnemployment")

fig.write_image("outputs/ue_graph.png")