#this chapter involve performing grouping operations on df, which contains all MLB batting data from 1871-2017. Using df, our goal is to retrieve home run (HR) statistics for 2017.
year_group = df.groupby(['yearID'])
#The yearly stats can be obtained from summing the values across the year-separated groups.
year_stats = year_group.sum()
# Using the loc property, we'll retrieve the home run total for 2017.
hr_2017 = year_stats.loc[2017, 'HR']
#we want to get the yearly totals for each batting statistic per team & just sum over all the groups.
year_team_group = df.groupby(['yearID', 'teamID'])
year_team_stats = year_team_group.sum()
