from selenium import webdriver
from time import sleep
import pynput.mouse as ms
from pynput.mouse import Button
from pynput.mouse import Button
from pynput.keyboard import Key, Controller

keyboard = Controller()
mouse=ms.Controller()

class downloader():
    def __init__(self):
       # self.driver=webdriver.Chrome("D:/python/chromedriver.exe")
       chrome_options = webdriver.ChromeOptions()
       chrome_options.add_argument("--disable-notifications")
       self.driver = webdriver.Chrome("D:/python/chromedriver.exe",chrome_options=chrome_options)
        
    def login(self):
        #a=input("ENTER EMAIL-----")
        #b=input("ENTER YOUR PASSWORD----")
        b=("D:\\python\\song name.txt")  #path of file
        f= open(b,"w+")
        

        self.driver.get('https://accounts.spotify.com/en/login?continue=https:%2F%2Fopen.spotify.com%2F')
        sleep(1)
        a=self.driver.find_element_by_xpath('//*[@id="login-username"]')
        a.click()
        a.send_keys('email')
        b=self.driver.find_element_by_xpath('//*[@id="login-password"]')
        b.click()
        b.send_keys('pswd')
        self.driver.find_element_by_xpath('//*[@id="login-button"]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="main"]/div/div[4]/div[2]/nav/ul/li[3]/div/div/a/div/span').click()
        sleep(1.5)
       
        self.driver.find_element_by_xpath('//*[@id="main"]/div/div[4]/div[4]/div[1]/div/div[2]/section[1]/div[2]/div[1]/div[1]/div/div/div[4]').click()
       

        sleep(2)
        j=self.driver.find_element_by_xpath('//*[@id="main"]/div/div[4]/div[4]/div[1]/div/div[2]/div/div/section/div/div/div[1]/div/header/div[3]/p').text
        
        k=str(j).split(' ')[0]
        print (k)
        


        for i in range(1,50):

           
            song_name=self.driver.find_element_by_xpath('//*[@id="main"]/div/div[4]/div[4]/div[1]/div/div[2]/div/div/section/div/div/div[2]/section/ol/div[' + str(i) + ']/div/li/div[2]/div/div[1]').text
            #song_name=self.driver.find_element_by_css_selector('')
            print (song_name)
            f.write(str(song_name))
            f.write('\n')
        f.close()
        self.driver.get('https://www.mp3juices.site/')
        search=self.driver.find_element_by_xpath('//*[@id="query"]')
        search.click()
        k=open("D:\\python\\song name.txt",'r')
        
        for m in k:
            self.driver.get('https://www.mp3juices.site/')
            search=self.driver.find_element_by_xpath('//*[@id="query"]')
            search.click()
                
            print(m)
            search.send_keys(m)
            self.driver.find_element_by_xpath('/html/body/div[2]/div/center/form/div/span/button').click()
            sleep(2)
            self.driver.find_element_by_xpath('//*[@id="items"]/li[1]/div/div/div[2]/div[3]/div/a').click()
            sleep(2)
            self.driver.find_element_by_xpath('//*[@id="download_button_show"]').click()
            sleep(30)
            
            mouse.position=(454,663)
            mouse.click(Button.left, 1)
           

            sleep(2)
            keyboard.press(Key.ctrl)
            keyboard.press(Key.tab)
            keyboard.release(Key.ctrl)
            keyboard.release(Key.tab)
            
            
                







        
            










bot=downloader()
bot.login()
