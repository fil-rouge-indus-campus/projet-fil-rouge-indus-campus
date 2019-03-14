from models import *

# fonction pour retourner une liste de tous les serveurs connus:
# doit retourner une liste de serveurs.
# parametres : adress_ip, nom

    # def __init__(self, nom, adress_ip):
    #     self.nom = nom
    #     self.adress_ip = adress_ip

    # def __str__(self):
    #     return
# try:
#     with mysql_db.atomic():
#         return GameServers.create(adress_ip=adress_ip, nom=nom, jeu_installe=jeu_installe)
# except peewee.IntegrityError:
#     return GameServers.get(GameServers.adress_ip==adress_ip, GameServers.nom==nom, GameServers.jeu_installe==jeu_installe)


# serv1 = GameServers.create(adress_ip='10.10.57', nom="A", jeu_installe="puissance4")
# serv2 = GameServers.create(adress_ip='10.10.89', nom="B", jeu_installe="morpion")
# serv1, created = GameServers.get_or_create(adress_ip='10.10.02', nom="serv1", jeu_installe="puissance4")
# serv2, created = GameServers.get_or_create(adress_ip='10.10.03', nom="serv2", jeu_installe="morpion")
# print(created)
#
#
# mess1, created = ReceivedMessage.get_or_create(message='ff', message_ID="01", machine=serv1)
# print(created)
#
#
# my_date = datetime.datetime.strptime("26/02/19 12:22", "%d/%m/%y %H:%M")
# messtat, created = StatsPerMatch.get_or_create(machine=serv1, date_debut=my_date, duree_jeu="30", gagnant="player1")
# print(created)
#
# ma_date = datetime.datetime.strptime("26/02/19", "%d/%m/%y").date()
# messperday, created = StatsPerDay.get_or_create(
#     date=ma_date, machine=serv1, nb_partie_jour="2",
#     duree_moy_partie_jour="200", nb_fois_gagnant1="2",
#     nb_fois_gagnant2="3", nb_fois_egalite="1"
#     )
# print(created)


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
mess1, created = ReceivedMessage.get_or_create(message=my_analyser.json_formatted_string, # crée un objet de json
                                               message_ID=my_analyser.msg_id,
                                               machine=my_analyser.machine)

messtat, created = StatsPerMatch.get_or_create(machine=my_analyser.machine, date_debut=my_analyser.day_date,
                                               duree_jeu=my_analyser.get_game_duration(), gagnant=my_analyser.winner)

messperday, created = StatsPerDay.get_or_create(
                                                date=my_analyser.day_date, machine=my_analyser.machine,
                                                nb_partie_jour="2",
                                                duree_moy_partie_jour="200", nb_fois_gagnant1="2",
                                                nb_fois_gagnant2="3", nb_fois_egalite="1"
                                                )


# StatsPerDay.get(StatsPerDay.machine==machine_A, StatsPerDay.day==date_of_game)



