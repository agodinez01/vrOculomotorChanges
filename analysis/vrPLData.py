import pandas as pd
import numpy as np

subject = ['jg', 'sd', 'as', 'jz', 'ri', 'am', 'wc', 'cs', 'aq', 'ez', 'cw', 'jk', 'gr', 'lf', 'aa', 'ns', 'er', 'cm', 'eb', 'rr']
myopia = ['noMyopia', 'noMyopia', 'noMyopia', 'myopia', 'noMyopia', 'noMyopia', 'noMyopia', 'noMyopia', 'myopia', 'myopia', 'myopia', 'myopia', 'noMyopia', 'myopia', 'noMyopia', 'myopia', 'myopia', 'myopia', 'myopia', 'noMyopia']
subjects = np.hstack([subject]*11)

#Measures taken before VR
verNearBO_blr = [16, 14, 10, 12, 10, 27.5, 12, 12, 14, 11, 21.5, 20.5, 11, 16, 11, 25, 40, 7, 9, 11]
verFarBO_blr = [20, 10, 9, 12, 25, 22.5, 10, 10, 13, 18, 16, 12, 21.5, 20, 7, 22.5, 32.5, 9, 8, 11]
vergenceBoBlr = np.hstack((verNearBO_blr, verFarBO_blr))
verLabelB = ['blur'] * len(vergenceBoBlr)

verNearBO_dbl = [32.5, 22.5, 22.5, 27.5, 20, 40, 18, 22.5, 22.5, 21.5, 30, 40, 17, 22.5, 15, 25, 40, 35, 35, 13]
verFarBO_dbl = [27.5, 19, 19, 22.5, 22.5, 40, 15, 18, 15, 25, 25, 40, 27.5, 30, 9, 22.5, 40, 17, 14, 14]
vergenceBoDbl = np.hstack((verNearBO_dbl, verFarBO_dbl))
verLabelD = ['double'] * len(vergenceBoBlr)

verNearBI_blr = [10, 11, 9, 6, 8, 19, 6, 6, 15, 7, 14, 6, 7, 9, 8, 25, 12, 7, 3, 6]
verFarBI_blr = [5, 7, 4, 6, 8, 14, 5, 6, 11, 9, 12, 5, 6, 4, 6, 15, 9, 5, 2, 7]
vergenceBiBlr = np.hstack((verNearBI_blr, verFarBI_blr))

verNearBI_dbl = [13, 11, 15, 11, 12, 32.5, 10, 11, 20, 17, 16, 13, 11, 14, 8, 25, 12, 10, 9, 9]
verFarBI_dbl = [7, 7, 6, 10, 10, 22.5, 7, 10, 18, 13, 12, 7, 9, 6, 8, 15, 9, 5, 4, 8]
vergenceBiDbl = np.hstack((verNearBI_dbl, verFarBI_dbl))

accomAmp = [15, 13.15, 10.1, 13, 15, 11.6, 11.9, 10.15, 13.25, 16.1, 12.75, 16.75, 13.15, 11.5, 10.75, 11, 15.15, 13.2, 15.05, 13.8]
accLabel = ['accommodation'] * len(accomAmp)
accDistance = ['none'] * len(accomAmp)
accNF = ['none'] * len(accomAmp)
accBD = ['none'] * len(accomAmp)

phoriaNear = [4.5, -3.5, -1.5, 6, -1.5, -10, -2, -2, -13, -3.5, -4, 5, -4, 2, -2, -18, -0.75, -3, 1, -1]
phoriaFar = [-0.5, -0.75, 2.5, 1, 0.25, -2.5, 1, -0.5, -4, 0.75, -3, 3.5, 0.25, 2.25, -1, -4, 0.5, -0.5, 2.25, 1.25]
phoria = np.hstack((phoriaNear, phoriaFar))
testP = ['phoria'] * len(phoria)
phoBD = ['none'] * len(phoria)

labelN = ['near'] * len(phoriaNear)
labelF = ['far'] * len(phoriaFar)
distanceP = np.hstack((labelN, labelF))

vergenceBo = np.hstack((vergenceBoBlr, vergenceBoDbl))
vergenceBi = np.hstack((vergenceBiBlr, vergenceBiDbl))
verLabel = np.hstack((verLabelB, verLabelD))
distance = np.hstack([distanceP]*4)

baseO = ['out'] * len(vergenceBo)
baseI = ['in'] * len(vergenceBi)

vergence = np.hstack((vergenceBo, vergenceBi))
testV = ['vergence'] * len(vergence)
base1 = np.hstack((baseO, baseI))

