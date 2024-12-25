from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from concurrent.futures import ThreadPoolExecutor
from time import sleep
from datetime import datetime
import discord_notifier

DIFFERENT = 5

def concurrent_run_bots(brower_count, first_team_array, second_team_array, pre_game_total_array, match_date_time_array):
    # Set the number of browsers you want to start
    num_browsers = brower_count

    # Set the path to your ChromeDriver executable

    # Create a list to store the browser instances
    browsers = []

    # Start the browsers
    for _ in range(num_browsers):

        # Set up browser instance
        browser = webdriver.Chrome()
        browser.maximize_window()

        # Append the browser instance to the list
        browsers.append(browser)


    def perform_task(browser, first_team_name, second_team_name, pre_game_total, match_date_time):
        # Example task: Open a webpage in each browser
        print("The bot runs at " + match_date_time)

        date_object = datetime.strptime(match_date_time, "%Y-%m-%d %H:%M")
        match_date = date_object.strftime("%Y-%m-%d %H:%M")

        while True:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
            # print(current_time)
            if current_time == match_date:
                # Execute your code here
                print("Running...")
                sleep(300)
                break  # Exit the loop after executing the code

            sleep(10)

        browser.get('https://www.sofascore.com/basketball')
        print(first_team_name, second_team_name, pre_game_total)
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label=\"Consent\"]"))).click()

        temp_total = 0
        while(True):
            sleep(3)
            browser.refresh()
            live_button = WebDriverWait(browser, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"sc-772fdc7b-0 leDECH\"]")))
            live_button.click()
            sleep(2)
            match_elements = browser.find_elements(By.CSS_SELECTOR, "div[class=\"sc-fqkvVR byYarT\"]")
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
                        show_more_button = browser.find_element(By.CSS_SELECTOR, "div[class=\"sc-fqkvVR blTHYz\"]")
                        show_more_button.click()

                        sleep(2)
                        
                        while(True):
                            # game_total = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[class=\"sc-jEACwC eUfCzl\"]"))).text
                            game_total_elements = browser.find_elements(By.CSS_SELECTOR, "span[class=\"sc-jEACwC eUfCzl\"]")
                            if len(game_total_elements) == 1:
                                game_total = game_total_elements[0].text
                                game_total = float(game_total)
                                pre_game_total = float(pre_game_total)
                                if temp_total != game_total:
                                    temp_total = game_total
                                    different_value = abs(game_total - pre_game_total)

                                    if different_value >= DIFFERENT:
                                        print("Changed!")
                                        curr_time = datetime.now().strftime("%Y-%m-%d %H:%M")
                                        discord_notifier.notify_to_discord_channel(first_team_name, second_team_name, different_value, browser.current_url, 
                                                                                   curr_time, pre_game_total, game_total, DIFFERENT)
                            else:
                                break
                except:
                    # sleep(30)
                    pass


    # Create a thread pool executor with the number of desired workers
    with ThreadPoolExecutor(max_workers=num_browsers) as executor:
        # Submit the tasks to the executor
        executor.map(perform_task, browsers, first_team_array, second_team_array, pre_game_total_array, match_date_time_array)

    # Close all browsers
    for browser in browsers:
        browser.quit()

# concurrent_run_bots(2, ["aaa", "sss"], ["dfger", "werwe"], ["werwer", "gfhfgh"])