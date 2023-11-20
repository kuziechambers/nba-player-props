import json
import os
import time
import datetime as dt
from datetime import datetime
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from utils import data_dump, team_abbrs


def scrape_player_shooting_stats(driver):
    driver.get(
        "https://www.nba.com/stats/players/shooting?CF=Restricted%20Area%20FGA*GE*0.1:In%20The%20Paint%20(Non-RA)%20FGA*GE*0.1&DistanceRange=By%20Zone&LastNGames=6&Season=2023-24&SeasonType=Regular%20Season&dir=D&sort=In%20The%20Paint%20(Non-RA)%20FGA"
    )
    driver.implicitly_wait(5)
    print("Close any ads that may appear")
    time.sleep(10)

    try:
        driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        pages_div = driver.find_element(
            By.CLASS_NAME, "Pagination_content__f2at7.Crom_cromSetting__Tqtiq"
        )
        pages_select = Select(pages_div.find_element(By.TAG_NAME, "select"))
        pages_select.select_by_index(0)
        time.sleep(1)
    except NoSuchElementException:
        try:
            pages_div = driver.find_element(
                By.CLASS_NAME, "Pagination_content__f2at7.Crom_cromSetting__Tqtiq"
            )
            pages_select = Select(pages_div.find_element(By.TAG_NAME, "select"))
            pages_select.select_by_index(0)
            time.sleep(1)
        except NoSuchElementException:
            pass

    players_table = driver.find_element(By.CLASS_NAME, "Crom_table__p1iZz")
    players_table_body = players_table.find_element(By.TAG_NAME, "tbody")
    players_table_rows = players_table_body.find_elements(By.TAG_NAME, "tr")

    players = []
    for row in players_table_rows:
        tds = row.find_elements(By.TAG_NAME, "td")

        tds_values = [tds[0].text, tds[1].text]
        for td in tds[2:]:
            if td.text == "-":
                value = 0.0
            else:
                try:
                    value = float(td.text)
                except ValueError:
                    time.sleep(30)
                    value = float(td.text)
            tds_values.append(value)

        players.append(
            {
                "name": tds_values[0],
                "team": tds_values[1],
                "rsaFGM": tds_values[3],
                "rsaFGA": tds_values[4],
                "rsaFGPER": tds_values[5],
                "pntFGM": tds_values[6],
                "pntFGA": tds_values[7],
                "pntFGPER": tds_values[8],
                "mrgFGM": tds_values[9],
                "mrgFGA": tds_values[10],
                "mrgFGPER": tds_values[11],
                "cr3FGM": tds_values[18],
                "cr3FGA": tds_values[19],
                "cr3FGPER": tds_values[20],
                "ab3FGM": tds_values[21],
                "ab3FGA": tds_values[22],
                "ab3FGPER": tds_values[23],
            }
        )

    date = datetime.now().strftime("%m-%d-%Y")
    stats_path = f"data/{date}/player-stats.json"

    if os.path.exists(stats_path) is True:
        with open(stats_path) as json_file:
            player_data = json.load(json_file)
            players_stats = player_data["playerStats"]

            for player in players:
                found = False
                for stats_player in players_stats:
                    if (
                        player["name"] == stats_player["name"]
                        and player["team"] == stats_player["team"]
                    ):
                        found = True
                        stats_player["rsaFGM"] = player["rsaFGM"]
                        stats_player["rsaFGA"] = player["rsaFGA"]
                        stats_player["rsaFGPER"] = player["rsaFGPER"]
                if found is False:
                    players_stats.append(
                        {
                            "name": player["name"],
                            "team": player["team"],
                            "rsaFGM": player["rsaFGM"],
                            "rsaFGA": player["rsaFGA"],
                            "rsaFGPER": player["rsaFGPER"],
                            "pntFGM": player["pntFGM"],
                            "pntFGA": player["pntFGA"],
                            "pntFGPER": player["pntFGPER"],
                            "mrgFGM": player["mrgFGM"],
                            "mrgFGA": player["mrgFGA"],
                            "mrgFGPER": player["mrgFGPER"],
                            "cr3FGM": player["cr3FGM"],
                            "cr3FGA": player["cr3FGA"],
                            "cr3FGPER": player["cr3FGPER"],
                            "ab3FGM": player["ab3FGM"],
                            "ab3FGA": player["ab3FGA"],
                            "ab3FGPER": player["ab3FGPER"],
                        }
                    )
        results = {"playerStats": players_stats}
    else:
        results = {"playerStats": players}

    data_dump(results, "player-stats")

    print("1 OF 7 SCRAPES COMPLETED")
    return results


