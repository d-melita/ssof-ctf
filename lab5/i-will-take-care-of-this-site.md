# Challenge `I will take care of this site` Writeup

- Vulnerability: 
  - SQL Injection attack
- Where:
  - Password text field
- Impact:
  - allows non-admin users to access the admin account

## Steps to reproduce

Firstly, it is useful to try and generate an error to see what query is being made to verify the login information.
By inputing `'` in the username and `'` in the password, the following error is displayed: `SELECT id, username, password, bio, age, jackpot_val FROM user WHERE username = ''' AND password = '265fda17a34611b1533d8a281ff680dc5791b0ce0a11c25b35e11c8e75685509'`. This SQL query is exploitable since we can comment out the verification of the password by inserting the username as `admin'; --` and a random non-empty password. The resulting query will be `SELECT id, username, password, bio, age, jackpot_val FROM user WHERE username = 'admin'`, granting access to the admin account where we can find the flag in the bio section of the profile.
