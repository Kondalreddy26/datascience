import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
cities = pd.read_csv("california_cities.csv")

# Extracting the data we are interested in
latitude, longitude = cities["latd"], cities["longd"]
population, area = cities["population_total"], cities["area_total_km2"]

# To scatter the points, using size and color but without label
sns.set()
plt.scatter(longitude, latitude, label=None, c=np.log10(population),
            cmap='viridis', s=area, linewidth=0, alpha=0.5)
plt.gca().set_aspect('equal', adjustable='box')  
# Adjusting the aspect ratio
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.colorbar(label='log$_{10}$(population)')
plt.clim(3, 7)

# Now we will create a legend, we will plot empty lists with the desired size and label
for area_value in [100, 300, 500]:
    plt.scatter([], [], c='k', alpha=0.3, s=area_value, label=str(area_value) + 'km$^2$')
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='City Areas')
plt.title("Area and Population of California Cities")
plt.show()
