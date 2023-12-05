# Challenge `Just my boring cookies` Writeup

- Vulnerability:
    - XSS attack

- Where:
    - Blog posts' search bar

- Impact:
    - Allows to inject javascript code that will be executed in client's browser

## Steps to reproduce

This challenge consists in grabbing the user's cookie. By searching for `<script>alert("Hello")</script>` in the search bar, we can see that the script is executed - an alert box will be displayed with the content "Hello". We can then try to grab the cookie by using the following script: `<script>alert(document.cookie)</script>`. This will display the cookie in an alert box and we can get the flag.
