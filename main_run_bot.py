from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from time import sleep
import mongo_db
from datetime import datetime, timedelta
import live_bots


def run():
    closest_match_date = mongo_db.get_nearest_date()
    # print("Starts at " + closest_match_date)

    date = datetime.strptime(closest_match_date, "%Y-%m-%d %H:%M")

    # Add one hour to the datetime object
    new_date = date + timedelta(hours=-1)

    # Format the new date as a string
    start_time = new_date.strftime("%Y-%m-%d %H:%M")

    print("Starts at " + start_time)  # Output: 2019-04-05 05:05

    while True:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        # print(current_time)
        if current_time == start_time:
            # Execute your code here
            print("Running...")
            break  # Exit the loop after executing the code

        sleep(10)


    first_team_name_array, second_team_name_array, pre_game_total_array, match_date_time_array = mongo_db.get_all_match_data()

    bot_count = len(first_team_name_array)


    # bot_count = 4
    # first_team_name_array = ["Hornets", "Pacers", "76ers", "Nets"]
    # second_team_name_array = ["Wizards", "Jazz", "Celtics", "Clippers"]
    # pre_game_total_array = ["232", "235", "222", "230"]

    live_bots.concurrent_run_bots(bot_count, first_team_name_array, second_team_name_array, pre_game_total_array, match_date_time_array)
    return True
