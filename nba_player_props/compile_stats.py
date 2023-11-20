import pandas as pd
import bcolors
from utils import make_left_align_formatter

from constants import attributes, fields_dict


def is_team_bad_scoring_field(
    percentiles,
    team_stats,
    team_name,
    players_dict,
    opposing_team_name,
    attribute,
    print_color,
):
    percent_key = fields_dict[attribute]["percent"]
    makes_key = fields_dict[attribute]["makes"]
    attempts_key = fields_dict[attribute]["attempts"]
    attribute_name = fields_dict[attribute]["name"]

    if (
        team_stats[percent_key] >= percentiles[percent_key]["bottom"]
        and team_stats[makes_key] >= percentiles[makes_key]["bottom"]
    ):
        players_team = players_dict[opposing_team_name]
        names = []
        percents = []
        attempts = []
        points = []
        pts_rebs_asts = []
        pts_rebs = []
        blanks = []

        for player in players_team:
            if (
                percent_key in player.keys()
                and attempts_key in player.keys()
                and "points" in player.keys()
            ):
                if (
                    player[percent_key] >= fields_dict[attribute]["playerPercentile"]
                    and player[attempts_key] >= 1.7
                ):
                    names.append(player["name"])
                    percents.append(f"{player[percent_key]}%")
                    attempts.append(player[attempts_key])
                    points.append(player["points"])
                    pts_rebs_asts.append(player["ptsRebsAsts"])
                    pts_rebs.append(player["ptsRebs"])
                    blanks.append("")
        if len(names) != 0:
            print(
                f"{print_color}{team_name}{bcolors.ENDC} | {attribute_name}: {bcolors.ERR}BAD{bcolors.ENDC}"
            )
            df = pd.DataFrame(
                {
                    "    ": names,
                    " ": blanks,
                    "FG%": percents,
                    "": blanks,
                    "FGA": attempts,
                    "  ": blanks,
                    "Points": points,
                    "PtsRebsAsts": pts_rebs_asts,
                    "PtsRebs": pts_rebs,
                }
            )
            df.sort_values(by="FGA", axis=0)

            print(
                f"{bcolors.ITALIC}{df.to_string(formatters=make_left_align_formatter(df), index=False, justify='left')}{bcolors.ENDC}"
            )
            print()


def is_team_good_scoring_field(
    percentiles,
    team_stats,
    team_name,
    players_dict,
    opposing_team_name,
    attribute,
    print_color,
):
    percent_key = fields_dict[attribute]["percent"]
    makes_key = fields_dict[attribute]["makes"]
    attempts_key = fields_dict[attribute]["attempts"]
    attribute_name = fields_dict[attribute]["name"]

    if (
        team_stats[percent_key] <= percentiles[percent_key]["top"]
        and team_stats[makes_key] <= percentiles[makes_key]["top"]
    ):
        players_team = players_dict[opposing_team_name]
        names = []
        percents = []
        attempts = []
        points = []
        pts_rebs_asts = []
        pts_rebs = []
        blanks = []

        for player in players_team:
            if (
                percent_key in player.keys()
                and attempts_key in player.keys()
                and "points" in player.keys()
            ):
                if (
                    player[percent_key] >= fields_dict[attribute]["playerPercentile"]
                    and player[attempts_key] >= 2.2
                ):
                    names.append(player["name"])
                    percents.append(f"{player[percent_key]}%")
                    attempts.append(player[attempts_key])
                    points.append(player["points"])
                    pts_rebs_asts.append(player["ptsRebsAsts"])
                    pts_rebs.append(player["ptsRebs"])
                    blanks.append("")

        if len(names) != 0:
            print(
                f"{print_color}{team_name}{bcolors.ENDC} | {attribute_name}: {bcolors.OK}GOOD{bcolors.ENDC}"
            )
            df = pd.DataFrame(
                {
                    "    ": names,
                    " ": blanks,
                    "FG%": percents,
                    "": blanks,
                    "FGA": attempts,
                    "  ": blanks,
                    "Points": points,
                    "PtsRebsAsts": pts_rebs_asts,
                    "PtsRebs": pts_rebs,
                }
            )
            df.sort_values(by="FGA", axis=0)

            print(
                f"{bcolors.ITALIC}{df.to_string(formatters=make_left_align_formatter(df), index=False, justify='left')}{bcolors.ENDC}"
            )
            print()


def is_team_bad_free_throws(
    percentiles, team_stats, team_name, players_dict, opposing_team_name, print_color
):
    if team_stats["oppFTARate"] >= percentiles["oppFTARate"]["bottom"]:
        players_team = players_dict[opposing_team_name]
        names = []
        percents = []
        attempts = []
        points = []
        pts_rebs_asts = []
        pts_rebs = []
        blanks = []

        for player in players_team:
            if "freeThrowAtts" in player.keys() and "freeThrowPercent" in player.keys():
                if (
                    player["freeThrowAtts"] >= 3.0
                    and player["freeThrowPercent"] >= 70.0
                ):
                    names.append(player["name"])
                    percents.append(f"{player['freeThrowPercent']}%")
                    attempts.append(player["freeThrowAtts"])
                    points.append(player["points"])
                    pts_rebs_asts.append(player["ptsRebsAsts"])
                    pts_rebs.append(player["ptsRebs"])
                    blanks.append("")
        if len(names) != 0:
            print(
                f"{print_color}{team_name}{bcolors.ENDC} | Opp Free Throw Rate: {bcolors.ERR}BAD{bcolors.ENDC}"
            )
            df = pd.DataFrame(
                {
                    "    ": names,
                    " ": blanks,
                    "FT%": percents,
                    "": blanks,
                    "FTA": attempts,
                    "  ": blanks,
                    "Points": points,
                    "PtsRebsAsts": pts_rebs_asts,
                    "PtsRebs": pts_rebs,
                }
            )
            df.sort_values(by="FTA", axis=0)

            print(
                f"{bcolors.ITALIC}{df.to_string(formatters=make_left_align_formatter(df), index=False, justify='left')}{bcolors.ENDC}"
            )
            print()


def is_team_good_free_throws(
    percentiles, team_stats, team_name, players_dict, opposing_team_name, print_color
):
    if team_stats["oppFTARate"] <= percentiles["oppFTARate"]["top"]:
        players_team = players_dict[opposing_team_name]
        names = []
        percents = []
        attempts = []
        points = []
        pts_rebs_asts = []
        pts_rebs = []
        blanks = []

        for player in players_team:
            if "freeThrowAtts" in player.keys() and "freeThrowPercent" in player.keys():
                if (
                    player["freeThrowAtts"] >= 5.5
                    and player["freeThrowPercent"] >= 75.0
                ):
                    names.append(player["name"])
                    percents.append(f"{player['freeThrowPercent']}%")
                    attempts.append(player["freeThrowAtts"])
                    points.append(player["points"])
                    pts_rebs_asts.append(player["ptsRebsAsts"])
                    pts_rebs.append(player["ptsRebs"])
                    blanks.append("")
        if len(names) != 0:
            print(
                f"{print_color}{team_name}{bcolors.ENDC} | Opp Free Throw Rate: {bcolors.OK}GOOD{bcolors.ENDC}"
            )
            df = pd.DataFrame(
                {
                    "    ": names,
                    " ": blanks,
                    "FT%": percents,
                    "": blanks,
                    "FTA": attempts,
                    "  ": blanks,
                    "Points": points,
                    "PtsRebsAsts": pts_rebs_asts,
                    "PtsRebs": pts_rebs,
                }
            )
            df.sort_values(by="FTA", axis=0)

            print(
                f"{bcolors.ITALIC}{df.to_string(formatters=make_left_align_formatter(df), index=False, justify='left')}{bcolors.ENDC}"
            )
            print()


def is_team_bad_offensive_rebounding(
    percentiles, team_stats, team_name, players_dict, opposing_team_name, print_color
):
    if team_stats["offRebPer"] <= percentiles["offRebPer"]["bottom"]:
        players_team = players_dict[opposing_team_name]
        names = []
        def_percents = []
        rebounds = []
        pts_rebs_asts = []
        pts_rebs = []
        blanks = []

        for player in players_team:
            if "defRebPer" in player.keys() and "rebounds" in player.keys():
                if player["defRebPer"] >= 17.0:
                    names.append(player["name"])
                    def_percents.append(f"{player['defRebPer']}%")
                    rebounds.append(player["rebounds"])
                    pts_rebs_asts.append(player["ptsRebsAsts"])
                    pts_rebs.append(player["ptsRebs"])
                    blanks.append("")
        if len(names) != 0:
            print(
                f"{print_color}{team_name}{bcolors.ENDC} | Offensive Rebound Rate: {bcolors.ERR}BAD{bcolors.ENDC}"
            )
            df = pd.DataFrame(
                {
                    "    ": names,
                    " ": blanks,
                    "DREB%": def_percents,
                    "  ": blanks,
                    "Rebounds": rebounds,
                    "PtsRebsAsts": pts_rebs_asts,
                    "PtsRebs": pts_rebs,
                }
            )
            df.sort_values(by="DREB%", axis=0)

            print(
                f"{bcolors.ITALIC}{df.to_string(formatters=make_left_align_formatter(df), index=False, justify='left')}{bcolors.ENDC}"
            )
            print()


