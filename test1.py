from selenium import webdriver

drive = webdriver.Chrome()

drive.get('http://www.baidu.com')

ele = drive.find_element_by_id('kw')

ele.send_keys('湖北工业大学')

drive.find_element_by_id('su').click()