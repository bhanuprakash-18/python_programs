#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.


#copy some lines of text before you run this program
#text like 'Lists of animals\nLists of aquarium life\nLists of biologists by author abbreviation\nLists of cultivars'

import pyperclip
text = pyperclip.paste()
# Separate lines and add stars.
lines = text.split('\\n')
for i in range(len(lines)):    # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list
text = '\n'.join(lines)
pyperclip.copy(text)
#'Lists of animals\nLists of aquarium life\nLists of biologists by author abbreviation\nLists of cultivars'
