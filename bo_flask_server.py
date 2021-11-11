from flask import Flask, render_template, request
from datetime import datetime

from waitress import serve
app = Flask(__name__)


@app.route("/")
def index():
    homepage = "<h1>林柏君Python測試網頁</h1>"
    homepage += "<a href=/aboutbo>aboutme</a><br>"
    homepage += "<a href=/mis>MIS</a><br>"
    homepage += "<a href=/current>開啟網頁及顯示日期時間</a><br>"
    homepage += "<a href=/welcome?nick=tcyang>開啟網頁及傳送使用者暱稱</a><br>"
    homepage += "<a href=/hi>計算總拜訪次數</a><br>"
    homepage += "<a href=/login>透過表單輸入名字傳值</a><br>"
    return homepage

@app.route("/aboutme")
def aboutme():
   return render_template("aboutbo.html")

@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>"

@app.route("/current")
def current():
    tz = timezone(timedelta(hours=+8))
    now = datetime.now(tz)
    return render_template("current.html", datetime = str(now))

@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    user = request.values.get("nick")
    return render_template("welcome.html", name=user)


@app.route("/hi")
def hi():
    # 載入原始檔案
    f = open("count.txt", "r")
    count = int(f.read())
    f.close()

    # 計數加1
    count += 1

    # 覆寫檔案
    f = open("count.txt", "w")
    f.write(str(count))
    f.close()
    return "本網站總拜訪人次：" + str(count)

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return "您輸入的名字為：" + user 
    else:
        return render_template("login.html")



if __name__ == "__main__":

   	#app.run()
	serve(app, host='0.0.0.0', port=8081)
