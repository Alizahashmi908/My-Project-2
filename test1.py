class Player:
    # constructor
    def __init__(self,player_id, name, franchise, role, credits):
        self.player_id = player_id
        self.name = name
        self.franchise = franchise
        self.role = role                # WK, BAT, AR, or BOWL
        self.credits = credits          # price in the fantasy game


# object
babar      =  Player("P089", "Babar Azam", "BAT", "Peshawar Zalmi", 10.5)
mendis     =  Player("P086", "BKG Mendis", "WK", "Peshawar Zalmi", 8.0)
roy        =  Player("P038", "JJ Roy", "BAT", "Karachi Kings", 9.0)
harper     =  Player("P109", "SB Harper", "BAT", "Quetta Gladiators", 7.5)
shadab     =  Player("P029", "Shadab Khan", "AR", "Islamabad United", 10.5)
saim       =  Player("P012", "Saim Ayub", "AR", "Hydrabad Kingsmen", 10.5)
ali        =  Player("P043", "M M Ali", "AR", "Karachi Kings", 7.5)
salman     =  Player("P034", "Salman Mirza", "BOWL", "Islamabad United", 10.5)
ahmad      =  Player("P115", "Ahamad Daniyal", "BOWL", "Quetta Gladiators", 10)
zahid      =  Player("P052", "Zahid Mahmood", "BOWL", "Karachi Kings", 8.5)
ubaid      =  Player("P069", "Ubaid Shah", "BOWL", "Lahore Qalandars", 7.0)      
                     