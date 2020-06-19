import requests
from bs4 import BeautifulSoup

def GetJobs(URL_list):
    jobs = {}

    for place, site in URL_list.items():
        page = requests.get(site["URL"])
        soup = BeautifulSoup(page.content, 'html.parser')
    
        class_content = soup.find(class_=site["Class"])

        joblist = class_content.find_all(site["Tag"])

        for job_html in joblist:
            job = job_html.string
        
            if "False_Headings" in site:
                if job in site["False_Headings"]:
                    continue
            
            jobs.update({job : place})
        
    return jobs
