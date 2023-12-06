#!/usr/bin/env python
# coding: utf-8

# # Madlibs
# In this notebook, we will be creating a "Madlibds" game: a game where the user is aksed to input specific types 
# of words (nouns, verbs, etc.) and which returns a full text which uses these words to in places which were
# previously left blank on purpose.

# In[1]:


# importing regex will allow us to easily parse the text generate by our good friend ChatGPT and find the blanks to
# be filled, and create the list of inputs we want to ask our user.

import regex as re


# In[2]:


# we first open our ChatGPT-produced Madlibs text. Don't forget to specify the path to your file in the first line.

with open("/madlibs_text.txt", "r") as file:
    text = file.read()


# In[ ]:


# now we want to parse that text using regex to find the blanks, extract what they should be filled by into a list,
# and replace them in the text with {} to be used with the .format method.

blanks = re.findall("[[][A-Za-z]+[]]", text)

for word in blanks:
    text = text.replace(word, "{}")


# In[ ]:


# we now ask the user for all his inputs, and store them in a list.

inputList = []

for inpt in blanks:
    user_input = input("Please give us a/an: " + inpt)
    inputList.append(user_input)


# In[ ]:


# we can now replace every blank in the original text with the user's words.

new_text = text.format(*inputList)


# In[ ]:


# and finally, we can print the new text generated with the user's input! Youhou!

print(new_text)