def is_team_bad_defensive_rebounding(
    percentiles, team_stats, team_name, players_dict, opposing_team_name, print_color
):
    if team_name == "BKN":
        print()
    if team_stats["defRebPer"] <= percentiles["defRebPer"]["bottom"]:
        players_team = players_dict[opposing_team_name]
        names = []
        off_percents = []
        rebounds = []
        pts_rebs_asts = []
        pts_rebs = []
        blanks = []

        for player in players_team:
            if "offRebPer" in player.keys() and "rebounds" in player.keys():
                if player["offRebPer"] >= 3.5:
                    names.append(player["name"])
                    off_percents.append(f"{player['offRebPer']}%")
                    rebounds.append(player["rebounds"])
                    pts_rebs_asts.append(player["ptsRebsAsts"])
                    pts_rebs.append(player["ptsRebs"])
                    blanks.append("")
        if len(names) != 0:
            print(
                f"{print_color}{team_name}{bcolors.ENDC} | Defensive Rebound Rate: {bcolors.ERR}BAD{bcolors.ENDC}"
            )
            df = pd.DataFrame(
                {
                    "    ": names,
                    " ": blanks,
                    "OREB%": off_percents,
                    "  ": blanks,
                    "Rebounds": rebounds,
                    "PtsRebsAsts": pts_rebs_asts,
                    "PtsRebs": pts_rebs,
                }
            )
            df.sort_values(by="OREB%", axis=0)

            print(
                f"{bcolors.ITALIC}{df.to_string(formatters=make_left_align_formatter(df), index=False, justify='left')}{bcolors.ENDC}"
            )
            print()


def is_team_good_offensive_rebounding(
    percentiles, team_stats, team_name, players_dict, opposing_team_name, print_color
):
    if team_stats["offRebPer"] >= percentiles["offRebPer"]["top"]:
        players_team = players_dict[opposing_team_name]
        names = []
        def_percents = []
        rebounds = []
        pts_rebs_asts = []
        pts_rebs = []
        blanks = []

        for player in players_team:
            if "defRebPer" in player.keys() and "rebounds" in player.keys():
                if player["defRebPer"] >= 17.0:
                    names.append(player["name"])
                    def_percents.append(f"{player['defRebPer']}%")
                    rebounds.append(player["rebounds"])
                    pts_rebs_asts.append(player["ptsRebsAsts"])
                    pts_rebs.append(player["ptsRebs"])
                    blanks.append("")
        if len(names) != 0:
            print(
                f"{print_color}{team_name}{bcolors.ENDC} | Offensive Rebound Rate: {bcolors.OK}GOOD{bcolors.ENDC}"
            )
            df = pd.DataFrame(
                {
                    "    ": names,
                    " ": blanks,
                    "DREB%": def_percents,
                    "  ": blanks,
                    "Rebounds": rebounds,
                    "PtsRebsAsts": pts_rebs_asts,
                    "PtsRebs": pts_rebs,
                }
            )
            df.sort_values(by="DREB%", axis=0)

            print(
                f"{bcolors.ITALIC}{df.to_string(formatters=make_left_align_formatter(df), index=False, justify='left')}{bcolors.ENDC}"
            )
            print()


