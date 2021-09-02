import typing


def get_percentage_value(value: typing.Union[float, None]):
  if not value or value < 0:
    return 0
  if value > 1:
    return 1
  return value
