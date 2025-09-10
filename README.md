Deployed PWS link: https://ayshia-la-footballshop.pbp.cs.ui.ac.id/

Questions:
1. How was it implemented?
   > First we need to initialize and configure the database for a new django project, before uploading it to a GitHub repo. After that we can deploy it through the PWS, making the web accessible to everyone. Once the project is initialized, we can start making the application. As per instructed, we create the main application in our project, where it stores the starting structure for our project and configure routing it by registering 'main' application on the project. Now we can start with the Models on MVT. As requested, the Product is the model we're defining inside models.py. Once all the attribute has been added, we need to create a show_main function in views.py that will show our main.html file when the web is accessed, and routing it by configuring the urls.py at the project level.
   
3. Client request -> Django Web Diagram
   <img width="1920" height="1080" alt="Client" src="https://github.com/user-attachments/assets/cffc7931-3760-49e5-9fb9-975c210fc003" />
   
4. Role of settings.py in a Django project: 
   In a Django project, settings.py is like the control center or configuration hub. Where it's main roles are:
   > Project Configuration:
     Defines how the Django project behaves.
     Holds global settings for the entire project, not just one app.
   > Database Settings: Tells Django which database to use and how to connect. (**DATABASES** in settings.py)
   > Installed Apps: Lists all Django and third-party apps that are active in the project. (**INSTALLED_APPS**)
   > Middleware: Configures middleware components that process requests and responses (e.g., authentication, security, sessions). (**MIDDLEWARE**)
   > Templates and Static Files: Configures where Django should look for HTML templates and static files (CSS, JS, images). (**TEMPLATES**)
   > Security & Authentication: Secret key, allowed hosts, password hashing, CSRF protection, etc.
   > Localization: Controls language and timezone.
   > Debugging & Environment Settings: Toggles debug mode (useful in development, dangerous in production). (**DEBUG**= True #development)

5. How does database migration work in Django?
   > A migration is a way to apply changes you make to your models (models.py) into the actual database schema (tables, columns, constraints, etc.). Instead of writing SQL manually, Django translates your Python model changes into database operations. Where models.py defined your data structure, the command **makemigrations** writes the  _instruction_ for the DB change, and the **migrate** command executes those instructions on the real DB.

6. Why is the Django framework chosen as the starting point for learning software development?
   > Because of its quick of use and results. Its framework has almost everything built in, so we can focus on how web apps works first before coming to the nitty-gritty. And it is also a great way to introduce core software development process throughout its whole project building (MVT, Database, HTTP response cycle, etc.).

7. Any feedback for the teaching assistant for Tutorial 1 that you previously completed?
   > None from me. The TA's are very helpful are always ready to help, it's just that Tutorial 1 is not as hard as Tutorial 0 so i didn't request for a TA's help. Keep it up kak!
