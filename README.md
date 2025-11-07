### Power Consumption Forecasting

#### Time Series Forecasting

- A time series is data collected periodically, over time.
- Time series forecasting is the task of predicting future data points, given some historical data.
- It is commonly used in a variety of tasks from weather forecasting, retail and sales forecasting, stock market prediction, and in behavior prediction (such as predicting the flow of car traffic over a day).
- There is a lot of time series data out there, and recognizing patterns in that data is an active area of machine learning research!

* In this notebook, we'll focus on one method for finding time-based patterns: using SageMaker's supervised learning model, DeepAR.

#### DeepAR

- DeepAR utilizes a recurrent neural network(RNN), which is designed to accept some sequence of data points as historical input and produce a predicted sequence of points. So, how does this model learn?

- During training, you'll provide a training dataset (made of several time series) to a DeepAR estimator. The estimator looks at all the training time series and tries to identify similarities across them.

- It trains by randomly sampling training examples from the training time series.

- Each training example consists of a pair of adjacent context and prediction windows of fixed, predefined lengths.

  - The context_length parameter controls how far in the past the model can see.
  - The prediction_length parameter controls how far in the future predictions can be made.

- In any forecasting task, you should choose the context window to provide enough, relevant information to a model so that it can produce accurate predictions.

- In general, data closest to the prediction time frame will contain the information that is most influential in defining that prediction.

- In many forecasting applications, like forecasting sales month-to-month, the context and prediction windows will be the same size, but sometimes it will be useful to have a larger context window to notice longer-term patterns in data.

#### Energy Consumption Data

- The data we'll be working with in this notebook is data about household electric power consumption, over the globe. The dataset is originally taken from [Kaggle](https://www.kaggle.com/datasets/uciml/electric-power-consumption-data-set), and represents power consumption collected over several years from 2006 to 2010

#### Pre-Process the Data

The 'household_power_consumption.txt' file has the following attributes:

- The 'household_power_consumption.txt' file has the following attributes:
- The various data features are separated by semicolons (;)
- Some values are 'nan' or '?', and we'll treat these both as NaN values

##### Managing NaN values

- This DataFrame does include some data points that have missing values.
- So far, we've mainly been dropping these values, but there are other ways to handle NaN values, as well.
- One technique is to just fill the missing column values with the mean value from that column; this way the added value is likely to be realistic.

- The preprocessing_methods.py module will help to load in the original text file as a DataFrame and fill in any NaN values, per column, with the mean feature value.
- This technique will be fine for long-term forecasting; if I wanted to do an hourly analysis and prediction, I'd consider dropping the NaN values or taking an average over a small, sliding window rather than an entire column of data.

#### Machine Learning Workflow

This notebook approaches time series forecasting in a number of steps:

- Loading and exploring the data
- Creating training and test sets of time series
- Formatting data as JSON files and uploading to S3
- Instantiating and training a DeepAR estimator
- Deploying a model and creating a predictor
- Evaluating the predictor

### USAGE

1. unzip data.zip
2. run preprocessing_methods.py
3. execute cell-by-cell in python notebook