def scrape_player_general_stats(driver):
    driver.get(
        "https://www.nba.com/stats/players/traditional?CF=FGA*GE*1.5&LastNGames=6&Season=2023-24&SeasonType=Regular%20Season&dir=-1&sort=FGA"
    )
    driver.implicitly_wait(5)

    try:
        driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        pages_div = driver.find_element(
            By.CLASS_NAME, "Pagination_content__f2at7.Crom_cromSetting__Tqtiq"
        )
        pages_select = Select(pages_div.find_element(By.TAG_NAME, "select"))
        pages_select.select_by_index(0)
        time.sleep(1)
    except NoSuchElementException:
        try:
            pages_div = driver.find_element(
                By.CLASS_NAME, "Pagination_content__f2at7.Crom_cromSetting__Tqtiq"
            )
            pages_select = Select(pages_div.find_element(By.TAG_NAME, "select"))
            pages_select.select_by_index(0)
            time.sleep(1)
        except NoSuchElementException:
            pass

    players_table = driver.find_element(By.CLASS_NAME, "Crom_table__p1iZz")
    players_table_body = players_table.find_element(By.TAG_NAME, "tbody")
    players_table_rows = players_table_body.find_elements(By.TAG_NAME, "tr")

    players = []
    for row in players_table_rows:
        tds = row.find_elements(By.TAG_NAME, "td")

        try:
            name = tds[1].text
            team = tds[2].text
            points = float(tds[8].text)
            free_throw_att = float(tds[16].text)
            free_throw_per = float(tds[17].text)
            rebounds = float(tds[20].text)
            assists = float(tds[21].text)
        except ValueError:
            time.sleep(30)
            name = tds[1].text
            team = tds[2].text
            points = float(tds[8].text)
            free_throw_att = float(tds[16].text)
            free_throw_per = float(tds[17].text)
            rebounds = float(tds[20].text)
            assists = float(tds[21].text)

        players.append(
            {
                "name": name,
                "team": team,
                "points": points,
                "rebounds": rebounds,
                "ptsRebsAsts": float(round(points + rebounds + assists, 1)),
                "ptsRebs": float(round(points + rebounds, 1)),
                "freeThrowAtts": free_throw_att,
                "freeThrowPercent": free_throw_per,
            }
        )

    date = datetime.now().strftime("%m-%d-%Y")
    stats_path = f"data/{date}/player-stats.json"

    if os.path.exists(stats_path) is True:
        with open(stats_path) as json_file:
            player_data = json.load(json_file)
            players_stats = player_data["playerStats"]

            for player in players:
                for stats_player in players_stats:
                    if (
                        player["name"] == stats_player["name"]
                        and player["team"] == stats_player["team"]
                    ):
                        stats_player["points"] = player["points"]
                        stats_player["rebounds"] = player["rebounds"]
                        stats_player["ptsRebsAsts"] = player["ptsRebsAsts"]
                        stats_player["ptsRebs"] = player["ptsRebs"]
                        stats_player["freeThrowAtts"] = player["freeThrowAtts"]
                        stats_player["freeThrowPercent"] = player["freeThrowPercent"]
        results = {"playerStats": players_stats}
    else:
        results = {"playerStats": players}

    data_dump(results, "player-stats")

    print("2 OF 7 SCRAPES COMPLETED")
    return results


def scrape_player_rebound_stats(driver):
    date_from = (dt.date.today() - dt.timedelta(11)).strftime("%m/%d/%Y")
    driver.get(
        f"https://www.nba.com/stats/players/advanced?CF=MIN*GE*15:GP*GE*1&DateFrom={date_from}&Season=2023-24&SeasonType=Regular%20Season&dir=-1&sort=OREB_PCT"
    )
    driver.implicitly_wait(5)

    try:
        driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        pages_div = driver.find_element(
            By.CLASS_NAME, "Pagination_content__f2at7.Crom_cromSetting__Tqtiq"
        )
        pages_select = Select(pages_div.find_element(By.TAG_NAME, "select"))
        pages_select.select_by_index(0)
        time.sleep(1)
    except NoSuchElementException:
        try:
            pages_div = driver.find_element(
                By.CLASS_NAME, "Pagination_content__f2at7.Crom_cromSetting__Tqtiq"
            )
            pages_select = Select(pages_div.find_element(By.TAG_NAME, "select"))
            pages_select.select_by_index(0)
            time.sleep(1)
        except NoSuchElementException:
            pass

    players_table = driver.find_element(By.CLASS_NAME, "Crom_table__p1iZz")
    players_table_body = players_table.find_element(By.TAG_NAME, "tbody")
    players_table_rows = players_table_body.find_elements(By.TAG_NAME, "tr")

    players = []
    for row in players_table_rows:
        tds = row.find_elements(By.TAG_NAME, "td")

        try:
            name = tds[1].text
            team = tds[2].text
            off_reb_per = float(tds[14].text)
            def_reb_per = float(tds[15].text)
        except ValueError:
            time.sleep(30)
            name = tds[1].text
            team = tds[2].text
            off_reb_per = float(tds[14].text)
            def_reb_per = float(tds[15].text)

        players.append(
            {
                "name": name,
                "team": team,
                "offRebPer": off_reb_per,
                "defRebPer": def_reb_per,
            }
        )

    date = datetime.now().strftime("%m-%d-%Y")
    stats_path = f"data/{date}/player-stats.json"

    if os.path.exists(stats_path) is True:
        with open(stats_path) as json_file:
            player_data = json.load(json_file)
            players_stats = player_data["playerStats"]

            for player in players:
                for stats_player in players_stats:
                    if (
                        player["name"] == stats_player["name"]
                        and player["team"] == stats_player["team"]
                    ):
                        stats_player["offRebPer"] = player["offRebPer"]
                        stats_player["defRebPer"] = player["defRebPer"]
        results = {"playerStats": players_stats}
    else:
        results = {"playerStats": players}

    data_dump(results, "player-stats")

    print("3 OF 7 SCRAPES COMPLETED")
    return results


