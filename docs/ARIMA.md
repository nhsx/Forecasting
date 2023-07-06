This workbook is a run through of univariate modeling using ARIMA and auto-select ARIMA. 
This will cover manually setting the hyperparameters Where this workbook will stop, is after using seasonal and non-seasonal ARIMA modeling.

ARIMA stands for AutoRegressive Integrated Moving Average. 
The model is a combination of the differenced autoregressive mode with the moving average model. 
The AR part shows time series is regressed on its own past data. the I part shows the data values have been replaced with differenced values of d to obtain stationary data. 
The MA part is the Moving Average part of the model. The benefit of all three combined is that for seasonal models the data prediction can follow the pattern up and down, and not remain at the mean. 
In this way the forecast becomes a combination of the most recent data's effect, the effect of differencing a non-stationary dataset, and the long-term mean value of the series. 
This also puts more value on the most recent data than further away data. Likewise the further into the future you forecast, the closer the data forecast resembles the mean. 
It should be note that ARMA models also exist, where the data is already stationary and does not require differencing. These would resemble (1,0,1) in the model parameters.

Further reading available here - [ARIMA/SARIMAX](https://github.com/nhsx/Time_Series_Forecasting_MS/blob/main/docs/sarimax.md)
