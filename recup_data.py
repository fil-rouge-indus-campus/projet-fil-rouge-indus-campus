
import datetime as dt
import bottle as bt
import config_model as cm

from bottle import get, route, request, template


@get('/config')
def config():
    return template('config.tpl')


@route('/config', method='POST')
def do_config():
    adresse_ip = request.forms.get('adresse_ip')
    name_server = request.forms.get('name_server')
    game = request.forms.get('game')
    max_player_delay = request.forms.get('Max player delay')
    max_coin_blink_delay = request.forms.get('Max coin blink delay')
    victory_blink_delay = request.forms.get('Victory blink delay')
    level = request.forms.get('level')
    player1_color = request.forms.get('player1_color')
    player2_color = request.forms.get('player2_color')
    (cm.GameServerConfig.get_or_create(adresse_ip=adresse_ip, name_server=name_server,
                                               game=game, max_player_delay=max_player_delay,
                                               max_coin_blink_delay=max_coin_blink_delay,
                                               victory_blink_delay=victory_blink_delay, level=level,
                                       player1_color=player1_color, player2_color=player2_color))
    return "OK"




if __name__ == '__main__':
    bt.run(debug=True, reloader=True)




