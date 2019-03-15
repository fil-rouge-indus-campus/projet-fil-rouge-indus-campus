from peewee import *
import datetime
import os
import json
mysql_db = MySQLDatabase('fil_rouge', user='equipeDavid', password='equipeDavid07210.', host='10.1.0.126')
mysql_db.connect()


class GameServers(Model):
    adress_ip = CharField(unique=True)
    nom = CharField(unique=True)
    jeu_installe = CharField(max_length=50)

    class Meta:
        database = mysql_db

    @classmethod
    def lister_serveur(cls):
        return cls.select()


class ReceivedMessage(Model):
    message = CharField(max_length=2000)
    message_ID = IntegerField()
    date_arrivee = DateTimeField(default=datetime.datetime.now)
    machine = ForeignKeyField(GameServers, backref='ReceivedMessage')

    class Meta:
        database = mysql_db


class StatsPerMatch(Model):
    machine = ForeignKeyField(GameServers, backref='StatsPerMatch')
    date_debut = DateTimeField()
    duree_jeu = IntegerField()
    gagnant = CharField()

    class Meta:
        database = mysql_db


class StatsPerDay(Model):
    date = DateField()
    machine = ForeignKeyField(GameServers, backref='StatsPerDay')
    nb_partie_jour = IntegerField()
    duree_moy_partie_jour = IntegerField()
    nb_fois_gagnant1 = IntegerField()
    nb_fois_gagnant2 = IntegerField()
    nb_fois_egalite = IntegerField()

    class Meta:
        database = mysql_db


mysql_db.create_tables([GameServers, ReceivedMessage, StatsPerMatch, StatsPerDay])

























