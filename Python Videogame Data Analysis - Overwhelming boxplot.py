import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
vg_data = pd.read_csv('vgsales.csv', na_values='N/A', delimiter=',')

# to-do:
# 0. Make note of NaNs  - CHECK!
# 1. visualize different datasets for EDA purposes
# 2. Use studio as a variable for analysis
# 3. Determine what calculations you actually want to run
# 4. Implement said calculations
# 5. visualize

# Best Seller by year project:
# objective: show the trend of videogames making more sales as time goes on
# Lvl 1: Do a line graph comparing global sales best-seller each year
# Lvl 2: Do a line graph comparing global sales best-seller each year for each studio (by colour)

# Genre comparisons: using genres listed, determine which is the best-selling
# Maybe using an anova? idk

vg_data.sort_values(by='Year')

vg_data.boxplot(column='Global_Sales', by='Publisher')

plt.xticks(rotation='vertical')
plt.xlabel('Publishing Studio')
plt.ylabel('Game Sales (In Millions)')

plt.margins(0.01, tight=False)

plt.show()
