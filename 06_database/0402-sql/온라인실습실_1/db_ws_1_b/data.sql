-- 1.
SELECT * FROM songs;

-- 2.
SELECT
  * 
FROM
  songs
ORDER BY
  title DESC;

-- 3.
SELECT
  *
FROM
  songs
WHERE
  genre = 'Pop';

-- 4.
SELECT
  *
FROM
  songs
WHERE
  duration >= 180;