import pandas as pd


def load_data():
    global olympics
    olympics = pd.read_csv('files/olympics.csv', skiprows=1)
    for column in olympics.columns:
        if column[:2]=='01':
            olympics.rename(columns={column:'Gold'+ column[4:]}, inplace=True)
        elif column[:2]=='02':
            olympics.rename(columns={column:'Silver'+ column[4:]}, inplace=True)
        elif column[:2]=='03':
            olympics.rename(columns={column:'Bronze'+ column[4:]}, inplace=True)

    country_names = [x.split('\xc2\xa0(')[0] for x in olympics.iloc[:,0]]
    olympics.set_index(pd.Series(country_names), inplace=True)
    olympics.rename(columns={"Unnamed: 0" : "Country"},inplace = True)
    olympics.iloc[:,0] = country_names
    olympics.drop(['Totals'], axis=0, inplace= True)
    return olympics

load_data()


def first_country(olympics):

    return olympics.iloc[0]

def gold_medal(olympics):

    return olympics['Gold'].idxmax()

def biggest_difference_in_gold_medal(olympics):
    gold_diff = olympics["Gold"] - olympics["Gold.1"]
    return gold_diff.idxmax()

def get_points(olympics):
    Points = olympics["Gold.2"]*3 + olympics["Silver.2"]*2 + olympics["Bronze.2"]
    olympics['Points'] = Points
    df = olympics['Points']
    return df
