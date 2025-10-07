# Assignment 3
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


# Assigment 4
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

# Assignment 5
1. Priority order for CSS Selector design
    > When multiple CSS selectors apply to the same element, the browser uses specificity rules to determine which one takes precedence. Inline styles written directly in the element have the highest priority, followed by ID selectors which are stronger than class or attribute selectors, and then by class selectors, attribute selectors, and pseudo-classes. Tag selectors and pseudo-elements have the lowest priority. If two selectors share the same specificity, the one written last in the stylesheet is applied. In rare cases, the !important rule can override everything, but it is generally discouraged because it makes CSS harder to manage.

2. Responsive design:
    > Responsive design is important because it ensures that a web application can be accessed and used comfortably across different devices and screen sizes, whether on desktop, tablet, or mobile. It improves user experience, accessibility, and even SEO rankings, since search engines like Google favor mobile-friendly sites. A good example of responsive design is YouTube, which automatically adjusts video size, navigation, and layout depending on the device, or Twitter/X, which adapts its feed and controls smoothly across platforms. On the other hand, older government websites or early 2000s forums often lack responsiveness, requiring horizontal scrolling or breaking on smaller screens. This happens because modern sites use flexible layouts, media queries, and frameworks like Bootstrap or Tailwind, while older ones were built with fixed pixel values and without mobile-first design in mind.

3. Box Model
    > The CSS box model describes how space is managed around elements. At the core is the content area, which contains text, images, or other elements. Surrounding the content is padding, which creates space between the content and the border. The border itself wraps around the padding and defines the visible boundary of the element. Finally, the margin is the space outside the border, separating the element from other elements on the page. For example, setting a card with margin: 20px, border: 2px solid black, and padding: 15px means the element will have space around it, a defined border, and some breathing room inside between its content and border.

4. Layout Systems
    > Flexbox is a one-dimensional layout model, meaning it excels at arranging items along a single axis—either horizontally in a row or vertically in a column. It is commonly used for tasks like building navigation bars, centering elements, or distributing space evenly between items. Grid, on the other hand, is a two-dimensional layout system that allows for controlling both rows and columns simultaneously, making it better suited for more complex layouts such as dashboards, product galleries, or entire web page structures. In short, flexbox is best for linear arrangements, while grid is designed for more structured, two-dimensional designs.

5. Implementation steps
    > First, implementing the delete and edit functions follows the same pattern as previous features: Create the functions in views.py and then connect them through routes in urls.py. For design customization, I use Tailwind CSS, which requires configuring settings.py, editing base.html, creating a global CSS file for forms, and preparing a static folder to store supporting elements. Each page was then customized individually by applying Tailwind classes directly in their respective HTML files to improve layout and styling, and handle responsiveness using conditional logic (if/else) directly in the HTML to showcase respective desired view. And create a navigation bar with Tailwind that adapts to both desktop and mobile screens.

# Assigment 6
1. What is the difference between synchronous request and asynchronous request?
    > Synchronous requests block the program's execution until a response is received, whereas asynchronous requests do not block the program, allowing it to continue other tasks while waiting for a response. In a synchronous operation, the client waits for the entire process to finish, like being stuck in a single-lane queue at a bank. In contrast, an asynchronous operation lets the client send a request, move on to other work, and receive a notification later when the request is complete, similar to getting a pager at a restaurant and being free to browse while you wait for your table. 

2. How does AJAX work in Django (request–response flow)?
    > AJAX (Asynchronous JavaScript and XML) in Django enables client-side JavaScript to communicate with the Django server without requiring a full page reload, leading to a more dynamic and responsive user experience. Usually, an event occurs in the user's browser (e.g., button click, form submission, page load) using fetch API or JQUery, This request can be a GET or POST request and might contain data (e.g., form data, JSON payload), where it creates and sends an asynchronous HTTP request to a specific URL on the Django server. The Django URL dispatcher routes the incoming AJAX request to the appropriate view function based on the URL pattern defined in urls.py and the view function processes the request data, interacts with the database (e.g., retrieving or saving data), and performs any necessary logic. After processing, the Django view constructs an HttpResponse object or for AJAX requests, this response is often in a structured format like JSON, using JsonResponse. The HttpResponse object, containing the processed data or status information, is then sent back to the client (The JavaScript code that initiated the AJAX request). It parses the response data (e.g., response.json() for JSON data), and based on the received data, the JavaScript dynamically updates specific parts of the web page without a full reload, providing a seamless user experience. This might involve updating elements, displaying messages, or manipulating the DOM.

3. What are the advantages of using AJAX compared to regular rendering in Django?
    > It enhances User Experience by providing dynamic updates of specific parts of a webpage without requiring full page reload and since AJAX requests are asynchronous, meaning the client-side browser can continue to interact with the page while data is being fetched from the server in the background. While Django handles the backend logic and data, AJAX allows for a more distinct separation of concerns by letting JavaScript on the frontend manage UI updates based on data received from Django's API endpoints. This can lead to more maintainable and scalable codebases.

4. How do you ensure security when using AJAX for Login and Register features in Django?
    > Without AJAX, to protect from CSRF we can iclude {% csrf_token %} in our forms submission, where Django's CsrfViewMiddleware will handle validation. However, when making an AJAX request, we extract the CSRF token from the DOM and include it in the X-CSRFToken header of your request.

5. How does AJAX affect user experience (UX) on websites?
    > AJAX enhances website user experience (UX) by providing faster, more responsive interactions through partial page updates, eliminating full page reloads and making web applications feel more like desktop applications. This leads to smoother navigation, real-time data updates, and improved performance without interrupting the user's current task, ultimately increasing user engagement and satisfaction. 
