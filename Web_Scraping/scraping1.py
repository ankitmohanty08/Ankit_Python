from tokenize import String
from unittest import result
import requests
from pprint import pprint 
from bs4 import BeautifulSoup


def searchJobByJobName(jobName,results):
    jobs=results.find_all("h2",string=lambda text: jobName in text.lower())
    # print(jobs)
    for job in jobs:
        print(job.text)
        # jobTitle=job.find("h2",{"class":"title is-5"})
        # print(jobTitle)
        # companyName=job.find("h3",{"class":"subtitle is-6 company"}).text.strip()
        # jobLocation=job.find("p",{"class":"location"}).text.strip()
        # print(companyName)
        # print(jobLocation)
        # print()

if __name__=="__main__" :       
    url="https://realpython.github.io/fake-jobs/"
    res=requests.get(url)
    soup=BeautifulSoup(res.content,"lxml")
    results = soup.find(id="ResultsContainer")
    # print(type(results))
    # print(soup.prettify())
    # jobElements=results.find_all("div",{"class":"card-content"})
    # for jobElement in jobElements:
    #     jobTitle=jobElement.find("h2",{"class":"title is-5"}).text.strip()
    #     companyName=jobElement.find("h3",{"class":"subtitle is-6 company"}).text.strip()
    #     jobLocation=jobElement.find("p",{"class":"location"}).text.strip()
        
    #     print(jobTitle)
    #     print(companyName)
    #     print(jobLocation)
    #     print()
    searchJobByJobName("python",results)

