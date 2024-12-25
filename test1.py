from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from time import sleep
import mongo_db
from datetime import datetime
import discord_notifier
# import live_bots

# closest_match_date = mongo_db.get_nearest_date()
# print("The bot runs at " + closest_match_date)

# first_team_name_array, second_team_name_array, pre_game_total_array = mongo_db.get_match_data(closest_match_date)
# print(first_team_name_array, second_team_name_array, pre_game_total_array)
# # sleep(1000)
# while True:
#     current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
#     # print(current_time)
#     if current_time == closest_match_date:
#         # Execute your code here
#         print("Running...")
#         break  # Exit the loop after executing the code

#     sleep(10)

# bot_count = len(first_team_name_array)

# live_bots.concurrent_run_bots(bot_count, first_team_name_array, second_team_name_array, pre_game_total_array)
# def run():
first_team_name = "Magic"
second_team_name = "Hawks"
pre_game_total = 233.5
match_date_time = "2023-11-10 04:30"

DIFFERENT = 5

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.sofascore.com/basketball")

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label=\"Consent\"]"))).click()


temp_total = 0
while(True):
    sleep(3)
    driver.refresh()
    live_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"sc-772fdc7b-0 leDECH\"]")))
    live_button.click()
    print("QQQQQQQQQQQQQQQQQQQQQQ")
    sleep(2)
    match_elements = driver.find_elements(By.CSS_SELECTOR, "div[class=\"sc-fqkvVR byYarT\"]")
    match_count = len(match_elements)
    print(match_count)
    
    for i in range(match_count):
        try:
            team_names = match_elements[i].find_elements(By.CSS_SELECTOR, "bdi[class=\"sc-jEACwC hvfflp\"]")
            first_team_text = team_names[0].text
            second_team_text = team_names[1].text
            if first_team_text == first_team_name and second_team_text == second_team_name:
                print(first_team_text, second_team_text)

            
                match_elements[i].click()
                sleep(5)
                # team_names = driver.find_elements(By.CSS_SELECTOR, "bdi[class=\"sc-jEACwC kmAxvx\"]")
                # first_team_name = team_names[0].text
                # second_team_name = team_names[1].text
                # print(first_team_name + " VS " + second_team_name)
                show_more_button = driver.find_element(By.CSS_SELECTOR, "div[class=\"sc-fqkvVR blTHYz\"]")
                show_more_button.click()

                sleep(2)
                
                while(True):
                    # game_total = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[class=\"sc-jEACwC eUfCzl\"]"))).text
                    game_total_elements = driver.find_elements(By.CSS_SELECTOR, "span[class=\"sc-jEACwC eUfCzl\"]")
                    if len(game_total_elements) == 1:
                        game_total = game_total_elements[0].text
                        game_total = float(game_total)
                        pre_game_total = float(pre_game_total)
                        if temp_total != game_total:
                            temp_total = game_total
                            different_value = abs(game_total - pre_game_total)

                            if different_value >= DIFFERENT:
                                print("Changed!")
                                current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
                                try:
                                    discord_notifier.notify_to_discord_channel(first_team_name, second_team_name, different_value, driver.current_url, 
                                                                            current_time, pre_game_total, game_total, DIFFERENT)
                                except:
                                    print("error")
                    else:
                        break
        except:
            # sleep(30)
            pass


sleep(1000)