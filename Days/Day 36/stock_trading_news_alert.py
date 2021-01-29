# Day 36 project - Stock Trading News Alert.

import requests
import smtplib

# User details.
EMAIL = "your_email@gmail.com"
PASSWORD = "your_email_password"
RECEIVER_EMAIL = "receiver's_email@gmail.com"

# Stock details.
STOCK = "stock name"
COMPANY_NAME = "company name"
STOCK_API_KEY = "your own Alpha Vantage API key"
NEWS_API_KEY = "your own NewsAPI key"


def main():
    """Main function to run the project."""
    price_differ_percentage = stock_price_difference_percentage()
    if abs(price_differ_percentage) > 3:
        articles = get_articles()
        for article in articles:
            title = article["title"]
            description = article["description"]
            send_email(title, description, price_differ_percentage)


def stock_price_difference_percentage():
    """
    Returns the stock price difference percentage between
    yesterday's and day before yesterday's closing time stock price.
    """
    stock_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": STOCK_API_KEY,
    }
    response = requests.get(
        url="https://www.alphavantage.co/query",
        params=stock_parameters
    )
    # Getting the last 2 days data.
    data = response.json()["Time Series (Daily)"]
    dates = list(data)[:2]
    yesterday_price = float(data[dates[0]]["4. close"])
    day_before_yesterday_price = float(data[dates[1]]["4. close"])

    # Calculate the price difference and return the percentage difference.
    price_difference = yesterday_price - day_before_yesterday_price
    return round(((price_difference/day_before_yesterday_price) * 100), 2)


def get_articles():
    """Returns the top 3 news articles related to the stock."""
    news_parameters = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
        "pageSize": 3,
        "language": "en"
    }
    response = requests.get(
        url="https://newsapi.org/v2/everything",
        params=news_parameters,
    )
    articles = response.json()["articles"]
    return articles


def send_email(title, description, differ_percentage):
    """
    Sends email to receiver's email with stock price difference percentage
    and the top 3 stock related news.
    """
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL, to_addrs=RECEIVER_EMAIL,
            msg=f"Subject :{STOCK}: {differ_percentage}%\n\n"
                f"Headline :{title}\nBrief: {description}".encode("utf-8")
        )


# Function call to run the program.
if __name__ == "__main__":
    main()
