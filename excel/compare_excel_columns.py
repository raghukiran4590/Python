import pandas as pd

sn_file = "/Users/AF35861/Downloads/sn_file.xlsx"
dba_file = "/Users/AF35861/Downloads/dba_file.xlsx"

snowdf = pd.read_excel(sn_file, sheet_name='Sheet1')
dbadf = pd.read_excel(dba_file, sheet_name='Sheet1')

matching_rows = snowdf[snowdf['instance'].isin(dbadf['instance'])]

print("DataFrame with matching rows:")
print(matching_rows)

merged_df = pd.merge(snowdf, dbadf, on='instance', how='left')
merged_rows = merged_df[merged_df['instance'].isin(dbadf['instance'])]
snowdf.loc[merged_df['instance'].isin(dbadf['instance']), 'comments'] = merged_df['comments_y']
# dbadf.loc[merged_df['instance'].isin(snowdf['instance']), 'comments'] = merged_df['comments_y']
# output_file = '/Users/AF35861/Downloads/common.xlsx'
# dbadf.to_excel(output_file, index=False, sheet_name='Sheet1')

print(f"Completed")