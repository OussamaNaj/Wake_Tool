#!/usr/bin/env python
# coding: utf-8

# In[401]:


import requests
import urllib.request
import re
import time
from bs4 import BeautifulSoup
import pandas as pd
from htmldate import find_date


# In[402]:


user_agent_desktop = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 '  'Safari/537.36'
user_agent_smartphone = 'Mozilla/5.0 (Linux; Android 9; SM-G960F '  'Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) '  'Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36'
user_agent_old_phone = 'Nokia5310XpressMusic_CMCC/2.0 (10.10) Profile/MIDP-2.1 '  'Configuration/CLDC-1.1 UCWEB/2.0 (Java; U; MIDP-2.0; en-US; '  'Nokia5310XpressMusic) U2/1.0.0 UCBrowser/9.5.0.449 U2/1.0.0 Mobile'



user_agents=[user_agent_desktop,user_agent_smartphone,user_agent_old_phone]

for user_agent in user_agents:

        headers = { 'User-Agent': user_agent}
        
patterns=['topnet','Topnet','توب نات',"توبنات"]


# In[403]:


def step_one(url):


    

    r = requests.get(url, headers=headers)  # Send request

    code = r.status_code  # HTTP response code
    test=(code==200)
    if test:
         soup = BeautifulSoup(r.content,features='lxml')  # Parsing the HTML
        #print(soup.prettify())
     #break
    else:
        #print(f'Error to load : {code}')
        pass
    return soup
    




# In[404]:


def get_text_from_url(url):
    soup=step_one(url)
    p_tags = soup.find_all('a')
    text = ''
    for tag in p_tags:
          text += tag.get_text()
    return text


# In[405]:


def resultat(soup):
    text = []
    hyperlien = []
    date=[]
    for a in soup.find_all('a', href=True):

        #if 'tunisair' in a['href']:
        for pattern in patterns:
            try:
                 if (re.search(pattern,a['href'])):
            
                    text.append(get_text_from_url(a['href']))
                    hyperlien.append(a['href'])
                    d=find_date(a['href'])
                    if d:
                        date.append(d)
                        
                    else:
                        date.append(None)
                    
            except:
                continue
    
    return hyperlien,text,date


# In[406]:


urls=['https://www.jetcost.com/',
      'https://www.tustex.com/',
      'https://www.lemanager.tn/tag/topnet/',
      'https://www.entreprises-magazine.com/tag/topnet/page/2/',
      'https://www.entreprises-magazine.com/',
      'https://thd.tn/tag/topnet/page/2/',
      'https://thd.tn/',
      'http://www.smarttunisia.tn/',
      'https://www.techno.rn.tn/component/tags/tag/topnet.html',
      'https://www.techno.rn.tn/',
      'http://www.havasworldwide.tn/index.php/clients/itemlist/tag/TOPNET',
      'https://tunivisions.net/tag/topnet/',
'https://lapresse.tn/tag/topnet/',
'https://lapresse.tn/',

'https://www.leconomistemaghrebin.com/tag/topnet-tunisie/',
'http://kapitalis.com/tunisie/tag/topnet/',
'https://www.tustex.com/node/188/actualites',
'https://www.webmanagercenter.com/tag/topnet/',
'https://www.businessnews.com.tn/',
'http://www.havasworldwide.tn/',
      'https://www.rtx.com/'
      'https://www.it-news.tn/tag/topnet/',
      'http://www.theguiks.com/tag/topnet',
      'http://www.letemps.com.tn/tags/topnet'
      'https://www.tuitec.com/ar/tag/topnet/',
      'https://www.tunisienumerique.com/',
      'https://www.prosdelacom.com/',
      'https://www.wiki.tn/topnet_123.html',
      'https://www.tuniscope.com/',
      'https://www.tekiano.com/',
      'https://ween.tn/fiche/topnet',
      'https://www.espacemanager.com/',
      'https://africanmanager.com/',
      'https://tn.kompass.com/',
      'http://www.btpnet.com/home.htm',
      'https://www.realites.com.tn/',
      'https://www.ilboursa.com/',
      'https://www.africanchallenges.com/',
      'https://www.tunisietelecom.tn/Fr',
      'https://www.tunisia-sat.com/forums/',
      'https://www.plasticomnium.com/en/',

'http://www.lepointtn.com/tag/topnet/?lang=fr',
      'https://www.baya.tn/Mots-Clefs/topnet/',
      'https://www.tunisietravail.net/',
      'https://www.radioexpressfm.com/tag/topnet/'
'https://lepetitjournal.com/tunis/actualites/covid-19-la-reouverture-des-frontieres-est-annoncee-officiellement-281966',
'https://ar.lemaghreb.tn/',
'http://www.alchourouk.com/',
'http://nawaat.org/portail/',
'http://www.assabah.com.tn/',
'https://www.leconomistemaghrebin.com/',
'www.tuniscope.com',
'www.wikipedia.org',
'www.alchourouk.com',

'https://www.medias24.com/',


'https://mondenews.net/fr/',

'https://www.icao.int/Pages/default.aspx',
'www.tayara.tn',
'www.alibaba.com',
'www.tunisietravail.net',
'www.nessma.tv',
'www.elhiwarettounsi.com',
'www.jumia.com.tn',
'www.Tunisie-annonce.com',
'www.Kooora.com',
'www.Orange.tn',
'www.webdo.tn',
'www.tunisie-news.com',
'www.leaders.com.tn',
'www.tunisienumerique.com',
'www.kapitamlis.com',
'www.lapresse.tn',
'www.digitalsyndrom.net',
'www.medianet.tn',
'www.traveltodo.com',
'www.tunisiebooking.com.tn',
'www.tunisiepromo.com',
'www.tumblr.com',
'www.tanitjobs.com',
'www.essada.net',
'www.keejob.com',
'www.Travian.com',
'www.forsa.tn',
'www.ballouchi.com',
'www.aljarida.com.tn',
'www.businessnews.com.tn',
'www.baidu.com',
'www.lufthansa.com',

'www.espacemanager.com',

'www.universnews.tn',

'www.tunisie-tribune.com',
'www.tounesnanews.com',
'https://www.jetcost.com/?fbclid=IwAR3B-Bo9S2MCitDIUM-QEBL4WsyIvKe8VkDQ-prqZ6u_vwZ46LV6LHf5O7U',
'https://www.mosaiquefm.net/fr/',
'https://www.jawharafm.net/ar/',
'https://www.shemsfm.net/amp/ar/',
'https://www.radioexpressfm.com/',
'http://www.bnacapitaux.com.tn/',
'http://www.assabahnews.tn/',
'http://www.letemps.com.tn/',
'https://news.gnet.tn/'
]


# In[407]:



#url_text=[]
#url_hyper=[]
#pattern=re.compile(r'tunisair[\.| ]',re.IGNORECASE)
#url='https://lapresse.tn/tag/tunisair/'
def scrap():
    hyperlien=[]
    text=[]
    date=[]
    for url in urls:
        try:
            soup=step_one(url)
            data0=resultat(soup)
            hyperlien.extend(data0[0])
            text.extend(data0[1])
            date.extend(data0[2])
        except:
            continue
#url_text=resultat[1]
#url_hyper=resultat[0]
#print(url_hyper)


    data={'url':hyperlien,'text':text,'date':date}    
    df = pd.DataFrame (data, columns=['url', 'text','date'])
    df = df.drop_duplicates(subset='text', keep='first')
    df=df.sort_values(by = 'date',ascending=False)
    df=df.reset_index()
    return df


# In[408]:


while 1:
    scrap()


# In[ ]:




