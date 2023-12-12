# Challenge `Sometimes we are just temporarily blind - V2` Writeup

- Vulnerability:
  - SQL Injection attack
- Where:
  - Search blog posts text field
- Impact:
  - allows users to find a hidden secret in the database

## Steps to reproduce
The steps to reproduce are the same as the previous challenge since we used the `substr` function to make the query case sensitive.
