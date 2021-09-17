import numpy as np
import pandas as pd
from scipy.stats import mode

xl_file = 'db_score.xlsx'
df = pd.read_excel(xl_file)

# (1) mean, median (midterm, final, score 각각)
mid_mean = np.mean(df.midterm)
fin_mean = np.mean(df.final)
scr_mean = np.mean(df.score)

mid_median = np.median(df.midterm)
fin_median = np.median(df.final)
scr_median = np.median(df.score)

print("(1) mean, median (midterm, final, score 각각)")
print("< mean >")
print(f"midterm : {mid_mean}")
print(f"final : {fin_mean}")
print(f"score : {scr_mean}")

print("< median >")
print(f"midterm : {mid_median}")
print(f"final : {fin_median}")
print(f"score : {scr_median}")

# (2) mode (grade)
grade_mode = mode(df.grade)[0]

print("\n(2) mode (grade)")
print(f"grade : {grade_mode}")

# (3) variance, standard deviation (midterm, final, score 각각)
mid_var = np.var(df.midterm)
fin_var = np.var(df.final)
scr_var = np.var(df.score)

mid_std = np.std(df.midterm)
fin_std = np.std(df.final)
scr_std = np.std(df.score)

print("\n(3) variance, standard deviation (midterm, final, score 각각)")
print("< variance >")
print(f"midterm : {mid_var}")
print(f"final : {fin_var}")
print(f"score : {scr_var}")

print("< standard deviation >")
print(f"midterm : {mid_std}")
print(f"final : {fin_std}")
print(f"score : {scr_std}")

# (4) percentile plot (midterm, final, score 각각)
print("\n(4) percentile plot (midterm, final, score 각각)")
for p in range(0,110,10):
    print(f"midterm {p}-th percentile : {np.percentile(df.midterm,p)}")
print("")
for p in range(0,110,10):
    print(f"final {p}-th percentile : {np.percentile(df.final,p)}")
print("")
for p in range(0,110,10):
    print(f"score {p}-th percentile : {np.percentile(df.score,p)}")
