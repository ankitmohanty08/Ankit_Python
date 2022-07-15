import imp
from operator import le
import requests
import os
import psutil
import json
from PIL import Image
from bs4 import BeautifulSoup
from pprint import pprint

def extractData(table):
     left_column_data=[]
     right_column_data=[]
     data={}
     tr_list=table.find_all("tr") 
     for tr in tr_list:
          td_list=tr.find_all("td")
          for i,td in enumerate(td_list):
               if i<1:
                    left_column_data.append(td.text)
               else:
                    right_column_data.append(td.text)     
     for i in range(len(left_column_data)):
          data[left_column_data[i]]=right_column_data[i]
                    
     pprint(data)

s=requests.Session()
headers={
     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36"
}
domain_name="https://www.mca.gov.in"
url=domain_name+"/mcafoportal/viewCompanyMasterData.do"
res=s.get(url,headers=headers)
print(res.status_code)

soup=BeautifulSoup(res.content,"lxml")

captcha_img=soup.find("img",{"id":"captcha"})
captcha_url=domain_name+captcha_img["src"]
headers.update({"Referer": "https://www.mca.gov.in/mcafoportal/viewCompanyMasterData.do"
               #    "Cookie":cookie[0]
                })
res2=s.get(captcha_url,headers=headers)
# print(s.headers)
with open("captcha.jpeg","wb") as fp:
     fp.write(res2.content)
     
Image.open("captcha.jpeg").show()

# company_cin_no=input("Enter CIN number: ")
company_cin_no="U74120MH2015PTC265316"
captcha=input("Enter the captcha on the screen: ")
url="https://www.mca.gov.in/mcafoportal/companyLLPMasterData.do"

data={
     "companyName":"",
     "companyID": company_cin_no,
     "displayCaptcha": True,
     "userEnteredCaptcha": captcha
}

res3=s.post(url,data=data,headers=headers)
soup=BeautifulSoup(res3.content,"lxml")
with open("trail.html","w") as fp:
     fp.write(res3.text)
print(res3.status_code)



table=soup.find("table",{"id":"resultTab1"})
extractData(table)


