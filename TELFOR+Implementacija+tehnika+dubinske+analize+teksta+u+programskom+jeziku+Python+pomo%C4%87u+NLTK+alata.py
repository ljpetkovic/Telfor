
# coding: utf-8

# # Preuzimanje NLTK-a

# In[2]:

import nltk
nltk.download()
from nltk.book import *


# # Konkordansa

# In[3]:

text2.concordance('affection')


# In[36]:

text3.concordance('lived')


# In[37]:

text4.concordance('terror', width = 100)


# In[38]:

text6.concordance("bloody")


# In[5]:

text1.concordance("bloody")


# # Procentualna zastupljenost reči na nivou čitavog teksta

# In[35]:

def zastupljenost(string, substring):
    a = string.count(substring) / len(string) * 100
    b = a * 100
    print(b)
zastupljenost(text2, 'affection')


# In[47]:

zastupljenost(text3, 'God')


# # Tokeni

# In[39]:

print(sorted((text3)))


# # Jedinstvene leksičke stavke

# In[8]:

print(sorted(set(text3)))


# # Prečišćena statistika 

# ## _The Man Who Was Thursday_, G. K. Chesterton

# In[44]:

from nltk.corpus import gutenberg
from nltk import word_tokenize
from nltk.corpus import stopwords
set(stopwords.words('english'))

def statistika(text):
    tokens = [word_tokenize(word) for word in gutenberg.words(text)]
    tokens = [token.strip() for token in gutenberg.words(text)]
    tokens = [token.lower() for token in gutenberg.words(text)]
    tokens = [token for token in tokens if token.isalpha()]
    stoplist = stopwords.words('english')
    tokens = [w for w in tokens if not w in stoplist]
    print(len(tokens), len(set(tokens)))
    a = len(set(tokens)) / len(tokens) * 100
    print(a)
statistika('chesterton-thursday.txt')


# ## _Knjiga postanja_

# In[46]:

from nltk.corpus import genesis
from nltk import word_tokenize
from nltk.corpus import stopwords
set(stopwords.words('english'))

def statistika2(text):
    tokens = [word_tokenize(word) for word in genesis.words(text)]
    tokens = [token.strip() for token in genesis.words(text)]
    tokens = [token.lower() for token in genesis.words(text)]
    tokens = [token for token in tokens if token.isalpha()]
    stoplist = stopwords.words('english')
    tokens = [w for w in tokens if not w in stoplist]
    print(len(tokens), len(set(tokens)))
    a = len(set(tokens)) / len(tokens) * 100
    print(a)
statistika2('english-kjv.txt')


# # Leksička frekvencija

# In[49]:

def frekvencija(string, substring):
    words = string.count(substring)
    print(words)
    
frekvencija(text3, 'God')


# ## _The Man Who Was Thursday_, G. K. Chesterton

# ## _Knjiga postanja_

# In[23]:

len(text3)


# In[24]:

len(set(text3))


# # Leksički diverzitet

# In[25]:

def leksički_diverzitet(text): 
    return len(set(text)) / len(text) * 100
leksički_diverzitet(text3)


# In[22]:

leksički_diverzitet(text9)


# # Grafik leksičke disperzije

# In[15]:

len(text9)


# In[17]:

len(set(text9))


# ## _Inaugural Address Corpus 1789-2009_

# In[50]:

text4.dispersion_plot(['people', 'nation', 'terror', 'God', 'liberty', 'children', 'men', 'women', 'work', 'citizens', 'constitution', 'democracy', 'solidarity', 'freedom', 'duties', 'America', 'future'])


# In[80]:

frekvencija(text4, 'men')


# # Najčešće reči

# ## _Lincoln_ (1865)

# In[73]:

from nltk.corpus import inaugural
from nltk import word_tokenize
from nltk.corpus import stopwords
set(stopwords.words('english'))

def najcesce_reci(text):
    tokens = [word_tokenize(word) for word in inaugural.words(text)]
    tokens = [token.strip() for token in inaugural.words(text)]
    tokens = [token.lower() for token in inaugural.words(text)]
    tokens = [token for token in tokens if token.isalpha()]
    stoplist = stopwords.words('english')
    tokens = [w for w in tokens if not w in stoplist]
    fdist = FreqDist(tokens)
    fdist1 = fdist.most_common(20)
    fdist.plot(20, cumulative = False)
    print(fdist1)

najcesce_reci('1865-Lincoln.txt')   


# # Prikaz dugačkih reči 

# In[71]:

def duge_reci(text):
    V = set(text)
    long_words = [w for w in V if len(w) >= 15]
    print(len(long_words), sorted(long_words))
duge_reci(text1)


# In[61]:

duge_reci(text2)


# # Bigrami 

# In[81]:

from nltk.util import bigrams
list(bigrams(['Jedan', 'primer','bigramizacije']))


# # Kolokacije

# In[3]:

text4.collocations()


# In[76]:

text1.concordance('passionlessness', width = 100)


# ## Procentualni udeo dugačkih reči 

# In[220]:

def perc(text):
    V = set(text)
    long_words = [w for w in V if len(w) >= 15]
    return len(long_words)/ len(V) * 100
perc(text1)


# In[219]:

perc(text1)


# In[71]:

import nltk 
from nltk import FreqDist
from nltk.corpus import inaugural

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
set(stopwords.words('english'))

