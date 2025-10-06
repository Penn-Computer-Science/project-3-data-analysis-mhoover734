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