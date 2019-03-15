from bottle import run, route, template
from models import StatsPerMatch


@route('/choucrout')
def index():
    return '<h1>WoooooooooooW</h1>'


@route('/test/<oui>/<nom>')
def test(oui, nom):
    return '<h1> ceci est la page test numéro ' + oui + ' qui appartient a ' + nom + '</h1>'


@route('/lastresult')
def lastresult():
    last_result = StatsPerMatch.select().order_by(StatsPerMatch.date_debut.desc())[0]
    return template('lastresulteuu', game=last_result)


@route('/index')
def index_robin():
    return template('index_robin', name='Robin', Stats_list=StatsPerMatch.select())


if __name__ == '__main__':
    run(debug=True, reloader=True)
