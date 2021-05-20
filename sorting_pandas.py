#The code exercises in this chapter involve sorting a DataFrame of yearly MLB player stats, yearly_stats_df.
#We'll sort yearly_stats_df using two different methods. The first method sorts by 'yearID' in ascending order.
by_year = yearly_stats_df.sort_values('yearID')
#The next sorting method will sort by 'HR' in descending order.
best_hr = yearly_stats_df.sort_values('HR', ascending = [False])
#The final sorting method will again sort yearly_stats_df by 'HR' in descending order, but this time we break ties with 'SO' in ascending order.
best_hr_so = yearly_stats_df.sort_values(['HR', 'SO'], ascending = [False, True])
