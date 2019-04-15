import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt

os.chdir('C:/Users/angie/Git Root/vrOculomotorChanges/data')
allData = pd.read_csv('subjectData.csv')

vergenceTable = allData.loc[allData.measure=='vergence']

allData