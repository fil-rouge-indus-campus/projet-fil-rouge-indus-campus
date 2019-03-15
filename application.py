from bottle import route, run, template
from models import GameServers
from models import StatsPerDay
from models import StatsPerMatch


@route('/gameservers')
def gameservers():
    return template('page_game_servers.html', Serveurs_info=GameServers.select())


@route('/config')
def config():
    return template('config.tpl')


@route('/page_stats_day/<nom_machine>')
def page_stats_day(nom_machine):
    return template('page_stat_par_jour', nom=nom_machine, stats=StatsPerDay.select())


@route('/spm')
def index_robin():
    return template('index_robin.html', name='Robin', Stats_list=StatsPerMatch.select())


@route('/page_last_game')
def page_last_game():
    last_result = StatsPerMatch.select().order_by(StatsPerMatch.date_debut.desc())[0]
    return template('page_last_game', last_game=last_result)




if __name__=='__main__':
    run(debug=True, reloader=True)
