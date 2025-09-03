#necessary imports
import nltk
import pandas as pd
import pyodbc
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon') 

def extract_from_sql():
    #Define the connection string with parameters for the database connection
    conn_str = (
        "Driver={SQL Server};"  # Specify the driver for SQL Server
        "Server=BLIZUM\SQLEXPRESS;"  # Specify your SQL Server instance
        "Database=PortfolioProject_MarketingAnalytics;"  # Specify the database name
        "Trusted_Connection=yes;"  # Use Windows Authentication for the connection
    )
    # Establish the connection to the database
    conn = pyodbc.connect(conn_str)
    
    # Define the SQL query to fetch customer reviews data
    query = "SELECT * FROM customer_reviews"
    
    # Execute the query and fetch the data into a DataFrame
    df = pd.read_sql(query, conn)
    
    # Close the connection to free up resources
    conn.close()
    
    # Return the fetched data as a DataFrame
    return df

#SIA Object
sia = SentimentIntensityAnalyzer()

def calculate_sentiment(review_scores):
    sentiment = sia.polarity_scores(review_scores)
    #Return the compound score, which is a normalized score between -1 (most negative) and 1 (most positive)
    return sentiment['compound']

def calculate_aggregate_sentiment_score(score, rating):
    if score > 0.05:  # Positive sentiment score
        if rating >= 4:
            return 'Positive'  # High rating and positive sentiment
        elif rating == 3:
            return 'Mixed Positive'  # Neutral rating but positive sentiment
        else:
            return 'Mixed Negative'  # Low rating but positive sentiment
    elif score < -0.05:  # Negative sentiment score
        if rating <= 2:
            return 'Negative'  # Low rating and negative sentiment
        elif rating == 3:
            return 'Mixed Negative'  # Neutral rating but negative sentiment
        else:
            return 'Mixed Positive'  # High rating but negative sentiment
    else:  # Neutral sentiment score
        if rating >= 4:
            return 'Positive'  # High rating with neutral sentiment
        elif rating <= 2:
            return 'Negative'  # Low rating with neutral sentiment
        else:
            return 'Neutral'  # Neutral rating and neutral sentiment
        
def calculate_sentiment_range(score):
    if score >= 0.5:
        return '0.5 to 1.0'  # Strongly positive sentiment
    elif 0.0 <= score < 0.5:
        return '0.0 to 0.49'  # Mildly positive sentiment
    elif -0.5 <= score < 0.0:
        return '-0.49 to 0.0'  # Mildly negative sentiment
    else:
        return '-1.0 to -0.5'  # Strongly negative sentiment
    

if __name__ == "__main__":
    customer_reviews_data = extract_from_sql()

    customer_reviews_data['SentimentScore'] = customer_reviews_data['ReviewText'].apply(calculate_sentiment)

    customer_reviews_data['SentimentCategory'] = customer_reviews_data.apply(
        lambda row: calculate_aggregate_sentiment_score(row['SentimentScore'], row['Rating']), axis=1)
    
    customer_reviews_data['SentimentRange'] = customer_reviews_data['SentimentScore'].apply(calculate_sentiment_range)

    print(customer_reviews_data.head(10))



    customer_reviews_data.to_csv('customer_reviews_with_sentiment.csv', index=False)