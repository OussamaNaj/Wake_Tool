#!/usr/bin/env python
# coding: utf-8

# In[371]:


import requests
import urllib.request
import re
import time
from bs4 import BeautifulSoup
import pandas as pd
from htmldate import find_date


# In[372]:


user_agent_desktop = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 '  'Safari/537.36'
user_agent_smartphone = 'Mozilla/5.0 (Linux; Android 9; SM-G960F '  'Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) '  'Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36'
user_agent_old_phone = 'Nokia5310XpressMusic_CMCC/2.0 (10.10) Profile/MIDP-2.1 '  'Configuration/CLDC-1.1 UCWEB/2.0 (Java; U; MIDP-2.0; en-US; '  'Nokia5310XpressMusic) U2/1.0.0 UCBrowser/9.5.0.449 U2/1.0.0 Mobile'



user_agents=[user_agent_desktop,user_agent_smartphone,user_agent_old_phone]

for user_agent in user_agents:

        headers = { 'User-Agent': user_agent}
        
patterns=['tunisair','Tunisair','الخطوط التونسية',"Société tunisienne de l'air"]


# In[373]:


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
    




# In[374]:


def get_text_from_url(url):
    soup=step_one(url)
    p_tags = soup.find_all('a')
    text = ''
    for tag in p_tags:
          text += tag.get_text()
    return text


# In[375]:


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


# In[376]:


urls=[
'https://lapresse.tn/tag/tunisair/',
'https://lapresse.tn/',
'https://www.leaders.com.tn/article/21774-tunisair',
'http://www.webdo.tn/tag/tunisair/',
 'https://www.tourmag.com/tags/tunisair/',
'https://www.leconomistemaghrebin.com/tag/tunisair/',
 'https://tunivisions.net/tag/tunisair/',
'http://kapitalis.com/tunisie/tag/tunisair/',
'https://www.tustex.com/node/188/actualites',
'https://www.webmanagercenter.com/tag/tunisair/',
'https://www.businessnews.com.tn/tunisair-la-crise-de-trop,519,98646,3',
'https://afrique.le360.ma/tunisie/economie/2019/02/05/24942-tunisair-en-crise-la-compagnie-revoit-ses-ambitions-la-baisse-24942',
'https://africanmanager.com/malgre-la-crise-les-agents-de-tunisair-protestent-aujourdhui/',
'https://www.lepoint.fr/afrique/tunisair-le-spectre-de-la-faillite-14-05-2020-2375514_3826.php',
'https://lepetitjournal.com/tunis/actualites/covid-19-la-reouverture-des-frontieres-est-annoncee-officiellement-281966',
'https://ar.lemaghreb.tn/',
'http://www.alchourouk.com/',
'http://nawaat.org/portail/',
'http://www.assabah.com.tn/',
'https://www.leconomistemaghrebin.com/',
'www.tuniscope.com',
'www.wikipedia.org',
'www.alchourouk.com',
'www.opodo.fr',
'www.topito.com',
'www.fr.lastminute.com',
'www.skyscanner.fr',
'www.travelstore.tn',
'www.destinationtunisie.info',
'www.omeilleursprix.com',
'www.bourse-des-vols.com',
'www.govoyages.com',
'www.edreams.fr',
'www.air-journal.fr',
'www.air-journal.fr',
'www.vol-retarde.be',
'www.google.tn/maps',
'www.voyagesetvagabondages.com',
'https://www.medias24.com/',
'https://www.vol-direct.fr/',
'https://simpleflying.com/',
'https://mondenews.net/fr/',
'https://voyage.gc.ca/',
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
'www.voyagespirates.com',
'www.lechotouristique.com',
'www.tripadvisor.fr',
'www.tourismag.com',
'www.espacemanager.com',
'www.bravofly.fr',
'www.tourhebdo.com',
'www.bvm.com.tn',
'www.cmf.tn',
'www.tripstyleblog.com',
'www.tourisminfo.com.tn',
'www.universnews.tn',
'www.books.google.tn',
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


# In[377]:



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
    return df


# In[378]:


while 1:
    scrap()


# In[ ]:




