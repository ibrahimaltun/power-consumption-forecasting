"""
This file was used to process the initial, raw text: household_power_consumption.txt
"""
import pandas as pd

EXPECTED_FILE = 'household_power_consumption.txt'
NA_VALUE_LIST = ['nan', '?']
SEP = ";"


class DataFrameOperations:
    def __init__(self, text_file):
        self.df = None
        self.name = text_file

        if self.name != EXPECTED_FILE:
            self.name = EXPECTED_FILE
            print('Unexpected file: '+str(self.name))

        self.df = pd.read_csv(self.name, sep=SEP,
                              parse_dates={'Date-Time': ['Date', 'Time']}, infer_datetime_format=True,
                              low_memory=False, na_values=NA_VALUE_LIST, index_col='Date-Time')

    def fill_nan_with_mean(self) -> pd.read_csv:
        """Fills NaN values in a given dataframe with the average values in a column.
        This technique works well for filling missing, hourly values 
        that will later be averaged into energy stats over a day (24hrs)."""

        # filling nan with mean value of any columns
        num_cols = len(list(self.df.columns.values))
        for col in range(num_cols):
            self.df.iloc[:, col] = self.df.iloc[:, col].fillna(
                self.df.iloc[:, col].mean())

        return self.df


if __name__ == "__main__":
    df_opt = DataFrameOperations(EXPECTED_FILE)
    df = df_opt.fill_nan_with_mean()
    df.to_csv("new_household_power_consumption.txt")
