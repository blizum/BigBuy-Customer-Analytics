SELECT * FROM Customers

SELECT * FROM Geography

SELECT 
C.CustomerID, C.CustomerName,
C.Email, C.Gender, C.Age,
G.GeographyID, G.Country, G.City
FROM customers C
LEFT JOIN geography G
ON C.GeographyID = G.GeographyID