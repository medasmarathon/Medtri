from typing import List
from medtri.medinode.event import Event


class Host:
  def __init__(self, name: str, possible_events: List[Event] = []) -> None:
    self.name = name
    self.possible_events = possible_events
