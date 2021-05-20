#here's how directly indexing into a predefined DataFrame, df. 
#We'll initially use direct indexing to get the first column of df as well as the first two rows.
import pandas as pandas
col_1 = df['c1']
row_12 = df[0:2]
#Next, we'll use iloc to retrieve the first and third rows of df.
import pandas as pd
row_13 = df.iloc[[0, 2]]
#Finally, we use loc to set each value of the second column, in the third and fourth rows, equal to 12. 
#The row key we use for indexing will be ['r3','r4'], while the column key will be 'c2'.
import pandas as pd
df.loc[['r3', 'r4'], 'c2'] = 12
