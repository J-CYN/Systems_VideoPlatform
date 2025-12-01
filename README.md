# Systems Video Platform
1) Executive Summary
   
The problem this project is meant to solve is that Althvinhaim, a DND style RPG, doesn't have its own place that hosts the videos of sessions to users, info about the world, and an easy way to upload videos. So a website that does all three utilizing Flask API and Blob Storage to process storing the mp4 videos and retrieving them for users. In addition, this process is ad free which is a plus compared to the service provided by Youtube. The website has two html files as pages, one screen has an uploader which the user will select mp4 files from their own device to upload to the blob storage. The dashboard page is where users can watch their uploaded mp4 files which are all displayed.

2) System Overview

Course Concepts:

UI have made a website that hosts and plays MP4 videos which are stored in the Azure Blob Storage using a backend which communicates between the frontend and the servers using Flask API. This stores the mp4 videos which will be pulled in the dashboard page when users refresh or enter the site.

Architecture Diagram: NOT DONE

Data/Models/Services: NOT DONE

3) How to Run (Local)

docker build -t myapp:latest .

docker run --rm -p 8080:8080 --env-file .env myapp:latest

4) Design Decisions

Why this concept?: NOT DONE

Tradeoffs: NOT DONE

Security/Privacy: NOT DONE

Ops: NOT DONE

5) Results & Evaluation

Screenshots or sample outputs (place assets in /assets): NOT DONE

Brief performance notes or resource footprint (if relevant): 

The performance works just fine, and it uses very little bandwidth outside startup. The website struggles with larger file uploads however and times out. This happens primarily on the Render Application. NOOOOOOOOOOOT DOOOOOOONE

Validation/tests performed and outcomes:

Tests were performed both within the local hosting of a dockerfile and within the Render App hosting. The switching between html pages was tested by using the buttons which is managed by the flask API. The MP4 files that are included in assets were uploaded and appeared within the blob storage and dashboard when switching pages. Checking /api/health resulted in "{"status":"ok"}", which is the correct output.
   
6) What’s Next
   
In addition, to make this service more usable. I can use better processing power, the website it running on the render free tier, as currently the website struggles with uploads of two hours or greater.

Cloudflare offers Cloudflare CDN which could allow faster retrieval and better watching experiences for people who live far away from the blob storage service by having copies of the same videos in different geographical regions.

The CSS code is separated in the html files. I think in the future I should refactor this code to make CSS files that helps make the html code more readable by moving that CSS code to its own file.

7) Links (Required)
   
GitHub Repo: https://github.com/J-CYN/Systems_VideoPlatform
Render App: https://systems-videoplatform.onrender.com