baseP = ['none'] * len(phoria)

vals = np.hstack((vergence, phoria, accomAmp))
test = np.hstack((testV, testP, accLabel))
base = np.hstack((base1, baseP, accNF))
verBlrDbl = np.hstack((verLabel, verLabel, phoBD, accBD))
distance = np.hstack((distance, distanceP, accDistance))


data = {'subject':subjects, 'vals':vals, 'measure':test, 'base':base, 'blurDouble':verBlrDbl, 'distance':distance}

df = pd.DataFrame(data)
df['condition'] = 'VR'
df['order'] = 'pre'

#Measures taken after VR
verNearBO_blr = [21.5, 18, 17, 12, 13, 27.5, 14, 14, 20, 15, 19, 16, 22.5, 21.5, 9, 30, 40, 12, 8, 14]
verFarBO_blr = [27.5, 14, 14, 11, 20, 40, 10, 11, 13, 12, 25, 9, 22.5, 19, 12, 27.5, 30, 13, 7, 22.5]
vergenceBoBlr = np.hstack((verNearBO_blr, verFarBO_blr))

verNearBO_dbl = [40, 32.5, 27.5, 22.5, 20, 40, 20, 27.5, 20, 19, 25, 40, 27.5, 27.5, 13, 30, 40, 40, 40, 18]
verFarBO_dbl = [32.5, 25, 20, 20, 40, 40, 16, 25, 13, 25, 25, 40, 30, 27.5, 15, 27.5, 40, 40, 16, 27.5]
vergenceBoDbl = np.hstack((verNearBO_dbl, verFarBO_dbl))

verNearBI_blr = [13, 15, 8, 7, 11, 19, 7, 7, 14, 9, 12, 8, 6, 8, 7, 18, 8, 9, 12, 8]
verFarBI_blr = [8, 6, 6, 8, 10, 23, 5, 7, 18, 5, 13, 4, 6, 6, 8, 19, 8, 5, 2, 6]
vergenceBiBlr = np.hstack((verNearBI_blr, verFarBI_blr))

verNearBI_dbl = [15, 17, 15, 12, 16, 37.5, 11, 15, 14, 19, 13, 13, 10, 12, 8, 18, 8, 10, 12, 8]
verFarBI_dbl = [8, 8, 8, 12, 10, 40, 9, 9, 18, 9, 13, 8, 10, 8, 10, 19, 8, 5, 5, 6]
vergenceBiDbl = np.hstack((verNearBI_dbl, verFarBI_dbl))

accomAmp = [14.25, 13.75, 9.2, 12.25, 11.95, 9.6, 13.8, 10.65, 13.45, 17.5, 13.1, 13.95, 12.6, 11.15, 10.8, 10.8, 13.95, 13.8, 14.85, 11.4]
accLabel = ['accommodation'] * len(accomAmp)
accDistance = ['none'] * len(accomAmp)
accNF = ['none'] * len(accomAmp)

phoriaNear = [-3.5, -2, -2.5, 0.5, 1.5, -11.5, 2, -3.5, -12, -0.75, -4, 5.75, -0.25, -3.75, 1, -17, 7.5, -1, 2.75, 0]
phoriaFar = [-0.5, -0.5, 2.75, -1, 0.5, -3.5, 1, -0.25, -4, 2, -2.5, 3.75, 1, 1, -0.75, -4, 3.5, 1.25, 1.25, 2.25]
phoria = np.hstack((phoriaNear, phoriaFar))
testP = ['phoria'] * len(phoria)

labelN = ['near'] * len(phoriaNear)
labelF = ['far'] * len(phoriaFar)
distanceP = np.hstack((labelN, labelF))

vergenceBo = np.hstack((vergenceBoBlr, vergenceBoDbl))
vergenceBi = np.hstack((vergenceBiBlr, vergenceBiDbl))
verLabel = np.hstack((verLabelB, verLabelD))
distance = np.hstack([distanceP]*4)

baseO = ['out'] * len(vergenceBo)
baseI = ['in'] * len(vergenceBi)

vergence = np.hstack((vergenceBo, vergenceBi))
testV = ['vergence'] * len(vergence)
labelBD = np.hstack((verLabel, verLabel))
base1 = np.hstack((baseO, baseI))

baseP = ['none'] * len(phoria)

vals = np.hstack((vergence, phoria, accomAmp))
test = np.hstack((testV, testP, accLabel))
base = np.hstack((base1, baseP, accNF))
distance = np.hstack((distance, distanceP, accDistance))

data1 = {'subject':subjects, 'vals':vals, 'measure':test, 'base':base, 'blurDouble':verBlrDbl, 'distance':distance}

