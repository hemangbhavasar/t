from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time
import os
import logging
import configparser

# Generate log file name
logfile = r'update_clockify_profile_{}.log'.format(time.strftime('%Y_%m_%d_%H.%M.%S'))
updateimage = r'update_clockify_profile_{}.png'.format(time.strftime('%Y_%m_%d_%H.%M.%S'))    
logging.basicConfig(filename=logfile, filemode='w', format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',datefmt='%Y-%m-%d:%H:%M:%S',level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.info('Start')

opts=Options()
opts.headless=False

# read config file for parameters
try:
    config=configparser.ConfigParser()
    config.read('config.ini')
    username=config['login']['username']
    password=config['login']['password']
    hours=config['login']['hours']
    
    #userid=config['login']['userid']
        
except Exception as ex:
    logger.error('Error in reading configuration file: {}'.format(ex))

# open browser, login and update clockify hours
try:
    browser=Chrome(options=opts,executable_path=r'chromedriver.exe')
    browser.get('https://clockify.me/login?')
    browser.maximize_window()
    
    logger.info('Open url in chrome')
    time.sleep(5)    
    
    usernameField = browser.find_element_by_id("email")    
    usernameField.send_keys(username)
    logger.info('Enter Email')
    
    passwordField=browser.find_element_by_id('password')
    passwordField.send_keys(password)
    logger.info('Enter Password')

    clickbtn=browser.find_element_by_xpath("/html/body/app-root/register-layout/div/div/div/div/div[2]/login/div/form/div/div/div/div[2]/div[5]/button").click()

    time.sleep(5)
    logger.info('Click login and wait for 5 sec')

    try:
        
        clickbtn=browser.find_element_by_xpath("/html/body/app-root/default-layout/div/aside/sidebar/nav/div[2]/div/div[2]/div/ul/li[2]/a").click()

        time.sleep(2)
        logger.info('Click TIMESHEET and wait for 2 sec')
        
    except Exception as ex:
        logger.error('Error in login and update hr: {}'.format(ex))


    try:
        
        clickbtn=browser.find_element_by_xpath("/html/body/app-root/default-layout/div/main/timesheet2/div/div/div[2]/table/tbody/tr[1]/td[1]/div/div/a/span").click()
        time.sleep(5)
        logger.info('Click Select Task and wait for 5 sec')
    
    except Exception as ex:
        logger.error('Error in login and update hr: {}'.format(ex))


    try:
        #browser.get('https://clockify.me/timesheet')
        clickbtn=browser.find_element_by_xpath("/html/body/app-root/default-layout/div/main/timesheet2/div/div/div[2]/table/tbody/tr[1]/td[1]/div/div/project-picker2/section/section/section/div[2]/div/div[2]/div/div/div/a").click()
        time.sleep(2)
        logger.info('Click to select Gilead Project and wait for 2 sec')
    
    except Exception as ex:
        logger.error('Error in login and update hr: {}'.format(ex))


    try:
        #browser.get('https://clockify.me/timesheet')
        clickbtn=browser.find_element_by_xpath("/html/body/app-root/default-layout/div/main/timesheet2/div/div/div[2]/table/tbody/tr[1]/td[1]/div/div/project-picker2/section/section/section/div[2]/div/div[2]/div/div[2]/div[1]/a").click()
        time.sleep(5)
        logger.info('Click to select Gilead under project and wait for 5 sec')
    
    except Exception as ex:
        logger.error('Error in login and update hr: {}'.format(ex))


#This is now hr's value inserting code
    try:#D1
        clickbtn1=browser.find_element_by_xpath("/html/body/app-root/default-layout/div/main/timesheet2/div/div/div[2]/table/tbody/tr[1]/td[2]/time-duration/input")
        clickbtn1.clear()
        clickbtn1.send_keys(hours)
     
        time.sleep(2)
        logger.info('Click D1 and wait for 2 sec')
    except Exception as ex:
        logger.error('Error in login and update hr: {}'.format(ex))
        

    try:#D2
        clickbtn1=browser.find_element_by_xpath("/html/body/app-root/default-layout/div/main/timesheet2/div/div/div[2]/table/tbody/tr[1]/td[3]/time-duration/input")
        clickbtn1.clear()
        clickbtn1.send_keys(hours)
     
        time.sleep(2)
        logger.info('Click D2 and wait for 2 sec')
    except Exception as ex:
        logger.error('Error in login and update hr: {}'.format(ex))


    try:#D3
        clickbtn1=browser.find_element_by_xpath("/html/body/app-root/default-layout/div/main/timesheet2/div/div/div[2]/table/tbody/tr[1]/td[4]/time-duration/input")
        clickbtn1.clear()
        clickbtn1.send_keys(hours)
     
        time.sleep(2)
        logger.info('Click D3 and wait for 2 sec')
    except Exception as ex:
        logger.error('Error in login and update hr: {}'.format(ex))


    try:#D4
        clickbtn1=browser.find_element_by_xpath("/html/body/app-root/default-layout/div/main/timesheet2/div/div/div[2]/table/tbody/tr[1]/td[5]/time-duration/input")
        clickbtn1.clear()
        clickbtn1.send_keys(hours)
     
        time.sleep(2)
        logger.info('Click D4 and wait for 2 sec')
    except Exception as ex:
        logger.error('Error in login and update hr: {}'.format(ex))


    try:#D5
        clickbtn1=browser.find_element_by_xpath("/html/body/app-root/default-layout/div/main/timesheet2/div/div/div[2]/table/tbody/tr[1]/td[6]/time-duration/input")
        clickbtn1.clear()
        clickbtn1.send_keys(hours)
     
        time.sleep(2)
        logger.info('Click D5 and wait for 8 sec')
        #browser.quit()
    except Exception as ex:
        logger.error('Error in login and update hr: {}'.format(ex))

    try:#D6
        clickbtn1=browser.find_element_by_xpath("/html/body/app-root/default-layout/div/main/timesheet2/div/div/div[2]/table/tbody/tr[1]/td[7]/time-duration/input")
        clickbtn1.clear()
        clickbtn1.send_keys()
     
        time.sleep(5)
        logger.info('Click D6 and wait for 5 sec')
        browser.quit()
    except Exception as ex:
        logger.error('Error in login and update hr: {}'.format(ex))


    '''    
    #clickbtn=browser.find_element_by_xpath("//*[@id='loginWithGoogle']/div[14]/div/button").click()
    #clickbtn=browser.find_element_by_xpath("//*[@class='loginWithGoogle']/div[14]/div/button").click()
    clickbtn=browser.find_element_by_xpath("/html/body/app-root/register-layout/div/div/div/div/div[2]/login/div/form/div/div/div/div[3]/a/span").click()
    #/html/body/app-root/register-layout/div/div/div/div/div[2]/login/div/form/div/div/div/div[3]/a/span
    time.sleep(5)
    logger.info('Click login and wait for 8 sec')

    try:
        browser.get('https://accounts.google.com/signin/oauth/identifier?client_id=800081634217-rbfe00vph9bbuk3cldi3hfemufs7r2bd.apps.googleusercontent.com&as=boEX4eXSe29UvaMkJjLaVw&destination=https%3A%2F%2Fclockify.me&approval_state=!ChRNdDNJZ012S3JUU3BsbXBBeWtLRRIfZ3dwWUVaeFJvamdZOEhuU1JuY2dubW9PMlh4UTd4WQ%E2%88%99AJDr988AAAAAXfI43zzIv4b_RnAPF598wZyZONxGJ420&oauthgdpr=1&xsrfsig=ChkAeAh8T5gWP3cEqPEtqoOZxO97c2k3huMuEg5hcHByb3ZhbF9zdGF0ZRILZGVzdGluYXRpb24SBXNvYWN1Eg9vYXV0aHJpc2t5c2NvcGU&flowName=GeneralOAuthFlow')
        
        usernameField = browser.find_element_by_id("identifierId")
        usernameField.send_keys(username)
        logger.info('Email or phone')

        clickbtn=browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span").click()
        
    except Exception as ex:
        logger.error('Error in login and cv upload: {}'.format(ex))


    
    WORKING FROM HERE
    try:
        browser.get('https://saama.onelogin.com/login2/?return=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1cmkiOiJodHRwczovL3NhYW1hLm9uZWxvZ2luLmNvbS90cnVzdC9zYW1sMi9odHRwLXBvc3Qvc3NvLzkwNDU1ND9zYW1sX3JlcXVlc3RfcGFyYW1zX3Rva2VuPWY5N2ZiNjgwNDIuOThjMWM0OGFjYzA1ZmZkZmUxYjFhODIwOTYzMTJkY2JmMTE0ZWVmYy5ycmdqdG9ZYTBycHFUYnhKdDFBenRXNno4NTJ0SmNyYl9qa01ZVlgxNFdjJTNEIiwibWV0aG9kIjoiZ2V0IiwiZXhwIjoxNTc2MDcxMzIxLCJpc3MiOiJNT05PUkFJTCIsImF1ZCI6IkFDQ0VTUyIsInBhcmFtcyI6e30sInN1YiI6NTAwNTQ3NjN9.x_NMtQeUat1rgE-TVp8vRi017jslFYdLvhpn4hjQxzU#action=dsso_auth')

        usernameField = browser.find_element_by_id("security-code")
        usernameField.send_keys(userid)
        logger.info('password')
    '''


    '''
    try:
        browser.find_element_by_id('attachCV').send_keys(path_to_resume)
        time.sleep(5)
        browser.save_screenshot(updateimage)
        logger.info('Upload cv and wait for 5 sec')
        browser.quit()
    except Exception as ex:
        logger.error('Error in login and cv upload: {}'.format(ex))
     '''       
except Exception as ex:
    print(ex)
    logger.error('Error in update hr- {}'.format(ex))
    browser.quit()
