SELECT * FROM engagement_data

SELECT ContentType
FROM [dbo].[engagement_data]
GROUP BY ContentType

SELECT 
EngagementID,
ContentID,
CampaignID,
ProductID,
LOWER(REPLACE(ContentType, 'Socialmedia', 'Social Media')) AS ContentType,
LEFT(ViewsClicksCombined, CHARINDEX('-', ViewsClicksCombined)-1) AS Views,
RIGHT(ViewsClicksCombined, LEN(ViewsClicksCombined) - CHARINDEX('-', ViewsClicksCombined)) AS Clicks,
Likes,
FORMAT(CONVERT(date, EngagementDate), 'dd.MM.yyyy') AS EngagementDate
FROM engagement_data
WHERE ContentType <> 'Newsletter'


WITH Duplicates AS(
SELECT *,
ROW_NUMBER() 
OVER (PARTITION BY EngagementID, ContentID, ContentType, EngagementDate, CampaignID, ProductID
ORDER BY EngagementID) AS RN
FROM engagement_data)

SELECT * FROM Duplicates
where RN > 1

