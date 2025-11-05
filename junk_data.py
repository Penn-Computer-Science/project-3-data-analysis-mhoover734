import random
import pandas as pd
hk_lists = {
    "played HK": [True, True, True, True],
    "HK hours": [5, 300, 50, 45],
    "HK rating": [6, 10, 10, 9],
    "HK sleep": ["Increased", "Stayed Same", "Increased", "Stayed Same"],
    "HK sleep #": [1,0,1,0]
}

ss_lists = {
    "played SS": [True, True],
    "SS hours": [60, 70],
    "SS rating": [10, 7],
    "SS sleep": ["Stayed Same", "Decreased"],
    "SS sleep #": [0,-1]
}

for i in range(500):
    while True:
        played_hk = random.choice([True, False])
        played_ss = random.choice([True, False])
        if played_hk or played_ss:
            break
    if played_hk and len(hk_lists["played HK"]) < 100:
        hk_hours = random.randint(5,300)
        hk_rating = random.randint(3,10)
        hk_sleep_num = random.randint(-2,2)
        hk_sleep = ["Greatly Decreased", "Decreased", "Stayed Same", "Increased", "Greatly Increased"][hk_sleep_num+2]
        hk_lists["played HK"].append(played_hk)
        hk_lists["HK hours"].append(hk_hours)
        hk_lists["HK rating"].append(hk_rating)
        hk_lists["HK sleep"].append(hk_sleep)
        hk_lists["HK sleep #"].append(hk_sleep_num)
    if played_ss and len(ss_lists["played SS"]) < 100:
        ss_hours = random.randint(5,300)
        ss_rating = random.randint(3,10)
        ss_sleep_num = random.randint(-2,2)
        ss_sleep = ["Greatly Decreased", "Decreased", "Stayed Same", "Increased", "Greatly Increased"][ss_sleep_num+2]
        ss_lists["played SS"].append(played_ss)
        ss_lists["SS hours"].append(ss_hours)
        ss_lists["SS rating"].append(ss_rating)
        ss_lists["SS sleep"].append(ss_sleep)
        ss_lists["SS sleep #"].append(ss_sleep_num)

hk_data = pd.DataFrame(hk_lists)
print()
print(hk_data)

hk_data.to_csv('hk_data.csv', index=False)

ss_data = pd.DataFrame(ss_lists)
print()
print(ss_data)

ss_data.to_csv('ss_data.csv', index=False)