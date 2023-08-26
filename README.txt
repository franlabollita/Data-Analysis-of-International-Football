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

  filterByNation:
  This function takes a DataFrame and a nation name as input and returns a filtered DataFrame containing all games 
  involving the specified nation, whether they were the home or away team.
  Parameters:
    df (DataFrame): The DataFrame containing the international football results data.
    nation (str): The name of the nation to filter the data by.
  Returns:
    totalGames (DataFrame): A filtered DataFrame containing all games involving the specified nation, regardless of whether they were the home or away team.

GRAPH,PY

