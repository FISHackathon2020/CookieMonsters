# CookieMonsters

Team:
Dev Agarwal,
Liz Tremblay,
Kunal Kewalramani,
Piyush Sahu,
Zaina Qasim.

Problem Statement:
The nature of student engagement has changed. As a company that values the talent and ideas that college students bring, we want to ensure that we're engaging with students on their terms. The goal of this challenge is to create a tool that will allow us to collect valuable information about a student's experiences and interests in order to partner through internships, co-ops, and other opportunities.

Our Project:
Our web application is a tool which parses the resumes and extracts important, relevent information from them. It uses keras and other pdf / docx mining libraries to do so with human annotations to train the model. After being parsed the resumes are stored in a folder which is synced with our backend database.
The web app is used to visit each resume and review them. With the help of visual aid regarding the job description and the skills listed in the resume, a spider node plot is created for easy visualization.
The parsers are built using python and the web app is built using flask and sqlite3 with the frontend just being plain html and CSS. 

Improvements to be made in the future:
To fully refine this tool, a friend-end framework like gatsby or nextjs can be used to make it look pretty and enhance the UI. the database can be linked to the server so that there will be no need to necesserily add resume data manually, instead the pipeline would automatically parse the resume and upload the metadata to the database. 

Protoype User Testing Link: https://xd.adobe.com/view/7b0e203a-f58d-44e8-9a60-6417953369fb-2e5d/?fullscreen&hints=off
