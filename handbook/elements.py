'''
Tags
'''

import os

# ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
# █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
# █░░░░░░░░░░░░░░░░░░░░░░░░░░░ SINGLE ELEMENT ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
# █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
# ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

class element:

  # ────────────────────────────────────────────────────────────────────────
  def __init__(self, type=None, single=False, content='', parameters=None):

    self.type = type
    self.single = single
    self.content = content
    self.parameters = {} if parameters is None else parameters

  # ────────────────────────────────────────────────────────────────────────
  def __str__(self):

    # Check
    if self.type is None: return self.content

    # ─── Start tag

    # Initialization
    s = '<' + self.type

    # Parameters
    for k, v in self.parameters.items():
      s += f' {k}='
      match v.__class__():
        case str(): s += "'" + v + "'"
        case _: s += str(v)

    # End of starting tag
    if self.single:
      return s + '/>'
    
    else:
      s += '>'
      
    # ─── Content

    s += self.content
    
    # ─── Closing tag

    s += '<' + self.type + '/>'

    return s

  # ────────────────────────────────────────────────────────────────────────
  def __add__(self, a):

    match a.__class__():

      case str():
        r = element()
        r.content = self.__str__() + a

      case element():
        r = element()
        r.content = self.__str__() + a.__str__()

      case _:
        return NotImplemented
      
    return r
  
  # ────────────────────────────────────────────────────────────────────────
  def __radd__(self, a):

    match a.__class__():

      case str():
        r = element()
        r.content = a + self.__str__()

      case _:
        return NotImplemented
      
    return r
  
  # ────────────────────────────────────────────────────────────────────────
  def __setattr__(self, name, value):

    if name is 'content' and isinstance(value, element):
      super(element, self).__setattr__(name, value.__str__())
    else:
      super(element, self).__setattr__(name, value)

# ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
# █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
# █░░░░░░░░░░░░░░░░░░░░░░░ COLLECTION OF ELEMENTS ░░░░░░░░░░░░░░░░░░░░░░░░░█
# █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
# ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

# class elements:

#   # ────────────────────────────────────────────────────────────────────────
#   def __init__(self):

#     # ─── Definitions

#     # Element list
#     self.list = []

#     # ─── Print options

#     self.compact = False
#     self.indent = '  '

#   # ────────────────────────────────────────────────────────────────────────
#   def __str__(self):

#     return 'test'
