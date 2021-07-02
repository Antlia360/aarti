#!/usr/bin/env python
# coding: utf-8

# In[1]:


conda install textblob

# Collecting package metadata (current_repodata.json): done
# Solving environment: done


# ==> WARNING: A newer version of conda exists. <==
#   current version: 4.8.2
#   latest version: 4.10.3

# Please update conda by running

#     $ conda update -n base conda



# ## Package Plan ##

#   environment location: /srv/conda/envs/notebook

#   added / updated specs:
#     - textblob


# The following packages will be downloaded:

#     package                    |            build
#     ---------------------------|-----------------
#     ca-certificates-2021.5.30  |       ha878542_0         136 KB  conda-forge
#     certifi-2021.5.30          |   py37h89c1867_0         141 KB  conda-forge
#     click-8.0.1                |   py37h89c1867_0         145 KB  conda-forge
#     joblib-1.0.1               |     pyhd8ed1ab_0         206 KB  conda-forge
#     libgcc-ng-9.3.0            |      h2828fa1_19         7.8 MB  conda-forge
#     libgomp-9.3.0              |      h2828fa1_19         376 KB  conda-forge
#     nltk-3.6.2                 |     pyhd8ed1ab_0         1.1 MB  conda-forge
#     openssl-1.1.1k             |       h7f98852_0         2.1 MB  conda-forge
#     regex-2021.4.4             |   py37h5e8e339_0         377 KB  conda-forge
#     textblob-0.15.3            |             py_0         595 KB  conda-forge
#     tqdm-4.61.1                |     pyhd8ed1ab_0          79 KB  conda-forge
#     ------------------------------------------------------------
#                                            Total:        13.0 MB

# The following NEW packages will be INSTALLED:

#   click              conda-forge/linux-64::click-8.0.1-py37h89c1867_0
#   joblib             conda-forge/noarch::joblib-1.0.1-pyhd8ed1ab_0
#   nltk               conda-forge/noarch::nltk-3.6.2-pyhd8ed1ab_0
#   regex              conda-forge/linux-64::regex-2021.4.4-py37h5e8e339_0
#   textblob           conda-forge/noarch::textblob-0.15.3-py_0
#   tqdm               conda-forge/noarch::tqdm-4.61.1-pyhd8ed1ab_0

# The following packages will be UPDATED:

#   ca-certificates                      2020.6.20-hecda079_0 --> 2021.5.30-ha878542_0
#   certifi                          2020.6.20-py37hc8dfbb8_0 --> 2021.5.30-py37h89c1867_0
#   libgcc-ng                                9.2.0-h24d8f2e_2 --> 9.3.0-h2828fa1_19
#   libgomp                                  9.2.0-h24d8f2e_2 --> 9.3.0-h2828fa1_19
#   openssl                                 1.1.1g-h516909a_0 --> 1.1.1k-h7f98852_0



# Downloading and Extracting Packages
# joblib-1.0.1         | 206 KB    | ##################################### | 100% 
# nltk-3.6.2           | 1.1 MB    | ##################################### | 100% 
# tqdm-4.61.1          | 79 KB     | ##################################### | 100% 
# libgomp-9.3.0        | 376 KB    | ##################################### | 100% 
# openssl-1.1.1k       | 2.1 MB    | ##################################### | 100% 
# certifi-2021.5.30    | 141 KB    | ##################################### | 100% 
# ca-certificates-2021 | 136 KB    | ##################################### | 100% 
# click-8.0.1          | 145 KB    | ##################################### | 100% 
# textblob-0.15.3      | 595 KB    | ##################################### | 100% 
# regex-2021.4.4       | 377 KB    | ##################################### | 100% 
# libgcc-ng-9.3.0      | 7.8 MB    | ##################################### | 100% 
# Preparing transaction: done
# Verifying transaction: done
# Executing transaction: done

# Note: you may need to restart the kernel to use updated packages.

# In[1]:


conda install tweepy

# Collecting package metadata (current_repodata.json): done
# Solving environment: done


# ==> WARNING: A newer version of conda exists. <==
#   current version: 4.8.2
#   latest version: 4.10.3

# Please update conda by running

#     $ conda update -n base conda



# ## Package Plan ##

#   environment location: /srv/conda/envs/notebook

#   added / updated specs:
#     - tweepy


