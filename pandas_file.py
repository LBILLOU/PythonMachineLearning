from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier as RandomForest
import pandas as pd
from sklearn.cross_validation import train_test_split
import sys
import os
import matplotlib.pyplot as plt
pd.set_option('display.width', 180)

# Import data from csv file chosen by user
# http://archive.ics.uci.edu/ml/
# https://opendata.paris.fr/explore/?sort=modified
# https://www.data.gouv.fr/fr/datasets/
print '\n>>> Import data from csv file, which file? (filename.csv)'
filename = raw_input()
while os.path.isfile(filename) is False:
    print 'ERROR -> Please choose a csv file in current directory.',
    print ' (filename.csv)'
    filename = raw_input()
# Read CSV file
data = pd.read_csv(filename, header=0)
# Fill na with 0
data = data.fillna(0)

# Printing Data Shape
print '\nImported Data shape'
print data.shape

# Printing Column List
print '\nImported Data columns'
columnList = list(data.columns)
print list(data.columns)

# Encoding data to numeric values
label_encoder = preprocessing.LabelEncoder()
for heading in columnList:
    data[heading] = label_encoder.fit_transform(data[heading])

# Let's user choose column to predict
print '\n>>> Which column would you like to predict?'
userTarget = raw_input()
while userTarget not in columnList:
    print 'ERROR -> Please choose a column you like to predict from',
    print ' the following list:'
    print list(data.columns)
    userTarget = raw_input()

# Defining target as the user-specified column
target = data[userTarget]
# Dropping target from training data
train = data[data.columns.drop(userTarget)]
# Remove userTarget from features
columnList.remove(userTarget)

print '\n>>> Whould you like to drop a column for the prediction model? y/n'
dropYN = raw_input()
while dropYN != 'y' and dropYN != 'n':
    print '>>> Whould you like to drop a column for the prediction model? y/n'
    dropYN = raw_input()
while dropYN == 'y':
    print '\n>>> Which column would you like to drop?'
    print columnList
    colToDrop = raw_input()
    while colToDrop not in columnList:
        print 'ERROR -> Please choose a column you want to drop from',
        print ' the following list:'
        print columnList
        colToDrop = raw_input()
    columnList.remove(colToDrop)
    print '\n>>> Would you like to drop another column? y?'
    dropYN = raw_input()

split = train_test_split(train, target, test_size=0.60, random_state=42)
data_train, data_test, target_train, target_test = split

# Printing data, test and training shape
print '\nData shape:', train.shape
print 'Training shape:', data_train.shape
print 'Testing shape:', data_test.shape

features = columnList
model = RandomForest(n_estimators=10)
model.fit(data_train[features], target_train)

print('\nPredictions Examples')
prediction = model.predict(data_test[features])
reality = target_test
result = pd.DataFrame({'prediction': prediction, 'reality': reality})
result['predictionTest'] = 'right'
result.loc[result.prediction == result.reality, 'predictionTest'] = 'wrong'
print result.head()

print '\nColumns weight for defining prediction'
featurePlot = []
impPlot = []
for feature, imp in zip(features, model.feature_importances_):
    print(feature, imp)
    featurePlot.append(feature)
    impPlot.append(float('%.3f' % (imp)))

# Plotting column weight
x = list(range(0, len(featurePlot)))
plt.bar(x, impPlot, align='center')
title = 'Attribute\'s Weight (%) \nFor {} Predictions in {}'
plt.title(title.format(userTarget, filename))
plt.xticks(x, featurePlot, rotation='vertical')
plt.ylabel('Weight (%)')
plt.xlabel('Attributes')
plt.tight_layout()
plt.show()

print '\nPrediction Results'
print result.predictionTest.value_counts()

print '\nModel Efficiency'
print model.score(data_test[features], target_test)

sys.exit('\nEND OF SCRIPT')
