import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

os.chdir('C:/Users/angie/Git Root/vrOculomotorChanges/data')
allData = pd.read_csv('subjectData.csv')
myopiaClassification = pd.read_csv('myopiaClassification.csv')
results_dir = "C:/Users/angie/Git Root/vrOculomotorChanges/figs/"

vergenceTable = allData.loc[allData.measure=='vergence']

#Function to make 1:1 (pre-post) plots comparing VR and PC values
#Result 1. Increase in convergence blur range at near (BO prism) in VRHMD condition compared to PC.
def makePlot(VRx_vals, VRy_vals, PCx_vals, PCy_vals, title):
    print(title)

    ttestAnalysis(VRx_vals, VRy_vals, PCx_vals, PCy_vals)

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
    # conditionMeans = myopiaDF.groupby(myopiaDF.condition).mean()
    # conditionStd = myopiaDF.groupby(myopiaDF.condition).std()

    sns.lmplot(x='x_vals', y='y_vals', data=myopiaDF, hue='condition', fit_reg=False, palette='colorblind')
    plt.plot([5, 40], [5, 40], 'k--')
    #plt.plot(conditionMeans.x_vals, conditionMeans.y_vals)

    plt.yticks(np.arange(10, max(myopiaDF.y_vals) + 10, step=10))
    plt.xticks(np.arange(10, max(myopiaDF.x_vals) + 10, step=10))
    plt.title(title + ' Scatterplot')

    xLabelPlot = 'Convergence Range (\u0394)'
    plt.xlabel('Pre Test ' + xLabelPlot)
    yLabelPlot = 'Convergence Range (\u0394)'
    plt.ylabel('Post Test ' + yLabelPlot)

    plt.savefig(fname=results_dir + title.replace(" ", "") + '_scatterplot.png', bbox_inches='tight', format='png', dpi=None)
    plt.show()

    plt.clf()

    sns.violinplot(x='condition', y='delta', data=myopiaDF, palette='colorblind')
    plt.text(0.5, 0.5, )
    plt.ylabel('Change after task')
    plt.title(title + ' Violin Plot')

    plt.savefig(fname=results_dir + title.replace(" ", "") + '_boxplot.png', bbox_inches='tight', format='png', dpi=None)
    plt.show()

def ttestAnalysis(preVerVR, postVerVR, preVerPC, postVerPC):
    [VRval, VRp] = stats.ttest_rel(preVerVR, postVerVR)
    [PCval, PCp] = stats.ttest_rel(preVerPC, postVerPC)

    print(VRval, VRp, PCval, PCp)


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
