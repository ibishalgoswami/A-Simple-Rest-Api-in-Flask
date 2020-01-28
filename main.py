from flask import Flask,jsonify,request

app = Flask(__name__)

languages=[{'name':'Python','Version':3.5},{'name':'JS','Version':'ES9'}]

@app.route('/',methods=['GET'])
def test():
    return jsonify({'Message':'It works'})

@app.route('/lang',methods=['GET'])
def test1():
    return jsonify({'lang':languages})

@app.route('/lang/<string:name>',methods=['GET'])
def getallthelang(name):
    lang=[languages for languages in languages if languages['name']==name]
    return jsonify({'languages':lang})

@app.route('/lang',methods=['POST'])
def add():
    language={'name':request.json['name'],'Version':request.json['Version']}
    languages.append(language)
    return jsonify({'languages':languages})

@app.route('/lang/<string:name>',methods=['PUT'])
def modify(name):
    lang=[languages for languages in languages if languages['name']==name]
    lang[0]['name']=request.json['name']
    return jsonify({'languages':lang[0]})

@app.route('/lang/<string:name>',methods=['DELETE'])
def delete(name):
    lang=[languages for languages in languages if languages['name']==name]
    languages.remove(lang[0])
    return jsonify({'languages':languages})


app.run(debug=True)