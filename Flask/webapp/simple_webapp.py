from flask import Flask, session

from checker import check_logged_in

app = Flask(__name__)

@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'ログイン中です'

app.secret_key = 'youwillneverguessmysecretkey'

@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'ログアウト中です'


@app.route('/')
def hello() -> str:
    return 'シンプルなwebアプリケーションです'

@app.route('/page1')
@check_logged_in
def page1() -> str:
    return 'ページ1です'

@app.route('/page2')
@check_logged_in
def page2() -> str:
    return 'ページ2'


@app.route('/page3')
@check_logged_in
def page3() -> str:
    return 'ページ3'

if __name__ == '__main__':
    app.run(debug=True)
