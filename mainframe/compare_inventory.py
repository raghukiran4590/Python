import pandas as pd

# MF DB2   ,8139     , InfoHub Count 8,134
# MF IMS   ,51900    , InfoHub Count 51,899
# MODEL204 ,4995     , InfoHub Count 4,986

# Read the two excel files
df1 = pd.read_excel('/Users/AF35861/Downloads/mainframe_source_data.xlsx', sheet_name='source')
df2 = pd.read_excel('/Users/AF35861/Downloads/mainframe_target_data.xlsx', sheet_name='target')

# Merge the dataframes on key columns with an indicator
# 'on' should be a list of columns that uniquely identify a row
merged_df = pd.merge(df1, df2, on=['DBMS_TYPE', 'INSTANCE_NM', 'DATABASE_NM'], how='outer', indicator=True)

# Filter for rows that are only in one of the dataframes
# '_merge' column will indicate 'left_only', 'right_only', or 'both'
rows_only_in_source = merged_df[merged_df['_merge'] == 'not_found_in_infohub']
rows_only_in_target = merged_df[merged_df['_merge'] == 'not_found_in_source']

# Save these unique rows to separate sheets in an output Excel file
with pd.ExcelWriter('/Users/AF35861/Downloads/mainframe_delta_output.xlsx') as writer:
    rows_only_in_source.to_excel(writer, sheet_name='Only in Source', index=False)
    rows_only_in_target.to_excel(writer, sheet_name='Only in Target', index=False)

print("Missing/extra rows saved to mainframe_delta_output.xlsx")