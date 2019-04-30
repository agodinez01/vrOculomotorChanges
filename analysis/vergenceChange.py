import os
import pandas as pd
import seaborn as sns
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# This script analyzes whether vergence in general is changing. Meaning both convergence and divergence are
# expanding or whether only convergence ranges are changing. Script makes plots and saves them in
# project_path/figs/vergence.

#Load variables
os.chdir('C:/Users/angie/Git Root/vrOculomotorChanges/data')
allData = pd.read_csv('subjectData.csv')
results_dir = "C:/Users/angie/Git Root/vrOculomotorChanges/figs/vergence/"

dataFrame = allData.loc[(allData.measure == 'vergence') & (allData.condition == 'VR')]
dataFrame = dataFrame.drop(columns=['measure', 'condition'])

distanceVals = dataFrame.distance.unique()
blrDblVals = dataFrame.blurDouble.unique()
baseVals = dataFrame.base.unique()

#unique vals
subjects = dataFrame.subject[0:20].tolist()
myopia = dataFrame.myopia[0:20].tolist()

def scatterPlot(x, y, dataFrame, hue, title):
    # Plot params
    font = {'weight': 'bold', 'size': 20}
    matplotlib.rc('font', **font)
    sns.set('poster', palette='colorblind')
    sns.set_style('whitegrid')

    #TODO: Make sure x and y labels work.
    sns.scatterplot(x=x, y=y, data=dataFrame, hue=hue)
    plt.xlabel('Convergence change (\u0394)')
    plt.ylabel('Divergence change (\u0394)')

    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., fontsize='xx-small')
    plt.hlines(0, min(dataFrame[x]), max(dataFrame[x]))
    plt.vlines(0, min(dataFrame[y]), max(dataFrame[y]))

    plt.savefig(fname=results_dir + title + '.pdf', bbox_inches='tight',
                format='pdf', dpi=300)
    plt.show()

for blrDbl in blrDblVals:
    for distance in distanceVals:
        convergenceDelta = np.subtract(dataFrame.vals[(dataFrame.order == 'post') & (dataFrame.base == 'out') &
                                                      (dataFrame.blurDouble == blrDbl) & (dataFrame.distance == distance)],
                                       dataFrame.vals[(dataFrame.order == 'pre') & (dataFrame.base == 'out') &
                                                      (dataFrame.blurDouble == blrDbl) & (dataFrame.distance == distance)]).tolist()

        divergenceDelta = np.subtract(dataFrame.vals[(dataFrame.order == 'post') & (dataFrame.base == 'in') &
                                                     (dataFrame.blurDouble == blrDbl) & (dataFrame.distance == distance)],
                                      dataFrame.vals[(dataFrame.order == 'pre') & (dataFrame.base == 'in') &
                                                     (dataFrame.blurDouble == blrDbl) & (dataFrame.distance == distance)]).tolist()

        d = {'subject': subjects, 'myopiaStatus': myopia, 'convergenceDelta': convergenceDelta, 'divergenceDelta': divergenceDelta}
        frame = pd.DataFrame(d)

        if (blrDbl == 'blur') & (distance == 'near'):
            plotTitle = 'Near blur'
        elif (blrDbl == 'blur') & (distance == 'far'):
            plotTitle = 'Far blur'
        elif (blrDbl == 'double') & (distance == 'near'):
            plotTitle = 'Near break'
        elif (blrDbl == 'double') & (distance == 'far'):
            plotTitle = 'Far break'

        print(plotTitle)
        scatterPlot('convergenceDelta', 'divergenceDelta', frame, 'myopiaStatus', plotTitle)
