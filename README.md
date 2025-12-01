# Systems Video Platform
1) Executive Summary
   
The problem this project is meant to solve is that Althvinhaim, a DND style RPG, doesn't have its own place that hosts the videos of sessions to users, info about the world, and an easy way to upload videos. So a website that does all three utilizing Flask API and Blob Storage to process storing the mp4 videos and retrieving them for users. In addition, this process is ad free which is a plus compared to the service provided by Youtube. The website has two html files as pages, one screen has an uploader which the user will select mp4 files from their own device to upload to the blob storage. The dashboard page is where users can watch their uploaded mp4 files which are all displayed.

2) System Overview

Course Concepts:

UI have made a website that hosts and plays MP4 videos which are stored in the Azure Blob Storage using a backend which communicates between the frontend and the servers using Flask API. This stores the mp4 videos which will be pulled in the dashboard page when users refresh or enter the site.

Architecture Diagram: NOT DONE

Data/Models/Services: 

The data uploaded are mp4 versions of Youtube videos that me and my friends have uploaded that can be seen in the assets as "Althvinhaim_Community.mp4", a 2472 kb mp4 file.
and 
"Althvinhaim_Intro.mp4", a 3971 kb mp4 file.
 
 No models are in use by the application. The application uses Azure Blob Storage and the cloud hosted application is using Render.com to host itself. For the license check the LICENSE.md file.

3) How to Run (Local)

Run the following individual commands in your terminal(This requires the .env file which holds environmental variables):

docker build -t myapp:latest .
docker run --rm -p 8080:8080 --env-file .env myapp:latest

Then, if the docker container was created successfully, access it at http://localhost:8080/

4) Design Decisions

Why this concept?: 

I chose this approach because tools such as Azure Blob Storage and FlaskAPI were concepts that I wished to solidify in practice. My previous experience with them gave me background experience that I could look to as I tried to modify my previous experiences with them to this project independently. Blob Storage can cheaply handle large amounts of MP4s without incurring much cost. FlaskAPI is very lightweight and runs smoothly. My relative inexperience, currently, with Django made Flask my natural choice for this project. I used Render to host the application since its free tier allowed for continuous deployment which Azure's App Service doesn't provide on the the Azure student accounts.

Tradeoffs:

These choices have allowed for a level of maintainability. FlaskAPI is very readable and serves as the backend of the application with relatively few lines to maintain. Blob Storage is relatively cheap, even for videos, which can easily store the files for this project to a larger scale into the future without having to change the code. However, the current application runs on the Render free tier which limits the size of MP4s to be uploaded. This can easily be changed with an upgrade to my subscription, so it isn't too much trouble on that front either.

Security/Privacy: 

Personal information of users is not stored or accessed. My Azure connection string is not visible and is contained in a .env file that is required to locally host this application, unless they create their own blob storage with similar permissions and naming. 

Ops:

As can be seen, the bandwidth usage is within reason.
![BandwidthUsage](assets\ResourceUsage.png)

I am not aware of any errors within the application and everything works to expectation according to current testing.

The current website is meant to handle only up to seven to eight users. From testing it works with up to three people accessing it at once, but more testing is required. If needed, the website can be scaled to serve more users.

The greatest limitation is mp4 videos of considerable length, such as over two hours. Have difficulty uploading and have the process fail at times. Small uploads do function quickly and effectively, however.

5) Results & Evaluation

Screenshots or sample outputs (place assets in /assets): NOT DONE

Brief performance notes or resource footprint (if relevant): 

The performance works just fine, and it uses very little bandwidth outside startup. The website struggles with larger file uploads however and times out.

Validation/tests performed and outcomes:

Tests were performed both within the local hosting of a dockerfile and within the Render App hosting. The switching between html pages was tested by using the buttons which is managed by the flask API. The MP4 files that are included in assets were uploaded and appeared within the blob storage and dashboard when switching pages which serves as both a test of /api/upload and /api/catalog which both work to expectation. Checking /api/health resulted in "{"status":"ok"}", which is the correct output.
   
6) What’s Next
   
In addition, to make this service more usable. I can use better processing power, the website it running on the render free tier, as currently the website struggles with uploads of two hours or greater.

Cloudflare offers Cloudflare CDN which could allow faster retrieval and better watching experiences for people who live far away from the blob storage service by having copies of the same videos in different geographical regions.

The CSS code is separated in the html files. I think in the future I should refactor this code to make CSS files that helps make the html code more readable by moving that CSS code to its own file.

7) Links (Required)
   
GitHub Repo: https://github.com/J-CYN/Systems_VideoPlatform
Render App: https://systems-videoplatform.onrender.com