import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
vg_data = pd.read_csv('vgsales.csv', na_values='N/A', delimiter=',', parse_dates=True)

film_data = pd.read_csv('Hollywood Box Office Trends.csv', delimiter=',', parse_dates=True)


vg_year = vg_data.groupby('Year')['Global_Sales'].max()

vg_data.dropna(how='any')

film_data.columns = ['Year', 'Title', 'Gross_Income']

film_year = film_data.groupby('Year')['Gross_Income'].max()

vg_year.drop(labels=[2017, 2020], inplace=True)

vg_year.drop(labels=[1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988], inplace=True)

plt.plot(film_year, color='brown', linestyle=':')
plt.plot(vg_year, color='blue')

plt.xlabel('Year')
plt.ylabel('# of Sales (Millions)')
plt.title('Best-selling Film & Videogame (By Year)')
plt.legend(labels=['Highest Film Sale', 'Highest V.Game Sale'])
plt.show()
