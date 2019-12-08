import sys

print("Starting Process ..")

import readFromPPT
import tokenizeSentence
import random


if len(sys.argv) == 2:
    isPPT = sys.argv[1]

if isPPT == '0':
    isPPT = 0
    print("Text Detected")
else:
    isPPT = 1
    print("PPT File Detected")
# isPPT=0


if (isPPT):
    text_runs = readFromPPT.pptPasredData()
else:
    text_runs = tokenizeSentence.getSentencec()



random.shuffle(text_runs)
if len(text_runs)>10:
    text_runs = text_runs[:10]
print(text_runs)






import ExtractKeyWords
print("Making Setup for Extracting Keywords")
all_keywords  = ExtractKeyWords.getKeyWords(text_runs)

# file = open("keywordss.txt",'w')
#
#
# for keyword in all_keywords:
#     file.write("{},".format(keyword))
# file.close()



# print(all_keywords)


print("Making Setup for Generating Distractors")
import word2vec
optAnsArr=word2vec.generateOprtions(all_keywords)


# print(optAnsArr)

print("Finalizing Results")
import re
import xml.etree.ElementTree as xml

filename = "test_xml.xml"
nrootTag = xml.Element("Questions")
nrootTag.text = "BLANKS AND OPTIONS"
i=0
for line in text_runs:
    if all_keywords[i] == "null":
        continue
    else:
        src_str = re.compile(all_keywords[i], re.IGNORECASE)
        sen = str(text_runs[i])
        questionTag = xml.Element("question")
        quesTag = xml.SubElement(questionTag, "ques")
        # questionTag.text=sen.replace(all_keywords[i][j],'________________')
        quesTag.text = src_str.sub('________________', sen)
        answerTag = xml.SubElement(questionTag, "answer")
        answerTag.text = all_keywords[i]
        ii=1
        for option in optAnsArr[i]:
            optionTag = xml.SubElement(questionTag, "option"+str(ii))
            optionTag.text = option
            ii+=1
        ii=0

    nrootTag.append(questionTag)
    i+=1

tree = xml.ElementTree(nrootTag)
tree.write("C:/xampp/htdocs/quru_v2/questions22.xml")
tree.write("questions22.xml")
print("Finished Processing")
