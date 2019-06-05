import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as matplotlib
from scipy import stats
import matplotlib.patches as mpatches

#Load variables
os.chdir('C:/Users/angie/Git Root/vrOculomotorChanges/data')
allData = pd.read_csv('subjectData.csv')
myopiaClassification = pd.read_csv('myopiaClassification.csv')
results_dir = "C:/Users/angie/Git Root/vrOculomotorChanges/figs/individualPlots/"

vergenceTable = allData.loc[allData.measure=='vergence']

#Plot params
font= {'weight': 'bold', 'size': 20}
matplotlib.rc('font', **font)
sns.set('poster', palette='colorblind')
sns.set_style('white')

subjects = myopiaClassification.subject.unique()

#Function to make 1:1 (pre-post) plots comparing VR and PC values
#Result 1. Increase in convergence blur range at near (BO prism) in VRHMD condition compared to PC.
def makePlot(VRx_vals, VRy_vals, PCx_vals, PCy_vals, title):
    print(title)

    [VRval, VRp, PCval, PCp, deltaVal, deltap] = ttestAnalysis(VRx_vals, VRy_vals, PCx_vals, PCy_vals)
    #TODO: Add ttest p values to figures

    VRy_vals = VRy_vals.tolist()
    PCx_vals = PCx_vals.tolist()
    PCy_vals = PCy_vals.tolist()

    myopiaDF = np.vstack((myopiaClassification, myopiaClassification))
    myopiaDF = pd.DataFrame(myopiaDF)
    myopiaDF.columns = ['subject', 'myopia']

    vrLable = ['VR'] * len(VRx_vals)
    pcLable = ['PC'] * len(PCx_vals)

    myopiaDF['x_vals'] = np.hstack((VRx_vals, PCx_vals))
    myopiaDF['y_vals'] = np.hstack((VRy_vals, PCy_vals))
    myopiaDF['condition'] = np.hstack((vrLable, pcLable))
    myopiaDF['delta'] = myopiaDF['y_vals'] - myopiaDF['x_vals']

    sns.lmplot(x='x_vals', y='y_vals', data=myopiaDF, hue='condition', fit_reg=False, palette='colorblind')
    plt.plot([0, 40], [0, 40], 'k--')
    #plt.text(25, 5, s='p= %.5s' %deltap, style='italic', size='x-small')
    plt.text(25, 4, s='VR: p= %.5s' % VRp, style='italic', size='xx-small')
    plt.text(25, 1, s='PC: p= %.5s' %PCp, style='italic', size='xx-small')
    plt.yticks(np.arange(10, max(myopiaDF.y_vals) + 10, step=10))
    plt.xticks(np.arange(10, max(myopiaDF.x_vals) + 10, step=10))
    #plt.title(title)

    #xLabelPlot = '(\u0394) Vergence'
    #plt.xlabel('Pre Test ' + xLabelPlot)
    plt.xlabel('Pre-task vergence')
    #yLabelPlot = '(\u0394) Vergence'
    plt.ylabel('Post-task vergence')

    plt.savefig(fname=results_dir + title.replace(" ", "") + '_scatterplot.pdf', bbox_inches='tight', format='pdf', dpi=300)
    #plt.show()

    plt.clf()

    sns.violinplot(x='condition', y='delta', data=myopiaDF, palette='colorblind')
    plt.ylabel('\u0394 Vergence')
    #plt.title(title)
    plt.text(0.30, -8, s='p= %.5s' % deltap, style='italic', size='x-small')

    plt.savefig(fname=results_dir + title.replace(" ", "") + '_boxplot.pdf', bbox_inches='tight', format='pdf', dpi=300)
    #plt.show()

def ttestAnalysis(preVerVR, postVerVR, preVerPC, postVerPC):
    [VRval, VRp] = stats.ttest_rel(preVerVR, postVerVR)
    [PCval, PCp] = stats.ttest_rel(preVerPC, postVerPC)

    deltaVR = np.subtract(postVerVR, preVerVR)
    deltaPC = np.subtract(postVerPC, preVerPC)

    [deltaVal, deltap] = stats.ttest_rel(deltaVR, deltaPC)

    vrChangeMean = np.mean(deltaVR)
    pcChangeMean = np.mean(deltaPC)

    vrPositiveChange = np.mean([x for x in deltaVR if x > 0])
    vrNegativeChange = np.mean([x for x in deltaVR if x < 0])
    pcPositiveChange = np.mean([x for x in deltaPC if x > 0])
    pcNegativeChange = np.mean([x for x in deltaPC if x < 0])


    print('vrPositiveChange = %s' % vrPositiveChange, 'vrNegativeChange = %s' % vrNegativeChange,
          'pcPositiveChange = %s' % pcPositiveChange, 'pcNegativeChange = %s' % pcNegativeChange)

    #TODO: T-test of the difference between pre and post for PC and VR
    print('vrChangeMean = %s' % vrChangeMean, 'VRp = %s' % VRp, 'pcChangeMean = %s' % pcChangeMean, 'PCp = %s' % PCp, 'deltaVal = %s' % deltaVal, 'deltap = %s' % deltap)
    return(VRval, VRp, PCval, PCp, deltaVal, deltap)


