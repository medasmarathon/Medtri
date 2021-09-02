from abc import ABC, abstractmethod


class IEvent(ABC):
  @property
  def prevalence(self):
    return self.__prevalence

  @prevalence.setter
  def prevalence(self, prevalence):
    if prevalence < 0:
      self.__prevalence = 0
    elif prevalence > 1:
      self.__prevalence = 1
    else:
      self.__prevalence = prevalence

  def remove_apriori_event(self, event: "IEvent"):
    pass

  def remove_outcome_event(self, event: "IEvent"):
    pass

  def get_apriori_event(self, event: "IEvent"):
    pass

  def get_outcome_event(self, event: "IEvent"):
    pass

  def is_outcome_of(self, event: "IEvent"):
    pass

  def is_apriori_of(self, event: "IEvent"):
    pass

  def __eq__(self, o: object) -> bool:
    return False


class IObservation(ABC):
  @property
  def presence_probability(self):
    return self.__presence_probability

  @presence_probability.setter
  def presence_probability(self, presence_probability):
    if presence_probability < 0:
      self.__presence_probability = 0
    elif presence_probability > 1:
      self.__presence_probability = 1
    else:
      self.__presence_probability = presence_probability


class IHost(ABC):
  def is_event_possible(self, event: IEvent):
    pass
