# Linear Regression toolkit. 

# Useful for baselines, and sometimes also the best model on smaller datasets.

# How to run for univariate data.

# read in the data

df = pd.read_csv('../data/weather.csv')
df['date'] = pd.to_datetime(df[['Day','Month','Year']])
df.set_index('date',inplace=True, drop=True)
dfU = df.Temperature

# turn the univariate series into a sliding window. 
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    n_vars = 1 if type(data) is list else data.shape[1]
    df = pd.DataFrame(data)
    cols = list()
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
    for i in range(0, n_out):
        cols.append(df.shift(-i))
    agg = pd.concat(cols, axis=1)
    if dropnan:
        agg.dropna(inplace=True)
    return agg.values
  
  #split a univariate dataset into train/test sets
def train_test_split(data, n_test):
    return data[:-n_test, :], data[-n_test:, :]
 

# forecast function
from sklearn.linear_model import LinearRegression
from numpy import asarray
def forecast(train, testX):
    train = asarray(train)
    trainX, trainy = train[:, :-1], train[:, -1]
    model = LinearRegression()
    model.fit(trainX, trainy)
    yhat = model.predict(asarray([testX]))
    return yhat[0]
  
# walk-forward validation for univariate data
def walk_forward(data, n_test):
    predictions = list()
    train, test = train_test_split(data, n_test)
    history = [x for x in train]

    for i in range(len(test)):
        x_test, y_test = test[i, :-1], test[i, 0]
        yhat = model.predict(history, x_test)
        predictions.append(yhat)
        history.append(test[i])
        print('>test=%.1f, predicted=%.1f' % (y_test, yhat))
#Input: %s, 
    mae = mean_absolute_error(test[:, -1], predictions)
    rmse = sqrt(mean_squared_error(test[:,-1],predictions))
    
    return mae, rmse,test[:, -1], predictions
  
#set input range and print a forecast length here of length 6 alongside test data
# set z = to how long you want to forecast.
data = series_to_supervised(df, n_in=len(df-z))

rmse,mae, y, yhat = walk_forward(data, z)
print('MAE: %.3f' % mae)
print('RMSE: %.3f' % rmse)
print('test mean price: %3f' % np.mean(y))
print('predicted mean price: %.3f' % np.mean(yhat))
# plot expected vs predicted
plt.plot(y, label='test')
plt.plot(yhat, label='Predicted')
plt.legend()
plt.show();


# For multivariate the following code will work


from sklearn.linear_model import LinearRegression
form sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score

# reloading the dataset as need a multivariate dataset for this modeling.
df = pd.read_csv('../data/weather.csv')
df['date'] = pd.to_datetime(df[['Day','Month','Year']])
df.set_index('date',inplace=True, drop=True)
dfm = df.resample('M').mean()




# apply a length to train and test.
n = (int(len(dfm)/5)*4)
train = dfm[:n]
test = dfm[n:]

X_train = train.drop('Temperature', axis=1)
y_train = train['Temperature']
X_test = test.drop('Temperature',axis=1)
y_test = test['Temperature']


from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
X_train = pd.DataFrame(scaler.fit_transform(X_train), columns=X_train.columns)
X_test = pd.DataFrame(scaler.transform(X_test), columns=X_test.columns)

# fit the model
model1 = LinearRegression()
model1.fit(X_train, y_train)

# score the model
model_scores = cross_val_score(model1, X_train, y_train, cv=10)
# and use the predict function from sklearn
y_pred = model1.predict(X_test)

# Now to see the metrics
print('Predicted mean Price', np.mean(y_pred))
print('test mean price', np.mean(y_test))
print('RSq', model1.score(X_test, y_test))
print('RMSE: %.3f' % rmse)
print('MAE: %.3f' % mae)


# Visualise the model predictions against the data

test['Predictions'] = y_pred
plt.figure(figsize=(20,10))
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.plot(train['Temperature'])
plt.plot(test[['Temperature','Predictions']])
plt.legend()
plt.show();


# Visualise the coefficients
df_coef= pd.DataFrame(list(zip(X_train.columns,np.abs(model1.coef_))),columns=['feature','coefficient'])

dfcoef = df_coef.sort_values(by='coefficient',ascending=False).head(20)
dfcoef.sort_values(by='coefficient',ascending=True,inplace=True)
dfcoef.plot(kind='barh', x='feature',y='coefficient', figsize=(10,8),legend=False)
plt.xlabel('Coefficient')
plt.ylabel('Feature')
plt.xscale('log')
plt.show();


