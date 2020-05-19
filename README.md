# Web-Crawler
This project was for an IT Staffing company that helps IT Candidates find jobs. 
Resumes of the candidates are posted on various job sitesor , for e.g. www.dice.com, www.indeed.com, www.monster.com, by the posting team.
The posting team had been manually doing this task on a daily basis which is very time consuming. 
This automates the entire process. A python script is used to find the job listing URL, which reduced manual work of searching the jobs.
The script accepts the parameters such as - Name of the job posting website (e.g. Indeed), skill (e.g. Java), location/state (e.g. New Jersey) and find the URL which lists all the Java Jobs on www.indeed.com in the New Jersey state.   
Once the page listing these jobs are found, the script would scrap all the URLs for the job listings on the listing webpage and put them in a text file.
