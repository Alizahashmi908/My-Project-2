class Player:
    """one real cricketer in psl player list ."""

    def __init__(self,player_id, name, role, franchise, credits):
        self.player_id = player_id
        self.name = name
        self.franchise = franchise
        self.role = role             # WK, BAT, AR, or BOWL
        self.credits = credits       # price in the fantasy game
   
    def __str__(self):
            return f"{self.name}, ({self.franchise}, {self.role}, {self.credits} cr)"    

class FantasyTeam :
    """A fantasy XI picked by one person. """

    def  __init__(self, team_name, owner) :
        self.team_name = team_name
        self.owner = owner
        self.players = []
        self.captain = None
        self.vice_captain = None

    
    def add_player(self, player) :
        self.players.append(player) 

    def total_credits(self) :
        total = 0
        for player in self.players :
            total = total + player.credits
        return total


    def count_by_role(self):
        count = {"WK": 0, "BAT": 0, "AR": 0, "BOWL": 0,}
        for player in self.players :
            count[player.role] = count[player.role] + 1
        return count
    
    
    def set_captian(self, captain, vice_captain) :
        self.captain = captain
        self.vice_captain =  vice_captain  
        

    def __str__(self) :
        size = len(self.player)
        cost = self.total_credits()
        return f"{self.team_name} (owner : {self.owner}, {size} players, {cost} cr)"
 

team       =  FantasyTeam   ("Star Fighters", "Aliza")
babar      =  Player("P089", "Babar Azam", "Peshawer Zalmi", "BAT", 10.5)
mendis     =  Player("P086", "BKG Mendis", "Peshawer Zalmi", "WK", 8.0)
roy        =  Player("P038", "JJ Roy", "Karachi Kings", "BAT", 9.0)
harper     =  Player("P109", "SB Harper", "Quetta Gladiators", "BAT", 7.5)
shadab     =  Player("P029", "Shadab Khan", "Islamabad United", "AR", 10.5)
saim       =  Player("P012", "Saim Ayub", "Hydrabad Kingsmen", "AR",  10.5)
ali        =  Player("P043", "M M Ali",  "Karachi Kings","AR",  7.5)
salman     =  Player("P034", "Salman Mirza",  "Islamabad United", "BOWL", 10.5)
ahmad      =  Player("P115", "Ahamad Daniyal", "Quetta Gladiators", "BOWL", 10)
zahid      =  Player("P052", "Zahid Mahmood",  "Karachi Kings", "BOWL",  8.5)
ubaid      =  Player("P069", "Ubaid Shah",  "Lahore Qalandars","BOWL",  7.0)      


for player in [babar, mendis, roy, harper, shadab, saim, ali, salman, ahmad, zahid, ubaid]:
    team.add_player(player)
team.set_captain(babar, shadab)

print(team)
print("Roles:", team.count_by_role())
print("Captain:", team.captain)

   