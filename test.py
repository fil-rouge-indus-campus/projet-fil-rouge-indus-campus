from models import *

class File_recup:

    def __init__(self, json_formatted_string):
        dico = json.loads(json_formatted_string)
        self.msg_type = dico["Msg type"]
        self.msg_id = dico["Msg ID"]
        self.machine_name = dico["Machine name"]
        self.game_type = dico["Game type"]
        self.winner = dico["Winner"]
        self.day_date = datetime.datetime.strptime(dico["Start time"], "%d/%m/%y %H:%M").date()
        self.game_start = datetime.datetime.strptime(dico["Start time"], "%d/%m/%y %H:%M")
        self.game_end = datetime.datetime.strptime(dico["End time"], "%d/%m/%y %H:%M")
        self.json_formatted_string = json_formatted_string
        self.machine = GameServers.get(GameServers.nom == dico["Machine name"]) # recupère un record simple dans table

    def get_winner(self):
        return self.winner

    def get_day(self):
        return self.day_date

    def get_game_duration(self):
        duration = self.game_end - self.game_start
        return duration.total_seconds()

    def get_machine(self):
        return self.machine


my_analyser = File_recup('{\
                            "Msg type": "STATS",\
                            "Msg ID": 235,\
                            "Machine name": "A",\
                            "Game type" : 1,\
                            "Start time": "26/02/19 12:22",\
                            "End time": "26/02/19 12:24",\
                            "Winner": "player1"\
                        }')
print(my_analyser.get_game_duration())

# METHODE Received Message
mess1, created = ReceivedMessage.get_or_create(message=my_analyser.json_formatted_string, # crée un objet de json
                                               message_ID=my_analyser.msg_id,
                                               machine=my_analyser.machine)


# METHODE Statistiques par Partie :
messtat, created = StatsPerMatch.get_or_create(machine=my_analyser.machine, date_debut=my_analyser.day_date,
                                               duree_jeu=my_analyser.get_game_duration(), gagnant=my_analyser.winner)


# METHODE Statistiques par Jour:
try:
    obj = StatsPerDay.get(StatsPerDay.machine == my_analyser.get_machine(),
                          StatsPerDay.date == my_analyser.get_day())
    obj.nb_partie_jour += 1
    obj.duree_moy_partie_jour += my_analyser.get_game_duration()
    if my_analyser.get_winner() == 'player1':
        obj.nb_fois_gagnant1 += 1
    elif my_analyser.get_winner() == 'player2':
        obj.nb_fois_gagnant2 += 1
    else:
        obj.nb_fois_egalite += 1
    obj.save()

except DoesNotExist:
    if my_analyser.get_winner() == 'player1':
        gagnant_is_player1 = 1
        gagnant_is_player2 = 0
        egalite = 0
    elif my_analyser.get_winner() == 'player2':
        gagnant_is_player1 = 1
        gagnant_is_player2 = 0
        egalite = 0
    else:
        gagnant_is_player1 = 0
        gagnant_is_player2 = 0
        egalite = 1
    StatsPerDay.create(date=my_analyser.get_day(),
                       machine=my_analyser.get_machine(),
                       nb_partie_jour=1,
                       duree_moy_partie_jour=my_analyser.get_game_duration(),
                       nb_fois_gagnant1=gagnant_is_player1,
                       nb_fois_gagnant2=gagnant_is_player2,
                       nb_fois_egalite=egalite)







