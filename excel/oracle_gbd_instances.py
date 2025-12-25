import pandas as pd
import numpy as np

sn_file = "/Users/AF35861/Downloads/Oracle_GBD_Instances.xlsx"
dba_file = "/Users/AF35861/Downloads/GBD_Errors_10-13-2025.xlsx"

df1 = pd.read_excel(sn_file, sheet_name='Sheet1')
df2 = pd.read_excel(dba_file, sheet_name='Sheet1')

compare_col1 = 'INSTANCE_NM'
compare_col2 = 'INSTANCE_NM'
copy_from_col = 'dba_comments'
copy_to_col = 'dba_comments'

if copy_to_col not in df1.columns:
    df1[copy_to_col] = None

for index, row in df1.iterrows():
    instance_nm = row[compare_col1]
    matching_row = df2[df2[compare_col2] == instance_nm]
    if not matching_row.empty:
        df1.at[index, copy_to_col] = matching_row.iloc[0][copy_from_col]

output_file = '/Users/AF35861/Downloads/output.xlsx'

df1.to_excel(output_file, index=False, sheet_name='Sheet1')

print(f"Completed")

# matching_values = df1[df1['INSTANCE_NM'].isin(df2['INSTANCE_NM'])]

# matching_values.to_excel('/Users/AF35861/Downloads/matches.xlsx', index=False)

# print("\nMatching rows saved to 'matches.xlsx'")

# merged_df = pd.merge(df1, df2[['INSTANCE_NM', 'dba_comments']], on='INSTANCE_NM', how='left', suffixes=('_df1', '_df2'))

# merged_df.to_excel('/Users/AF35861/Downloads/merged.xlsx', index=False)

# print("\Merged rows saved to 'merged.xlsx'")
