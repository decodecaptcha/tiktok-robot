from sanic import Sanic, json
from functions import get_datetime, sum_x_y, auto_sign

app = Sanic("CodeToAPI")
HOST = "localhost"
PORT = 7777

@app.route("/getdatetime")
async def getdatetime(request):
    return json({"now": get_datetime()})

@app.get('/sumxy')
async def sumxy(request):
    parameters = request.args
    result = sum_x_y(int(parameters['x'][0]), int(parameters['y'][0]))
    return json({'result': result})

# @app.post('/sumxy')
# async def sumxy(request):
#     parameters = request.json
#     print(parameters)
#     result = sum_x_y(int(parameters['x']), int(parameters['y']))
#     return json({'result': result})

# host = '192.168.11.195'
# port = 5555
# http://localhost:7777/wework/autosign?ip=192.168.11.195&port=5555&token=123456
@app.get('/wework/autosign')
async def autosign(request):
    parameters = request.args
    result = auto_sign(str(parameters['ip'][0]), int(parameters['port'][0]), str(parameters['token'][0]))
    return json({'result': result})


if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=False)


# 浏览器访问 http://localhost:7777/getdatetime
# 返回 {"now":"2022-08-25 14:44:58"}

# 浏览器访问 http://localhost:7777/sumxy?x=1&y=2
# 返回 {"result":3}

