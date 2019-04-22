import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols

main_dir = main_dir = "C:/Users/angie/Git Root/StereoTraining/"
results_dir = "C:/Users/angie/Git Root/StereoTraining/violinPlot/figs/"
allData = pd.read_pickle(main_dir + 'processed_data.pkl')

#anova
formula = 'group'

a = allData