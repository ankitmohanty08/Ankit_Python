import textwrap
import json
import requests
from pprint import pprint
from bs4 import BeautifulSoup




def formatData(td,ColumnData,titleTextList):
    title=td.parent.find_previous_sibling('td')
    titleText=title.text.strip()
    if titleText!="":
        titleTextList.append(titleText)
    contentText=td.text.strip()
    if titleText not in ColumnData.keys() :
        if titleText=="" and contentText!="":
            ColumnData[titleTextList[-1]]=ColumnData[titleTextList[-1]]+" "+contentText
        elif titleText!="" and contentText!="":
            ColumnData[titleTextList[-1]]=contentText 
    return (ColumnData,titleTextList)        

def getDetails(url,memId):  
     
    body={
    "t1": memId
    }
    res=requests.post(url,data=body)
    soup=BeautifulSoup(res.content,"lxml")
    result=soup.find_all("form")
    
    table=result[0].find("table",{"width":"100%"}) #----> Tables inside in the form
    tr_list=table.find_all("tr")
    
    leftColumnData={}
    rightColumnData={}
    titleTextList=[]
    titleTextList1=[]
    heading=[]
    
    for i,tr in enumerate(tr_list):
        td_list=tr.find_all("b")
        if i!=0:
            for j,td in enumerate(td_list):
                if j<1:
                    (leftColumnData,titleTextList)=formatData(td,leftColumnData,titleTextList)    
                else:
                    (rightColumnData,titleTextList1)=formatData(td,rightColumnData,titleTextList1)    
        else:
            for td in td_list:
                text=td.text.strip()
                text=text.replace(" ","")
                text=text.replace("\r","")
                text=text.replace("\n","")
                heading.append(text)
    data={}
    data[heading[0]]=leftColumnData
    data[heading[1]]=rightColumnData
    data_json=json.dumps(data)
    pprint(data)
    
if __name__=="__main__":
    
    url="http://112.133.194.254/lom.asp"
    memId=input("Enter member Id: ")
    data_json=getDetails(url,memId)
    
    
