from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


'''
print("请输入uis用户名") 
usrname = input()
print("请输入uis密码")
password = input()
'''

usrname = ''
password = ''

driver = webdriver.Chrome()
url = "http://ce.fudan.edu.cn"

driver.get(url)
usr = driver.find_element(By.ID,'username')
pwd = driver.find_element(By.ID,'password')
submit = driver.find_element(By.ID,'idcheckloginbtn')

usr.send_keys(usrname)   #填入uis用户名
pwd.send_keys(password)   #填入uis密码



submit.click()
#driver.get("http://ce.fudan.edu.cn/q.aspx?id=9957450&beginTime=2020-04-24%2015:00&endTime=2020-06-20%2023:59&previewTime=2020-03-22%2008:00%20&sqid=b956f4a567ed4ab982a7aede07a4a6da&type=5&stepseq=45ff583eeca240959051a0bf2f11efee&targettype=2&targetcode=869a78ece4374719a3ee006f8661746b&tag=b956f4a567ed4ab982a7aede07a4a6da_5_869a78ece4374719a3ee006f8661746b_2_2019-2020-2-COMP130154_0_9957450&name=2020%E5%B9%B4%E6%98%A5%E5%AD%A3%E5%AD%A6%E6%9C%9F%E7%90%86%E8%AE%BA%E8%AF%BE%E8%AF%84%E6%95%99-%E8%AE%A1%E7%AE%97%E6%9C%BA%E5%8E%9F%E7%90%86")

#driver.get("http://ce.fudan.edu.cn/q.aspx?id=9957450&sqid=b956f4a567ed4ab982a7aede07a4a6da&type=5&stepseq=45ff583eeca240959051a0bf2f11efee&targettype=2&targetcode=869a78ece4374719a3ee006f8661746b&tag=b956f4a567ed4ab982a7aede07a4a6da_5_869a78ece4374719a3ee006f8661746b_2_2019-2020-2-COMP130154_0_9957450&beginTime=2020-04-24%2015:00&endTime=2020-06-14%2023:59&previewTime=2020-03-22%2008:00&name=2020%E5%B9%B4%E6%98%A5%E5%AD%A3%E5%AD%A6%E6%9C%9F%E7%90%86%E8%AE%BA%E8%AF%BE%E8%AF%84%E6%95%99-%E8%AE%A1%E7%AE%97%E6%9C%BA%E5%8E%9F%E7%90%86")
while 1 :
    driver.get("http://ce.fudan.edu.cn/")
    driver.find_element(By.CLASS_NAME,'evaluateMyTask').click()
    time.sleep(1)
    driver.switch_to.frame("iframepage")
    a = driver.find_element(By.CSS_SELECTOR,'#tblQuestion > tbody > tr:nth-child(1) > td.operate > a.mcopen')
    a.click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    # radios = driver.find_elements_by_class_name('jqTransformRadioWrapper')
    # checkboxes = driver.find_elements_by_class_name('jqTransformCheckboxWrapper')
    # cnt = 0
    # for i in reversed(radios):
    #     if i.is_displayed() :
    #         i.click()

    # for i in checkboxes :
    #     if i.is_displayed() :
    #         cnt = cnt + 1
    #         i.click()
    #     if cnt >= 8 : break
    questions = driver.find_elements(By.CLASS_NAME,'formstyle.subject.clearfix.jqtransformdone')
    for q in questions:
        if q.is_displayed():
            radios = q.find_elements(By.CLASS_NAME,"jqTransformRadioWrapper")
            checkboxes = q.find_elements(By.CLASS_NAME,"jqTransformCheckboxWrapper")
        if (len(radios)):
            radios[0].click()
        else:
            checkboxes[0].click()
        # 等待题目充分展开
        time.sleep(0.3)

    text = driver.find_elements(By.TAG_NAME,'textarea')
    for i in text :
        i.send_keys('好')
    try:
        button = driver.find_element(By.ID,'next_button')
        button.click()

        buttons = driver.find_elements(By.TAG_NAME,'button')
        for i in buttons :
            if i.get_attribute('data-id')=='ok' : 
                print('here')
                i.send_keys(Keys.ENTER)
    except:
        pass
    driver.close()
    driver.switch_to.window(driver.window_handles[0])