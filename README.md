**ASSIGNMENT 3**
1. Why do we need data delivery in implementing a platform?
    > data delivery is important because the platform doesn’t only serve HTML pages, it often needs to exchange data with other systems, apps, or even its own frontend.

2. In your opinion, which is better, XML or JSON? Why is JSON more popular than XML?
    > While they both might bring slightly different benefits, i prefer JSON more due to how easier it is to read the data. It is also particularly for this reason that JSON is more popular, because of ease and ecosystem support, where most modern programming language have built-in JSON library.

3. What is the purpose of the is_valid() method in Django forms, and why do we need it?
    > is_valid() checks if form input follows all validation rules and, if so, makes the cleaned data available. We need it to prevent invalid or unsafe data from being saved or processed.

4. Why do we need a csrf_token when making forms in Django? What can happen if we don't include a csrf_token in a Django form? How can this be exploited by an attacker?
    > Django includes csrf_token to protect against Cross-Site Request Forgery (CSRF) attacks. It ensures that a form submission really comes from your website and not from a malicious third-party site. Without it, attackers could trick authenticated users into submitting malicious requests (e.g., adding/deleting data) on their behalf.

5. How I implemented the checklists
    > First we add 4 new functions in views.py to show data by XML, JSON, XML by ID, and JSON by ID where each function takes a request as a parameter, and define a variable inside the function to store the query result of all data in Product. After that we add  a return statement using HttpResponse that contains the query results serialized as XML/JSON, along with the parameter. Then we can create the URL routings for each function by importing the function to urls.py and add the url path for each function to urlpatterns. To create the webpage for creating a product(form) and showing the detail, we can make the html page for create_product and product_detail, where we can set up the commands on what each page does on views.py, and then route the url on urls.py. For forms, we also need to define what the form is on forms.py. 

6. TA's feedback
    > None for the TA, but more towards the material given. There's quite a few typos that's detrimental to the program. Other than that, the TA's are very helpful.

7. Postman Screenshot
    1. XML
       <img width="1240" height="756" alt="Screenshot 2025-09-15 102936" src="https://github.com/user-attachments/assets/ff0edb50-9e26-42f8-90ca-f933e5ddbad5" />
   2. JSON
      <img width="1242" height="769" alt="Screenshot 2025-09-15 103407" src="https://github.com/user-attachments/assets/63eeeee3-a549-45c3-b580-ba3d0ba1eede" />
   3. XML by ID
      <img width="1271" height="767" alt="Screenshot 2025-09-15 103449" src="https://github.com/user-attachments/assets/66546568-fe6e-4a22-a627-8d2311b40132" />
   4. JSON by ID
      <img width="1253" height="763" alt="Screenshot 2025-09-15 103431" src="https://github.com/user-attachments/assets/0e5fbd64-038c-461b-9318-72d7c1942c08" />


**ASSIGNMENT 4**
1. What is Django's AuthenticationForm?
    > AuthenticationForm is a built-in Django form (from django.contrib.auth.forms) that handles user login. It checks that the username and password are valid. If credentials are correct, it authenticates the user and can be used with Django’s LoginView. It's advantages include: Saves time (no need to write your own login form), automatically validates credentials using Django’s authenticate(), provides helpful error messages out of the box, integrates seamlessly with Django’s authentication system. While its disadvantages include: Limited flexibility — if you need custom login logic (like logging in with email instead of username), you must subclass/override it, error messages may be too generic unless customized.

2. What is the difference between authentication and authorization? How does Django implement the two concepts?
    > Authentication: verifies a user's identity. Authorization: checking a user's permission. Django implements authentication via django.contrib.auth.authenticate() and LoginView. The request.user object represents the logged-in user. While it implements authorization via Django’s permissions and groups system (user.has_perm(), user.is_staff, @permission_required, etc.).

3. What are the benefits and drawbacks of using sessions and cookies in storing the state of a web application?
    > Sessions and cookies are both used to store state in web applications. Sessions store data on the server, with only a session ID saved in the client’s cookie. This makes them more secure and capable of handling larger or more complex data, but they require server storage and management. Cookies store data directly in the user’s browser, making them lightweight and not dependent on server storage, which is useful for small pieces of information like user preferences. However, cookies are limited in size, easy for users to tamper with, and can expose sensitive data if not secured properly.

4. In web development, is the usage of cookies secure by default, or is there any potential risk that we should be aware of? How does Django handle this problem?
    > Cookies are not secure by default because they are stored as plain text in the browser and can be exposed to attacks such as cross-site scripting or session hijacking. Django addresses these risks by providing security features such as SESSION_COOKIE_HTTPONLY, which prevents JavaScript from reading cookies, and SESSION_COOKIE_SECURE, which ensures cookies are only transmitted over HTTPS. It also protects against CSRF attacks using CSRF tokens and can sign cookies to prevent tampering.

5. Explain the implementation.
    > To implement register, login, and logout, we use Django’s built-in authentication system (django.contrib.auth). For registration, we use UserCreationForm. For login, we use AuthenticationForm together with built in functions authenticate() and login(). Logout is handled with Django’s logout() function, which clears the session and removes the user’s authentication state. To restrict user access, we use the login_required decorator. Next we create two user accounts with dummy data by running the python manage.py runserver and test the website. And to connect the Product to User, we add user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) to the Product Model. To show the user's last login, we explicitly set a cookie for last_login in our login view using response.set_cookie("last_login", str(datetime. datetime.now())), and then read it back with request.COOKIES.get('last_login', 'Never'). To display the user's username, we use request.user object.