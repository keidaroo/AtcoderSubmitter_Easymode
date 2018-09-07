from bottle import post, request, run,get

problemID=""
contestID=""

@post('/')
def problemPost():
    global contestID,problemID
    req=request.params;
    contestID=req.contestID
    problemID=req.problemID
    print(contestID+" "+problemID)

@get('/')
def ret():
    print(contestID+" "+problemID)
    return contestID+" "+problemID
    

run(host='localhost', port=8080)
