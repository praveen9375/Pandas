#The coding exercises for this chapter involve getting metrics from a DataFrame of MLB players, player_df.
#First, we'll get a summary of all the statistics in player_df.
summary_all = player_df.describe()
#Next, we want to get summaries specifically for the home run totals. The first summary will contain the default metrics from describe, while the second summary will contain the 10th and 90th percentiles.
hr_df = player_df['HR']
summary_hr = hr_df.describe()
low_high_10 = hr_df.describe(percentiles = [.1,.9])
#Finally, we'll treat the 'HR' feature as a categorical variable, with each unique home run total as a separate category. We then get the frequency counts for each category.
hr_counts = hr_df.value_counts()
