import pandas as pd 
import numpy as np
from string import ascii_lowercase 
import copy
import re
import warnings
import unicodedata

warnings.simplefilter(action='ignore')


cols = ['Player','From','To','Pos','Ht','Wt','Birth Date','Colleges'] 
players = pd.read_csv('A.txt', sep=",", encoding = 'utf-8') 
players['Player'] = players['Player'].str.split("\\").str[0]
players['FirstName'] = players['Player'].str.split(" ").str[0]
players['LastName'] = players['Player'].str.split(" ").str[1]

def remove_non_ascii(text):
    return ''.join(i for i in text if ord(i)<128)
 
players['FirstName'] = players['FirstName'].apply(remove_non_ascii)
players['LastName'] = players['LastName'].apply(remove_non_ascii)

for c in ascii_lowercase: 
    if c == 'a' or c == 'x':
        continue
    fileName = c.upper() + '.txt'
    df = pd.read_csv(fileName, sep=",", encoding = 'utf-8')

    df['Player'] = df['Player'].apply(remove_non_ascii)

    df['Player'] = df['Player'].str.split("\\").str[0]
    df['FirstName'] = df['Player'].str.split(" ").str[0]

    df['LastName'] = df['Player'].str.split(" ").str[2]  

    df.LastName.fillna(df.Player.str.split(" ").str[1], inplace=True)

    # df['LastName'] = df['Player'].str.split(" ").str[1]

    players = players.append(df)


playersDF = players[['FirstName', 'LastName']]
playersDF['ID'] = range(1, len(playersDF) + 1)

firstNameFrequency = pd.DataFrame(playersDF.groupby('FirstName').count())

firstnames = playersDF['FirstName'].value_counts()
lastnames = playersDF['LastName'].value_counts()

firstNameDict = firstnames.to_dict()
lastNameDict = lastnames.to_dict()

firstNameID = dict(zip(playersDF.ID, playersDF.FirstName))
lastNameID = dict(zip(playersDF.ID, playersDF.LastName))


# First Merge
playersDFMerge = pd.merge(left = playersDF, right = playersDF, left_on = 'LastName', right_on = 'FirstName')

# Rid repeats
playersDFMerge = playersDFMerge[playersDFMerge.FirstName_x != playersDFMerge.FirstName_y]

# Assign df1 
df1 = playersDFMerge

df1.to_csv('df1.csv')

# Second merge
playersDFMerge = pd.merge(left = playersDFMerge, right = playersDF, left_on = 'LastName_y', right_on = 'FirstName')

# Rid repeats
playersDFMerge = playersDFMerge[playersDFMerge.ID != playersDFMerge.ID_x]
playersDFMerge = playersDFMerge[playersDFMerge.ID != playersDFMerge.ID_y]

# Assign df2 
df2 = playersDFMerge

# Third merge
playersDFMerge = pd.merge(left = playersDFMerge, right = playersDF, left_on = 'LastName', right_on = 'FirstName', suffixes = ['2', '3'])

# Assign df3
df3 = playersDFMerge

# Fourth merge
playersDFMerge = pd.merge(left = playersDFMerge, right = playersDF, left_on = 'LastName3', right_on = 'FirstName', suffixes = ['3', '4'])

# Assign df4 
df4 = playersDFMerge

# Fifth merge
playersDFMerge = pd.merge(left = playersDFMerge, right = playersDF, left_on = 'LastName', right_on = 'FirstName', suffixes = ['4', '5'])

# Assign df5 
df5 = playersDFMerge

# Sixth merge 
playersDFMerge = pd.merge(left = playersDFMerge, right = playersDF, left_on = 'LastName5', right_on = 'FirstName', suffixes = ['5', '6'])

# Assign df6
df6 = playersDFMerge

# Seventh merge
playersDFMerge = pd.merge(left = playersDFMerge, right = playersDF, left_on = 'LastName', right_on = 'FirstName', suffixes = ['6', '7'])

# Assign df7
df7 = playersDFMerge

# Eighth merge
playersDFMerge = pd.merge(left = playersDFMerge, right = playersDF, left_on = 'LastName7', right_on = 'FirstName', suffixes = ['7', '8'])

# Assign df8 
df8 = playersDFMerge

