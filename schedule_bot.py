from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from time import sleep
import mongo_db
from datetime import datetime, timedelta

def schedule_scraping():

    firefox_profile_directory = 'C:/Users/root/AppData/Roaming/Mozilla/Firefox/Profiles/bcgxfdql.default-release'
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.profile = webdriver.FirefoxProfile(firefox_profile_directory)

    
    

    def select_calender(driv):
        calender_buttons = driv.find_elements(By.CSS_SELECTOR, "span[class=\"sc-jEACwC ZlQdx\"]")
        current_button = driv.find_element(By.CSS_SELECTOR, "span[class=\"sc-jEACwC gdpgVm\"]")
        current_date = current_button.text
        print(current_date)
        calender_buttons[int(current_date) - 1].click()
    while(True):
        driver = webdriver.Firefox(options=firefox_options)
        driver.maximize_window()
        driver.get("https://www.sofascore.com/basketball")
        try:
            while(True):
                # try:
                    sleep(2)
                    pinned_matches_list = WebDriverWait(driver, 9).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[id=\"pinned-list-fade-target\"]")))
                    nba_match_elements = pinned_matches_list.find_elements(By.CSS_SELECTOR, "div[class=\"sc-fqkvVR byYarT\"]")
                    nba_match_elements.pop(0)
                    print(len(nba_match_elements))

                    for match in nba_match_elements:
                        
                        match_date = ""
                        match_time = ""
                        
                        match.click()
                        sleep(2)

                        team_names = driver.find_elements(By.CSS_SELECTOR, "bdi[class=\"sc-jEACwC kmAxvx\"]")
                        first_team_name = team_names[0].text
                        second_team_name = team_names[1].text
                        print(first_team_name + " VS " + second_team_name)

                        try:
                            match_time_raw = driver.find_element(By.CSS_SELECTOR, "span[class=\"sc-jEACwC kqiZtc\"]").text
                            match_date_raw = driver.find_element(By.CSS_SELECTOR, "span[class=\"sc-jEACwC dVEgDy\"]").text
                            print(match_time_raw, match_date_raw)

                            if match_date_raw == "Today":
                                match_date = datetime.now().strftime("%Y-%m-%d")
                                match_time = match_time_raw
                            elif match_date_raw == "Tomorrow":
                                tomorrow = datetime.now() + timedelta(1)
                                match_date = tomorrow.strftime("%Y-%m-%d")
                                match_time = match_time_raw
                            else :
                                match_time = match_date_raw
                                date_object = datetime.datetime.strptime(match_time_raw, "%d/%m/%Y")
                                match_date = date_object.strftime("%Y-%m-%d")

                            show_more_button = driver.find_element(By.CSS_SELECTOR, "div[class=\"sc-fqkvVR blTHYz\"]")
                            show_more_button.click()
                            sleep(2)
                            game_total_score = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[class=\"sc-jEACwC eUfCzl\"]"))).text
                            result = mongo_db.data_save(first_team_name, second_team_name, match_date, match_time, game_total_score)
                            print(result)

                        except:
                            try:
                                match_status = driver.find_element(By.CSS_SELECTOR, "span[class=\"sc-jEACwC bFGOXv\"]").text
                                print(match_status)
                            except:
                                pass
                # except:
                #     pass
                    select_calender(driver)
                    sleep(2)
        except:
            pass
        driver.quit()
        print("Done!")
        sleep(1800)
    # return True
