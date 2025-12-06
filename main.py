from flask import Flask, render_template, redirect, request, send_file
from extractor.berlinen import berlinen_Scrap
from extractor.web3 import web3_scrap
from extractor.wwr import wwr_scrap
from extractor.file import save_to_file

app = Flask("Challenge_Scrapper")

db = {}

@app.route("/")
def home():
    return render_template("home.html", name="nico")

@app.route('/search')
def search():
    keyword = request.args.get("keyword")
    if keyword == None or keyword == "":
        return redirect("/")
    # 일자리 검색
    
    if keyword in db:
        jobs = db[keyword]
    else:
        wwr = wwr_scrap(keyword)
        berlinen = berlinen_Scrap(keyword)
        web3 = web3_scrap(keyword)
        # 검색한 일자리 합침
        jobs = wwr + berlinen + web3
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)

@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == "" or keyword == None: 
        return redirect("/")
    if keyword not in db: #키워드 데이터가 DB에 있는지 확인
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword, db[keyword]) #파일을 만들고
    return send_file(f"{keyword}.csv", as_attachment=True) #만든파일을 우리가 지정한 곳으로 보낸다.
app.run("0.0.0.0")