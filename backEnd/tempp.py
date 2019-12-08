
print("Starting Process ..")



import readFromPPT

text_runs = readFromPPT.pptData()
print(text_runs)




      # /* text_frame = shape.text_frame*/
      #for paragraph in shape.text_frame.paragraphs:
      #   for run in paragraph.runs:
      #      text_runs.append(run.text)

# print(len(title))
# print(title)
# print(len(text_runs))
# print(text_runs[0])

# for i in range(0, len(text_runs)):
#     print(title[i+1])
#     print( text_runs[i], end="")



#----# Storing data in xml

# print("Generating xml file of valid content ..")
#
#
# filename = "test_xml.xml"
# rootTag = xml.Element("Slides")
# rootTag.text = title[0]
#
# for i in range(0, len(text_runs)):
#     elementTag = xml.Element("Slide")
#     titleTag = xml.SubElement(elementTag, "Title")
#     titleTag.text = title[i]
#     contentTag  = xml.SubElement(elementTag, "Content")
#
#     for slide in text_runs[i]:
#         pointsTag = xml.SubElement(contentTag, "Points")
#         pointsTag.text =slide
#     rootTag.append(elementTag)
# tree = xml.ElementTree(rootTag)
# tree.write("filename.xml")

#---# Store in xml file


#---# Extract KeyWord


print("Generating Key words ..")
from rake_nltk import Rake

rake = Rake(min_length=1, max_length=2)

print(text_runs[0])

all_keywords=[]

for slide in text_runs:
    slide_Arr = []

    for line in slide:

        # myText = text_runs[0][0]
        rake.extract_keywords_from_text(line)
        if len(rake.get_ranked_phrases())>0:
            slide_Arr.append(rake.get_ranked_phrases()[0])
        else:
            slide_Arr.append("null")
    all_keywords.append(slide_Arr)


filename = "test_xml.xml"
nrootTag = xml.Element("Questions")
nrootTag.text = "BLANKS AND OPTIONS"
i=0
j=0

import xml.etree.ElementTree as xml
import re
for slide in text_runs:

    for line in slide:
        if all_keywords[i][j] == 'null':
            continue
        else:
            print("i = ", i , "  j = ", j )
            src_str = re.compile(all_keywords[i][j],re.IGNORECASE)
            sen = str(text_runs[i][j])

            questionTag = xml.Element("question")
            quesTag = xml.SubElement(questionTag, "ques")
            # questionTag.text=sen.replace(all_keywords[i][j],'________________')
            quesTag.text=src_str.sub('________________',sen)
            answerTag = xml.SubElement(questionTag, "answer")
            answerTag.text = all_keywords[i][j]
        nrootTag.append(questionTag)

        j+=1


    j=0
    i+=1


tree = xml.ElementTree(nrootTag)
tree.write("questions.xml")

print("Cleaning and tokenizing Keywords ..")

from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
# using average perceptron Tagger pos
text = word_tokenize(all_keywords[2][0])
print (all_keywords[2][0])
print (nltk.pos_tag(text))
