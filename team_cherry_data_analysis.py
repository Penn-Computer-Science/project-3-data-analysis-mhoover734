import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random as rng

# Linebreak
lineBreak = "I>-=-<"*20+"I"

# Load HK data
df = pd.read_csv('hk_data.csv')
hk_data = pd.DataFrame(df)

# First five lines of the HK dataframe
print(f"\n{lineBreak}\n\nHead of the HK Dataframe\n")
print(hk_data.head())

# Last five lines of the HK dataframe
print(f"\n{lineBreak}\n\nTail of the HK Dataframe\n")
print(hk_data.tail())

# Summary of the HK dataframe
print(f"\n{lineBreak}\n\nSummary of the HK Dataframe\n")
print(hk_data.info())

# Statistical Analysis of the HK dataframe
print(f"\n{lineBreak}\n\nStatistics of the HK Dataframe\n")
print(hk_data.describe())

# Top 5 datasets by HK playtime
print(f"\n{lineBreak}\n\nTop 5 datasets by HK playtime\n")
print(hk_data.sort_values(by="HK hours", ascending=False).head(5))

# Top datasets by HK sleep
print(f"\n{lineBreak}\n\nTop sleep quality in HK Dataframe\n")
print(hk_data[hk_data["HK sleep"]=='Greatly Increased'])

# Scatterplot of HK Sleep Change vs. HK Hours
for rating, group in hk_data.groupby('HK sleep #'):
	plt.scatter([rating]*len(group['HK hours']), group['HK hours'], label=str(rating))
plt.title('HK Hours for Sleep Change')
plt.xlabel('Sleep Change')
plt.ylabel('HK Rating')
plt.show()

# Pie chart of HK Ratings
sizes = hk_data['HK rating'].value_counts().sort_index() / hk_data['HK rating'].value_counts().sum() * 100
sizes.plot(kind='pie', labels=sizes.index, autopct='%1.1f%%')
plt.title('HK Rating Spread')
plt.ylabel('HK Rating')
plt.show()

# Histogram of spread of HK Hours
df['HK hours'].plot(kind='hist', bins = 20, edgecolor='Black')
plt.title('HK Hour Spread')
plt.xlabel('Hours in HK')
plt.ylabel('# of people')
plt.show()

#I>-=-<I>-=-<I>-=-<I>-=-<I>-=-<I>-=-<I>-=-<I>-=-<I>-=-<I>-=-<I>-=-<I>-=-<I>-=-<I>-=-<I>-=-<I>-=-<I>-=-<I>-=-<I>-=-<I>-=-<I

# Load SS data
df = pd.read_csv('ss_data.csv')
ss_data = pd.DataFrame(df)

# First five lines of the SS dataframe
print(f"\n{lineBreak}\n\n{lineBreak}\n\nHead of the SS Dataframe\n")
print(ss_data.head())

# Last five lines of the SS dataframe
print(f"\n{lineBreak}\n\nTail of the SS Dataframe\n")
print(ss_data.tail())

# Summary of the SS dataframe
print(f"\n{lineBreak}\n\nSummary of the SS Dataframe\n")
print(ss_data.info())

# Statistical Analysis of the SS dataframe
print(f"\n{lineBreak}\n\nStatistics of the SS Dataframe\n")
print(ss_data.describe())

# Top 5 datasets by SS playtime
print(f"\n{lineBreak}\n\nTop 5 datasets by SS playtime\n")
print(ss_data.sort_values(by="SS hours", ascending=False).head(5))

# Top datasets by SS sleep
print(f"\n{lineBreak}\n\nTop sleep quality in SS Dataframe\n")
print(ss_data[ss_data["SS sleep"]=='Greatly Increased'])
print("\n\n\n\n")
print(ss_data.groupby('SS rating')['SS hours'])

# Scatterplot of SS Sleep Change vs. SS Hours
for rating, group in ss_data.groupby('SS sleep #'):
	plt.scatter([rating]*len(group['SS hours']), group['SS hours'], label=str(rating))
plt.title('SS Hours for Sleep Change')
plt.xlabel('Sleep Change')
plt.ylabel('SS Rating')
plt.show()

# Pie chart of SS Ratings
sizes = ss_data['SS rating'].value_counts().sort_index() / ss_data['SS rating'].value_counts().sum() * 100
sizes.plot(kind='pie', labels=sizes.index, autopct='%1.1f%%')
plt.title('SS Rating Spread')
plt.ylabel('SS Rating')
plt.show()

# Histogram of spread of SS Hours
df['SS hours'].plot(kind='hist', bins = 20, edgecolor='Black')
plt.title('SS Hour Spread')
plt.xlabel('Hours in SS')
plt.ylabel('# of people')
plt.show()