def scrape_team_stats(driver):
    driver.get(
        "https://www.nba.com/stats/teams/opponent-shooting?Season=2023-24&SeasonType=Regular+Season&DistanceRange=By+Zone&LastNGames=8"
    )
    driver.implicitly_wait(5)

    teams_table = driver.find_element(By.CLASS_NAME, "Crom_table__p1iZz")
    teams_table_body = teams_table.find_element(By.TAG_NAME, "tbody")
    teams_table_rows = teams_table_body.find_elements(By.TAG_NAME, "tr")

    teams_stats = {}
    for row in teams_table_rows:
        tds = row.find_elements(By.TAG_NAME, "td")

        team_name = tds[0].text
        for mascot, abbr in team_abbrs.items():
            if mascot in team_name:
                team_name = abbr
        teams_stats[team_name] = {
            "rsaFGM": float(tds[1].text),
            "rsaFGPER": float(tds[3].text),
            "pntFGM": float(tds[4].text),
            "pntFGPER": float(tds[6].text),
            "mrgFGM": float(tds[7].text),
            "mrgFGPER": float(tds[9].text),
            "cr3FGM": float(tds[16].text),
            "cr3FGPER": float(tds[18].text),
            "ab3FGM": float(tds[19].text),
            "ab3FGPER": float(tds[21].text),
        }

    data_dump(teams_stats, "team-stats")

    print("4 OF 7 SCRAPES COMPLETED")
    return teams_stats


def scrape_team_reb_stats(driver):
    date_from = (dt.date.today() - dt.timedelta(17)).strftime("%m/%d/%Y")
    driver.get(
        f"https://www.nba.com/stats/teams/advanced?CF=MIN*GE*15&DateFrom={date_from}&Season=2023-24&SeasonType=Regular%20Season&dir=-1&sort=OREB_PCT"
    )
    driver.implicitly_wait(5)

    teams_table = driver.find_element(By.CLASS_NAME, "Crom_table__p1iZz")
    teams_table_body = teams_table.find_element(By.TAG_NAME, "tbody")
    teams_table_rows = teams_table_body.find_elements(By.TAG_NAME, "tr")

    date = datetime.now().strftime("%m-%d-%Y")
    stats_path = f"data/{date}/team-stats.json"
    with open(stats_path) as json_file:
        teams_stats = json.load(json_file)

    for row in teams_table_rows:
        tds = row.find_elements(By.TAG_NAME, "td")

        team_name = tds[1].text
        for mascot, abbr in team_abbrs.items():
            if mascot in team_name:
                team_name = abbr
        teams_stats[team_name]["offRebPer"] = float(tds[12].text)
        teams_stats[team_name]["defRebPer"] = float(tds[13].text)

    data_dump(teams_stats, "team-stats")

    print("5 OF 7 SCRAPES COMPLETED")
    return teams_stats


def scrape_team_free_throw_stats(driver):
    date_from = (dt.date.today() - dt.timedelta(17)).strftime("%m/%d/%Y")
    date_from_split = date_from.split("/")
    day = date_from_split[0]
    month = date_from_split[1]
    year = date_from_split[2]

    driver.get(
        f"https://www.nba.com/stats/teams/four-factors?sort=TEAM_NAME&dir=-1&Season=2023-24&SeasonType=Regular+Season&DateFrom={day}%2F{month}%2F{year}"
    )
    driver.implicitly_wait(5)

    teams_table = driver.find_element(By.CLASS_NAME, "Crom_table__p1iZz")
    teams_table_body = teams_table.find_element(By.TAG_NAME, "tbody")
    teams_table_rows = teams_table_body.find_elements(By.TAG_NAME, "tr")

    date = datetime.now().strftime("%m-%d-%Y")
    stats_path = f"data/{date}/team-stats.json"
    with open(stats_path) as json_file:
        teams_stats = json.load(json_file)

    for row in teams_table_rows:
        try:
            tds = row.find_elements(By.TAG_NAME, "td")

            team_name = tds[1].text
            for mascot, abbr in team_abbrs.items():
                if mascot in team_name:
                    team_name = abbr
            teams_stats[team_name]["oppFTARate"] = round(
                float(100 * float(tds[12].text)), 2
            )
        except ValueError:
            time.sleep(30)
            tds = row.find_elements(By.TAG_NAME, "td")

            team_name = tds[1].text
            for mascot, abbr in team_abbrs.items():
                if mascot in team_name:
                    team_name = abbr
            teams_stats[team_name]["oppFTARate"] = round(
                float(100 * float(tds[12].text)), 2
            )

    data_dump(teams_stats, "team-stats")

    print("6 OF 7 SCRAPES COMPLETED")
    return teams_stats
