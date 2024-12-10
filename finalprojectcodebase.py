# -*- coding: utf-8 -*-
"""finalProjectCodeBase.ipynb
Original file is located at
    https://colab.research.google.com/drive/1aVvADOvy_pAPHD2A2vy1hzbcAN3HkYRE
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("/content/sample_data/2FA_data_Trail.csv")
data.head()

#Dataframe data: 3G	4G Slow	4G Fast	unthrottled find averages

import pandas as pd
import matplotlib.pyplot as plt

#Relevant columns to numeric, handling errors
for col in ['3G', '4G Slow', '4G Fast', 'unthrottled']:
    data[col] = pd.to_numeric(data[col], errors='coerce')


#The averages for each network type
averages = {
    '3G': data['3G'].mean(),
    '4G Slow': data['4G Slow'].mean(),
    '4G Fast': data['4G Fast'].mean(),
    'unthrottled': data['unthrottled'].mean()
}
print(averages)

#Bar plot
plt.figure(figsize=(8, 6))
plt.bar(averages.keys(), averages.values(), color=['skyblue', 'lightcoral', 'lightgreen', 'gold'])
plt.xlabel("Network Type")
plt.ylabel("Average Value")
plt.title("Average Values for Different Network Types")
plt.show()
