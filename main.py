import filter as ft
import graph as gf
import pandas as pd

def main():

    #Open file path
    resultsPathFile = 'mainArchive/results.csv'
    df = pd.read_csv(resultsPathFile)

    #Create Dataframe of Bermuda Games
    bermudaGames = ft.filterByNation(df, 'Bermuda')

    #Dived it into wins, losses, and draws
    berWins = ft.filterByResult(df, 'Bermuda', ft.wins)
    berLosses = ft.filterByResult(df, 'Bermuda', ft.losses)
    berDraws = ft.filterByResult(df, 'Bermuda', ft.draws)

    #create Y values for graph
    yValues = [berWins.shape[0], berDraws.shape[0], berLosses.shape[0]]
    #gf.barGraph(yValues, ['Wins', 'Draws', 'Losses'], 'Bermuda', ['Green', 'Gray', 'Red'])

    FWCYears = ft.findAllTournamentYears(df, 'FIFA World Cup')
    print(FWCYears)

main()
