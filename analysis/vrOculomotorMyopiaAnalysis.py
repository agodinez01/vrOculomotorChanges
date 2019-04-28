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
results_dir = "C:/Users/angie/Git Root/vrOculomotorChanges/figs/VRPC/"

vergenceTable = allData.loc[allData.measure=='vergence']
vergenceTable = vergenceTable.drop(columns='measure')

#Plot params
font= {'weight': 'bold', 'size': 20}
matplotlib.rc('font', **font)
sns.set('poster', palette='colorblind')

#Unique vals
subjects = vergenceTable.subject[0:20]
distanceVals = vergenceTable.distance.unique()
conditionVals = vergenceTable.condition.unique()
blrDblVals = vergenceTable.blurDouble.unique()
baseVals = vergenceTable.base.unique()
orderVals = vergenceTable.order.unique()
myopiaLabel = vergenceTable.myopia.unique()
myopiaArray = vergenceTable.myopia[0:20]

def makeDF(VR_near, VR_far, PC_near, PC_far, title):

    VR_near = VR_near.tolist()
    VR_far = VR_far.tolist()
    PC_near = PC_near.tolist()
    PC_far = PC_far.tolist()

    #frame = pd.DataFrame(np.hstack((subjects, subjects, subjects, subjects)))
    frame = pd.DataFrame(np.hstack(([subjects] * 4)))
    frame.columns= ['subject']
    frame['myopia'] = np.hstack(([myopiaArray] * 4))

    vrLabel = ['VR'] * len(VR_near) * 2
    pcLabel = ['PC'] * len(PC_near) * 2
    nearLabel = ['near'] * len(VR_near)
    farLabel = ['far'] * len(VR_near)

    frame['delta'] = np.hstack((VR_near, VR_far, PC_near, PC_far))
    frame['condition'] = np.hstack((vrLabel, pcLabel))
    frame['distance'] = np.hstack((nearLabel, farLabel, nearLabel, farLabel))

    frame2 = pd.DataFrame(subjects)
    frame2.columns = ['subject']
    frame2['myopia'] = myopiaArray
    frame2['pcNearDelta'] = PC_near
    frame2['pcFarDelta'] = PC_far
    frame2['vrNearDelta'] = VR_near
    frame2['vrFarDelta'] = VR_far

    grouped = frame2.groupby(['myopia'])
    print(grouped.mean())
    print(grouped.median())
    print(grouped.std())

    makePlot(frame, title, frame2)
    makeScatterPlot(title, frame2)

def makeScatterPlot(title, DF2):
    print(title)

    sns.set_style('whitegrid')
    sns.scatterplot(x='pcNearDelta', y='vrNearDelta', hue='myopia', data=DF2, palette='dark', legend=False)
    plt.yticks(np.arange(-30, 30, step=10))
    plt.hlines(0, -30, 30)
    plt.vlines(0, -30, 30)
    plt.xlabel('PC \u0394 Vergence')
    plt.ylabel('VR \u0394 Vergence')
    plt.plot([-30, 30], [-30, 30], 'k--')

    plt.savefig(fname=results_dir + 'myopia_' + title.replace(" ", "") + '_NearScatter.pdf', bbox_inches='tight',
                format='pdf', dpi=300)
    plt.clf()

def makePlot(DF, title, DF2):
    print(title)

    [nearVal, nearP] = stats.ttest_rel(DF.delta[(DF.distance=='near') & (DF.condition=='VR')], DF.delta[(DF.distance == 'near') & (DF.condition == 'PC')])
    [farVal, farP] = stats.ttest_rel(DF.delta[(DF.distance == 'far') & (DF.condition == 'VR')], DF.delta[(DF.distance == 'far') & (DF.condition == 'PC')])

    #TODO: Find statistical test to show significant difference between myopia vs no-myopia

    font = {'weight': 'bold', 'size': 20}
    matplotlib.rc('font', **font)
    sns.set('poster')
    sns.set_style('whitegrid')
    sns.scatterplot(x='pcFarDelta', y='vrFarDelta', hue='myopia', data=DF2, legend=False, palette='dark')

    plt.yticks(np.arange(-30, 30, step=10))
    plt.hlines(0, -30, 30)
    plt.vlines(0, -30, 30)
    plt.xlabel('PC \u0394 Vergence')
    plt.ylabel('VR \u0394 Vergence')
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., fontsize='xx-small')
    plt.plot([-30, 30], [-30, 30], 'k--')
    #plt.text(5, -5, s='p= %.5s' % farPVal, style='italic', size='xx-small')
    plt.savefig(fname=results_dir + 'myopia_' + title.replace(" ", "") + '_FarScatter.pdf', bbox_inches='tight',
                format='pdf', dpi=300)
    plt.clf()

def getVals4Plot():
    plotTitle = []

    for blrDbl in blrDblVals:
        for base in baseVals:
            preVerNearVR = vergenceTable.vals[(vergenceTable.distance == 'near') & (vergenceTable.condition == 'VR') & (vergenceTable.order=='pre') &
                                              (vergenceTable.blurDouble == blrDbl) & (vergenceTable.base == base)]
            postVerNearVR = vergenceTable.vals[(vergenceTable.distance == 'near') & (vergenceTable.condition == 'VR') & (vergenceTable.order=='post') &
                                               (vergenceTable.blurDouble == blrDbl) & (vergenceTable.base == base)]
            preVerNearPC = vergenceTable.vals[(vergenceTable.distance == 'near') & (vergenceTable.condition == 'PC') & (vergenceTable.order=='pre') &
                                              (vergenceTable.blurDouble == blrDbl) & (vergenceTable.base == base)]
            postVerNearPC = vergenceTable.vals[(vergenceTable.distance =='near') & (vergenceTable.condition == 'PC') & (vergenceTable.order=='post') &
                                               (vergenceTable.blurDouble == blrDbl) & (vergenceTable.base == base)]

            preVerFarVR = vergenceTable.vals[(vergenceTable.distance == 'far') & (vergenceTable.condition == 'VR') & (vergenceTable.order == 'pre') &
                                             (vergenceTable.blurDouble == blrDbl) & (vergenceTable.base == base)]
            postVerFarVR = vergenceTable.vals[(vergenceTable.distance == 'far') & (vergenceTable.condition == 'VR') & (vergenceTable.order == 'post') &
                                              (vergenceTable.blurDouble == blrDbl) & (vergenceTable.base == base)]
            preVerFarPC = vergenceTable.vals[(vergenceTable.distance == 'far') & (vergenceTable.condition == 'PC') & (vergenceTable.order == 'pre') &
                                              (vergenceTable.blurDouble == blrDbl) & (vergenceTable.base == base)]
            postVerFarPC = vergenceTable.vals[(vergenceTable.distance == 'far') & (vergenceTable.condition == 'PC') & (vergenceTable.order == 'post') &
                                               (vergenceTable.blurDouble == blrDbl) & (vergenceTable.base == base)]

            nearVRdelta = np.subtract(postVerNearVR, preVerNearVR)
            nearPCdelta = np.subtract(postVerNearPC, preVerNearPC)

            farVRdelta = np.subtract(postVerFarVR, preVerFarVR)
            farPCdelta = np.subtract(postVerFarPC, preVerFarPC)

            if (blrDbl=='blur') & (base=='out'):
                plotTitle = 'BO ' + ' Blur'
            elif (blrDbl=='blur') & (base=='in'):
                plotTitle = 'BI ' + ' Blur'
            elif (blrDbl=='double') & (base=='out'):
                plotTitle = 'BO ' + ' Double'
            elif (blrDbl=='double') & (base=='in'):
                plotTitle = 'BI ' + ' Double'

            makeDF(nearVRdelta, farVRdelta, nearPCdelta, farPCdelta, plotTitle)
    return nearVRdelta, farVRdelta, nearPCdelta, farPCdelta, plotTitle
getVals4Plot()

allData
# preVR = vergenceTable.vals[(vergenceTable.order=='pre') & (vergenceTable.condition=='VR') & (vergenceTable.base=='out') & (vergenceTable.blurDouble=='blur') & (vergenceTable.distance=='near')]
# prePC = vergenceTable.vals[(vergenceTable.order=='pre') & (vergenceTable.condition=='PC') & (vergenceTable.base=='out') & (vergenceTable.blurDouble=='blur') & (vergenceTable.distance=='near')]
#
# baselineVergence = abs(np.subtract(preVR, prePC))
#
# postVR = vergenceTable.vals[(vergenceTable.order=='post') & (vergenceTable.condition=='VR') & (vergenceTable.base=='out') & (vergenceTable.blurDouble=='blur') & (vergenceTable.distance=='near')]
# vrDelta = abs(np.subtract(postVR, preVR))
#
# [val, p] = stats.ttest_rel(baselineVergence, vrDelta)
#
# BOdata = vergenceTable.loc[(vergenceTable.base == 'out')].drop(columns='base')

# sns.violinplot(x='distance', y='delta', hue='condition', data=DF, split=True, legend=False)
# plt.ylabel('\u0394 Vergence')
# plt.xticks([0, 1], ('Near', 'Far'))
# plt.xlabel('')
# plt.text(0.30, -6, s='near p= %.5s' % nearP, style='italic', size='xx-small')
# plt.text(0.30, -10, s='far p= %.5s' % farP, style='italic', size='xx-small')
# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., fontsize='xx-small')
# plt.savefig(fname=results_dir + 'VRPC_' + title.replace(" ", "") + '_boxplot.pdf', bbox_inches='tight', format='pdf', dpi=300)


# plt.figure(figsize=(15, 5))
# sns.boxplot(x='subject', y='delta', data=DF, hue='myopia')
# locs, labels = plt.xticks()
# plt.xticks(np.arange(0, 19, step=1), (np.arange(1, 20)))
# plt.ylabel('\u0394 Vergence')
# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., fontsize='x-small')
# plt.savefig(fname=results_dir + 'subject_' + title.replace(" ", "") + '_boxplot.pdf', bbox_inches='tight',
#             format='pdf', dpi=300)
# plt.clf()

