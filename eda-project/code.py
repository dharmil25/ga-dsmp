# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns





#Code starts here
data = pd.read_csv(path)
data.hist(column='Rating', bins=8, figsize=(10,10))

data = data[data['Rating'] <=5]
data.hist(column='Rating', bins=8, figsize=(10,10))
plt.show()
#Code ends here


# --------------
# code starts here


# code ends here
total_null = data.isnull().sum()

percent_null = (total_null/data.isnull().count())

missing_data = pd.concat([total_null, percent_null], axis=1, keys=['Total','Percent'])
print(missing_data)

data.dropna(axis=0, inplace=True)

total_null_1 = data.isnull().sum()
percent_null_1 = (total_null_1/data.isnull().count())

missing_data_1 = pd.concat([total_null_1, percent_null_1], axis=1, keys=['Total','Percent'])
print(missing_data_1)



# --------------

#Code starts here
catplot = sns.catplot(x="Category", y="Rating", kind="box", data=data, height=10)
catplot.set_xticklabels(rotation=90)
catplot.fig.suptitle("Rating vs Category [BoxPlot]")

#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here
data['Installs'].value_counts()

data['Installs'] = data['Installs'].str.replace(',', '')
data['Installs'] = data['Installs'].str.replace('+', '')
data['Installs'] = data['Installs'].astype(int)

le = LabelEncoder()

data['Installs'] = le.fit_transform(data['Installs'])

regplot = sns.regplot(x="Installs", y="Rating", data=data)
plt.title("Rating vs Installs [RegPlot]")
#Code ends here



# --------------
#Code starts here
data['Price'].value_counts()

data['Price'] = data['Price'].str.replace('$', '')
data['Price'] = data['Price'].astype(float)

regplot = sns.regplot(x="Price", y="Rating", data=data)
plt.title("Rating vs Price [RegPlot]")
#Code ends here


# --------------

#Code starts here
data['Genres'].unique()

data['Genres'] = data['Genres'].str.split(';').str[0]


gr_mean = data.groupby('Genres', as_index=False)[['Rating']].mean()

print(gr_mean.describe())

gr_mean = gr_mean.sort_values(by='Rating')

print(gr_mean.iloc[0], gr_mean.iloc[-1])

#Code ends here


# --------------

#Code starts here
print(data['Last Updated'].head())

data['Last Updated'] = pd.to_datetime(data['Last Updated'])

print(data['Last Updated'].head())

max_date = data['Last Updated'].max()
print(max_date)

data['Last Updated Days'] = ((max_date - data['Last Updated']).dt.days)
print(data['Last Updated Days'].head())

regplot = sns.regplot(x="Last Updated Days", y="Rating", data=data)
plt.title("Rating vs Last Updated [RegPlot]")

#Code ends here



