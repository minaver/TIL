import numpy as np
import pandas as pd
from scipy.stats import mode
import matplotlib.pyplot as plt

xl_file = 'db_score.xlsx'
df = pd.read_excel(xl_file)

# (5) boxplot (midterm, final, score 각각)
print("\n(5) boxplot (midterm, final, score 각각)")
boxplot = df.boxplot(column=['midterm', 'final', 'score'],grid=False)

boxplot.plot()
plt.show()

# (6) histogram (midterm, final, score 각각)
print("\n(6) histogram (midterm, final, score 각각)")
mid_hist = df.midterm.plot.hist()
plt.xlabel('midterm')
plt.show()
fin_hist = df.final.plot.hist()
plt.xlabel('final')
plt.show()
scr_hist = df.score.plot.hist()
plt.xlabel('score')
plt.show()

# (7) scatter plot (midterm, final, score 에 대한, 모든 가능한 attribute 조합에 대하여 그릴 것)
print("\n(7) scatter plot (midterm, final, score 에 대한, 모든 가능한 attribute 조합에 대하여 그릴 것)")
plt.scatter(df.midterm,df.final)
plt.xlabel('midterm')
plt.ylabel('final')
plt.show()

plt.scatter(df.final,df.score)
plt.xlabel('fianl')
plt.ylabel('score')
plt.show()

plt.scatter(df.midterm,df.score)
plt.xlabel('midterm')
plt.ylabel('score')
plt.show()