'''
A test file for creating handbook pages
'''

import os

import handbook as hb

os.system('clear')

# ═══ Parameters ═══════════════════════════════════════════════════════════



# ══════════════════════════════════════════════════════════════════════════

P = hb.page()

P.body < 'ok'

print(P)
P.save('test.html')

# print(H.head)

# c1 = H.comment('This is a comment')
# e1 = H.div('Some text...', {'id': 'my_div'})
# e2 = H.span('-----')
# e3 = H.div(c1 + e2 + c1)

# res = c1 + H.div(H.div(e1 + c1 + e2 + e3))

# print(res)

# ────────────

# <!doctype html>
# <html lang="fr">
# <head>
#   <meta charset="utf-8">
#   <title>Titre de la page</title>
#   <link rel="stylesheet" href="style.css">
#   <script src="script.js"></script>
# </head>
# <body>
#   ...
#   <!-- Le reste du contenu -->
#   ...
# </body>
# </html>