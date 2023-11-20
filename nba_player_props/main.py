import json
import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
import bcolors

from nba_player_props.compile_stats import process_matchup
from scrape_stats import (
    scrape_player_shooting_stats,
    scrape_player_general_stats,
    scrape_player_rebound_stats,
    scrape_team_stats,
    scrape_team_reb_stats,
    scrape_team_free_throw_stats,
)
from scrape_matchups import scrape_matchups
from utils import group_players_by_team, get_team_stats_percentiles


def main(scrape_bool: bool):
    if scrape_bool is True:
        driver = webdriver.Chrome()
        driver.set_window_size(1000, 1000)

        driver.get("https://www.nba.com/account/sign-in")
        driver.implicitly_wait(5)
        time.sleep(8)
        driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(
            "kuzie.chambers@gmail.com"
        )
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("Kc24962387103!")
        driver.find_element(By.XPATH, '//*[@id="submit"]').click()

        time.sleep(8)
        scrape_player_shooting_stats(driver)
        scrape_player_general_stats(driver)
        scrape_player_rebound_stats(driver)
        scrape_team_stats(driver)
        scrape_team_reb_stats(driver)
        scrape_team_free_throw_stats(driver)
        scrape_matchups(driver)

        driver.close()

    date = datetime.now().strftime("%m-%d-%Y")
    players_path = f"data/{date}/player-stats.json"
    with open(players_path) as json_file:
        player_data = json.load(json_file)
        player_stats = player_data["playerStats"]

    teams_path = f"data/{date}/team-stats.json"
    with open(teams_path) as json_file:
        team_stats = json.load(json_file)

    matchups_path = f"data/{date}/matchups.json"
    with open(matchups_path) as json_file:
        matchup_data = json.load(json_file)
        matchups = matchup_data["matchups"]

    players_by_team_stats = group_players_by_team(player_stats)
    bottom_threshold = 5
    top_threshold = 5

    percentiles = get_team_stats_percentiles(
        team_stats, bottom_threshold, top_threshold
    )

    print()
    print()
    print(f"{bcolors.BOLD}{bcolors.ERR}RED    ==  TEAM DEFENSE IS BAD{bcolors.ENDC}")
    print(f"{bcolors.BOLD}{bcolors.OK}GREEN  ==  TEAM DEFENSE IS GOOD{bcolors.ENDC}")
    print()
    print()
    for matchup in matchups:
        process_matchup(
            matchup=matchup,
            teams_stats=team_stats,
            players_by_team_stats=players_by_team_stats,
            percentiles=percentiles,
        )
        print()
        print()
        print()
