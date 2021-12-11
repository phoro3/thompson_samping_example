from bottle import route, run, template, request, redirect, static_file
from TsAgent import TsAgent

banner_num = 3
agent = TsAgent(banner_num)

@route('/')
def index():
    expectations = agent.get_expectation()
    sd = agent.get_sd()
    selected_banner_num = agent.get_arm()

    data_dic = {
        'expected_ctr_a': expectations[0],
        'expected_ctr_b': expectations[1],
        'expected_ctr_c': expectations[2],
        'sd_a': sd[0],
        'sd_b': sd[1],
        'sd_c': sd[2],
        'selected_banner_num': selected_banner_num,
    }
    return template('index', **data_dic)

@route('/selected', method='POST')
def selected():
    selected_banner = int(request.forms.get('selected_banner_num'))
    agent.sample(selected_banner, 1)
    redirect('/')


@route('/not_selected', method='POST')
def selected():
    selected_banner = int(request.forms.get('selected_banner_num'))
    agent.sample(selected_banner, 0)
    redirect('/')

@route('/reset', method='POST')
def reset():
    global agent 
    agent = TsAgent(banner_num)
    redirect('/')

@route('/index.css')
def css():
    return static_file('index.css', root='./static')


run(host='localhost', port=8080)