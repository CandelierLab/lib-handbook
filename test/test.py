'''
A test file for creating handbook pages
'''

import os

import handbook as hb

os.system('clear')

# ═══ Parameters ═══════════════════════════════════════════════════════════



# ══════════════════════════════════════════════════════════════════════════

H = hb.html(compact = False)

e1 = H.div('Some text...', {'id': 'my_div'})
e2 = H.span('-----')
e3 = H.div(e2)

res = H.div(H.div(e1 + e2 + e3))

print(res)

# ────────────