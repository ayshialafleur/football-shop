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
