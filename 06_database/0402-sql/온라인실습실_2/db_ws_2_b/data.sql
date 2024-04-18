SELECT
  *
FROM
  invoices;

-- 1.
SELECT
  InvoiceId, InvoiceDate
FROM
  invoices;

-- 2.
SELECT
  *
FROM
  invoices
WHERE
  BillingCountry = 'USA' AND
  Total > 10;

-- 3.
SELECT
  *
FROM
  invoices
WHERE
  BillingCity = 'London' OR
  BillingCity = 'Berlin';

-- 4.
SELECT
  *
FROM
  invoices
WHERE
  Total = (SELECT MAX(Total) FROM invoices);

-- 5.
SELECT
  *
FROM
  invoices
WHERE
  InvoiceDate >= '2013-03-31' AND
  Total > 3;

-- 6.
SELECT
  *
FROM
  invoices
WHERE
  BillingCountry = 'USA' AND
  BillingState = 'CA' AND
  Total > 10;

-- 7.
SELECT
  *
FROM
  invoices
WHERE
  BillingCountry = 'Canada' AND
  BillingState = 'ON' AND
  BillingCity = 'Toronto';

-- 8.
SELECT
  *
FROM
  invoices
WHERE
  InvoiceDate < '2023-01-01' AND
  (Total >= 50 OR BillingCountry = 'Brazil');