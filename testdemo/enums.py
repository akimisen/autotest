from enum import Enum

class SupportedDrivers(Enum):
  Chrome=Chrome
  Firefox=Firefox
  Safari=Safari

class By(Enum):
  id=1
  xpath=2
  css=3
  linktext=4

class Action(Enum):
  click=1