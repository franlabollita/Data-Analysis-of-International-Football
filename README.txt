Football Data Analytics Project


**INTRODUCTION**
  Welcome to my first foray into data analysis. Throughout this project, I will delve into fundamental libraries 
  such as pandas, numpy, and matplotlib. The core focus will be on proficiently handling dataframes and employing 
  graphical representations to visualize the data effectively.

DATA
  Special thanks to Mart Jurisoo (martj42) for uploading this free data on Kraggle. 
  The data set is titled: "International football results from 1872 to 2023" and contains 3 CSV files
  goalscorers.csv: (Doesn't include friendly goals)
results.csv:
shootouts.csv:
Link to dataset: https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017

MAIN.PY

FILTER.PY

filterByNation():
  This function takes a DataFrame and a nation name as input and returns a filtered DataFrame containing all games 
  involving the specified nation, whether they were the home or away team.
  Parameters:
  - df (DataFrame): The DataFrame containing the international football results data.
  - nation (str): The name of the nation to filter the data by.
  Returns:
  - totalGames (DataFrame): A filtered DataFrame containing all games involving the specified nation, regardless of 
    whether they were the home or away team.

filterByResult():
  This function is designed to filter an input DataFrame to retrieve specific game results for a given nation based 
  on the result type (e.g., wins, losses, draws). It processes both home and away games involving the specified 
  nation and returns a DataFrame containing     the selected result type for that nation.
  Parameters:
  - df (DataFrame): The DataFrame containing the international football results data.
  - nation (str): The name of the nation to filter the data by.
  - resultType (function): A function that takes two arguments (home score and away score) and returns a boolean value 
                           representing whether the specified result type is achieved.
  Returns:
  - totalResults (DataFrame): A filtered DataFrame containing game results of the specified type for the specified nation.

filterByTournament():
  This function aims to filter a given DataFrame to extract matches that match a specific tournament and date. 
  It primarily targets matches from the designated tournament and date within the dataset and returns a DataFrame 
  containing these filtered matches.
  Parameters:
  - df (DataFrame): The DataFrame containing the international football results data.
  - tournament (str): The name of the tournament to filter the data by.
  - date (str): The date to filter the data by.
  Returns:
  - tournamentMatches (DataFrame): A DataFrame containing matches that belong to the specified tournament and date.

findAllTournamentYears():
  This function serves to identify all unique years in which a specified tournament took place within the given DataFrame. 
  It collects the years from the dataset corresponding to the particular tournament and returns a sorted list of these years.
  Parameters:
  - df (DataFrame): The DataFrame containing the international football results data.
  - tournament (str): The name of the tournament to find the years for.
  Returns:
  - tournamentDates (list): A sorted list of unique years in which the specified tournament occurred.

matchGoalscorers():
  This function is designed to extract match data involving a specified nation and a given date from the provided DataFrame. 
  It identifies matches where the nation played either as the home or away team on the specified date and returns the 
  corresponding match data.
  Parameters:
  - df (DataFrame): The DataFrame containing the international football results data.
  - nation (str): The name of the nation to filter the data by.
  - date (str): The date of the match to filter the data by.
  Returns:
  - matchData (DataFrame): A DataFrame containing data of matches involving the specified nation on the specified date.

nationGoalscorers():
  This function aims to compile a dictionary of goal scorers for a specified nation, using the provided DataFrame. It 
  filters and extracts match data where the nation played as either the home or away team, and subsequently compiles 
  a dictionary that associates players' names with the number of goals they scored for the nation.
  Parameters:
  - df (DataFrame): The DataFrame containing the international football results data.
  - nation (str): The name of the nation to identify goal scorers for.
  Returns:
  - scorersDict (dict): A dictionary where keys represent players' names and values represent the number of goals they 
                        scored for the specified nation.

playerGoals():
  This function is designed to calculate the total number of goals scored by a specific player, using the provided DataFrame. 
  It filters the DataFrame to extract rows where the given player's name appears in the 'scorer' column, and then returns the 
  count of goals scored by that player.
  Parameters:
  - df (DataFrame): The DataFrame containing the international football results data.
  - player (str): The name of the player to calculate the total goals for.
  Returns:
  - goalsCount (int): The total number of goals scored by the specified player.

GRAPH,PY

