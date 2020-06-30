import requests
from bs4 import BeautifulSoup

def GetJobs(URL_list):
    jobs = {}

    for place, site in URL_list.items():
        page = requests.get(site["URL"])
        soup = BeautifulSoup(page.content, 'html.parser')
    
        class_content = soup.find(class_=site["Class"])

        if "Tag" in site:
            joblist = class_content.find_all(site["Tag"])
        else:
            joblist = class_content

           
        Valid = JobValidate(site)

        for job_html in joblist:
            job = job_html.string

            if Valid.Validate(job):
                jobs.update({job : place})

    return jobs

class JobValidate:
    def __init__(self, site):
        self.last = False
        self.site = site
        print("New class created")

    def Validate(self, job):
        print("Validating ....")
        site = self.site
        
        if job == None:
            return False

        if "False_Headings" in site:
            if job in site["False_Headings"]:
                return False

        if ("Last_False_Heading" in site) and (self.last == False):
            if job == site["Last_False_Heading"]:
                self.last = True
            return False

        return True