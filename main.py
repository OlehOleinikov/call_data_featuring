"""
Module for normalizing and prepare data, extract features for call data column content
"""

import pandas as pd
import numpy as np

from typing import Union


class DataFrameFeaturer:
    """User's interface for dataframe featuring"""
    pass


class Featurer:
    """User's interface for single column featuring"""

    def __init__(self, series_data: pd.Series):
        self.data = series_data


class DataSampling:
    """Select enough data from all column's range (from different parts)"""
    critical_size = 200
    warning_size = 500

    def __init__(self,
                 sample_area=10,
                 sample_count=100,
                 head_size=25,
                 tail_size=25):
        self.sample_area = sample_area
        self.sample_count = sample_count
        self.head_size = head_size
        self.tail_size = tail_size
        self.selected_size = head_size + (sample_area * sample_count) + tail_size
        if self.selected_size < self.critical_size:
            raise AttributeError('ERROR! Critical sampling setup. Size less then critical. Increase the sample size')
        if self.selected_size < self.critical_size:
            print("WARNING! Sampling setup less then normal size. Increase the sample size.")

    def count_possible_samples(self, data: Union[pd.DataFrame, pd.Series]):
        size = data.shape[0]
        body_size = size - (self.head_size + self.tail_size)
        if body_size < 0:
            return 1



    def get_sample_series(self, series: pd.Series):
        pass


    def get_sample_df(self, data: Union[pd.DataFrame, pd.Series]):
        pass


class DigitalFeatures:
    """Common statistics features"""
    pass


class TelecomFeatures:
    """Specific features for telecom data"""
    pass
