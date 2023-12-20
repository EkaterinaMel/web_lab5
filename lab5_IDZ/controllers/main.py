import constants
from app import app
from flask import render_template, request
@app.route('/main', methods=['GET'])
def main():
    a_sum = 0
    b_sum = 0
    a_prod = 0
    b_prod = 0
    a_quot = 0
    b_quot = 0
    shape = ""
    act_id = [-1 for i in constants.actions]
    isClick = True
    a1 = int(request.values.get('a1'))
    b1 = int(request.values.get('b1'))
    a2 = int(request.values.get('a2'))
    b2 = int(request.values.get('b2'))
    shape = request.values.get('shape')
    acts = request.values.getlist('act[]')
    if shape == "a":
        for i in range(len(acts)):
            act_id[int(acts[i])]=int(acts[i])
            if acts[i] == "0" :
                a_prod = a1*a2 - b1*b2
                b_prod = a1*b2 + a2*b1
            elif acts[i] == "1" :
                a_sum = a1 + a2
                b_sum = b1 + b2
            else :
                a_quot = (a1*a2 + b1*b2) / (a2^2 + b2^2)
                b_quot = (a2*b1 - a1*b2) / (a2^2 + b2^2)
    else :
        for i in range(len(acts)):
            act_id[int(acts[i])]=int(acts[i])
            if acts[i] == "0" :
                a_prod = a1 * a2
                b_prod = b1 + b2
            elif acts[i] == "1" :
                a_sum = a1 + a2
                b_sum = b1 + b2
            else :
                a_quot = a1 / a2
                b_quot = b1 - b2

    html = render_template(
        'main.html',
        a1 = a1,
        b1 = b1,
        a2 = a2,
        b2 = b2,
        shape = shape,
        shapes = constants.shape,
        act_id = act_id,
        act_list = constants.actions,
        len = len,
        isClick = isClick,
        a_sum = a_sum,
        b_sum = b_sum,
        a_prod = a_prod,
        b_prod = b_prod,
        a_quot = a_quot,
        b_quot = b_quot
    )
    return html

#app.run(debug=True)