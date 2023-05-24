# Trekkers API
#
This is the backend api for the trekkers Frontemd React app. It contains the models and logic to allow the frontend application to perform CRUD operations.

#
* [Deployed Back-End page](https://pp5-trekkers-api.herokuapp.com/)
* [Deployed Front-End page](https://trekkers.herokuapp.com/)
* [Frontend repository](https://github.com/HPCarey/trekkers)
#
### Agile Planning
#### **GitHub Project Board**

* This project was made using agile methodologies. Epics, user stories, bugs and issues are recorded on the [Project Board](https://github.com/users/HPCarey/projects/5/views/1)

![Screenshot of project board](/readme/kanban-board.png)

#### **Github Issues**
Here is a [link](https://github.com/HPCarey/trekkers/issues)  to the project issues and labels. 
* A list of Frontend Bugs can be viewed via the Frontend Bug label. 
* A list of backend bugs can be viewed via the Backend bug label.
* A list of all bugs can be viewed via the bugs label.


#### **ERD Plan for backend models**
 * The plan for this project is based on the Code Institute Moments walkthrough project. 
 * Most of the models are the same except for the post model which has been customised to better suit the needs of the site owner and users.
 * Initial plans were to include an event model, but that has been assigned as a future feature to help focus on the minimal viable product of  the site. 

![Database](/readme/trekkers_erd.jpeg)
#
## **Credits**
### Code Institute

This project is a variation and laregely based on the [Code Institute Moments](https://github.com/Code-Institute-Solutions/drf-api/tree/ed54af9450e64d71bc4ecf16af0c35d00829a106) walkthrough project.
It contains models and logic from that project which have bee modified for the prupose of this one.

### Resources for creating the rating field in post model:
1.	Geeksforgeeks: [Posititive Integer field](https://www.geeksforgeeks.org/positiveintegerfield-django-models/)
2.	Stack overflow: [Set a default min/max value for inetger field](https://stackoverflow.com/questions/42425933/how-do-i-set-a-default-max-and-min-value-for-an-integerfield-django)

### Bug fixes sources:
1.	Application labels aren’t unique error when deploying backend api : [Stack Overflow](https://stackoverflow.com/questions/24319558/how-to-resolve-django-core-exceptions-improperlyconfigured-application-labels)
2. Other bug fix sources are credited in the Project Board under Issues labelled "Backend bug"
