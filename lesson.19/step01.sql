-- SELECT *
-- FROM users;

-- SELECT name, email
-- FROM users;


-- select *
-- from orders
-- where status = 'paid';


-- select *
-- from orders
-- where amount > 3000;

--   > < >= <= != =


-- SELECT *  FROM orders
--          WHERE amount > 3000
-- AND status = 'paid';

-- AND OR


-- SELECT *
-- FROM orders
-- WHERE amount > 3000
-- ORDER BY user_id;


-- SELECT *
-- FROM orders
-- WHERE amount > 3000
-- ORDER BY user_id ASC;


-- SELECT *
-- FROM orders
-- WHERE amount > 3000
-- ORDER BY user_id DESC;


-- SELECT *
-- FROM orders
-- WHERE amount > 3000
-- ORDER BY user_id DESC
-- LIMIT 5;
-- ;


-- SELECT *
-- FROM users
-- INNER JOIN orders
-- ON users.id = orders.user_id;


-- SELECT name, amount
-- FROM users
-- INNER JOIN orders
-- ON users.id = orders.user_id;


-- SELECT users.name, orders.amount
-- FROM users
-- INNER JOIN orders
-- ON users.id = orders.user_id;


-- SELECT u.name, o.amount
-- FROM users AS u
-- INNER JOIN orders AS o
-- ON u.id = o.user_id;


-- SELECT u.name AS NAME_USER, o.amount
-- FROM users AS u
-- INNER JOIN orders AS o
-- ON u.id = o.user_id;



SELECT u.name AS NAME_USER, o.amount
FROM users u
INNER JOIN orders o
ON u.id = o.user_id
WHERE o.status = 'paid';