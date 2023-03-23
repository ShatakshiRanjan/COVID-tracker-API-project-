#This program looks at a COVID tracker API and visually presents the data using matplotlib
import requests
import matplotlib.pyplot as plt

#Retrives data from a COVID tracker API
r = requests.get("https://api.covidtracking.com/v1/states/current.json")
COVID_data = r.json()

#Method 1: Bar graph showing number of death in states within the United States
xAxis = []
yAxis = []
for data in COVID_data:
    xAxis.append(data["state"])
    yAxis.append(data["death"])

plt.bar(xAxis, yAxis)
plt.xlabel("State")
plt.ylabel("Deaths")
plt.title("Number of death in states due to COVID")
plt.show()

#Method 2: Scatter plot showing the corrolation between people in each state being hospitalized compared to the number of death in the state
xAxis = []
for data in COVID_data:
    xAxis.append(data["hospitalizedCurrently"])

plt.scatter(xAxis, yAxis)
plt.xlabel("Hospitalized")
plt.ylabel("Deaths")
plt.title("COVID-19 Hospitalizations vs. Deaths by State")
plt.show()

#Method 3: Pie chart showing the icrease in death faced by States
state = []
size = []

for data in COVID_data:
    if data["deathIncrease"] > 0:
        state.append(data["state"])
        size.append(data["deathIncrease"])

fig1, ax1 = plt.subplots()
ax1.pie(size, labels=state, autopct="%1.1f%%")
plt.title("Percentage Increase in COVID-19 Deaths in the US")
plt.show()