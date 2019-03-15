from bottle import route, run, template
from models import StatsPerDay, StatsPerMatch


# page stats par jour
@route('/page_stats_day/<nom_machine>')
def page_stats_day(nom_machine):
    return template('page_stat_par_jour', nom=nom_machine, stats=StatsPerDay.select().order_by())


# page affichage de la dernière partie jouée
@route('/page_last_game')
def page_last_game():
    last_result = StatsPerMatch.select().order_by(StatsPerMatch.date_debut.desc())[0]
    return template('page_last_game', last_game=last_result)


if __name__ == '__main__':
    run(debug=True, reloader=True)

