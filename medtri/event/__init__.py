from typing import List
import pandas as pd

class Event:
  def __init__(
    self,
    name : str,
    causative_factors : List["Event"] = None,
    prevalence : int = None,
    *args, 
    **kwargs
  ):
    self.name = name
    self.causative_factors = causative_factors
    self.prevalence = prevalence
    
