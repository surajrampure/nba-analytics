def getValue(s):
    s = s[:-1]
    pointing_right = s.rfind(">")
    pointing_left = s.rfind("<")
    return s[pointing_right+1:pointing_left]

def year_results(soup):

    disect = soup.find_all("tr")

    eastern_conference = [None]        # Pushes a None to the front so seeds match positions
    western_conference = [None]
    for i in range (2, 17):
        team_data = disect[i]
        temp_dict = {
            "name": getValue(str(team_data.contents[0].find_all('a')[0])),
            "seed": i-1,
            "wins": int(getValue(str(team_data.contents[1]))),
            "losses": int(getValue(str(team_data.contents[2]))),
            "win_percentage": float(getValue(str(team_data.contents[3]))),
            "games_behind": 0 if i == 2 else float(getValue(str(team_data.contents[4]))),
            "points_per_game": float(getValue(str(team_data.contents[5]))),
            "opp_points_per_game": float(getValue(str(team_data.contents[6]))),
            "srs": float(getValue(str(team_data.contents[7])))
        }
        eastern_conference.append(temp_dict)

    for i in range (18, 33):
        team_data = disect[i]
        temp_dict = {
            "name": getValue(str(team_data.contents[0].find_all('a')[0])),
            "seed": i-17,
            "wins": int(getValue(str(team_data.contents[1]))),
            "losses": int(getValue(str(team_data.contents[2]))),
            "win_percentage": float(getValue(str(team_data.contents[3]))),
            "games_behind": 0 if i == 18 else float(getValue(str(team_data.contents[4]))),
            "points_per_game": float(getValue(str(team_data.contents[5]))),
            "opp_points_per_game": float(getValue(str(team_data.contents[6]))),
            "srs": float(getValue(str(team_data.contents[7])))
        }
        western_conference.append(temp_dict)

    year_mapping = {'east': eastern_conference, 'west': western_conference}
    return year_mapping


def find_team(data, year, desired):
    for team in data[year]['east'][1:]:
        if team['name'].lower() == desired.lower():
            return team
    for team in data[year]['west'][1:]:
        if team['name'].lower() == desired.lower():
            return team
    return "No such team"