df1 = pd.DataFrame(data1)
df1['condition'] = 'VR'
df1['order'] = 'post'

#Measures taken before PC
verNearBO_blr = [25, 17, 11, 12, 20, 18, 13, 17, 13, 10, 22.5, 17, 20, 17, 12, 22.5, 40, 7, 40, 18]
verFarBO_blr = [22.5, 17, 13, 9, 19, 19, 10, 15, 10, 17, 22.5, 16, 22.5, 14, 11, 22.5, 27.5, 12, 11, 21.5]
vergenceBoBlr = np.hstack((verNearBO_blr, verFarBO_blr))
verLabelB = ['blur'] * len(vergenceBoBlr)

verNearBO_dbl = [35, 32.5, 22.5, 21.5, 27.5, 40, 30, 22.5, 22.5, 25, 22.5, 40, 27.5, 22.5, 14, 22.5, 40, 20, 40, 30]
verFarBO_dbl = [27.5, 30, 22.5, 17, 30, 40, 17, 21.5, 16, 27.5, 22.5, 40, 27.5, 22.5, 17, 22.5, 40, 12, 14, 30]
vergenceBoDbl = np.hstack((verNearBO_dbl, verFarBO_dbl))
verLabelD = ['double'] * len(vergenceBoBlr)

verNearBI_blr = [11, 11, 6, 8, 10, 14, 8, 6, 15, 6, 15, 13, 8, 8, 6, 18, 11, 9, 5, 6]
verFarBI_blr = [6, 7, 4, 7, 10, 12, 6, 6, 10, 8, 14, 6, 8, 6, 6, 13, 8, 4, 4, 12]
vergenceBiBlr = np.hstack((verNearBI_blr, verFarBI_blr))

verNearBI_dbl = [12, 13, 15, 12, 12, 25, 12, 12, 21.5, 15, 15, 19, 10, 13, 8, 18, 11, 10, 5, 6]
verFarBI_dbl = [8, 9, 7, 11, 10, 22.5, 8, 8, 16, 10, 14, 13, 10, 8, 8, 13, 8, 6, 4, 12]
vergenceBiDbl = np.hstack((verNearBI_dbl, verFarBI_dbl))

accomAmp = [15.4, 14.1, 8.75, 13.3, 12.1, 9.5, 10.55, 11.85, 13.25, 13.45, 12.55, 16.7, 12.45, 12.45, 10.8, 13.65, 13.75, 15.85, 16.8, 12.3]
accLabel = ['accommodation'] * len(accomAmp)
accDistance = ['none'] * len(accomAmp)
accNF = ['none'] * len(accomAmp)

phoriaNear = [-5, -2.5, -3, 1.5, -1.5, -10, -2, -1.5, -13, -2, -6.25, 7.25, -5, 2, -2, -13, -2, -4, 3, -1.75]
phoriaFar = [-0.75, -0.25, 3, 0.25, 0.25, -2.5, 1, 0.25, -4, 2.5, -2, 4, -1, 2, -1.75, -4, 0.5, -0.5, 3, 2]
phoria = np.hstack((phoriaNear, phoriaFar))
testP = ['phoria'] * len(phoria)

labelN = ['near'] * len(phoriaNear)
labelF = ['far'] * len(phoriaFar)
distanceP = np.hstack((labelN, labelF))

vergenceBo = np.hstack((vergenceBoBlr, vergenceBoDbl))
vergenceBi = np.hstack((vergenceBiBlr, vergenceBiDbl))
verLabel = np.hstack((verLabelB, verLabelD))
distance = np.hstack([distanceP]*4)

baseO = ['out'] * len(vergenceBo)
baseI = ['in'] * len(vergenceBi)

vergence = np.hstack((vergenceBo, vergenceBi))
testV = ['vergence'] * len(vergence)
base1 = np.hstack((baseO, baseI))

baseP = ['none'] * len(phoria)

vals = np.hstack((vergence, phoria, accomAmp))
test = np.hstack((testV, testP, accLabel))
base = np.hstack((base1, baseP, accNF))
distance = np.hstack((distance, distanceP, accDistance))

data2 = {'subject':subjects, 'vals':vals, 'measure':test, 'base':base, 'blurDouble':verBlrDbl, 'distance':distance}

df2 = pd.DataFrame(data2)
df2['condition'] = 'PC'
df2['order'] = 'pre'

