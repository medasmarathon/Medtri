from typing import List
import pandas as pd

class Event:
  def __init__(
    self,
    name : str,
    apriori_events : List["Event"] = None,
    posteriori_events : List["Event"] = None,
    prevalence : int = None,
    *args, 
    **kwargs
  ):
    self.name = name
    self.apriori_events = apriori_events
    self.posteriori_events = posteriori_events
    self.prevalence = prevalence
    
