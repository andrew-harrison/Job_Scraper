# Job_Scraper
Python script to search favourite companies job boards to see if a new job has been posted. Designed to work on windows.

Script to be run with the run_jobs.bat file, as this can be run through windows task scheduler to allow the programm to run automatically

Script will generate Available Jobs.csv and msgbox.vbs each time it is run.

👔
Edit the Jobsites.yml file with the URL of website that you want to program to track, inspect the website with a browser to find the class and tag used for each job title and add any False headings if necessary.

📩
Script should bring up a message window with results of search, alternatively code at the end of the script can be un commented to bring up a windows10 style popup (using plyer). However this won't work when task is automatically scheduled and set to run when user not logged in (I prefere to use this option as it prevents the cmd prompt displaying everytime the program runs)😒

# Install
💻
Script requires pip, pipenv and python 3 installed. Remainder of dependancies can be installed by running setup_jobs.bat
