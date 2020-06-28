from flask import Flask, render_template, request, escape
from vsearch import search4letters
app = Flask(__name__)


def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')

@app.route('/search4', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = "検索結果"
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results,)

@app.route('/viewlog')
def view_the_log() -> str:
    contents = [] #新しい空のリストを作成
    with open('vsearch.log') as log: #ログファイルを開いてファイルオブジェクトlogに代入
        for line in log: #ファイルオブジェクトlogの各行をループ
            contents.append([]) # 新しい空のリストをcontentsに追加
            for item in line.split('|'): #バーで行を分割し、その結果分割されたリストの各項目を処理
                contents[-1].append(escape(item))  #エスケープしたデータをcontentsの末尾に追加
    titles = ('フォームデータ', 'リモートアドレス', 'ユーザーエージェント', '結果')
    return render_template('viewlog.html',
    the_title='ログの閲覧',
    the_row_titles=titles,
    the_data=contents,)

@app.route('/')
@app.route('/entry')
def entry_page() -> str:
    return render_template('entry.html', the_title='web版のsearch4lettersへようこそ')

if __name__ == '__main__':
    app.run(debug=True)
