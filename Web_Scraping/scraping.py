from pprint import pprint
from bs4 import BeautifulSoup

with open("file.html") as fp:
    html_content=fp.read()
    soup=BeautifulSoup(html_content,"lxml")
    # print(soup.prettify())
    tables=soup.find_all("table")
    tableData={}
    
    for j in range(len(tables)):
        data=[]
        tr_list=tables[j].find_all("tr")
        tr_head=tr_list[0]
        tr_body=tr_list[1:]
        
        
        if j==3:
           tr_head1=tr_list[0]
           tr_head=tr_list[1]
           tr_body=tr_list[2:] 
           headingsTop=[th.text for th in tr_head1.find_all("th")]

        headings=[th.text for th in tr_head.find_all("th")]   
        
        for tr in tr_body:
             row=[]
             td_list= tr.find_all("td")
             
             if j==3:
                 x_data=[]
                 row.append(dict([[headings[0],td_list[0].text]]))
                 for i in range(1,3):
                    temp=[headings[i],td_list[i].text]
                    x_data.append(temp)
                 row.append(dict(x_data))
                 row.append(dict([[headings[3],td_list[3].text]]))
                 
                 rowData=[]
                 rowData.append([headings[0],td_list[0].text])
                 for i in range(1,len(headingsTop)):
                     if i!=0:  
                        temp=[headingsTop[i],row[i]]
                        rowData.append(temp)
                 data.append(dict(rowData))
                 
                 
             else:    
                x_data=[]
                for i in range(len(td_list)):
                    x_data=[headings[i],td_list[i].text]
                    row.append(x_data)
                data.append(dict(row))             
             
    
        tableData["table"+str(j)]=data

    pprint(tableData)
        
        
        # [{  "#":1,
        #     "Person":{
        #         "fn":dd,
        #         "ln":DN_DELETE
        #     },
        #     "Userdata":{
        #         "username":abc
        #     }
        # },
        #  {},...]