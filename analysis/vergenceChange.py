import os
import pandas as pd
import seaborn as sns
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#Load variables
os.chdir('C:/Users/angie/Git Root/vrOculomotorChanges/data')
allData = pd.read_csv('subjectData.csv')
results_dir = "C:/Users/angie/Git Root/vrOculomotorChanges/figs/vergence/"

nearBreakTable = allData.loc[(allData.measure=='vergence') & (allData.distance=='near') & (allData.blurDouble=='blur')
                             & (allData.condition=='VR')]
nearBreakTable = nearBreakTable.drop(columns=['measure', 'distance', 'blurDouble', 'condition'])

convergenceDelta = np.subtract(nearBreakTable.vals[(nearBreakTable.order=='post') & (nearBreakTable.base=='out')],
                               nearBreakTable.vals[(nearBreakTable.order=='pre') & (nearBreakTable.base=='out')]).tolist()
divergenceDelta = np.subtract(nearBreakTable.vals[(nearBreakTable.order=='post') & (nearBreakTable.base=='in')],
                               nearBreakTable.vals[(nearBreakTable.order=='pre') & (nearBreakTable.base=='in')]).tolist()

#unique vals
subjects = nearBreakTable.subject[0:20].tolist()
myopia = nearBreakTable.myopia[0:20].tolist()
d = {'subject':subjects,'myopiaStatus':myopia, 'convergenceDelta':convergenceDelta, 'divergenceDelta':divergenceDelta}
frame = pd.DataFrame(d)

def scatterPlot(x, y, dataFrame, hue):
    # Plot params
    font = {'weight': 'bold', 'size': 20}
    matplotlib.rc('font', **font)
    sns.set('poster', palette='colorblind')
    sns.set_style('whitegrid')

    sns.scatterplot(x=x, y=y, data=dataFrame, hue=hue)
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., fontsize='xx-small')
    plt.hlines(0, min(dataFrame[x]), max(dataFrame[x]))
    plt.vlines(0, min(dataFrame[y]), max(dataFrame[y]))
    plt.savefig(fname=results_dir + 'BreakVergenceChange.pdf', bbox_inches='tight',
                format='pdf', dpi=300)
    plt.show()

scatterPlot('convergenceDelta', 'divergenceDelta', frame, 'myopiaStatus')

