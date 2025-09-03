# BigBuy-Customer-Analytics
BigBuy, an e-commerce store facing a severe loss in revenue and engagement despite spending a lot on marketing. This project analyses the trends and causes of these problems faced  by the store.

## The Problem
BigBuy is experiencing a decline in customer engagement and conversion despite ongoing and substantial
marketing investments. The business needs a structured analytics investigation to diagnose where the
marketing funnel is leaking, determine which channels and campaigns are underperforming, understand
customer sentiment about products and the shopping experience, and recommend tactical and strategic
improvements to increase engagement, improve conversion rates, and reduce wasted marketing spend.

## Symptoms
Reduced customer engagement: fewer pageviews per session, lower time on site, reduced clicks on
marketing assets and product detail pages, declining email open/click rates and social interactions.

Decreased conversion rates: fewer visitors complete key conversion steps (add to cart, checkout), or
higher drop-off at payment/checkout pages.

High marketing expenses with poor ROI: campaigns require significant investment but deliver low
conversion and high CAC.

Lack of clear customer feedback insights: limited or unstructured customer feedback that prevents
understanding of product satisfaction, UX issues, pricing perceptions, or fulfillment problems.

## KPIs to find the Cause
Conversion Rate: Percentage of website visitors who make a
purchase and who abandon (abandonment rate)

Customer Engagement Rate: Level of interaction with marketing
content, such as clicks, likes, comments, session duration

Amount spent on Purchase: Average amount spent by a customer
per transaction, repeat purchase rate

Customer Feedback Score: Net sentiment of customers

## Procedure
- We start by cleaning the fact and dimension tables in SQL Server. We utilise data manipulation, exploratory data analysis to understand the data and finally clean the data for vizualisation and calculations
- Then we utilise NLTK library in Python to perform a simple sentiment analysis on the reviews of the customers and categorise the review text into various categories from Neutral to Positive
- Finally, we import the fact and dimension tables into PowerBI. We perform the required transformations, establish relationships and calculate all the required measures to find the KPIs. Finally, we draw up a neat dashboard to have
  a comprehensive understanding of the business problem and find the cause and solutions.
