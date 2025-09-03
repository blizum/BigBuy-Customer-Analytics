SELECT * FROM customer_journey

---Checking Duplicates
WITH Duplicates AS(
SELECT *,
ROW_NUMBER()
OVER (PARTITION BY JourneyID, CustomerID, ProductID, VisitDate, Stage, Action
ORDER BY JourneyID) AS RowNum
FROM customer_journey
)

SELECT * FROM Duplicates
WHERE RowNum > 1
ORDER BY JourneyID








SELECT 
JourneyID,
CustomerID,
ProductID,
FORMAT(CONVERT(date, VisitDate), 'dd.MM.yyyy') AS VisitDate,
LOWER(Stage) AS Stage,
LOWER(Action) AS Action,
COALESCE(Duration, AvgDuratn) AS Duration
FROM 

(SELECT *, 
AVG(Duration) OVER(PARTITION BY VisitDate) AS AvgDuratn,
ROW_NUMBER()
OVER (PARTITION BY JourneyID, CustomerID, ProductID, VisitDate, Stage, Action
ORDER BY JourneyID) AS RowNum
FROM customer_journey) AS SQ
WHERE RowNum = 1