# Ninth merge - no more results
playersDFMerge = pd.merge(left = playersDFMerge, right = playersDF, left_on = 'LastName', right_on = 'FirstName', suffixes = ['8', '9'])

# Assign df9 
df9 = playersDFMerge

i = 1
i2 = 1
for df in [df1, df2, df3, df4, df5, df6, df7, df8, df9] :
    csv_name = 'Counts' + str(i2) + '.csv'
    f = open(csv_name, "w")
    f.truncate()
    f.close()
    for column in df.columns: 
        if i % 3 == 0: 
            counts = pd.value_counts(df[column].values)
            counts = pd.DataFrame(counts, columns = ['Count'])

            counts.to_csv(csv_name, mode = 'a')

        i += 1
    
    i2 += 1



dict1 = {}; dict2 = {}; dict3 = {}; dict4 = {}; dict5 = {}; dict6 = {}; dict7 = {}; dict8 = {} 

for csv in [1,2,3,4,5,6,7,8]:
    csv_name = 'Counts' + str(csv) + '.csv'
    df = pd.read_csv(csv_name, header = None)
    df = df.dropna()

    df.columns = ['PlayerID', 'Count']
    df['PlayerID'] = df['PlayerID'].astype('int32')
    df['Count'] = df['Count'].astype('int32')

    
    df = df.groupby('PlayerID')

    if csv == 1: 
        for name, group in df:
            player_id = name
            count = group['Count'].sum()
            if player_id in dict1: 
                dict1[player_id] += count

            else: 
                dict1[player_id] = count
            
    elif csv == 2: 
        for name, group in df:
            count = group['Count'].sum()
            
            if name in dict2: 
                dict2[name] += count

            else: 
                dict2[name] = count
    
    elif csv == 3: 
        for name, group in df:
            count = group['Count'].sum()
            
            if name in dict3: 
                dict3[name] += count

            else: 
                dict3[name] = count

    elif csv == 4: 
        for name, group in df:
            count = group['Count'].sum()
            
            if name in dict4: 
                dict4[name] += count

            else: 
                dict4[name] = count
    
    elif csv == 5: 
        for name, group in df:
            count = group['Count'].sum()
            
            if name in dict5: 
                dict5[name] += count

            else: 
                dict5[name] = count
    
    elif csv == 6: 
        for name, group in df:
            count = group['Count'].sum()
            
            if name in dict6: 
                dict6[name] += count

            else: 
                dict6[name] = count

    elif csv == 7: 
        for name, group in df:
            count = group['Count'].sum()
            
            if name in dict7: 
                dict7[name] += count

            else: 
                dict7[name] = count

    elif csv == 8: 
        for name, group in df:
            count = group['Count'].sum()
            
            if name in dict8: 
                dict8[name] += count

            else: 
                dict8[name] = count


allPlayers = dict1.keys()
playerPoints = {}

for player in allPlayers: 
    points = 0

    points += dict1[player]

    try:
        points += dict2[player] * 2
    except: 
        pass
    try: 
        points += dict3[player] * 3
    except: 
        pass
    try: 
        points += dict4[player] * 4
    except: 
        pass
    try: 
        points += dict5[player] * 5
    except: 
        pass
    try: 
        points += dict6[player] * 6
    except: 
        pass
    try: 
        points += dict7[player] * 7
    except: 
        pass
    try: 
        points += dict8[player] * 8
    except: 
        pass

    playerPoints[player] = points


def getPlayer(id): 
    row = playersDF.loc[playersDF['ID'] == id]
    firstname = row['FirstName'].values[0]
    lastname = row['LastName'].values[0]

    return firstname + ' ' + lastname

playerNamePoints = pd.DataFrame(columns=['Player_Name', 'Name_Points', 'Name_Replaceability'])
numNames = len(playersDF)


for key in playerPoints:
    playerName = getPlayer(key)
    pPoints = playerPoints[key]

    firstName = firstNameID[key]
    lastName = lastNameID[key]

    fReplace = firstNameDict[firstName] / numNames
    lReplace = lastNameDict[lastName] / numNames

    tReplace = round((fReplace + lReplace) / 2, 4) * 100

    playerNamePoints = playerNamePoints.append({'Player_Name': playerName, 'Name_Points': pPoints, 'Name_Replaceability': tReplace}, ignore_index=True)

playerNamePoints.to_csv('NBA_Player_Name_Points.csv')
