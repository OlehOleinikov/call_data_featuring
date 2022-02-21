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
    def __init__(series_data: pd.Series):
        self.data = data_sample
    


class DataSampling:
    """Select enough data from all column's range (from different parts)"""
    def __init__(dataframe: pd.DataFrame, sampling_area=100, sampling_count=100, ):
        self.df_sample = dataframe
        self.smp_area = sampling_zone
        self.smp_count = sampling_injections


class DigitalFeatures:
  """Common statistics features"""
  pass


class TelecomFeatures:
  """Specific features for telecom data"""
  pass


