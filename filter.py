import pandas as pd

def draws(a, b):
    return a == b

def wins(a, b):
    return a > b

def losses(a, b):
    return a < b


def filterByNation(df, nation):

    #find results of specified nation
    homeGames = df[df['home_team'].str.contains(nation, case=False, na=False)]
    awayGames = df[df['away_team'].str.contains(nation, case=False, na=False)]

    #Append both df and sort
    totalGames = pd.concat([homeGames, awayGames], ignore_index=True)
    totalGames = totalGames.sort_values(by='date')

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

    tM = df[df['tournament'].str.contains(tournament, case=False, na=False)]
    tournamentMatches = tM[tM['date'].str.contains(date, case=False, na=False)]

    return tournamentMatches

#def main():

    #Open file path
  #  resultsPathFile = 'mainArchive/results.csv'
  #  df = pd.read_csv(resultsPathFile)

   # bermudaGames = filterByNation(df, 'Bermuda')

   # bermudaDraws = filterByResult(bermudaGames, 'Bermuda', wins)
    #print(bermudaDraws)

    #worldCup86 = filterByTournament(df, 'FIFA World Cup', '1986')
    #print(worldCup86)

#main()