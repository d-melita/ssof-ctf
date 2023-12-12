# Challenge `Money, money, money!` Writeup

- Vulnerability: 
  - SQL Injection attack
- Where:
  - Bio text field of the user profile
- Impact:
  - allows users to manipulate tokens or jackpot values

## Steps to Reproduce

From the previous challenge, we known that the table `user` has a `jackpot_val` column. Since this is an `UPDATE` statement, it possible to set this parameter to any value.
Currently the user has zero tokens, so to hit the jackpot we should set the `jackpot_val` to zero.

By typing `'` on the bio field, we get the following error: `UPDATE user SET bio = ''' WHERE username = 'user123'`. We can exploit this query and update the user's jackpot value by typing `', jackpot_val = '0` on the bio field. This will create the query `UPDATE user SET bio = '', jackpot_val='0' WHERE username = 'user123'` and display the flag hidden in the jackpot.
