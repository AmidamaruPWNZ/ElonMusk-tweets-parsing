from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import undetected_chromedriver as uc

def scrape_elon_tweets():
    driver = uc.Chrome()

    url = "https://twitter.com/elonmusk"

    driver.get(url)

    driver.implicitly_wait(10)

    tweets = driver.find_element(By.XPATH, '//div[@data-testid="tweet"]')

    tweet_texts = []

    for tweet in tweets[:10]:
        try:
            tweet_text = tweet.find_element_by_xpath('.//div[@lang="en"]').text
            tweet_texts.append(tweet_text)
        except:
            pass

    driver.quit()

    return tweet_texts

def save_to_csv(tweet_texts):
    with open('elon_tweets.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Tweet'])
        for tweet in tweet_texts:
            writer.writerow([tweet])

def main():
    tweet_texts = scrape_elon_tweets()
    save_to_csv(tweet_texts)
    print("Elon Musk's recent tweets have been saved to 'elon_tweets.csv'")

if __name__ == "__main__":
    main()
