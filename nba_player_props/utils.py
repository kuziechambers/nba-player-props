import json
import os
from datetime import datetime


def data_dump(data_dict: dict, file_name: str):
    """
    :param data_dict:
    :param file_name:
    """
    date = datetime.now().strftime("%m-%d-%Y")
    file_path = f"data/{date}/{file_name}.json"

    try:
        os.mkdir(f"data/{date}")
    except OSError:
        pass

    try:
        os.mkdir(f"data/{date}")
    except OSError:
        pass

    with open(file_path, "w") as json_outfile:
        json.dump(data_dict, json_outfile)


def group_players_by_team(players: list):
    team_names = []
    for player in players:
        if player["team"] not in team_names:
            team_names.append(player["team"])

    team_names.sort()

    teams_data = {}
    for team_name in team_names:
        team_players = []
        for player in players:
            if player["team"] == team_name:
                team_players.append(player)
        teams_data[team_name] = team_players

    return teams_data


def get_team_stats_percentiles(team_stats, top_threshold, bottom_threshold):
    stats_lists = [[], [], [], [], [], [], [], [], [], [], [], [], []]

    for team_name, stats in team_stats.items():
        stats_lists[0].append(stats["rsaFGM"])
        stats_lists[1].append(stats["rsaFGPER"])
        stats_lists[2].append(stats["pntFGM"])
        stats_lists[3].append(stats["pntFGPER"])
        stats_lists[4].append(stats["mrgFGM"])
        stats_lists[5].append(stats["mrgFGPER"])
        stats_lists[6].append(stats["cr3FGM"])
        stats_lists[7].append(stats["cr3FGPER"])
        stats_lists[8].append(stats["ab3FGM"])
        stats_lists[9].append(stats["ab3FGPER"])
        stats_lists[10].append(stats["oppFTARate"])
        stats_lists[11].append(stats["offRebPer"])
        stats_lists[12].append(stats["defRebPer"])

    for stats_list in stats_lists:
        stats_list.sort(reverse=True)

    percentiles = {
        "rsaFGM": {
            "top": stats_lists[0][-bottom_threshold],
            "bottom": stats_lists[0][top_threshold],
        },
        "rsaFGPER": {
            "top": stats_lists[1][-bottom_threshold],
            "bottom": stats_lists[1][top_threshold],
        },
        "pntFGM": {
            "top": stats_lists[2][-bottom_threshold],
            "bottom": stats_lists[2][top_threshold],
        },
        "pntFGPER": {
            "top": stats_lists[3][-bottom_threshold],
            "bottom": stats_lists[3][top_threshold],
        },
        "mrgFGM": {
            "top": stats_lists[4][-bottom_threshold],
            "bottom": stats_lists[4][top_threshold],
        },
        "mrgFGPER": {
            "top": stats_lists[5][-bottom_threshold],
            "bottom": stats_lists[5][top_threshold],
        },
        "cr3FGM": {
            "top": stats_lists[6][-bottom_threshold],
            "bottom": stats_lists[6][top_threshold],
        },
        "cr3FGPER": {
            "top": stats_lists[7][-bottom_threshold],
            "bottom": stats_lists[7][top_threshold],
        },
        "ab3FGM": {
            "top": stats_lists[8][-bottom_threshold],
            "bottom": stats_lists[8][top_threshold],
        },
        "ab3FGPER": {
            "top": stats_lists[9][-bottom_threshold],
            "bottom": stats_lists[9][top_threshold],
        },
        "oppFTARate": {
            "top": stats_lists[10][-bottom_threshold],
            "bottom": stats_lists[10][top_threshold],
        },
        "offRebPer": {
            "bottom": stats_lists[11][-bottom_threshold],
            "top": stats_lists[11][top_threshold],
        },
        "defRebPer": {
            "bottom": stats_lists[12][-bottom_threshold],
            "top": stats_lists[12][top_threshold],
        },
    }

    return percentiles


alt_team_abbrs = [
    {"wrongAbbr": "NO", "rightAbbr": "NOP"},
    {"wrongAbbr": "PHO", "rightAbbr": "PHX"},
    {"wrongAbbr": "GS", "rightAbbr": "GSW"},
    {"wrongAbbr": "SA", "rightAbbr": "SAS"},
    {"wrongAbbr": "UTAH", "rightAbbr": "UTA"},
    {"wrongAbbr": "WSH", "rightAbbr": "WAS"},
    {"wrongAbbr": "NY", "rightAbbr": "NYK"},
]

bad_name_chars = ["III", "II", "-", "`", "'", ".", "Jr", " "]

team_abbrs = {
    "Hawks": "ATL",
    "Nets": "BKN",
    "Celtics": "BOS",
    "Hornets": "CHA",
    "Bulls": "CHI",
    "Cavaliers": "CLE",
    "Mavericks": "DAL",
    "Nuggets": "DEN",
    "Pistons": "DET",
    "Warriors": "GSW",
    "Rockets": "HOU",
    "Pacers": "IND",
    "Clippers": "LAC",
    "Lakers": "LAL",
    "Grizzlies": "MEM",
    "Heat": "MIA",
    "Bucks": "MIL",
    "Timberwolves": "MIN",
    "Pelicans": "NOP",
    "Knicks": "NYK",
    "Thunder": "OKC",
    "Magic": "ORL",
    "76ers": "PHI",
    "Suns": "PHX",
    "Trail Blazers": "POR",
    "Kings": "SAC",
    "Spurs": "SAS",
    "Raptors": "TOR",
    "Jazz": "UTA",
    "Wizards": "WAS",
}


def make_left_align_formatter(df, cols=None):
    if cols is None:
        cols = df.columns[df.dtypes == "object"]

    return {col: f"{{:<{df[col].str.len().max()}s}}".format for col in cols}
