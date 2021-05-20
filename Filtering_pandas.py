#In this code exercises, we'll apply various filters to a predefined DataFrame, mlb_df, which contains MLB statistics.
#We'll first filter mlb_df for the top MLB hitting seasons in history, which we define as having a batting average above .300.
top_hitters = mlb_df[mlb_df['BA'] > .300]
#Next we filter for the players whose player ID does not start with the letter a.
exclude_a = mlb_df[~mlb_df['playerID'].str.startswith('a')]
#We'll now retrieve the statistics for two specific players. Their player IDs are 'bondsba01' and 'troutmi01'
two_ids = ['bondsba01', 'troutmi01']
two_players = mlb_df[mlb_df['playerID'].isin(two_ids)]