#Make plots
distanceVals = vergenceTable.distance.unique()
conditionVals = vergenceTable.condition.unique()
blrDblVals = vergenceTable.blurDouble.unique()
baseVals = vergenceTable.base.unique()
orderVals = vergenceTable.order.unique()

def getVals_Plot():
    plotTitle = []

    for blrDbl in blrDblVals:
        for base in baseVals:
            for distance in distanceVals:
                preVerVR = vergenceTable.vals[
                    (vergenceTable.distance==distance) & (vergenceTable.condition=='VR') & ( vergenceTable.order=='pre') & (vergenceTable.blurDouble==blrDbl) & (vergenceTable.base==base)]
                postVerVR = vergenceTable.vals[
                    (vergenceTable.distance==distance) & (vergenceTable.condition=='VR') & ( vergenceTable.order=='post') & (vergenceTable.blurDouble==blrDbl) & (vergenceTable.base==base)]
                preVerPC = vergenceTable.vals[
                    (vergenceTable.distance==distance) & (vergenceTable.condition=='PC') & ( vergenceTable.order=='pre') & (vergenceTable.blurDouble==blrDbl) & (vergenceTable.base==base)]
                postVerPC = vergenceTable.vals[
                    (vergenceTable.distance==distance) & (vergenceTable.condition=='PC') & (vergenceTable.order=='post') & (vergenceTable.blurDouble==blrDbl) & (vergenceTable.base==base)]

                if (blrDbl=='blur') & (base=='out'):
                    plotTitle = 'BO ' + distance + ' Blur'
                elif (blrDbl=='blur') & (base=='in'):
                    plotTitle = 'BI ' + distance +' Blur'
                elif (blrDbl=='double') & (base=='out'):
                    plotTitle = 'BO ' + distance + ' Double'
                elif (blrDbl=='double') & (base=='in'):
                    plotTitle = 'BI ' + distance + ' Double'

                makePlot(preVerVR, postVerVR, preVerPC, postVerPC, plotTitle)

    return preVerVR, postVerVR, preVerPC, postVerPC, plotTitle

getVals_Plot()

distanceVals

plt.clf()

def noDataFigs(type):
    font = {'weight': 'bold', 'size': 20}
    matplotlib.rc('font', **font)
    sns.set('poster', palette='colorblind')
    sns.set_style('white')

    plt.plot([0, 40], [0, 40], 'k--')
    plt.yticks(np.arange(10, 50, step=10))
    plt.xticks(np.arange(10, 50, step=10))

    plt.xlabel('Pre-task vergence')
    plt.ylabel('Post-task vergence')

    if type == 'blank':
        plt.savefig(fname=results_dir + 'NoDataFig1' + '.png', bbox_inches='tight', format='png', dpi=300)

    if type == 'triangles':
        triangle1 = mpatches.Polygon(np.array([[0, 0], [0, 40], [40, 40]]), fc="mediumAquaMarine")
        triangle2 = mpatches.Polygon(np.array([[40, 40], [40, 0], [0, 0]]), fc='salmon')

        ax = plt.axes([0, 0, 1, 1])
        ax.add_artist(triangle1)
        ax.add_artist(triangle2)

        plt.plot([0, 40], [0, 40], 'k--')
        plt.yticks(np.arange(10, 50, step=10))
        plt.xticks(np.arange(10, 50, step=10))

        plt.xlabel('Pre-task vergence')
        plt.ylabel('Post-task vergence')

        plt.savefig(fname=results_dir + 'NoDataFig1_triangles' + '.png', bbox_inches='tight', format='png', dpi=300)

        plt.clf()

noDataFigs('blank')
noDataFigs('triangles')

#plt.show()

#plt.savefig(fname=results_dir + 'NoDataFig1_triangles' + '.png', bbox_inches='tight', format='png', dpi=300)
