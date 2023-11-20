import time

from utils import data_dump, alt_team_abbrs
from selenium.webdriver.common.by import By


def scrape_matchups(driver):
    driver.set_window_size(100, 1000)
    driver.get("https://www.espn.com/nba/schedule")
    driver.implicitly_wait(5)
    time.sleep(5)

    matchup_divs = driver.find_elements(By.CLASS_NAME, "ScheduleTables.mb5")[0]
    matchup_tbody = matchup_divs.find_element(By.TAG_NAME, "tbody")
    matchup_rows = matchup_tbody.find_elements(By.TAG_NAME, "tr")

    matchups = []
    for row in matchup_rows:
        teams = row.find_elements(By.CLASS_NAME, "Table__Team")
        home_team = teams[1].text
        away_team = teams[0].text

        for abbr in alt_team_abbrs:
            if abbr["wrongAbbr"] == home_team:
                home_team = abbr["rightAbbr"]
            if abbr["wrongAbbr"] == away_team:
                away_team = abbr["rightAbbr"]

        matchups.append([home_team, away_team])

    results = {"matchups": matchups}
    data_dump(results, "matchups")

    print("7 OF 7 SCRAPES COMPLETED")
    return results
