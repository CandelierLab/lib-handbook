'''
A test file for creating handbook pages
'''

import os

from handbook import element, handbook

os.system('clear')

# ═══ Parameters ═══════════════════════════════════════════════════════════



# ══════════════════════════════════════════════════════════════════════════

E = element()
E.type = 'span'
E.content = 'Some text...'
E.parameters['id'] = 'my_span'

F = element()
F.type = 'div'
F.content = E
F.parameters['class'] = 'my_div'


print(F)

# H = handbook()

# ────────────