# -*- coding: utf-8 -*-

import nltk

sentence = "I agree! Because I vape Candybeca so much, I am used to that stronger flavor. That is a very good point about the Hazelnut (FW), thank you for letting me know! I never make negative comments because I simply don't like a recipe, I only try to give positive feedback or, feedback on recipes that are good but I have some constructive thoughts. If I didn't like RY4 or Peanut Butter and complained that your recipe is not very good, well that's just silly! In that case it's not that there is anything wrong with the recipe just because I don't like the flavors in it. Lol! I think your flavors here are all working together really well, I just thought I would share my thoughts for others who are having a similar experience. I just increased the RY4 double and the peanut butter, and it's amazing! Thanks for the response!"

tokens = nltk.word_tokenize(sentence)
# print(tokens)

tagged = nltk.pos_tag(tokens)
print(tagged)


# File = open(fileName) #open file
# lines = File.read() #read all lines
# sentences = nltk.sent_tokenize(lines) #tokenize sentences
nouns = [] #empty to array to hold all nouns

for word,pos in nltk.pos_tag(tokens):
    if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
        nouns.append(word)
print(nouns)

tagged2 = nltk.pos_tag(nouns)
print(tagged2)
