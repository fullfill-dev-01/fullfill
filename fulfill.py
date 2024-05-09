import docx
import json
doc = docx.Document("example form.docx")
data = open("fulfill_userdata.json")
values = json.load(data)
for par in doc.paragraphs:
  line = par.text.lower()
  while line.endswith("_"):
     line = line[:-1]
     par.text = par.text[:-1]
  while line.endswith(":"):
     line = line[:-1]
  for x,y in values.items():
      if line.endswith(x) == True:
         par.text = par.text + " " + y
  print(par.text)
doc.save("fulfilled.docx")