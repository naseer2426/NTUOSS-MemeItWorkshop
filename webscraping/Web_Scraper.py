from selenium import webdriver
import wget
subreddits_file = open("subreddits.txt","r")
subreddits = subreddits_file.read().split('\n')
print(subreddits)
image_path = "./images"
total_images = 0
driver = webdriver.Chrome()

for j in subreddits:
    driver.get("https://www.reddit.com/r/"+j+"/")
    images = driver.find_elements_by_tag_name('img')
    attributes = []
    file_names = []
    total_images+=len(images)
    for i in images:
        curr_source =i.get_attribute("src")
        attributes.append(curr_source)
        try:
            file_names.append(wget.download(curr_source,image_path))
        except:
            pass
        print()

driver.close()
print("total images scraped",total_images)