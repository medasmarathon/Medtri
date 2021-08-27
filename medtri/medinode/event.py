from typing import List
from .factor import Factor

class Event:
  def __init__(
    self,
    name : str,
    apriori_factors : List["Factor"] = None,
    posteriori_factors : List["Factor"] = None,
    prevalence : int = None,
    *args, 
    **kwargs
  ):
    self.name = name
    self.apriori_factors = apriori_factors
    self.posteriori_factors = posteriori_factors
    self.prevalence = prevalence
  
  def has_apriori_factor(self, factor_event : "Event", prevalence : int):
    return self