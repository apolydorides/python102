import numpy as np
import pandas as pd

from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from keras.models import Sequential
from keras.layers.core import Dense, Activation

# Read the CSV
df = pd.read_csv('./druguse.csv')
# print(df)

print(df.columns.values)
del df['amphetamine']
del df['amylnitrite']
del df['benzodiaz']
del df['cannabis']
del df['cocaine']
del df['crack']
del df['ecstasy']
del df['heroin']
del df['ketamine']
del df['legalhighs']
del df['LSD']
del df['methadone']
del df['mushrooms']
del df['volatiles']
del df['any']
del df['UseLevel']
# del df['severity']

print(df)
# df['UseLevel'] = df['UseLevel'].map({
#     'low':  0,
#     'high': 1
# })
# print(df)
print(df.columns.values)


def jitter_plot(data, x, y):
    x_data = data[x].values + (np.random.rand(len(data)) * 0.5)
    y_data = data[y].values + (np.random.rand(len(data)) * 0.5)
    plt.scatter(x_data, y_data, alpha=0.3)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.show()
    plt.clf()

# jitter_plot(df, 'chocolate', 'nicotine')

# We need to now 'prepare' the data


race_df = pd.get_dummies(df['ethnicity'], prefix='race')
df = df.drop('ethnicity', axis=1)
df = df.join(race_df)

country_df = pd.get_dummies(df['country'], prefix='country')
df = df.drop('country', axis=1)
df = df.join(country_df)


df['gender'] = df['gender'].map({
    'male':  0,
    'female': 1
})

df['agegroup'] = df['agegroup'].map({
    '18-24':  0,
    '25-34': 1,
    '35-44': 2,
    '45-54': 3,
    '55-64': 4,
    '65+': 5
})

# print(df)

train_set = df.iloc[:1500]
train_x = train_set.drop('severity', axis=1).values
train_y = train_set['severity'].values

test_set = df.iloc[1500:]
test_x = test_set.drop('severity', axis=1).values
test_y = test_set['severity'].values

print(train_x.shape)
print(train_y)

exit()

# rf = RandomForestRegressor()
# rf.fit(train_x, train_y)

# pred_y = rf.predict(test_x)

model = Sequential()
# model.add(Dense())

results = pd.DataFrame({
    'predictions': pred_y,
    'actual': test_y,
    'error': np.absolute(pred_y - test_y)
})

print(results)

root_mean_squared_error = (sum([(x - y) ** 2 for x, y in zip(pred_y, test_y)]) ** 0.5) / len(results)
print('Root Mean Squared Error:', root_mean_squared_error)
