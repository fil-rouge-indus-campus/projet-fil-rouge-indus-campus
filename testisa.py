from bottle import route, run, template

@route('/game servers page')
def gameserverspage():
    return '<h1>Page Game Servers<h1>'


@route('/results page')
def results():
    return '<h1>page Last game results<h1>'


@route('/config page')
def config():
    return '<h1>page de config<h1>'


@route('/page/<id>')
def page(id):
    return '<h1> page avec hhhh id !!!' + id + '</h1>'


@route('/article/<id>/<nom>')
def article(id, nom):
    return '<h1> avec id' +id+ 'le nom' + nom + '</h1>'


@route('/')
def isa():
    return template('isa')


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./home/isabelle/Images')


if __name__=='__main__':
    run(debug=True, reloader=True)
