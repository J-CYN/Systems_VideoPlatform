# Systems Video Platform
1) Executive Summary
   
The problem this project is meant to solve is that Althvinhaim, a DND style RPG, doesn't have its own place that hosts the videos of sessions to users, info about the world, and an easy way to upload videos. So a website that does all three utilizing Flask API and Blob Storage to process storing the mp4 videos and retrieving them for users. In addition, this process is ad free which is a plus compared to the service provided by Youtube.

2) System Overview

UI have made a website that hosts and plays MP4 videos which are stored in the Azure Blob Storage using a backend which communicates between the frontend and the servers using Flask API.

3) How to Run (Local)

docker build -t myapp .

docker run -p 8080:8080 -e AZURE_STORAGE_CONNECTION_STRING="" myapp

4) Design Decisions
   
5) Results & Evaluation
   
6) What’s Next
   
In addition, to make this service more usable. I can use better processing power, the website it running on the render free tier, as currently the website struggles with uploads of two hours or greater.

Cloudflare offers Cloudflare CDN which could allow faster retrieval and better watching experiences for people who live far away from the blob storage service by having copies of the same videos in different geographical regions.

The CSS code is separated in the html files. I think in the future I should refactor this code to make CSS files that helps make the html code more readable by moving that CSS code to its own file.

7) Links (Required)
GitHub Repo: https://github.com/J-CYN/Systems_VideoPlatform
Render App: https://systems-videoplatform.onrender.com