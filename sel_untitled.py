from selenium import webdriver
from selenium.webdriver.common.keys import Keys


pswd = ""

driver = webdriver.Firefox()


driver.get("http://www.quora.com/")


email = driver.find_element_by_name('email')


passwd = driver.find_element_by_name("password")



email.send_keys("bot@healthage.tk")
passwd.send_keys(pswd)



login = driver.find_element_by_css_selector("input[value=Login]").click()
#passwd.send_keys(Keys.ENTER)



driver.get("http://www.quora.com/search?q=nokia")



#base_url = driver.current_url


questions = driver.find_elements_by_class_name("question_link")
questions_text = [e.text for e in questions]
questions_href = [ q.get_attribute("href") for q in questions ]


for e in questions_href:
    driver.get(e)
    #----------question information-----------
    #question = driver.find_element_by_css_selector(".inline_editor_value h1")
    question = driver.title
    q_description = driver.find_element_by_css_selector(".inline_editor_value span").text
    q_tags = driver.find_element_by_css_selector(".q_view .name_text")
    no_shared = driver.find_element_by_css_selector(".repost_count_link").text
    comments_count = driver.find_element_by_class_name("view_comments supp").text
    answers_count_text = driver.find_elements_by_css_selector(".answer_header_text h3").text
    #views = driver.find_element_by_css_selector("a span strong")
    #followers = driver.find_element_by_css_selector(".following_count strong")
    followers_text = driver.find_element_by_css_selector('a[href="%s"]' % (e[21:]+'/followers')).text
    views_text = driver.find_element_by_css_selector('a[href="%s"]' %(e[21:]+"/views")).text
    #answer_header = driver.find_element_by_class_name("answer_header row").text
    
    #-----------------answers information---------
    answers_content_list = driver.find_element_by_css_selector(".answer_content")
    answers_users_list = driver.find_element_by_css_selector(".answer_user_wrapper")
    answers_users_href_list = driver.find_element_by_css_selector(".answer_user_wrapper a").get_attribute("href")
    answers_users_list = driver.find_element_by_css_selector(".answer_rating")
    break



