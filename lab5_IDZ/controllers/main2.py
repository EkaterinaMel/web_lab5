import constants
from app import app
from flask import render_template, request
@app.route('/', methods=['GET'])
def main2():
    shape = ""
    act_id = [-1 for i in constants.actions]
    isClick = False
    html = render_template(
        'main.html',
        a1 = 0,
        b1 = 0,
        a2 = 0,
        b2 = 0,
        shapes = constants.shape,
        act_id = act_id,
        act_list = constants.actions,
        len = len,
        isClick = isClick,
    )
    return html

app.run(debug=True)