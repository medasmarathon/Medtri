from medtri.medinode.constraints.datatype import percentage_value
from typing import List
from copy import copy, deepcopy
from .factor import Factor


class Event:
  def __init__(
      self,
      name: str,
      apriori_factors: List["Factor"] = [],
      posteriori_factors: List["Factor"] = [],
      prevalence: float = 0,
      *args,
      **kwargs
      ):
    self.name = name
    self.apriori_factors = apriori_factors
    self.posteriori_factors = posteriori_factors
    self.prevalence = percentage_value(prevalence)

  def has_apriori_factor(
      self, factor_event: "Event", factor_prevalence: float
      ) -> "Event":
    factor = Factor(factor_event, factor_prevalence)
    self.apriori_factors.append(factor)
    return self
