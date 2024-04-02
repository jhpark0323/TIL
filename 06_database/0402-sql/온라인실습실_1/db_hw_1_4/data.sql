-- 1.
SELECT
  *
FROM
  tracks
WHERE
  name LIKE '%love%';

-- 2.
SELECT
  *
FROM
  tracks
WHERE
  GenreId = 1 AND
  Milliseconds >= 300000
ORDER BY
  UnitPrice DESC;


-- 3.
SELECT
  GenreId, COUNT(*) AS 'TotalTracks'
FROM
  tracks
GROUP BY
  GenreId;

-- 4.
SELECT
  GenreId, SUM(UnitPrice) AS 'TotalPrice'
FROM
  tracks
GROUP BY
  GenreId
HAVING
  TotalPrice >= 100;