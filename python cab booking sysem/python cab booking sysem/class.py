import matplotlib.pyplot as plt
import seaborn as sns
tips=sns.load_dataset("tips")
g=sns.PairGrid(tips)
g=g.map(plt.scatter)