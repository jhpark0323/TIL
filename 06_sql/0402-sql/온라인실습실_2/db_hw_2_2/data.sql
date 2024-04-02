-- orders
CREATE TABLE orders (
  order_id INTEGER PRIMARY KEY AUTOINCREMENT,
  order_date VARCHAR(50) NOT NULL,
  total_amount Real NOT NULL
);

PRAGMA table_info('orders');

INSERT INTO
  orders (order_date, total_amount)
VALUES
  ('2023-07-15', '50.99'),
  ('2023-07-16', '75.5'),
  ('2023-07-17', '30.25');

SELECT * FROM orders;

-- customers
CREATE TABLE customers (
  customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(50) NOT NULL,
  email VARCHAR(100) NOT NULL,
  phone VARCHAR(50) NOT NULL
);

INSERT INTO
  customers (name, email, phone)
VALUES
  ('허균', 'hong.gildong@example.com', '010-1234-5678'),
  ('김영희', 'kim.younghee@example.com', '010-9876-5432'),
  ('이철수', 'lee.cheolsu@example.com', '010-5555-4444');

SELECT * FROM customers;

-- 생성 완료

DELETE FROM
  orders
WHERE
  order_id = 3;

UPDATE
  customers
SET
  name = '홍길동'
WHERE
  customer_id = 1;

SELECT * FROM customers;
SELECT * FROM orders;
