-- 공통
SELECT * FROM articles;
DROP TABLE articles;
PRAGMA table_info('articles');

CREATE TABLE articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(100) NOT NULL,
  content VARCHAR(200) NOT NULL,
  createdAt DATE NOT NULL
);

-- 1. Insert data into table
INSERT INTO
  articles (title, content, createdAt)
VALUES
  ('hello', 'world', '2000-01-01');

INSERT INTO
  articles (title, content, createdAt)
VALUES
  ('hello', 'DB', '2024-04-02');

INSERT INTO
  articles (title, content, createdAt)
VALUES
  ('python', 'clear', '2024-01-20'),
  ('algorithm', 'clear', '2024-03-16'),
  ('django', 'in progress', '2024-04-01'),
  ('hello', 'DB', '2024-04-02');

SELECT * FROM articles;

SELECT rowid, id, title FROM articles;

-- 2. Update data in table
UPDATE
  articles
SET
  title = 'update Title'
WHERE
  id = 1;

UPDATE
  articles
SET
  title = 'update Title',
  content = 'update Content'
WHERE
  id = 2;

UPDATE
  articles
SET
  title = 'JavaScript',
  content = 'Not Started'
WHERE
  title = 'hello';

SELECT * FROM articles;

-- 3. Delete data from table
DELETE FROM
  articles
WHERE
  id = 6;

INSERT INTO
  articles (title, content, createdAt)
VALUES
  ('new_title', 'new_content', '2020-01-02');

DELETE FROM
  articles
WHERE id IN (
  SELECT
    id
  FROM
    articles
  ORDER BY
    createdAt
  LIMIT
    2
);

SELECT * FROM articles;

