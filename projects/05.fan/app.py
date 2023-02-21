#활성화 명령어: source venv/bin/activate
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb+srv://sparta:test@cluster0.1spozhb.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/guestbook", methods=["POST"])
def guestbook_post():
    name_receive = request.form["name_give"]
    comment_receive = request.form["comment_give"]

    doc = {
        'name': name_receive,
        'comment': comment_receive
    }

    db.guestbook.insert_one(doc)
    return jsonify({'msg':'응원 완료!'})

@app.route("/guestbook", methods=["GET"])
def guestbook_get():
    comment_list = list(db.guestbook.find({},{'_id':False}))
    return jsonify({'comments':comment_list})


if __name__ == '__main__':
   app.run('0.0.0.0', port=5001, debug=True)