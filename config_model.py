import peewee as pw
import datetime as dt
import bottle as bt

# Connection de la base avec PEEWEE
db = pw.MySQLDatabase(host='10.1.0.126', user='equipeDavid', password='equipeDavid07210.', database='fil_rouge')


# Création de la table SQL configuration
class GameServerConfig(pw.Model):
    adresse_ip = pw.CharField(max_length=50, unique=True)
    name_server = pw.CharField(max_length=50, unique=True)
    game = pw.CharField(max_length=50)
    max_player_delay = pw.CharField(max_length=50, unique=True)
    max_coin_blink_delay = pw.CharField(max_length=50, unique=True)
    victory_blink_delay = pw.CharField(max_length=50)
    level = pw.CharField()
    heure_modif = pw.DateTimeField(default=dt.datetime.now)
    player1_color = pw.CharField(max_length=50, unique=True)
    player2_color = pw.CharField(max_length=50, unique=True)


    class Meta:
        database = db


db.connect()
db.create_tables([GameServerConfig])
print("table config créer dans la BDD")
db.close()