def most_common(text):
    with open(text, 'r') as t:
        data = str(t.readlines())
        tokens = nltk.word_tokenize(data)
        tokens = [token.strip() for token in tokens]
#     tokens = [token.lower() for token in tokens]
#     tokens = [token for token in tokens if token.isalpha()]
#     stoplist = stopwords.words('english')
#     tokens = [w for w in tokens if not w in stoplist]
#     fdist = FreqDist(tokens) 
#     fdist1 = fdist.most_common(20)
#     print(fdist1)
    print(tokens)
text4.most_common


# In[84]:

from nltk.corpus import inaugural
from nltk import word_tokenize
from nltk.corpus import stopwords
set(stopwords.words('english'))

tokens = [word_tokenize(word) for word in inaugural.words('1865-Lincoln.txt')]
tokens = [token.strip() for token in inaugural.words('1865-Lincoln.txt')]
tokens = [token.lower() for token in inaugural.words('1865-Lincoln.txt')]
tokens = [token for token in tokens if token.isalpha()]
stoplist = stopwords.words('english')
tokens = [w for w in tokens if not w in stoplist]
fdist = FreqDist(tokens)
fdist1 = fdist.most_common(20)
print(fdist1)


# In[6]:

fdist1 = FreqDist(text4)
print(fdist1)


# In[35]:

fdist1.most_common(20)


# In[15]:

import nltk
from nltk import sent_tokenize 
from nltk.tokenize import word_tokenize
from nltk.book import *
from nltk.corpus import stopwords
set(stopwords.words('english'))
tokens = word_tokenize(raw)
type(tokens)
get_ipython().system("class 'list'")
len(tokens)


# In[ ]:

text4.concordance("God")


# In[ ]:

text4.concordance("people")


# In[ ]:

text4.concordance("terror")


# In[ ]:

fdist1 = FreqDist(text4)


# In[ ]:

print(fdist1)


# In[ ]:

fdist1['men']


# In[ ]:

fdist1['women']


# In[ ]:

fdist1['children']


# In[ ]:

len(text3)


# In[ ]:

len(set(text3)) 


# In[ ]:

len(text9)


# In[ ]:

len(set(text9))


# In[ ]:

len(set(text3)) / len(text3)


# In[ ]:

len(text9) / len(set(text9))


# In[ ]:

def lexical_diversity(text): 
    return (len(set(text)) / len(text)) * 100


# In[ ]:

percentage(text3.count('God'), len(text3))


# In[ ]:

lexical_diversity(text9)


# In[ ]:

lexical_diversity(text3)


# In[ ]:

percentage(text3.count("God"), len(text3))


# In[ ]:

percentage(text3.count("God"), len(text3)) * 100


# In[ ]:

V = set(text2)
long_words = [w for w in V if len(w) >= 15]
print(sorted(long_words))


# In[ ]:

V = set(text1)
long_words = [w for w in V if len(w) >= 15]
print(sorted(long_words))


# In[ ]:

V = set(text1)
long_words = [w for w in V if len(w) >= 15]


# In[ ]:

def perc(text):
    V = set(text1)
    long_words = [w for w in V if len(w) >= 15]
    return(len(long_words)/ len(V)) * 100


# In[ ]:

def perc(text):
    return(len(long_words)/ len(V)) * 100


# In[ ]:

perc(text1)


# In[ ]:

def perc(text):
    V = set(text)
    long_words = [w for w in V if len(w) >= 15]
    return(len(long_words)/ len(V)) * 100

perc(text2)


# In[ ]:

VV = set(text2)
long_words2 = [w for w in V if len(w) >= 15]


# In[ ]:

def perc(text):
    return(len(long_words2) / len(VV)) * 100


# In[ ]:

perc(text2)


# In[ ]:

from nltk.util import bigrams


# In[ ]:

list(bigrams(['more', ',', 'is', 'said', 'than', 'done']))


# In[ ]:

list(bigrams(['шта','је', 'бре', 'ово']))


# In[ ]:

text5.collocations()


# In[ ]:

text3.collocations()


# In[ ]:

len(set(text9)) / len(text9) * 100


# In[ ]:

len(set(text8)) / len(text8) * 100


# In[ ]:

text4.count("God")


# In[ ]:

def count(string, substring):
    
    count = 0

    for i in range(len(string) - len(substring) + 1):
        if string[i: i + len(substring)] == substring:
            count += 1

    return count

text2.count('affection')


# In[ ]:

from nltk.corpus import gutenberg
from nltk import word_tokenize
from nltk.corpus import stopwords
set(stopwords.words('english'))

def najcesce_reci(text):
    tokens = [word_tokenize(word) for word in gutenberg.words(text)]
    tokens = [token.strip() for token in gutenberg.words(text)]
    tokens = [token.lower() for token in gutenberg.words(text)]
    tokens = [token for token in tokens if token.isalpha()]
    stoplist = stopwords.words('english')
    tokens = [w for w in tokens if not w in stoplist]
    fdist = FreqDist(tokens)
    fdist1 = fdist.most_common(20)
    fdist.plot(20,cumulative=False)
    print(fdist1)

najcesce_reci('chesterton-thursday.txt')   
  
# text = nltk.corpus.gutenberg.raw('chesterton-thursday.txt')
# nltk.word_tokenize(text)

