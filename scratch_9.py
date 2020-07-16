import twint
from datetime import datetime

c = twint.Config()
#c.Username = "" pour preciser un user
c.Limit = 1
"""""""""
c.Store_csv = True
c.Output = "none.csv"
c.Lang = "fr"
c.Translate = True
c.TranslateDest = "it"
config = twint.Config()
config.Since = "2019–04–29"    date de depart
config.Until = "2020–04–29"    date de fin
config.Store_json = True
config.Output = "custom_out.json" ou csv
"""""""""

#now=datetime.now()
#c.Since = now.strftime("%Y-%m-%d %H:%M:%S") #à l'instant actuel
#c.Until = now.strftime("%Y-%m-%d %H:%M:%S")

c.Search = 'tunisair'
c.format ="Tweet id : {id} | Username : {Username} | Date : {date} | Time : {time} | Tweet : {tweet}"
twint.run.Search(c)