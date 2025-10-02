import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random as rng

# Linebreak
lineBreak = "I>-=-<"*20+"I"

# Load Data
df = pd.read_csv('team_cherry_data.csv')
cherry_data = pd.DataFrame(df)

# First five lines of the dataframe
print(f"\n{lineBreak}\n\nHead of the Dataframe\n")
print(cherry_data.head())

# Last five lines of the dataframe
print(f"\n{lineBreak}\n\nTail of the Dataframe\n")
print(cherry_data.tail())

# Summary of the dataframe
print(f"\n{lineBreak}\n\nSummary of the Dataframe\n")
print(cherry_data.info())

# Statistical Analysis of the dataframe
print(f"\n{lineBreak}\n\nStatistics of the Dataframe\n")
print(cherry_data.describe())