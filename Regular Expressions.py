#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import regex as re


# In[2]:


Sample_Text = 'Python Exercises, PHP exercises.'
replaced_text = re.sub("[ ,.]",":", Sample_Text)
print(replaced_text)


# In[3]:


data = {'SUMMARY' : ['hello, world!', 'XXXXX test', '123four, five:; six...']}
df = pd.DataFrame(data)
pat = '[^a-z\s]'
df['SUMMARY'] = df['SUMMARY'].str.replace(pat, '', regex=True)
print(df)


# In[4]:


str1 = "Virat Kohli is an Indian cricketer who plays for India national cricket team. He was born in Delhi, India on November 5, 1988. Virat is the first player in ICC cricket history to win all 3 ICC awards in a single year- ICC ODI player of the year, ICC Test player of the year and ICC Player of the year award in 2018."

pat = r"\b\w{4}\b"
reg_pat = re.compile(pat)
result = reg_pat.findall(str1)
print(result)


# In[5]:


str1 = "Virat Kohli is an Indian cricketer who plays for India national cricket team. He was born in Delhi, India on November 5, 1988. Virat is the first player in ICC cricket history to win all 3 ICC awards in a single year- ICC ODI player of the year, ICC Test player of the year and ICC Player of the year award in 2018."

pat = r"\b\w{3,5}\b"
reg_pat = re.compile(pat)
result = reg_pat.findall(str1)
print(result)


# In[6]:


texts = ["example (.com)","hr@fliprobo (.com)","github (.com)","Hello (Data Science World)","Data (Scientist)"]
pat = (r"[()]")
pattern = re.compile(pat)
for text in texts:
    print(re.sub(pattern,"", text))


# In[7]:


texts = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
for text in texts:
    print(re.sub("\([^)]*\)", '', text))


# In[8]:


pattern = '.[^A-Z]*'
text = "ImportanceOfRegularExpressionsInPython"
match = re.findall(pattern, text)
print(match)


# In[9]:


pattern = r'(\d+)([A-Za-z]+)'
text = "RegularExpression1IsAn2ImportantTopic3InPython"
match = re.sub(pattern, r' \1\2', text,)
print(match)


# In[10]:


pattern = r'(\d+)([A-Za-z]+)'
text = "RegularExpression1IsAn2ImportantTopic3InPython"
match = re.sub(pattern, r' \1 \2', text,)
print(match)


# In[11]:


df = pd.read_csv("https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv")
df


# In[12]:


pattern = r"(\w{6})"
df['first_five_letters'] = df['Country'].str.extract(pattern, expand=True)
df


# In[13]:


str2 = "Mahendra Singh Dhoni was born on 7 July 1981 in Ranchi, Bihar, India. He is an actor and producer, known for Let's_Get_Married (2023), Star Sports India vs Australia ODI Series 2013 (2013) and 2011 Cricket World Cup (2011)."

pat = r"\w+"

result = re.findall(pat, str2)

print('match_object = ',result )


# In[14]:


str2 = "1981 month of July day 7th, Mahendra Singh Dhoni was born on in Ranchi, Bihar, India. He is an actor and producer, known for Let's_Get_Married (2023), Star Sports India vs Australia ODI Series 2013 (2013) and 2011 Cricket World Cup (2011)."
pat = r"^\d+"
result = re.match(pat, str2)
#result = re.findall(pat, str2)
print('match_object = ',result )


# In[15]:


x = '0'
ip = '192.108.10.170'

result = re.sub(x, "",ip)

print('expected_result = ',result)


# In[16]:


text = "On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country"
pat = r"(\b([A-Z][a-z]+).\d{2}(th).\d{4}\b)"

result = re.search(pat, text)
print(result.group())


# In[17]:


#Question 15
text = "The quick brown fox jumps over the lazy dog."
pat = "fox|dog|horse"

match = re.findall(pat,text)
print(match)


# In[18]:


#Question 16
text = "The quick brown fox jumps over the lazy dog."
pat = "fox|dog"

match = re.search(pat,text)
print(match.group())


# In[19]:


#Question 17
text = "Python exercises, PHP exercises, C# exercises"
#pat = "exercises"

#match = re.findall(pat,text)
#print(match)

pat = re.compile("exercises")
for match in pat.finditer(text):
    print(match.group())
    


# In[20]:


#Question 18
#texts = ["Python exercises", "PHP exercises", "C# exercises"]

#for text in texts:
#    match = re.search("exercises",text)
 #   print(match)
    
text = "Python exercises, PHP exercises, C# exercises"
pat = re.finditer(r"exercises",text)
for match in pat:
    print(match)
    print(match.group())


# In[21]:


#Question 19
text = "2023-01-06"

match = re.sub(r"(\d{4})-(\d{1,2})-(\d{1,2})", '\\3-\\2-\\1',text)
print(match)


# In[22]:


#Question 20

text = "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
pat = re.compile(r'\d+\.\d{1,2}\b')

match = re.findall(pat, text)
print(match)


# In[23]:


#Question 21

text = "leading the Test rankings for 18 months starting December 2009"
pat = re.finditer('\d+', text)
for match in pat:
    print(match.group())
    print("position of str:- ", match.start())
    


# In[24]:


#Question 22

text = "My marks in each semester are: 947, 896, 926, 524, 734, 950, 642"
largest_numeric_value = re.findall(r'\d+',text)
max_marks = max(largest_numeric_value)
print(max_marks)


# In[25]:


#Question 23

text = "RegularExpressionIsAnImportantTopicInPython"
pat = r"(\w)([A-Z])"

result = re.sub(pat,r"\1 \2" ,text)
print(result)


# In[26]:


#Question 24
text = "Rishu Raj Kumar"
pat = '[A-Z][a-z]+'
reg_pat = re.compile(pat)
result = reg_pat.findall(text)
print(result)


# In[27]:


#Question 25
text = "Hello hello world world"
pat = r'\b(\w+)( \1\b)'

result = re.sub(pat, r'\1', text, re.UNICODE)
print(result)


# In[28]:


#Question 26
text = "this is abcd1234"

pat= r'\w+$'
result = re.search(pat, text)
print(result)


# In[29]:


#Question 27

text = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
pat = r'#\S+'

result = re.findall(pat, text)
print(result)


# In[30]:


#Question 28

text = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"

pat = r"<U\+\w{4}>"

result = re.sub(pat, "", text)
print(result)


# In[31]:


#Question 29

text = "Ron was born on 12-09-1992 and he was admitted to school 15-12-1999."
pat = r'\d{2}-\d{2}-\d{4}'

result = re.findall(pat, text)
print(result)


# In[32]:


#Question 30

text = "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
pat = r'\b\w{2,4}\b'
pattern = re.compile(pat)
print(re.sub(pattern,'', text))


# In[ ]:




