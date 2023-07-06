# Time Series Forecasting
A repo of different forecasting methods for different situations.


Within this repo, there are several ways of going about Time Series Forecasting (TSF). 
When you come to look at a dataset, and the question is, how do I predict y from my existing data, quite often the area that's hardest is knowing where to begin, how to go about the forecasting, and what method is most appropriate, and which method will give you the best results.

What this repo will do, is try and guide you through this forest, so you can see the wood for the trees. The repo will only cover numerical forecasting, so regression style forecasting, as opposed to classification (binary) forecasting. 

When it comes to Time Series Forecasting, or any other type of modeling, knowing whether your model is performing well is critical. Whether your dataset for prediction is univariate (one variable in, one out), or multivariate (multiple variables in, can be multiple variables out), and how far you want to forecast, the first step is to establish a baseline, from which you can compare and contrast the various models. 
In this repo we will use two measures to compare and contrast each model against the baseline, Residual Mean Squared Error (RMSE) and Mean Absolute Error, (MAE). In TSF, these work together. A very good starting place to establish a baseline is to look at the mean. For your dataset, this can be the last 3 months to predict the next month, or the last 6 periods to predict period 7. From my experience, it can be tough to beat these styles of mean forecasts. 
Additionally we will use a basic linear regression model for these scores, and use this as a model baseline. 


### Know your data

The starting point for any data analysis, is to know your data. What do I mean by this?
Lets go through a 5 step process specifically for Time Series Forecasting. 

1. Is your dataset univariate or multivariate. I.e. do you have a list of Temperatures for the last x years, and are trying to forecast the next week's temperatures. Or do you have a dataframe of variables about weather, so sunshine hours, cloudcover, rainfall, and are trying to forecast the temperature from these other variables. This way of thinking can be applied to any dataset. Previous stock prices for next few days' stock price, or patient's admission dataset and history to forecast their outcome at time of admission, or length of stay post admission.
The answer to this will help you decide which model to use in this repo. 

2. Critical within model accuracy is data preparation. Is your data stationary? What does this mean. Stock prices are a good example of this, as is energy usage over a year. Both of these over time, will display either trend or seasonality or both. In order for your models to perform better, a time series will need to be made stationary. If youre time series is not stationary, it came be made stationary by differencing. What this means, is instead of training a model on a series of stock prices, the model performs a lot better on the differences in the period stock prices, so +0.5, -0.25, +0.75, as opposed to 175, 175.5, 175.25, 176. In stats we call this the p value. Use seasonal_decompose function to examine your data, this will expose seasonality and trend. Also plot the y variable to examine outliers and trend.

3. Autocorrelation and partial autocorrelation. Is your data correlated. Use the ACF and PACF functions to examine your data. These are related to ARIMA and SARIMAX modeling if you decide to go down this route. Checking the ACF and PACF is vital to understanding your data. I've spent more time within the ARIMA and SARIMAX workbooks talking about this, but effectively these are designed to show you where your data is correlated with the mean and current data with past data.

4. Length of dataset. If you have a small/ short dataset, more often than not, means and simple linear regression perform extremely well. ARIMA, SARIMAX and LSTM are a lot of work to get a model working on your dataset. On small datasets it's extremely difficult for these models to beat the performance from simple means, or Linear Regression (Elastic Nets, Ridge and Lasso). What qualifies as small, anything under 100 data points for multivariate datasets, and under 1000 for univariate datasets.

5. Examine your model and your data. What are you trying to forecast? Is it bank holiday attendances in hospital A&E. If so, if your model performing badly and you don't know why? Take a step back here and look at the data you're feeding into your model. For example if you have A&E attendance figures for the last 5 years, and you're trying to forecast the next three bank holiday attendances, why are you feeding in all the datapoints? Split your data into bank holiday data and other data, or weekend data, bank holiday data and non-weekend data, separate and re-run your models. You can always combine the datasets post modeling for a complete picture, but sometimes separating your data may prove more fruitful. Forecasting isn't an exact science, but being prepared to iterate over the numbers, refine your models by experimentation not just on hyper-parameters but also on datasets used for training. You may see your results improve dramatically following this. 
For example here, if you've run a multivariate dataset through a LinearRegression model, and it's performed ok, but you're not sure where to go next. 
Experiment, try ElasticNet, or Lasso regression, drop the bottom performing 5% of variables and see if this improves the model performance. Maybe add a gridsearch hyperparameter search (RAM dependent) to the regression, code for this is in the XGBoost file.
Iterate, and experiment. 



## Baselines

Lets begin this by finding the mean of the dataset. 

With Time Series data you can average the whole length of the dataset, and take this as your next forecast baseline.
This works if your data doesn't have trend, or the mean takes into account a whole seasonal period. 

Code and Instructions are in the Baselines.py file. 

### Built With

[![Python v3.8](https://img.shields.io/badge/python-v3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Python v3.9](https://img.shields.io/badge/python-v3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
- [sklearn](https://scikit-learn.org/stable/)
- [statsmodels](https://www.statsmodels.org/stable/index.html)
- [Tensorflow](https://tensorflow.org/)

### Getting Started

### Installation

Install the above software packages as per the following example:
conda install -c conda-forge sklearn

To get a local copy up and running follow these simple steps.

To clone the repo:

`git clone https://github.com/nhsx/Forecasting.git`

### Datasets

The data sources are saved for your use in the data folder in the repo, or are widely available with links to the data within the workbooks. 

### Second Forecasting Repo - More Advanced

(Forecasting_2)[https://github.com/nhsx/Time_Series_Forecasting_MS/tree/main]

### Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

_See [CONTRIBUTING.md](./CONTRIBUTING.md) for detailed guidance._

### License

Distributed under the MIT License. _See [LICENSE](./LICENSE) for more information._