#Measures taken after PC
verNearBO_blr = [21.5, 18, 10, 12, 10, 18, 14, 15, 10, 12, 25, 20, 20, 17, 11, 27.5, 32.5, 12, 9, 11]
verFarBO_blr = [22.5, 16, 7, 9, 22.5, 20.5, 11, 11, 11, 18, 22.5, 12, 22.5, 18, 9, 22.5, 30, 8, 7, 10]
vergenceBoBlr = np.hstack((verNearBO_blr, verFarBO_blr))
verLabelB = ['blur'] * len(vergenceBoBlr)

verNearBO_dbl = [32.5, 35, 32.5, 20, 15, 40, 20, 25, 17, 22.5, 30, 40, 25, 25, 16, 27.5, 40, 40, 40, 13]
verFarBO_dbl = [25, 35, 19, 22.5, 32.5, 40, 16, 18, 17, 30, 22.5, 40, 27.5, 27.5, 13, 22.5, 40, 37.5, 12, 16]
vergenceBoDbl = np.hstack((verNearBO_dbl, verFarBO_dbl))
verLabelD = ['double'] * len(vergenceBoBlr)

verNearBI_blr = [11, 12, 2, 7, 11, 14, 8, 6, 11, 7, 17, 11, 7, 7, 7, 14, 10, 8, 4, 5]
verFarBI_blr = [6, 7, 3, 8, 10, 14, 6, 5, 11, 5, 11, 6, 7, 6, 5, 17, 9, 5, 4, 6]
vergenceBiBlr = np.hstack((verNearBI_blr, verFarBI_blr))

verNearBI_dbl = [12, 12, 12, 13, 13, 30, 12, 8, 16, 15, 17, 21.5, 9, 13, 10, 14, 10, 10, 6, 5]
verFarBI_dbl = [6, 9, 7, 12, 12, 25, 8, 9, 17, 10, 11, 14, 9, 8, 8, 17, 9, 7, 4, 6]
vergenceBiDbl = np.hstack((verNearBI_dbl, verFarBI_dbl))

accomAmp = [15.4, 13.85, 8.85, 14.75, 14.15, 13.8, 12.6, 12.35, 12.65, 13, 12.65, 14.75, 11.75, 11.25, 11, 12.6, 13.45, 15.25, 16.9, 15.4]
accLabel = ['accommodation'] * len(accomAmp)
accDistance = ['none'] * len(accomAmp)
accNF = ['none'] * len(accomAmp)

phoriaNear = [-3.5, -3.5, -3.75, -5, -1, -11.5, 2, -2, -17, 1, -6.5, 5, -0.5, -4, -2, -9, 2.5, 1.5, 0.75, -1]
phoriaFar = [-0.5, -0.5, 1.25, -0.5, 2, -3.75, 1, 0.25, -4, 1.5, -3.5, 4, 0.75, 0.5, -1, -4, 1.25, 1, 2.25, 2.25]
phoria = np.hstack((phoriaNear, phoriaFar))
testP = ['phoria'] * len(phoria)

labelN = ['near'] * len(phoriaNear)
labelF = ['far'] * len(phoriaFar)
distanceP = np.hstack((labelN, labelF))

vergenceBo = np.hstack((vergenceBoBlr, vergenceBoDbl))
vergenceBi = np.hstack((vergenceBiBlr, vergenceBiDbl))
verLabel = np.hstack((verLabelB, verLabelD))
distance = np.hstack([distanceP]*4)

baseO = ['out'] * len(vergenceBo)
baseI = ['in'] * len(vergenceBi)

vergence = np.hstack((vergenceBo, vergenceBi))
testV = ['vergence'] * len(vergence)
base1 = np.hstack((baseO, baseI))

baseP = ['none'] * len(phoria)

vals = np.hstack((vergence, phoria, accomAmp))
test = np.hstack((testV, testP, accLabel))
base = np.hstack((base1, baseP, accNF))
distance = np.hstack((distance, distanceP, accDistance))

data3 = {'subject':subjects, 'vals':vals, 'measure':test, 'base':base, 'blurDouble':verBlrDbl, 'distance':distance}

df3 = pd.DataFrame(data3)
df3['condition'] = 'PC'
df3['order'] = 'post'

frames = [df, df1, df2, df3]
result = pd.concat(frames)

#Make table of observer data
data4 = {'subject':subject, 'myopia':myopia}

obsData = pd.DataFrame(data4)
#obsFrames = [subject, myopia]
#obsData = pd.concat(obsFrames)

result.to_csv(r'C:\Users\angie\Git Root\vrOculomotorChanges\data\subjectData.csv', index=False)
obsData.to_csv(r'C:\Users\angie\Git Root\vrOculomotorChanges\data\myopiaClassification.csv', index=False)
