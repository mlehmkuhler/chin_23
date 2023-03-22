#make it into spreadsheet--get the text, extract the info (match objects), define it, then make it into a dataframe.
#number  title   text    notes (pattern. Notes isn't always present)

#imports reg exp library
import re

#opens and reads file
with open('ftales.txt','r', encoding='utf8') as rf:
    text = rf.read()

#splits into chapters along roman numeral dividers
chapters = re.split(r'([IVXCL]+\.)', text)

#regex for roman numeral (roman numerals, single line, not within parentheses)
ftale_regex = re.compile(r'''
[IVXCL] #matches roman numeral (with brackets letting us do "or")
#[find one line all caps] #matches titles
#[matches text (use nltk, or define paragraph on own?)]
[matches text] #matches note, question mark means it doesn't have to be there.

''', re.X)

#search titles (all caps, single line, some include roman numerals following in parentheses)
#search text (paragraphs, between titles and notes (not always notes at end)
#search notes (all begin with "Note: " and the rest of the line)

#put those items into a dataframe/spreadsheet

with open('ftales.tsv', 'w', encoding='utf8') as wf:
    wf.write("\n".join(outputdata))