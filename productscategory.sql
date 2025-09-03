SELECT * FROM Products

SELECT MIN(Price) [MinPrice], MAX(Price) [MaxPrice]
FROM Products

SELECT *,
CASE
	WHEN Price < 50 THEN 'Low'
	WHEN Price BETWEEN 50 AND 200 THEN 'Medium'
	ELSE 'High'
END AS PriceCategory
FROM products