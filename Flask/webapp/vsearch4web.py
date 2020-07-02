from flask import Flask, render_template, request, escape, session
from vsearch import search4letters

from DBcm import UseDatabase, ConnectionError, CredentialsError, SQLError
from checker import check_logged_in
from threading import Thread

app = Flask(__name__)


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'ログイン中です'

@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'ログアウト中です'

app.config['dbconfig'] = {'host': '127.0.0.1',
            'user': 'vsearch',
            'password': 'vsearchpasswd',
            'database': 'vsearchlogDB', }


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':

    @copy_current_request_context
    def log_request(req: 'flask_request', res: str) -> None:
        sleep(15)
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """insert into log
                (phrase, letters, ip, browser_string, results)
                values
                (%s,%s,%s,%s,%s)"""
            cursor.execute(_SQL, (req.form['phrase'],
                                req.form['letters'],
                                req.remote_addr,
                                req.user_agent.browser,
                                res, ))
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = "検索結果"
    results = str(search4letters(phrase, letters))
    try:
        t = Thread(target=log_request, args=(request, results))
        t.start()
    except Exception as err:
        print ('エラーが発生しました:', str(err))
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results,)




@app.route('/viewlog')
@check_logged_in
def view_the_log() -> 'html':
    try:
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """select phrase, letters, ip, browser_string, results from log"""
            cursor.execute(_SQL)
            contents = cursor.fetchall()
        titles = ('フレーズ','検索文字', 'リモートアドレス', 'ユーザーエージェント', '結果')
        return render_template('viewlog.html',
                            the_title='ログの閲覧',
                            the_row_titles=titles,
                            the_data=contents,)
    except ConnectionError as err:
        print('データベースが動作していますか？', str(err))
    except CredentialsError as err:
        print('ユーザーID/パスワード問題。エラー：', str(err))
    except SQLError as err:
        print('何か問題が発生しました。エラー：', str(err))
    except Exception as err:
        print('何か問題が発生しました', str(err))


@app.route('/')
@app.route('/entry')
def entry_page() -> str:
    return render_template('entry.html', the_title='web版のsearch4lettersへようこそ')


app.secret_key = 'youwillneverguessmysecretkey'

if __name__ == '__main__':
    app.run(debug=True)
