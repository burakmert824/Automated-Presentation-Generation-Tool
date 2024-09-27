Project Overview
This project aims to automate the creation of PowerPoint presentations for customer reports by capturing dynamic web images and embedding them into slides. Originally developed during my internship at Nokia, the solution leverages screenshots from specific web elements to automate report generation, significantly reducing the time and manual effort required to create presentations.

Due to access restrictions on Nokia's web application, the project was prototyped using weather data from the AccuWeather website. The program captures daily and weekly weather forecasts for Izmit and automatically generates a PowerPoint presentation based on the forecast data. However, the implementation is flexible and can be adapted to gather data from other websites, making it a versatile tool for various use cases.

Features
Automated Web Data Capture: The program automatically accesses a website, captures specific web elements (e.g., weather forecasts), and generates a PowerPoint presentation.
Customizable and Extensible: The current implementation works with AccuWeather, but the script can be easily modified to extract and use data from any website.
Daily and Weekly Reports: It gathers daily and weekly forecast data for Izmit and embeds it into a cleanly formatted PowerPoint presentation.
Consistent Deployment: The project is Dockerized to ensure smooth deployment across different environments.
Getting Started
Prerequisites
Python 3.x
Selenium for web scraping
PowerPoint generation libraries (e.g., python-pptx)
