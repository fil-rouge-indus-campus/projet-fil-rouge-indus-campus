from bottle import route, run, template
from models import StatsPerDay



@route('/page_stats_day/<nom_machine>')
def page_stats_day(nom_machine):
    return template('page_stat_par_jour', nom=nom_machine, stats=StatsPerDay.select())


if __name__ == '__main__':
    run(debug=True, reloader=True)
