'''
Html
'''

# Classes to import
__all__ = ['html', 'comment', 'doctype', 
           'a', 'abbr', 'address', 'area', 'article', 'aside', 'audio',
           'b', 'base', 'bdi', 'bdo', 'blockquote', 'br', 'button',
           'canvas', 'caption', 'cite', 'code', 'col', 'colgroup',
           'data', 'datalist', 'dd', 'd_l', 'details', 'dfn', 'dialog', 'div', 'dl', 'dt',
           'em', 'embed', 'fieldset', 'figcaption', 'figure', 'footer', 'form',
           'h', 'head', 'header', 'hgroup', 'hr', 'i', 'iframe', 'img', 'input', 'ins', 
           'kbd', 'label', 'legend', 'li', 'link', 'main', 'map', 'mark', 'menu', 'meta', 'meter',
           'nav', 'noscript', 'object', 'ol', 'optgroup', 'option', 'output', 
           'p', 'param', 'picture', 'pre', 'progress', 'q', 'rp', 'rt', 'ruby', 
           's', 'samp', 'script', 'search', 'section', 'select', 'small',
           'source', 'span', 'strong', 'style', 'sub', 'summary', 'sup', 'svg', 
           'table', 'tbody', 'td', 'template', 'textarea', 'tfoot', 'th', 'thead', 'time', 
           'title', 'tr', 'track', 'u', 'ul', 'var', 'video', 'wbr']

import os

# ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
# █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
# █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ELEMENTS ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
# █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
# ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

class element:

  # ────────────────────────────────────────────────────────────────────────
  def __init__(self, type=None, content=None, parameters=None, single=False, inline=False):

    # Tag type (div, span, img, etc.)
    self.type = type

    # Single tag representation
    self.single = single

    # Html display
    self.inline = inline    

    # Parameters and content 
    self.parameters = {} if parameters is None else parameters
    self.content = [] if content is None else (content if isinstance(content, list) else [content])
    
  # ────────────────────────────────────────────────────────────────────────
  def __call__(self):
    return self.__str__()

  # ────────────────────────────────────────────────────────────────────────
  def __str__(self):

    s = f'─── {self.type} ─────────────────────────────────\n'
    s += self.str() #.strip()

    return s

  # ────────────────────────────────────────────────────────────────────────
  def str(self, compact=False, indent='  '):

    # Manage indent for simple containers
    _indent_ = '' if self.type is None else indent

    # Output string
    s = ''

    # ─── Start tag

    if self.type is not None:

      # Initialization
      s += '<' + self.type

      # Parameters
      for k, v in self.parameters.items():

        # Substitutes for the reserved keyword 'class'
        if k.lower() in ['class', 'cls']: k = 'class'

        if v is None:
          s += ' ' + k
        else:
          s += f' {k}='
          match v.__class__():
            case str(): s += "'" + v + "'"
            case _: s += str(v)
      s += '>'

      # End of starting tag
      if self.single: return s  #if compact else s + '\n'

      # Inline
      if not compact and not self.inline: s += '\n'
      
    # ─── Content

    if len(self.content):

      for c in self.content:

        if isinstance(c, str):
          if compact or self.inline:
            s += c.strip()
          else:
            s += _indent_ + c.strip() + '\n'

        elif isinstance(c, element):      
          if compact or self.inline:
            s += c.str(compact, indent).strip()
          else:
            s += _indent_ + c.str(compact, indent).strip().replace('\n', '\n' + _indent_) + '\n'
              
    # ─── Closing tag

    if self.type is not None:

      s += '</' + self.type + '>'
      
      # Inline
      if not compact and not self.inline: s += '\n'

    return s

  # ────────────────────────────────────────────────────────────────────────
  def __lt__(self, elm):
    self.content.append(elm)

  # ────────────────────────────────────────────────────────────────────────
  def __add__(self, a):

    if isinstance(a, (str, element)):
      r = element()
      r < self
      r < a
      return r
    else:
      return NotImplemented
      
  # ────────────────────────────────────────────────────────────────────────
  def __radd__(self, a):

    if isinstance(a, (str, element)):
      r = element()
      r < a
      r < self
      return r
    else:
      return NotImplemented

# ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
# █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
# █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ HTML CLASS ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
# █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
# ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

class html(element):

  # ────────────────────────────────────────────────────────────────────────
  def __init__(self, compact=False):

    super().__init__()

    # ─── Html display

    self.compact = compact
    self.indent = '  '

    # ─── Content

    self.head = head()
    self.body = body()

    self.built = None

  # ────────────────────────────────────────────────────────────────────────
  def __str__(self):
    return self.build()

  # ────────────────────────────────────────────────────────────────────────
  def build(self):

    if self.built is None:
      '''
      The html document is built just once
      '''

      # Build html document
      self < doctype('html')
      H = element('html')
      H < self.head
      H < self.body
      self < H

      self.built = self.str(compact=self.compact, indent=self.indent).strip()

    # Output string
    return self.built

  # ────────────────────────────────────────────────────────────────────────
  def save(self, filename):

    with open(filename, 'w') as f:
      f.write(self.build())

# ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
# █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
# █░░░░░░░░░░░░░░░░░░░░░░░░░░░ HTML5 ELEMENTS ░░░░░░░░░░░░░░░░░░░░░░░░░░░█
# █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
# ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

# ────────────────────────────────────────────────────────────────────────
class comment(element):

  # ────────────────────────────────────────────────────────────────────────
  def __init__(self, string:str):

    super().__init__('comment')
    self.string = string
    
  # ────────────────────────────────────────────────────────────────────────
  def str(self, compact=False, indent='  '):

    # Comment
    s = f'<!-- {self.string} -->'
        
    # Inline
    if not compact: s += '\n'

    return s

# ────────────────────────────────────────────────────────────────────────
class doctype(element):
  def __init__(self, doctype):
    super().__init__('!DOCTYPE', parameters={doctype:None}, single=True)

# ────────────────────────────────────────────────────────────────────────
class a(element):
  def __init__(self, href, *args, **kwargs):
    super().__init__('a', content=list(args), parameters=dict({'href':href}, **kwargs), inline=True)

# ────────────────────────────────────────────────────────────────────────
class abbr(element):
  def __init__(self, title, *args):
    super().__init__('abbr', content=list(args), parameters={'title':title}, inline=True)

