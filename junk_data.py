import random
import pandas as pd
lists = {
    "played HK": [True, True, True, True],
    "played SS": [False, True, False, True],
    "HK hours": [5, 300, 50, 45],
    "SS hours": [None, 60, None, 70],
    "HK rating": [6, 10, 10, 9],
    "SS rating": [None, 10, None, 7],
    "HK sleep": ["Increased", "Stayed Same", "Increased", "Stayed Same"],
    "SS sleep": [None, "Stayed Same", None, "Decreased"]
}

for i in range(21):
    while True:
        played_hk = random.choice([True, False])
        played_ss = random.choice([True, False])
        if played_hk or played_ss:
            break
    hk_hours = random.randint(5,300)
    hk_rating = random.randint(3,10)
    hk_sleep = random.choice(["Greatly Decreased", "Decreased", "Stayed Same", "Increased", "Greatly Increased"])
    ss_hours = random.randint(5,300)
    ss_rating = random.randint(3,10)
    ss_sleep = random.choice(["Greatly Decreased", "Decreased", "Stayed Same", "Increased", "Greatly Increased"])
    if not(played_hk):
        hk_hours = None
        hk_rating = None
        hk_sleep = None
    if not(played_ss):
        ss_hours = None
        ss_rating = None
        ss_sleep = None
    lists["played HK"].append(played_hk)
    lists["played SS"].append(played_ss)
    lists["HK hours"].append(hk_hours)
    lists["SS hours"].append(ss_hours)
    lists["HK rating"].append(hk_rating)
    lists["SS rating"].append(ss_rating)
    lists["HK sleep"].append(hk_sleep)
    lists["SS sleep"].append(ss_sleep)

team_cherry_data = pd.DataFrame(lists)
print()
print(team_cherry_data)

team_cherry_data.to_csv('team_cherry_data.csv', index=False)