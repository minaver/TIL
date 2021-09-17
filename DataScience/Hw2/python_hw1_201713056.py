import pandas as pd

xl_file = 'score.xlsx'
df = pd.read_excel(xl_file)
mid_df = df[df.midterm >= 20]
new_df = mid_df[mid_df.final >= 20]
print(new_df.iloc[:,[0,4,5]])