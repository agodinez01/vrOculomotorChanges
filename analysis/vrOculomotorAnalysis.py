import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as matplotlib
from scipy import stats

#Load variables
os.chdir('C:/Users/angie/Git Root/vrOculomotorChanges/data')
allData = pd.read_csv('subjectData.csv')
myopiaClassification = pd.read_csv('myopiaClassification.csv')
results_dir = "C:/Users/angie/Git Root/vrOculomotorChanges/figs/"

vergenceTable = allData.loc[allData.measure=='vergence']

#Plot params
font= {'weight': 'bold', 'size': 20}
matplotlib.rc('font', **font)
sns.set('poster', palette='colorblind')
sns.set_style('white')

subjects = myopiaClassification.subject.unique()

def addMyopia():
    for sub in subjects:
        allData['myopia'] = myopiaClassification.myopia[myopiaClassification.subject==sub]
    return allData

addMyopia()

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

    # sns.lmplot(x='x_vals', y='y_vals', data=myopiaDF, hue='condition', fit_reg=False, palette='colorblind')
    # plt.plot([0, 40], [0, 40], 'k--')
    # #plt.text(25, 5, s='p= %.5s' %deltap, style='italic', size='x-small')
    # plt.text(25, 4, s='VR: p= %.5s' % VRp, style='italic', size='xx-small')
    # plt.text(25, 1, s='PC: p= %.5s' %PCp, style='italic', size='xx-small')
    # plt.yticks(np.arange(10, max(myopiaDF.y_vals) + 10, step=10))
    # plt.xticks(np.arange(10, max(myopiaDF.x_vals) + 10, step=10))
    # #plt.title(title)
    #
    # #xLabelPlot = '(\u0394) Vergence'
    # #plt.xlabel('Pre Test ' + xLabelPlot)
    # plt.xlabel('Baseline vergence')
    # #yLabelPlot = '(\u0394) Vergence'
    # plt.ylabel('Post-task vergence')
    #
    # plt.savefig(fname=results_dir + title.replace(" ", "") + '_scatterplot.pdf', bbox_inches='tight', format='pdf', dpi=300)
    # plt.show()
    #
    # plt.clf()
    #
    # sns.violinplot(x='condition', y='delta', data=myopiaDF, palette='colorblind')
    # plt.ylabel('\u0394 Vergence')
    # #plt.title(title)
    # plt.text(0.30, -8, s='p= %.5s' % deltap, style='italic', size='x-small')
    #
    # plt.savefig(fname=results_dir + title.replace(" ", "") + '_boxplot.pdf', bbox_inches='tight', format='pdf', dpi=300)
    # plt.show()
    #
    # plt.clf()
    #
    # sns.lmplot(x=myopiaDF.delta[myopiaDF.condition=='PC'], y=myopiaDF.delta[myopiaDF.condition=='VR'], data=myopiaDF, hue='myopia', palette='colorblind')

def ttestAnalysis(preVerVR, postVerVR, preVerPC, postVerPC):
    [VRval, VRp] = stats.ttest_rel(preVerVR, postVerVR)
    [PCval, PCp] = stats.ttest_rel(preVerPC, postVerPC)

    deltaVR = np.subtract(postVerVR, preVerVR)
    deltaPC = np.subtract(postVerPC, preVerPC)

    [deltaVal, deltap] = stats.ttest_rel(deltaVR, deltaPC)

    vrChangeMean = np.mean(deltaVR)
    pcChangeMean = np.mean(deltaPC)

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