from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
subreddits_file = open("subreddits.txt","r")
subreddits = subreddits_file.read().split('\n')
print(subreddits)

for i in subreddits:
    driver.get("https://www.reddit.com/r/"+i+"/")