from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from xpaths import XPaths
import sqlite3



#Xpaths here for now will fix
youtube_url = XPaths.youtube_url
input_search = XPaths.input_search
click_playlist = XPaths.click_playlist
click_song = XPaths.click_song
playing_song = XPaths.playing_song


class youtubeHelper:

    def youtube_homepage(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        #allow elements to be found on dom
        self.driver.get(youtube_url)
    
    def searhing(self,search):
        input_search_bar = WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((By.XPATH, input_search))
        )
        input_search_bar.clear()
        input_search_bar.send_keys(search)
        input_search_bar.submit()
        
    def click_search_bar(self):
        search_bar = WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((By.XPATH,input_search)))
        search_bar.click()
        
    def click_playlist(self):
        playlist_displayed = WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((By.XPATH,click_playlist))
        )
        playlist_displayed.click()
        
    def click_song(self):
        play_song = WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((By.XPATH,playing_song))
        )
        play_song.click()
        time.sleep(50)
        # allow song to play for duration & quit driver

    def validate_search_results(self,expected_outcome):
        search_outcome = WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((By.XPATH,playing_song))
        )
        time.sleep(5) 
        final_outcome = search_outcome.text
        #unable to loop through element so text
        #loop through results & return true if there is text else return false
        for outcome in final_outcome:
            if expected_outcome in outcome:
                return True
            else:
               return False    