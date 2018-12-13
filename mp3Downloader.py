from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")

class YoutubeMp3:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='/Users/edwardcox/chromedriver/chromedriver',chrome_options=options)
        self.wait = WebDriverWait(self.driver, 100)
        self.songs_list = open("songs.txt")
        
    def convert_song(self):
        for song in self.songs_list:
            link = self.get_youtubelink(song)
            self.download_mp3(link)

    def get_youtubelink(self,name):
        url_friendly = name.replace(" ","+")
        self.driver.get("https://www.youtube.com/results?search_query=" + url_friendly)
        song_link = self.wait.until(EC.element_to_be_clickable((By.XPATH,'//a[@id="video-title"]'))) #catch element not found error
        video_id = song_link.get_attribute("href")
        return video_id

    def download_mp3(self,link):
        self.driver.get("https://ytmp3.cc")
        try: 
            enter_url = self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="input"]')))
            enter_url.send_keys(link)
            submit_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='submit']")))
            submit_btn.click()
            download = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='download']")))
            download.click()
        except Exception as e:
            print(e)
        
if __name__=="__main__":
    song_convert = YoutubeMp3()
    song_convert.convert_song()

