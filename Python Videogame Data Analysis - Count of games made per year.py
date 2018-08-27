import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
vg_data = pd.read_csv('vgsales.csv', na_values='N/A', delimiter=',', parse_dates=True)

# to-do:
# 0. Make note of NaNs  - CHECK!
# 1. visualize different datasets for EDA purposes - check!
# 2. Use studio as a variable for analysis
# 3. Determine what calculations you actually want to run
# 4. Implement said calculations
# 5. visualize


# Genre comparisons: using genres listed, determine which is the best-selling
# Maybe using an anova? idk

# filter using .max() of each year

vg_data.dropna(how='any')

vg_year = vg_data.groupby('Year')['Global_Sales'].count()

# holy fuck this actually works properly

vg_year.drop(labels = [2017, 2020], inplace=True)

print(vg_year.head(n=40))

plt.bar(x= vg_year.index, height = vg_year, color='purple')
# change line colour
plt.xlabel('Year')
plt.ylabel('# of Games Produced')
plt.title('Number of Games Produced per Year')
plt.show()
