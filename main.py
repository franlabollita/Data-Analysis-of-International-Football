import filter as ft
import graph as gf
import pandas as pd

def main():

    #Open file path
    resultsPathFile = 'mainArchive/results.csv'
    df = pd.read_csv(resultsPathFile)

    bermudaGames = ft.filterByNation(df, 'Bermuda')

    berWins = ft.filterByResult(df, 'Bermuda', ft.wins)
    berLosses = ft.filterByResult(df, 'Bermuda', ft.losses)
    berDraws = ft.filterByResult(df, 'Bermuda', ft.draws)

    xValues = [berWins.shape[0], berDraws.shape[0], berLosses.shape[0]]

    gf.barGraph(xValues, 'Bermuda')

main()
