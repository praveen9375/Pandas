#The first function, concat_rows will concatenate the rows of the two DataFrames.
def concat_rows(df1, df2):
  row_concat = pd.concat([df1, df2])
  return row_concat
#The next function, concat_cols will concatenate the columns of the two input DataFrames.
def concat_cols(df1, df2):
  col_concat = pd.concat([df1, df2], axis = 1)
  return col_concat
#The final function, merge_dfs will merge the two input DataFrames along their columns.
def merge_dfs(df1, df2):
  merge_df = pd.merge(df1, df2)
  return merge_df
