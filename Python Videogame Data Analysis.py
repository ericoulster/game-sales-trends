import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
vg_data = pd.read_csv('vgsales.csv', na_values='N/A', delimiter=',', parse_dates=['Year'])

# to-do:
# 0. Make note of NaNs  - CHECK!
# 1. visualize different datasets for EDA purposes - check!
# 2. Use studio as a variable for analysis
# 3. Determine what calculations you actually want to run
# 4. Implement said calculations
# 5. visualize

# Best Seller by year project:
# objective: show the trend of videogames making more sales as time goes on
# Lvl 1: Do a line graph comparing global sales best-seller each year
# Lvl 2: Do a line graph comparing global sales best-seller each year for
#   each studio (by colour)
# for both of these

# number of games a year: use a count method for each year, compare end results w/ bar graph

# Genre comparisons: using genres listed, determine which is the best-selling
# Maybe using an anova? idk

vg_data.sort_values(by='Year')

# filter using .max() of each year
by_year = vg_data.loc['Year', 'Global_Sales']
yearly_vgd_sales = by_year.resample('A').max()

print(yearly_vgd_sales.head())
