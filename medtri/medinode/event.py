from typing import List
from copy import copy, deepcopy
from .factor import Factor

class Event:
  def __init__(
    self,
    name : str,
    apriori_factors : List["Factor"] = [],
    posteriori_factors : List["Factor"] = [],
    prevalence : int = None,
    *args, 
    **kwargs
  ):
    self.name = name
    self.apriori_factors = apriori_factors
    self.posteriori_factors = posteriori_factors
    self.prevalence = prevalence
  
  def has_apriori_factor(self, factor_event : "Event", factor_prevalence : int) -> "Event":
    factor = Factor(factor_event, factor_prevalence)
    self.apriori_factors.append(factor)
    return self