import pandas as pd

def draws(a, b):
    return a == b

def wins(a, b):
    return a > b

def losses(a, b):
    return a < b


def filterByNation(df, nation):
    totalGames = df[df['home_team'].str.contains(nation, case=False, na=False) | df['away_team'].str.contains(nation, case=False, na=False)]
    return totalGames

def filterByResult(df, nation, resultType):

    #Find specified home results
    homeGames = df[df['home_team'].str.contains(nation, case=False, na=False)]
    homeResults = homeGames[resultType(homeGames['home_score'].astype(int), homeGames['away_score'].astype(int))]
    
    #Find specified away results
    awayGames = df[df['away_team'].str.contains(nation, case=False, na=False)]
    awayResults = awayGames[resultType(awayGames['away_score'].astype(int), awayGames['home_score'].astype(int))]

    #Append both df and sort
    totalResults = pd.concat([homeResults, awayResults], ignore_index=True).drop_duplicates()
    totalResults = totalResults.sort_values(by='date')

    return totalResults

def filterByTournament(df, tournament, date):

    tM = df[df['tournament'].str.contains(f'^{tournament}$', case=False, na=False)]
    tournamentMatches = tM[tM['date'].str.contains(date, case=False, na=False)]

    return tournamentMatches

def gamesPerYear(df, nation):
    #return a dictionary year:games
    df['year'] = pd.to_datetime(df['date']).dt.year
    nationGames = {}
    
    for year, group in df.groupby('year'):
        total_games = (group['home_team'] == nation).sum() + (group['away_team'] == nation).sum()
        nationGames[year] = total_games

    return nationGames

def goalsPerYear(df, nation):
    #return a dictionary year:goals
    df['year'] = pd.to_datetime(df['date']).dt.year
    nationGoals = {}
    
    for year, group in df.groupby('year'):
        total_goals = (group[(group['home_team'] == nation)]
                       ['home_score'].sum() +
                       group[(group['away_team'] == nation)]
                       ['away_score'].sum())
        nationGoals[year] = total_goals

    return nationGoals

def goalsAgainstPerYear(df, nation):
    #return a dictionary year:goalsAgainst
    return

def findAllTournamentYears(df, tournament):

    tDf = df[df['tournament'].str.contains(f'^{tournament}$')]
    tDates = tDf['date'].tolist()

    #Get years only
    modified_list = [item[:4] for item in tDates]

    tournamentDates = list(set(modified_list))
    for year in tournamentDates:
        year = int(year)

    return sorted(tournamentDates)

def matchGoalscorers(df, nation, date):

    mDf = df[df['home_team'].str.contains(f'^{nation}$') | df['away_team'].str.contains(f'^{nation}$')]
    matchData = mDf[mDf['date'].str.contains(f'^{date}$')]

    return matchData

def nationGoalscorers(df, nation):
    nationGoalsDf = df[df['home_team'].str.contains(f'^{nation}$') | df['away_team'].str.contains(f'^{nation}$')]
    nationGoalsDf = nationGoalsDf[nationGoalsDf['team'].str.contains(f'^{nation}$')]
    #dictionary con name:goals 
    scorersDict = {}
    # Iterate through the DataFrame rows
    for index, row in nationGoalsDf.iterrows():
        player = row['scorer']
        if player in scorersDict:
            scorersDict[player] += 1
        else:
            scorersDict[player] = 1

    return scorersDict

def playerGoals(df, player):
    playerDF = df[df['scorer'].str.contains(f'^{player}$', na=False)]
    return playerDF.shape[0]