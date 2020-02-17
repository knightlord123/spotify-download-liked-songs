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
        a.send_keys('gargvishu2011@gmail.com')
        b=self.driver.find_element_by_xpath('//*[@id="login-password"]')
        b.click()
        b.send_keys('gargkid2011')
        self.driver.find_element_by_xpath('//*[@id="login-button"]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="main"]/div/div[4]/div[2]/nav/ul/li[3]/div/div/a/div/span').click()
        sleep(2)
       
        self.driver.find_element_by_xpath('//*[@id="main"]/div/div[4]/div[4]/div[1]/div/div[2]/section[1]/div[2]/div/div[1]/div[1]/div/div/div[4]').click()
       

        sleep(2)
        j=self.driver.find_element_by_xpath('//*[@id="main"]/div/div[4]/div[4]/div[1]/div/div[2]/div/div/section/div/div/div[1]/div/header/div[3]/p').text
        
        q=str(j).split(' ')[0]
        print (q)
        


        for i in range(1,50):

           
            song_name=self.driver.find_element_by_xpath('//*[@id="main"]/div/div[4]/div[4]/div[1]/div/div[2]/div/div/section/div/div/div[2]/section/ol/div[' + str(i) + ']/div/li/div[2]/div/div[1]').text
            #song_name=self.driver.find_element_by_css_selector('')
            print (song_name)
            f.write(str(song_name))
            f.write('\n')
        f.close()
        
        k=open("D:\\python\\song name.txt",'r')
        
        for m in k:
            self.driver.get('https://www.y2mate.com/en5')
            search=self.driver.find_element_by_xpath('//*[@id="txt-url"]')
            search.click()
                
            print(m)
            search.send_keys(m)
            self.driver.find_element_by_xpath('//*[@id="btn-submit"]').click()
            sleep(5)
            self.driver.find_element_by_xpath('//*[@id="search-result"]/div[1]/div/div/p/a').click()
            sleep(5)
            #self.driver.find_element_by_xpath('//*[@id="result"]/div[1]/div[2]/ul/li[3]/a').click()
            #sleep(1)
            #self.driver.find_element_by_xpath('//*[@id="result"]/div[1]/div[2]/ul/li[2]/a').click()
            
            mouse.position=(587,702)
            mouse.click(Button.left, 1)
            for p in range(0,5):
                keyboard.press(Key.down)
                keyboard.release(Key.down)
            sleep(2)
            mouse.position=(820,607)
            mouse.click(Button.left, 1)
            sleep(15)
            mouse.position=(461,251)
            mouse.click(Button.left, 1)

            

bot=downloader()
bot.login()
            
            
            
           

            
            
            
                