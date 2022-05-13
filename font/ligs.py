import fontforge
from os.path import exists

font = fontforge.font()
font.encoding = "UnicodeFull"

font.fontname="Lotrazi Neue"

letters = ['b','B','t','T','r','R','w','e','q','n','N','m','M','j','J','k','K','h','H','u','U','f','F','v','V','d','s','a','x','c','z','y','Y','g','G']
diacritics = ["Q", "A", "Z", "W", "S", "X"] 
stressors = ["E"]

index = 57344

# for i in range(33,126):
#   glyph = font.createChar(i)
#   if (exists(f'svg/{i}.svg')):
#     glyph.importOutlines(f'svg/{i}.svg')
#     font[glyph.glyphname].width = 600

# for i in ["Q", "A", "Z", "W", "S", "X", "E", "D", "C"]:
#     font[i].width = 250

base = fontforge.open("Lotrazi_Neue_base.sfd")
base.selection.select(("ranges",None),33,126)
base.copy()

font.selection.select(("ranges",None),33,126)
font.paste()

def usedGlyphs(glyph):
  names = []
  for i in glyph.references:
    names.append(i[0])
  return names

for i in letters:
  for j in diacritics:
    ligature_name = f'{i}_{j}'
    ligature_tuple = (i,j)
    font.addLookup(f'ligature_{i}_{j}','gsub_ligature',(),[['liga',[['latn',['dflt']]]]])
    font.addLookupSubtable(f'ligature_{i}_{j}',f'ligaturesh_{i}_{j}')
    glyph = font.createChar(index, ligature_name)
    glyph.width = font[i].width - font[j].width
    index = index + 1
    glyph.addPosSub(f'ligaturesh_{i}_{j}',ligature_tuple)
    glyph.build()

for i in letters:
  for j in stressors:
    ligature_name = f'{i}_{j}'
    ligature_tuple = (i,j)
    font.addLookup(f'ligature_{i}_{j}','gsub_ligature',(),[['liga',[['latn',['dflt']]]]])
    font.addLookupSubtable(f'ligature_{i}_{j}',f'ligaturesh_{i}_{j}')
    glyph = font.createChar(index, ligature_name)
    glyph.width = font[i].width - font[j].width
    index = index + 1
    glyph.addPosSub(f'ligaturesh_{i}_{j}',ligature_tuple)
    glyph.build()

stressors = ["E", "D", "C"]

for i in letters:
  for j in diacritics:
    for k in stressors:
      if (j == "W" and (k == "D" or k == "C")):
        continue
      ligature_name = f'{i}_{j}_{k}'
      ligature_tuple = (i,j,k)
      font.addLookup(f'ligature_{i}_{j}_{k}','gsub_ligature',(),[['liga',[['latn',['dflt']]]]])
      font.addLookupSubtable(f'ligature_{i}_{j}_{k}',f'ligaturesh_{i}_{j}_{k}')
      glyph = font.createChar(index, ligature_name)
      glyph.width = font[i].width - font[j].width - font[k].width
      index = index + 1
      glyph.addPosSub(f'ligaturesh_{i}_{j}_{k}',ligature_tuple)
      glyph.build()

for i in range(57344,index):
    font[i].width = 1000

for i in range(57344,57356):
  comps = usedGlyphs(font[i])
  font[i].unlinkRef()
  print(f'{font[i].glyphname} has {len(font[i].layers[1])} contours from glyphs {comps}')
  for j in range(0,len(font[i].layers[1])):
    print(f'contour {j} has {len(font[i].layers[1][j])} points')
#  font[i].layers[1][2] = font[i].layers[1][2].transform([1,0,1,1,100.0,100.0])

font.save("Lotrazi_Neue.sfd")

exit()