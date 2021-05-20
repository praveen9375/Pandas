#We'll first create a DataFrame from a Python dictionary. The dictionary will have key-value pairs 'c1':[0, 1, 2, 3] and 'c2':[5, 6, 7, 8], in that order.
#The index for the DataFrame will come from the list of row labels ['r1', 'r2', 'r3', 'r4'].
import pandas as pd
df = pd.DataFrame({'c1':[0,1,2,3], 'c2':[5,6,7,8]}, index = ['r1','r2','r3','r4'])
#We'll create another DataFrame, this one representing a single row. Rather than a dictionary for the first argument, we use a list of lists, and manually set the column labels to ['c1, 'c2'].
#Since there is only one row, the row labels will be ['r5'].
import pandas as pd
row_df = pd.DataFrame([[9,9]], columns = ['c1','c2'], index = ['r5'])
#After creating row_df, we append it to the end of df and drop row 'r2'
df_app = df.append(row_df)
df_drop = df_app.drop(labels ='r2')