def is_team_good_defensive_rebounding(
    percentiles, team_stats, team_name, players_dict, opposing_team_name, print_color
):
    if team_stats["defRebPer"] >= percentiles["defRebPer"]["top"]:
        players_team = players_dict[opposing_team_name]
        names = []
        off_percents = []
        rebounds = []
        pts_rebs_asts = []
        pts_rebs = []
        blanks = []

        for player in players_team:
            if "offRebPer" in player.keys() and "rebounds" in player.keys():
                if player["offRebPer"] >= 3.5:
                    names.append(player["name"])
                    off_percents.append(f"{player['offRebPer']}%")
                    rebounds.append(player["rebounds"])
                    pts_rebs_asts.append(player["ptsRebsAsts"])
                    pts_rebs.append(player["ptsRebs"])
                    blanks.append("")
        if len(names) != 0:
            print(
                f"{print_color}{team_name}{bcolors.ENDC} | Defensive Rebound Rate: {bcolors.OK}GOOD{bcolors.ENDC}"
            )
            df = pd.DataFrame(
                {
                    "    ": names,
                    " ": blanks,
                    "OREB%": off_percents,
                    "  ": blanks,
                    "Rebounds": rebounds,
                    "PtsRebsAsts": pts_rebs_asts,
                    "PtsRebs": pts_rebs,
                }
            )
            df.sort_values(by="OREB%", axis=0)

            print(
                f"{bcolors.ITALIC}{df.to_string(formatters=make_left_align_formatter(df), index=False, justify='left')}{bcolors.ENDC}"
            )
            print()


def process_matchup(matchup, teams_stats, players_by_team_stats, percentiles):
    home_team = matchup[0]
    away_team = matchup[1]
    print(
        f"{bcolors.BOLD}{bcolors.HEADER}------------------{bcolors.ENDC}{bcolors.ENDC}"
    )
    print(
        f"{bcolors.BOLD}{bcolors.HEADER}|{bcolors.ENDC}  {bcolors.WARN}{home_team}{bcolors.ENDC} VS. {bcolors.BLUE}{away_team}{bcolors.ENDC}{bcolors.ENDC}:  {bcolors.HEADER}|{bcolors.ENDC}"
    )
    print(
        f"{bcolors.BOLD}{bcolors.HEADER}------------------{bcolors.ENDC}{bcolors.ENDC}"
    )

    for team in matchup:
        if team == matchup[0]:
            team_name = matchup[0]
            opposing_team_name = matchup[1]
            print_color = bcolors.WARN
        else:
            team_name = matchup[1]
            opposing_team_name = matchup[0]
            print_color = bcolors.BLUE

        team_stats = teams_stats[team_name]

        for attribute in attributes:
            is_team_bad_scoring_field(
                percentiles=percentiles,
                team_stats=team_stats,
                team_name=team_name,
                players_dict=players_by_team_stats,
                opposing_team_name=opposing_team_name,
                attribute=attribute,
                print_color=print_color,
            )
        is_team_bad_free_throws(
            percentiles=percentiles,
            team_stats=team_stats,
            team_name=team_name,
            players_dict=players_by_team_stats,
            opposing_team_name=opposing_team_name,
            print_color=print_color,
        )
        is_team_bad_offensive_rebounding(
            percentiles=percentiles,
            team_stats=team_stats,
            team_name=team_name,
            players_dict=players_by_team_stats,
            opposing_team_name=opposing_team_name,
            print_color=print_color,
        )
        is_team_bad_defensive_rebounding(
            percentiles=percentiles,
            team_stats=team_stats,
            team_name=team_name,
            players_dict=players_by_team_stats,
            opposing_team_name=opposing_team_name,
            print_color=print_color,
        )
        is_team_good_free_throws(
            percentiles=percentiles,
            team_stats=team_stats,
            team_name=team_name,
            players_dict=players_by_team_stats,
            opposing_team_name=opposing_team_name,
            print_color=print_color,
        )
        is_team_good_offensive_rebounding(
            percentiles=percentiles,
            team_stats=team_stats,
            team_name=team_name,
            players_dict=players_by_team_stats,
            opposing_team_name=opposing_team_name,
            print_color=print_color,
        )
        is_team_good_defensive_rebounding(
            percentiles=percentiles,
            team_stats=team_stats,
            team_name=team_name,
            players_dict=players_by_team_stats,
            opposing_team_name=opposing_team_name,
            print_color=print_color,
        )
        for attribute in attributes:
            is_team_good_scoring_field(
                percentiles=percentiles,
                team_stats=team_stats,
                team_name=team_name,
                players_dict=players_by_team_stats,
                opposing_team_name=opposing_team_name,
                attribute=attribute,
                print_color=print_color,
            )
