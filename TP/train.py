import sqlite3
import os
from random import randint

class Connection:

    def __init__(self, db_file):
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
    

    def execute(self, query):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = self.conn.cursor()
        cur.execute(query)
        names = [description[0] for description in cur.description]
        rows = cur.fetchall()
    
        return rows, names


def write_file(filename, data, header = None):
    with open(filename, "w", encoding = "utf-8") as f:
        if header:
            f.write(header[0])
            for title in header:
                f.write("," + title)
            f.write("\n")
        for elem in data:
            f.write(str(elem[0]))
            for cell in elem:
                f.write(", " + str(cell) )
            f.write("\n")
            
def write_matches(filename, data, header = None):
    with open(filename, "w", encoding = "utf-8") as f:
        if header:
            f.write(header[0])
            for title in header:
                f.write("," + title)
            f.write("\n")
        for elem in data:
            if elem[3] == "2015/2016":
                f.write(str(elem[0]))
                for cell in elem:
                    f.write(", " + str(cell) )
                f.write("\n")



conn = Connection("database.sqlite")
countries, names = conn.execute("SELECT * FROM COUNTRY")
write_file(os.path.join("files", "Countries.csv"),  countries, names)

leagues, names = conn.execute("SELECT * FROM LEAGUE")
write_file(os.path.join("files", "Leagues.csv"), leagues, names)

matches, names = conn.execute("SELECT * FROM MATCH")
write_matches(os.path.join("files", "Matches.csv"), matches, names)


players, names = conn.execute("SELECT * FROM PLAYER")
write_file(os.path.join("files", "Players.csv"), players, names)

players_attr, names = conn.execute("SELECT * FROM PLAYER_ATTRIBUTES")
print(names)
write_file(os.path.join("files", "Player_Attributes.csv"), players_attr, names)

teams, names = conn.execute("SELECT * FROM TEAM")
write_file(os.path.join("files", "Teams.csv"), teams, names)

teams_attr, names = conn.execute("SELECT * FROM TEAM_ATTRIBUTES")
write_file(os.path.join("files", "Team_Attributes.csv"), teams_attr, names)


games, names = conn.execute("SELECT T1.team_long_name as home_team_name, T2.team_long_name as away_team_name,  M.home_team_goal, M.away_team_goal, L.name as league_name From League AS L join Match as M ON L.id =  M.league_id join Team as T1 ON M.home_team_api_id = T1.team_api_id Join Team as T2 On M.away_team_api_id = T2.team_api_id;")

g = [x for x in range(0, len(games))]
write_file(os.path.join("files", "Games.csv"), [games[g1] for g1 in g], names)



