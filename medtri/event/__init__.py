import pandas as pd

class Event:
  def __init__(self, *args, **kwargs):
    self.feature_to_frequency = kwargs.pop("feature_to_frequency")
    self.prevalence = kwargs.get("prevalence")
    
