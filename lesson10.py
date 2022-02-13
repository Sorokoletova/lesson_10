from flask import Flask
from function10 import get_candidates_list, get_candidates_by_id, get_candidates_skill
app = Flask(__name__)


@app.route('/',)
def page_all():
    candidates = get_candidates_list()
    candidates_page = ""
    for candidate in candidates:
        candidates_page += candidate["name"]+"\n"
        candidates_page += candidate["position"]+"\n"
        candidates_page += candidate["skills"]+"\n"
        candidates_page += "\n"
    return "<pre>"+candidates_page+"<pre>"


@app.route('/candidate/<int:number_id>')
def page_number_id(number_id):
    candidates = get_candidates_by_id(number_id)
    candidates_page = ""
    candidates_page += candidates["picture"] + "\n"
    candidates_page += candidates["name"]+"\n"
    candidates_page += candidates["position"]+"\n"
    candidates_page += candidates["skills"]+"\n"
    candidates_page += "\n"
    return "<pre>"+candidates_page+"<pre>"


@app.route('/skill/<skill>')
def page_skill(skill):
    candidates = get_candidates_skill(skill)
    candidates_page = ""
    for candidate in candidates:
        candidates_page += candidate["name"] + "\n"
        candidates_page += candidate["position"] + "\n"
        candidates_page += candidate["skills"] + "\n"
        candidates_page += "\n"

    return "<pre>"+candidates_page+"<pre>"


app.run()
