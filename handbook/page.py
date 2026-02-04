import os
from handbook.html import *

class page(html):

  # ────────────────────────────────────────────────────────────────────────
  def __init__(self, compact=False):

    super().__init__(compact=compact)

    # ─── Head contents ─────────────────────────

    # ─── Meta tags
     
    self.head < meta(charset='UTF-8')
    self.head < meta(name='viewport', content='width=device-width, initial-scale=1.0')

    # Stylesheet
    self.head < link(rel="stylesheet", href="files/style.css")

    # ─── Page content ──────────────────────────

    # Main 
    self.main = main()

    self.body < self.main


