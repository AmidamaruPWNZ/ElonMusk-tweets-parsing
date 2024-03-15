from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import undetected_chromedriver as uc

# Function to scrape Elon Musk's recent tweets
def scrape_elon_tweets():
    # Set up Selenium webdriver (make sure to install the appropriate webdriver for your browser)
    driver = uc.Chrome()  # You can change this to Firefox or any other supported browser

    # URL of Elon Musk's Twitter profile
    url = "https://twitter.com/elonmusk"

    # Open the URL
    driver.get(url)

    # Wait for tweets to load (adjust this time according to your internet speed)
    driver.implicitly_wait(10)

    # Find all tweet elements
    tweets = driver.find_element(By.XPATH, '//div[@data-testid="tweet"]')

    # Create a list to store tweet texts
    tweet_texts = []

    # Iterate through the tweet elements and extract text
    for tweet in tweets[:10]:  # Only the first 10 tweets
        try:
            tweet_text = tweet.find_element_by_xpath('.//div[@lang="en"]').text
            tweet_texts.append(tweet_text)
        except:
            pass

    # Close the webdriver
    driver.quit()

    return tweet_texts

# Function to save tweets to a CSV file
def save_to_csv(tweet_texts):
    with open('elon_tweets.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Tweet'])
        for tweet in tweet_texts:
            writer.writerow([tweet])

# Main function
def main():
    tweet_texts = scrape_elon_tweets()
    save_to_csv(tweet_texts)
    print("Elon Musk's recent tweets have been saved to 'elon_tweets.csv'")

if __name__ == "__main__":
    main()