# ────────────────────────────────────────────────────────────────────────
class address(element):
  def __init__(self, *args, **kwargs):
    super().__init__('address', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class area(element):
  def __init__(self, **kwargs):
    super().__init__('area', parameters=kwargs, single=True)

# ────────────────────────────────────────────────────────────────────────
class article(element):
  def __init__(self, *args, **kwargs):
    super().__init__('article', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class aside(element):
  def __init__(self, *args, **kwargs):
    super().__init__('aside', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class audio(element):
  def __init__(self, *args, **kwargs):
    super().__init__('audio', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class b(element):
  def __init__(self, *args, **kwargs):
    super().__init__('b', content=list(args), parameters=kwargs, inline=True)

# ────────────────────────────────────────────────────────────────────────
class base(element):
  def __init__(self, **kwargs):
    super().__init__('base', parameters=kwargs, single=True)

# ────────────────────────────────────────────────────────────────────────
class bdi(element):
  def __init__(self, *args, **kwargs):
    super().__init__('bdi', content=list(args), parameters=kwargs, inline=True)

# ────────────────────────────────────────────────────────────────────────
class bdo(element):
  def __init__(self, *args, **kwargs):
    super().__init__('bdo', content=list(args), parameters=kwargs, inline=True)

# ────────────────────────────────────────────────────────────────────────
class blockquote(element):
  def __init__(self, *args, **kwargs):
    super().__init__('blockquote', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class body(element):
  def __init__(self, *args, **kwargs):
    super().__init__('body', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class br(element):
  def __init__(self, **kwargs):
    super().__init__('br', parameters=kwargs, single=True)

# ────────────────────────────────────────────────────────────────────────
class button(element):
  def __init__(self, *args, **kwargs):
    super().__init__('button', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class canvas(element):
  def __init__(self, *args, **kwargs):
    super().__init__('canvas', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class caption(element):
  def __init__(self, *args, **kwargs):
    super().__init__('caption', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class cite(element):
  def __init__(self, *args, **kwargs):
    super().__init__('cite', content=list(args), parameters=kwargs, inline=True)

# ────────────────────────────────────────────────────────────────────────
class code(element):
  def __init__(self, *args, **kwargs):
    super().__init__('code', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class col(element):
  def __init__(self, **kwargs):
    super().__init__('col', parameters=kwargs, single=True)

# ────────────────────────────────────────────────────────────────────────
class colgroup(element):
  def __init__(self, *args, **kwargs):
    super().__init__('colgroup', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class data(element):
  def __init__(self, *args, **kwargs):
    super().__init__('data', content=list(args), parameters=kwargs, inline=True)

# ────────────────────────────────────────────────────────────────────────
class datalist(element):
  def __init__(self, *args, **kwargs):
    super().__init__('datalist', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class dd(element):
  def __init__(self, *args, **kwargs):
    super().__init__('dd', content=list(args), parameters=kwargs, inline=True)

# ────────────────────────────────────────────────────────────────────────
class d_l(element):
  def __init__(self, *args, **kwargs):
    super().__init__('del', content=list(args), parameters=kwargs, inline=True)

# ────────────────────────────────────────────────────────────────────────
class details(element):
  def __init__(self, *args, **kwargs):
    super().__init__('details', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class dfn(element):
  def __init__(self, *args, **kwargs):
    super().__init__('dfn', content=list(args), parameters=kwargs, inline=True)

# ────────────────────────────────────────────────────────────────────────
class dialog(element):
  def __init__(self, *args, **kwargs):
    super().__init__('dialog', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class div(element):
  def __init__(self, *args, **kwargs):
    super().__init__('div', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class dl(element):
  def __init__(self, *args, **kwargs):
    super().__init__('dl', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class dt(element):
  def __init__(self, *args, **kwargs):
    super().__init__('dt', content=list(args), parameters=kwargs, inline=True)

# ────────────────────────────────────────────────────────────────────────
class em(element):
  def __init__(self, *args, **kwargs):
    super().__init__('em', content=list(args), parameters=kwargs, inline=True)

# ────────────────────────────────────────────────────────────────────────
class embed(element):
  def __init__(self, **kwargs):
    super().__init__('embed', parameters=kwargs, single=True)

# ────────────────────────────────────────────────────────────────────────
class fieldset(element):
  def __init__(self, *args, **kwargs):
    super().__init__('fieldset', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class figcaption(element):
  def __init__(self, *args, **kwargs):
    super().__init__('figcaption', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class figure(element):
  def __init__(self, *args, **kwargs):
    super().__init__('figure', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class footer(element):
  def __init__(self, *args, **kwargs):
    super().__init__('footer', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class form(element):
  def __init__(self, *args, **kwargs):
    super().__init__('form', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class inline(element):
  def __init__(self, *args, **kwargs):
    super().__init__('inline', content=list(args), parameters=kwargs, inline=True)

# ────────────────────────────────────────────────────────────────────────
class h(element):
  def __init__(self, level=1, *args, **kwargs):
    super().__init__(f'h{level}', content=list(args), parameters=kwargs, inline=True)

# ────────────────────────────────────────────────────────────────────────
class head(element):
  def __init__(self, *args, **kwargs):
    super().__init__('head', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class header(element):
  def __init__(self, *args, **kwargs):
    super().__init__('header', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class hgroup(element):
  def __init__(self, *args, **kwargs):
    super().__init__('hgroup', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class hr(element):
  def __init__(self, **kwargs):
    super().__init__('hr', parameters=kwargs, single=True)

# ────────────────────────────────────────────────────────────────────────
class i(element):
  def __init__(self, *args, **kwargs):
    super().__init__('i', content=list(args), parameters=kwargs, inline=True)

# ────────────────────────────────────────────────────────────────────────
class iframe(element):
  def __init__(self, *args, **kwargs):
    super().__init__('iframe', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class img(element):
  def __init__(self, src, **kwargs):
    super().__init__('img', parameters=dict({'src':src}, **kwargs), single=True)

# ────────────────────────────────────────────────────────────────────────
class input(element):
  def __init__(self, **kwargs):
    super().__init__('input', parameters=kwargs, single=True)

# ────────────────────────────────────────────────────────────────────────
class ins(element):
  def __init__(self, *args, **kwargs):
    super().__init__('ins', content=list(args), parameters=kwargs, inline=True)

# ────────────────────────────────────────────────────────────────────────
class kbd(element):
  def __init__(self, *args, **kwargs):
    super().__init__('kbd', content=list(args), parameters=kwargs, inline=True)

# ────────────────────────────────────────────────────────────────────────
class label(element):
  def __init__(self, *args, **kwargs):
    super().__init__('label', content=list(args), parameters=kwargs, inline=True)

# ────────────────────────────────────────────────────────────────────────
class legend(element):
  def __init__(self, *args, **kwargs):
    super().__init__('legend', content=list(args), parameters=kwargs, inline=True)

# ────────────────────────────────────────────────────────────────────────
class li(element):
  def __init__(self, *args, **kwargs):
    super().__init__('li', content=list(args), parameters=kwargs, inline=True)

# ────────────────────────────────────────────────────────────────────────
class link(element):
  def __init__(self, **kwargs):
    super().__init__('link', parameters=kwargs, single=True)

# ────────────────────────────────────────────────────────────────────────
class main(element):
  def __init__(self, *args, **kwargs):
    super().__init__('main', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class map(element):
  def __init__(self, *args, **kwargs):
    super().__init__('map', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class mark(element):
  def __init__(self, *args, **kwargs):
    super().__init__('mark', content=list(args), parameters=kwargs, inline=True)

# ────────────────────────────────────────────────────────────────────────
class menu(element):
  def __init__(self, *args, **kwargs):
    super().__init__('menu', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class meta(element):
  def __init__(self, **kwargs):
    super().__init__('meta', parameters=kwargs, single=True)

# ────────────────────────────────────────────────────────────────────────
class meter(element):
  def __init__(self, *args, **kwargs):
    super().__init__('meter', content=list(args), parameters=kwargs, inline=True)

# ────────────────────────────────────────────────────────────────────────
class nav(element):
  def __init__(self, *args, **kwargs):
    super().__init__('nav', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class noscript(element):
  def __init__(self, *args, **kwargs):
    super().__init__('noscript', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class object(element):
  def __init__(self, *args, **kwargs):
    super().__init__('object', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class ol(element):
  def __init__(self, *args, **kwargs):
    super().__init__('ol', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class optgroup(element):
  def __init__(self, *args, **kwargs):
    super().__init__('optgroup', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class option(element):
  def __init__(self, *args, **kwargs):
    super().__init__('option', content=list(args), parameters=kwargs, inline=True)

# ────────────────────────────────────────────────────────────────────────
class output(element):
  def __init__(self, *args, **kwargs):
    super().__init__('output', content=list(args), parameters=kwargs, inline=True)

# ────────────────────────────────────────────────────────────────────────
class p(element):
  def __init__(self, *args, **kwargs):
    super().__init__('p', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class param(element):
  def __init__(self, **kwargs):
    super().__init__('param', parameters=kwargs, single=True)

# ────────────────────────────────────────────────────────────────────────
class picture(element):
  def __init__(self, *args, **kwargs):
    super().__init__('picture', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class pre(element):
  def __init__(self, *args, **kwargs):
    super().__init__('pre', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class progress(element):
  def __init__(self, *args, **kwargs):
    super().__init__('progress', content=list(args), parameters=kwargs, inline=True)

# ────────────────────────────────────────────────────────────────────────
class q(element):
  def __init__(self, *args, **kwargs):
    super().__init__('q', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class rp(element):
  def __init__(self, *args, **kwargs):
    super().__init__('rp', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class rt(element):
  def __init__(self, *args, **kwargs):
    super().__init__('rt', content=list(args), parameters=kwargs, inline=True)

# ────────────────────────────────────────────────────────────────────────
class ruby(element):
  def __init__(self, *args, **kwargs):
    super().__init__('ruby', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class s(element):
  def __init__(self, *args, **kwargs):
    super().__init__('s', content=list(args), parameters=kwargs, inline=True)

# ────────────────────────────────────────────────────────────────────────
class samp(element):
  def __init__(self, *args, **kwargs):
    super().__init__('samp', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class script(element):
  def __init__(self, *args, **kwargs):
    super().__init__('script', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class search(element):
  def __init__(self, *args, **kwargs):
    super().__init__('search', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class section(element):
  def __init__(self, *args, **kwargs):
    super().__init__('section', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class select(element):
  def __init__(self, *args, **kwargs):
    super().__init__('select', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class small(element):
  def __init__(self, *args, **kwargs):
    super().__init__('small', content=list(args), parameters=kwargs, inline=True)

# ────────────────────────────────────────────────────────────────────────
class source(element):
  def __init__(self, **kwargs):
    super().__init__('source', parameters=kwargs, single=True)

# ────────────────────────────────────────────────────────────────────────
class span(element):
  def __init__(self, *args, **kwargs):
    super().__init__('span', content=list(args), parameters=kwargs, inline=True)

# ────────────────────────────────────────────────────────────────────────
class strong(element):
  def __init__(self, *args, **kwargs):
    super().__init__('strong', content=list(args), parameters=kwargs, inline=True)

# ────────────────────────────────────────────────────────────────────────
class style(element):
  def __init__(self, *args, **kwargs):
    super().__init__('style', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class sub(element):
  def __init__(self, *args, **kwargs):
    super().__init__('sub', content=list(args), parameters=kwargs, inline=True)

# ────────────────────────────────────────────────────────────────────────
class summary(element):
  def __init__(self, *args, **kwargs):
    super().__init__('summary', content=list(args), parameters=kwargs, inline=True)

# ────────────────────────────────────────────────────────────────────────
class sup(element):
  def __init__(self, *args, **kwargs):
    super().__init__('sup', content=list(args), parameters=kwargs, inline=True)

# ────────────────────────────────────────────────────────────────────────
class svg(element):
  def __init__(self, *args, **kwargs):
    super().__init__('svg', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class table(element):
  def __init__(self, *args, **kwargs):
    super().__init__('table', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class tbody(element):
  def __init__(self, *args, **kwargs):
    super().__init__('tbody', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class td(element):
  def __init__(self, *args, **kwargs):
    super().__init__('td', content=list(args), parameters=kwargs, inline=True)

# ────────────────────────────────────────────────────────────────────────
class template(element):
  def __init__(self, *args, **kwargs):
    super().__init__('template', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class textarea(element):
  def __init__(self, *args, **kwargs):
    super().__init__('textarea', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class tfoot(element):
  def __init__(self, *args, **kwargs):
    super().__init__('tfoot', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class th(element):
  def __init__(self, *args, **kwargs):
    super().__init__('th', content=list(args), parameters=kwargs, inline=True)

# ────────────────────────────────────────────────────────────────────────
class thead(element):
  def __init__(self, *args, **kwargs):
    super().__init__('thead', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class time(element):
  def __init__(self, *args, **kwargs):
    super().__init__('time', content=list(args), parameters=kwargs, inline=True)

# ────────────────────────────────────────────────────────────────────────
class title(element):
  def __init__(self, *args, **kwargs):
    super().__init__('title', content=list(args), parameters=kwargs, inline=True)

# ────────────────────────────────────────────────────────────────────────
class tr(element):
  def __init__(self, *args, **kwargs):
    super().__init__('tr', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class track(element):
  def __init__(self, **kwargs):
    super().__init__('track', parameters=kwargs, single=True)

# ────────────────────────────────────────────────────────────────────────
class u(element):
  def __init__(self, *args, **kwargs):
    super().__init__('u', content=list(args), parameters=kwargs, inline=True)

# ────────────────────────────────────────────────────────────────────────
class ul(element):
  def __init__(self, *args, **kwargs):
    super().__init__('ul', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class var(element):
  def __init__(self, *args, **kwargs):
    super().__init__('var', content=list(args), parameters=kwargs, inline=True)

# ────────────────────────────────────────────────────────────────────────
class video(element):
  def __init__(self, *args, **kwargs):
    super().__init__('video', content=list(args), parameters=kwargs)

# ────────────────────────────────────────────────────────────────────────
class wbr(element):
  def __init__(self):
    super().__init__('wbr', single=True)