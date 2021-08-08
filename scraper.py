from selenium import webdriver
from selenium.common import exceptions
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome('chromedriver.exe')
browser.get('https://www.walmart.com/ip/Clorox-Disinfecting-Wipes-225-Count-Value-Pack-Crisp-Lemon-and-Fresh-Scent-3-Pack-75-Count-Each/14898365')

element = browser.find_element_by_xpath('//*[@id="customer-reviews-header"]/div[2]/div/div[3]/a[2]/span')
actions = ActionChains(browser)
actions.move_to_element(element).perform()
browser.find_element_by_xpath('//*[@id="customer-reviews-header"]/div[2]/div/div[3]/a[2]/span').click()
browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[5]/div/div[2]/div/div[2]/div/div[2]/select/option[3]').click()

reviews = pd.DataFrame(columns=['Date', 'name', 'title', 'rating', 'description'])
ultimatum = 1
j = 1
while (j <= 702):
    if (ultimatum == 1):
        url = 'https://www.walmart.com/reviews/product/14898365?page=' + str(j) + '&sort=submission-desc'
        browser.get(url)

        dates = browser.find_elements_by_class_name('review-date-submissionTime')
        names = browser.find_elements_by_class_name('review-footer-userNickname')
        ratings_pre = browser.find_elements_by_class_name('seo-avg-rating')
        ratings = ratings_pre[5:]
        review_texts = browser.find_elements_by_class_name('review-text')

        for i in range(20):
            date = dates[i].text
            date_1 = date.split(',')
            date_2 = int(date_1[1][1:])
            if date_2 < 2021:
                ultimatum = 2
                break
            else:
                name = names[i].text
                rating = ratings[i].text
                review_text = review_texts[i].text
                try:
                    link = browser.find_element_by_xpath(
                        '/html/body/div[1]/div/div/div/div[1]/div/div[6]/div[1]/div[' + str(
                            i + 1) + ']/div/div[1]/div/div[1]/div[1]/h3')
                    review_title = link.text
                except:
                    review_title = "N/A"
                reviews.loc[len(reviews)] = [date, name, review_title, rating, review_text]
        j += 1
    else:
        break

reviews.to_csv('output.csv', index=False)