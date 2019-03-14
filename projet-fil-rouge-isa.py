from bottle import route, run, template
from models import GameServers


@route('/gameservers')
def gameservers():
    return template('page_game_servers', Serveurs_info=GameServers.select())


if __name__=='__main__':
    run(debug=True, reloader=True)


