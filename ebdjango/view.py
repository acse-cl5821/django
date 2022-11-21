from django.http import HttpResponse
from selenium import webdriver
import time

def detail(request):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    # open it, go to a website, and get results
    driver = webdriver.Chrome('chromedriver', options=options)
    driver.get("https://merchant-uk.hungrypanda.co/login")
    btn_username = driver.find_element('id', "phone")  # 定位账号标签
    btn_username.send_keys('7859999838')  # 填充账号
    btn_password = driver.find_element('id', "password")  # 定位密码标签
    btn_password.send_keys('Mql654321')  # 填充密码

    btn_login = driver.find_element('xpath',
                                    "html/body/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form/div[5]/div[1]/div[1]/div[1]/button")
    btn_login.click()  # 点击登录按钮
    time.sleep(1)
    driver.get("https://merchant-uk.hungrypanda.co/order/ordermanage")
    time.sleep(1)
    view_btn = driver.find_element('xpath',
                                   'html/body/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table/tbody/tr[1]/td[6]/a')
    view_btn.click()
    time.sleep(1)
    order = driver.find_element('xpath', 'html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]')
    return HttpResponse(order.text)

def id(request):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    # open it, go to a website, and get results
    driver = webdriver.Chrome('chromedriver', options=options)
    driver.get("https://merchant-uk.hungrypanda.co/login")
    btn_username = driver.find_element('id', "phone")  # 定位账号标签
    btn_username.send_keys('7859999838')  # 填充账号
    btn_password = driver.find_element('id', "password")  # 定位密码标签
    btn_password.send_keys('Mql654321')  # 填充密码

    btn_login = driver.find_element('xpath',
                                    "html/body/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form/div[5]/div[1]/div[1]/div[1]/button")
    btn_login.click()  # 点击登录按钮
    time.sleep(1)
    driver.get("https://merchant-uk.hungrypanda.co/order/ordermanage")
    time.sleep(1)
    view_btn = driver.find_element('xpath',
                                   'html/body/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table/tbody/tr[1]/td[6]/a')
    view_btn.click()
    time.sleep(1)
    order = driver.find_element('xpath', 'html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]')
    return HttpResponse(order.text)

def menu(request):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    # open it, go to a website, and get results
    driver = webdriver.Chrome('chromedriver', options=options)
    driver.get("https://merchant-uk.hungrypanda.co/login")
    btn_username = driver.find_element('id', "phone")  # 定位账号标签
    btn_username.send_keys('7859999838')  # 填充账号
    btn_password = driver.find_element('id', "password")  # 定位密码标签
    btn_password.send_keys('Mql654321')  # 填充密码

    btn_login = driver.find_element('xpath',
                                    "html/body/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form/div[5]/div[1]/div[1]/div[1]/button")
    btn_login.click()  # 点击登录按钮
    time.sleep(1)
    driver.get("https://merchant-uk.hungrypanda.co/order/ordermanage")
    time.sleep(1)
    view_btn = driver.find_element('xpath',
                                   'html/body/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table/tbody/tr[1]/td[6]/a')
    view_btn.click()
    time.sleep(1)
    order = driver.find_element('xpath', 'html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]')
    return HttpResponse(order.text)