# The following packages will be downloaded:

#     package                    |            build
#     ---------------------------|-----------------
#     requests-oauthlib-1.3.0    |     pyh9f0ad1d_0          21 KB  conda-forge
#     tweepy-3.10.0              |     pyhd8ed1ab_0          28 KB  conda-forge
#     ------------------------------------------------------------
#                                            Total:          49 KB

# The following NEW packages will be INSTALLED:

#   requests-oauthlib  conda-forge/noarch::requests-oauthlib-1.3.0-pyh9f0ad1d_0
#   tweepy             conda-forge/noarch::tweepy-3.10.0-pyhd8ed1ab_0



# Downloading and Extracting Packages
# tweepy-3.10.0        | 28 KB     | ##################################### | 100% 
# requests-oauthlib-1. | 21 KB     | ##################################### | 100% 
# Preparing transaction: done
# Verifying transaction: done
# Executing transaction: done

# Note: you may need to restart the kernel to use updated packages.

# In[1]:


import tweepy
from textblob import TextBlob
consumer_key = 'enter your api key'
consumer_secret = 'secret key'
access_token = 'enter'
access_token_secret = 'enter '
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret )
api = tweepy.API(auth)
public_tweets = api.search('Donald Trump')
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)

# The answer: Have you no shame? Look in the mirror. It is you who are…
# Sentiment(polarity=0.0, subjectivity=0.0)
# NEW INVENTION! 'The Nice Donald Trump' is a computer pizza for $122
# Sentiment(polarity=0.3852272727272727, subjectivity=0.7272727272727273)
# RT @norm: How could America let Donald Trump run the country but won’t let Britney Spears run her life?
# Sentiment(polarity=0.0, subjectivity=0.0)
# RT @colonelhogans: @ljayes @ScottMorrisonMP @ljayes Morrison just repeating the same blah blah blah! He promised the world a year ago. Amer…
# Sentiment(polarity=0.0, subjectivity=0.125)
# RT @MeghUpdates: #BREAKING: Donald Trump Team Launches Alternative to Twitter-  'GETTR'
# Sentiment(polarity=0.0, subjectivity=0.0)
# RT @EricStallinga: Volg me ook op GETTR.

# GETTR is een nieuw platform voor sociale media gemaakt door Jason Miller, een voormalige assisten…
# Sentiment(polarity=0.0, subjectivity=0.0)
# RT @saradannerdukic: Also, paying people with a free apartment wasn't anything new to Trump.  He did the same for his pilot, after his pilo…
# Sentiment(polarity=0.1787878787878788, subjectivity=0.4598484848484849)
# RT @DeathBattleBot: DEATH BATTLE! Donald Trump VS SCP-1715 https://t.co/MLrRuJeZBE
# Sentiment(polarity=0.0, subjectivity=0.0)
# RT @realLizUSA: NEW: 

# "Do people see the Radical Left prosecutors, and what they are trying to do to 75M+++ Voters and Patriots, for what…
# Sentiment(polarity=0.06818181818181818, subjectivity=0.22727272727272727)
# RT @saradannerdukic: I'm still reading through the indictment, but I think it's worth remembering that the scheme outlined in it starts at…
# Sentiment(polarity=0.3, subjectivity=0.1)
# RT @newsmax: Eric Trump on Thursday accused prosecutors of running a "political vendetta" against his father, former President Donald Trump…
# Sentiment(polarity=0.0, subjectivity=0.05)
# I have these player edition jerseys in various sizes S - XL

# ₦10,000 with full customization
# 📌 Kaduna
# 🚛nationwide d… https://t.co/8eH3GmkokY
# Sentiment(polarity=0.175, subjectivity=0.525)
# RT @PalmerReport: He screamed. He yelled. For stretches he couldn't seem to open his eyes. He seemed to be fighting back tears. Don Jr just…
# Sentiment(polarity=0.0, subjectivity=0.25)
# Why is George Galloway still a thing in 2021? He's like Donald Trump unsuccessfully cosplaying as a socialist.
# Sentiment(polarity=0.0, subjectivity=0.0)
# RT @1813Doncarlo: When are we going to see Donald Trump's tax returns?
# Ways &amp; Means Committee Chairman Richard Neal should release Trump's…
# Sentiment(polarity=0.0, subjectivity=0.0)

# In[ ]:




