import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

os.chdir('C:/Users/angie/Git Root/vrOculomotorChanges/data')
allData = pd.read_csv('subjectData.csv')
myopiaClassification = pd.read_csv('myopiaClassification.csv')

vergenceTable = allData.loc[allData.measure=='vergence']

#Function to make 1:1 (pre-post) plots
def makePlot(x_vals, y_vals):
    # plt.figure(1)
    #
    # plt.subplot(2, 1, 1, aspect='equal')
    # #plt.subplot(2, 1, 1, adjustable='box')
    # plt.plot([5, 45], [5, 45], 'k--')
    # plt.plot(x_vals, y_vals, 'b.')
    # plt.xticks([])
    # plt.yticks(np.arange(10, max(y_vals) + 10, step=10))
    # plt.title('blah')
    #
    # plt.subplot(2, 1, 2, aspect='equal')
    # plt.plot([5, 45], [5, 45], 'k--')
    #
    # plt.xticks(np.arange(10, max(x_vals) + 10, step=10))
    # plt.title('balh 2')
    #
    # xLabelPlot = 'Convergence Range (\u0394)'
    # plt.xlabel('Pre Test ' + xLabelPlot)
    # yLabelPlot = 'Convergence Range (\u0394)'
    # plt.ylabel('Post Test ' + yLabelPlot)
    #
    # plt.show()

    fig = plt.figure()


    ax = fig.add_subplot(1, 1, 1)
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)

    xLabelPlot = 'Convergence Range (\u0394)'
    #plt.xlabel('Pre Test ' + xLabelPlot)
    yLabelPlot = 'Convergence Range (\u0394)'
    #plt.ylabel('Post Test ' + yLabelPlot)

    ax.set_xlabel('Pre Test ' + xLabelPlot)
    #set_xlabel('Pre Test ' + xLabelPlot)
    #set_ylabel('Post Test ' + yLabelPlot)

    plt.subplot(2, 1, 1, aspect='equal')
    plt.plot([5, 45], [5, 45], 'k--')
    plt.plot(x_vals, y_vals, 'b.')
    plt.xticks([])
    plt.yticks(np.arange(10, max(y_vals) + 10, step=10))
    plt.title('blah')


    plt.subplot(2, 1, 2, aspect='equal')
    plt.plot([5, 45], [5, 45], 'k--')

    plt.xticks(np.arange(10, max(x_vals) + 10, step=10))
    plt.title('balh 2')

    plt.show()

preVerVRNearBO = vergenceTable.vals[(vergenceTable.condition=='VR') & (vergenceTable.base=='out') & (vergenceTable.distance=='near') & (vergenceTable.order=='pre') & (vergenceTable.blurDouble=='blur')]
postVerVRNearBO = vergenceTable.vals[(vergenceTable.condition=='VR') & (vergenceTable.base=='out') & (vergenceTable.distance=='near') & (vergenceTable.order=='post') & (vergenceTable.blurDouble=='blur')]

makePlot(preVerVRNearBO, postVerVRNearBO)


allData