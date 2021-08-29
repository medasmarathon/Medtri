from medtri.medinode.constraints.datatype import percentage_value
from typing import List
from copy import copy, deepcopy
from .factor import Factor


class Event:
  def __init__(
      self,
      name: str,
      apriori_factors: List["Factor"] = [],
      outcome_factors: List["Factor"] = [],
      prevalence: float = 0,
      *args,
      **kwargs
      ):
    self.name = name
    self.apriori_factors = apriori_factors
    self.outcome_factors = outcome_factors
    self.prevalence = percentage_value(prevalence)

  def has_apriori_factor(self, factor_event: "Event", factor_prevalence: float) -> "Event":
    existed_apriori_factor_index = self.__get_apriori_factor_index_for_event(factor_event)
    if existed_apriori_factor_index == -1:
      # If not exist factor for event, create new
      factor = Factor(factor_event, factor_prevalence)
      self.apriori_factors.append(factor)
    else:
      # Else update prevalence
      self.apriori_factors[existed_apriori_factor_index].prevalence = factor_prevalence
    return self

  def remove_apriori_factor_of_event(self, event: "Event"):
    existed_apriori_factor_index = self.__get_apriori_factor_index_for_event(event)
    if existed_apriori_factor_index != -1:
      # Current observations not include this event
      self.apriori_factors.pop(existed_apriori_factor_index)

  def remove_outcome_factor_of_event(self, event: "Event"):
    existed_outcome_factor_index = self.__get_outcome_factor_index_for_event(event)
    if existed_outcome_factor_index != -1:
      # Current observations not include this event
      self.apriori_factors.pop(existed_outcome_factor_index)

  def __get_apriori_factor_index_for_event(self, event: "Event") -> int:
    for index, factor in enumerate(self.apriori_factors):
      if event is factor.event:
        return index
    return -1

  def __get_outcome_factor_index_for_event(self, event: "Event") -> int:
    for index, factor in enumerate(self.outcome_factors):
      if event is factor.event:
        return index
    return -1