select user_id, email
from users
where email regexp "^[a-zA-Z0-9_]+@[a-zA-z]+\\.com"
order by user_id ;


SELECT user_id,email FROM Users WHERE
regexp_like(email,'[A-Za-z0-9_]+@[a-zA-Z0-9_]+\.com$')
ORDER BY user_id;
