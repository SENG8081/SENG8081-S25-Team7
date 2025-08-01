# SENG8081-S25-Team7
- Shivani Shivani
- Andrews Owusu
- Jai Vadhani
- Kulwinder singh


# Project Topic:
How student sleep patterns and lifestyle affect academic performance.


# Project Expectation:
The project aims to analyze the sleep habits of university students and how it affects their daily lives. 
Aside sleep patterns, the data also takes into account lifestyle choices like screen time, exercise, and study hours, and how these activities may affect their sleep. 
Our goal is to find patterns that show how these factors are connected.


# Data Research Process: 

In order to determine appropriate datasets, we used search terms such as "college sleep behavior", "student sleeping patterns", and "sleep and academic performance" on Google Dataset Search, Kaggle, GitHub, and RPubs. This helped us to locate datasets that aligned with our project expectations.
Having evaluated a few sources, we chose three sets of data that are close to our study objectives:

- Student Sleep Patterns (Kaggle, by Arsalan Jamal):
- Insomnia of students and college performance (Mendeley):
- RPubs Sleep Study Dataset:


Collectively these datasets will enable us to ask questions like:

- Is there a linkage between more screen time and poorer sleep?
- What is the effect of physical exercise on the length of sleep?
- Does academic performance have anything to do with sleeping habits?

Through these trends, we would like to emphasize the significance of sleep as the key to student well-being and academic results.



# Description of Dataset 
The dataset contains information on students’ sleep duration, quality of sleep, screen time, physical activity, and overall health, among other factors. Each row represents a student, with columns which include their age, gender, university year, sleep duration and timing (weekday and weekend start and end times), study hours, screen time, caffeine intake, physical activity levels, and self-reported sleep quality. It includes a manageable number of records and is available in a clean CSV format.The dataset has uniform data types which make such data clean easily in Python using libs like pandas and visualise in R including ggplot2 or through Shiny dashboards.

- ### Student Sleep Patterns Dataset (Kaggle, by Arsalan Jamal):
The data has a good structure and the variables present in the data are the hours of sleep, quality of sleep, the time spent using screens, stress, study time, and physical activity. It was best suited to conduct statistical and visual analysis to determine some patterns of student sleeping behavior.

- ### Insomnia of students and college performance Dataset (Mendeley):
This is a collection of the survey data of 985 students that covers information regarding the frequency of insomnia, their GPA, stress, and characteristics of their lifestyle. It offers great insights concerning the effect of sleep disorders on academic performance.

- ### RPubs Sleep Study Dataset:
This dataset contains structured variables of sleep in a clean form, which is appropriate in regression, correlation analyses, and visualizations.



# Data Storage and Maintenance 
In this project, the databases will be in a SQL server relational database to make it easy to organize, integrate, and analyze. Each dataset will be stored in separate tables, and relationship between tables will be established by common fields.

## Keeping information in SQL server will have the following benefits:

- Relational structure: Allows SQL joins to be able to join data on different tables to get more insight.
- Central accessibility: The data source is handled using a single control, without complicating update and queries.
- Data cleaning and filtering: It is possible to clean and filter the data with SQL queries prior to analysis.
- Export flexibility: It is quick and simple to export cleaned and combined datasets to work with Python, R, Power BI, or excel.
- Security and control: SQL Server has features of built-in access control, and backup, versioning.








# Link to dataset:
https://www.kaggle.com/datasets/arsalanjamal002/student-sleep-patterns/data

https://data.mendeley.com/datasets/5mvrx4v62z/3

https://rpubs.com/cp2185kc/1253151

