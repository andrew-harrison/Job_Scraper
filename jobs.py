import sys
import yaml
from webscraper import GetJobs

prev_jobs = []
E_jobs = 'Existing jobs found: '
N_jobs = {}

# Find jobs by webscraping through pages in yaml file
with open(r'Jobsites.yml') as file:
    URL_list = yaml.load(file, Loader=yaml.FullLoader)

jobs = GetJobs(URL_list)

print(jobs)

# Find resesults of previous search in .csv file
with open("Available Jobs.csv","r") as f:
    for line in f:
        prev_jobs.append(line.strip("\n"))

# Compares list of jobs from web search to jobs listed in .csv file
for job, place in jobs.items():
    if job in set(prev_jobs):
        print(f'Existing job found: {job}')
    else:
        N_jobs.update({job: place})
        print(f'New job found: {job}')

# If arguments are given to script csv containing job titles will be updated
write_csv = None
if len(sys.argv)>1: write_csv = sys.argv[1]

if(write_csv == "1"):
    with open("Available Jobs.csv","w") as f:
        for job in jobs:
            f.write(job + "\n")

if(N_jobs):
    message = 'New jobs: ' + ", ".join( [job + " at " + place for job,place in N_jobs.items()] )
else:
    message = "No new jobs found"

# Generate a vbs file with windows message contents
with open("msgbox.vbs","w") as f:
    f.write("x=msgbox("
    + '"' + message + '"'
    + ',0, "Message from your computer")'
    )

# Can be used in windows 10 if task is scheduled when user is logged in (requires plyer install)
# from plyer import notification as popup
# popup.notify(
#     title='Job scanning complete',
#     message= N_jobs,
#     app_name='Job scan',
#     timeout= 20
#     # app_icon='path/to/the/icon.png'
# )
