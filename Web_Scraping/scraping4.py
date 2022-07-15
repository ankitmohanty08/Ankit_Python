
import requests
import os
from bs4 import BeautifulSoup
from pprint import pprint

def download_image(url,headers):    
    res=requests.get(url,headers=headers)
    soup=BeautifulSoup(res.content,"lxml")
    
    images=soup.find_all("img",{"class":"lzy"})

    for i,image in enumerate(images):
        image_response=requests.get(image['data-src'])
        filename="image"+str(i)+".jpeg"
        dir=os.getcwd()+"/Images/"
        with open(dir+filename,"wb") as fp:
            fp.write(image_response.content)
    print(str(len(images))+" images saved to "+dir)

if __name__=="__main__":
    search=input("Enter name to download image: ")
    url="https://www.freepik.com/search?format=search&query="+search
    headers={
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36"
    }
    download_image(url,headers)
