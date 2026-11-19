class Player:
    """One real cricketer in the PSL player list."""


    def __init__(self,player_id, name, role, franchise, credits):
        self.player_id = player_id
        self.name = name
        self.franchise = franchise
        self.role = role             # WK, BAT, AR, or BOWL
        self.credits = credits       # price in the fantasy game


    def __str__(self):
        return f"{self.name}, ({self.franchise}, {self.role}, {self.credits} cr)"


babar      =  Player("P089", "Babar Azam", "Peshawer Zalmi", "BAT", 10.5)
mendis     =  Player("P086", "BKG Mendis", "Peshawer Zalmi", "WK", 8.0)
roy        =  Player("P038", "JJ Roy", "Karachi Kings", "BAT", 9.0)
harper     =  Player("P109", "SB Harper", "Quetta Gladiators", "BAT", 7.5)
shadab     =  Player("P029", "Shadab Khan", "Islamabad United", "AR", 10.5)

for player in [babar, mendis, roy, harper, shadab]:

 print(babar)
    