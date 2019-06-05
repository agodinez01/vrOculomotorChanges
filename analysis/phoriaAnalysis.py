import os
import pandas as pd
import seaborn as sns
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

#Load variables
os.chdir('C:/Users/angie/Git Root/vrOculomotorChanges/data')
allData = pd.read_csv('subjectData.csv')
results_dir = "C:/Users/angie/Git Root/vrOculomotorChanges/figs/"

phoriaTable = allData.loc[allData.measure == 'phoria']
phoriaTable = phoriaTable.drop(columns=['base', 'measure', 'blurDouble'])

#Plot params
font= {'weight': 'bold', 'size': 20}
matplotlib.rc('font', **font)
sns.set('poster', palette='colorblind')
sns.set_style('white')

subjects = phoriaTable.subject.unique()
distanceVals = phoriaTable.distance.unique()
conditionVals = phoriaTable.condition.unique()

def scatterPlot(x, y, dataFrame, hue, title):
    # Plot params
    font = {'weight': 'bold', 'size': 20}
    matplotlib.rc('font', **font)
    sns.set('poster', palette='colorblind')
    sns.set_style('whitegrid')

    #TODO: Make sure x and y labels work.
    sns.scatterplot(x=x, y=y, data=dataFrame, hue=hue)
    plt.xlabel('Pre task phoria')
    plt.ylabel('Post task phoria')

    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., fontsize='xx-small')
    plt.plot([-20, 20], [-20, 20], 'k--')
    plt.hlines(0, -20, 20)
    plt.vlines(0, -20, 20)
    #plt.hlines(0, min(dataFrame[x]), max(dataFrame[x]))
    #plt.vlines(0, min(dataFrame[y]), max(dataFrame[y]))
    plt.title(title)

    plt.savefig(fname=results_dir + title + '.png', bbox_inches='tight',
                format='png', dpi=300)
    plt.clf()
    #plt.show()

for distance in distanceVals:
    dataFrame = phoriaTable.loc[phoriaTable.distance == distance]

    vrPreVals = dataFrame.vals[(dataFrame.order == 'pre') & (dataFrame.condition == 'VR')].tolist()
    pcPreVals = dataFrame.vals[(dataFrame.order == 'pre') & (dataFrame.condition == 'PC')].tolist()

    vrPostVals = dataFrame.vals[(dataFrame.order == 'post') & (dataFrame.condition == 'VR')].tolist()
    pcPostVals = dataFrame.vals[(dataFrame.order == 'post') & (dataFrame.condition == 'PC')].tolist()

    subjects = dataFrame.subject[(dataFrame.order == 'pre') & (dataFrame.condition == 'VR')].tolist()

    d = {'subject': subjects, 'vrPreVals': vrPreVals, 'pcPreVals': pcPreVals, 'vrPostVals': vrPostVals, 'pcPostVals': pcPostVals}
    frame = pd.DataFrame(d)

    if distance == 'near':
        plotTitle = 'Near'
    elif distance == 'far':
        plotTitle = 'Far'

    print(plotTitle)
    scatterPlot('vrPreVals', 'vrPostVals', frame, 'subject', plotTitle + ' VR')
    scatterPlot('pcPreVals', 'pcPostVals', frame, 'subject', plotTitle + ' PC')

def noDataFigs(type):
    font = {'weight': 'bold', 'size': 20}
    matplotlib.rc('font', **font)
    sns.set('poster', palette='colorblind')
    sns.set_style('whitegrid')

    plt.hlines(0, -20, 20)
    plt.vlines(0, -20, 20)
    plt.plot([-20, 20], [-20, 20], 'k--')

    plt.xlabel('Pre task phoria')
    plt.ylabel('Post task phoria')

    if type == 'blank':
        plt.savefig(fname=results_dir + 'NoDataFig2' + '.png', bbox_inches='tight',
                    format='png', dpi=300)

    elif type == 'triangles':
        triangle1 = mpatches.Polygon(np.array([[-20,-20],[-20,20],[20,20]]), fc="mediumAquaMarine")
        triangle2 = mpatches.Polygon(np.array([[20, 20], [20, -20], [-20, -20]]), fc='salmon')

        ax = plt.axes([0,0,1,1])
        ax.add_artist(triangle1)
        ax.add_artist(triangle2)

        plt.hlines(0, -20, 20)
        plt.vlines(0, -20, 20)
        plt.plot([-20, 20], [-20, 20], 'k--')

        plt.savefig(fname=results_dir + 'NoDataFig2_triangles' + '.png', bbox_inches='tight',
                    format='png', dpi=300)
        plt.clf()

noDataFigs('blank')
noDataFigs('triangles')


