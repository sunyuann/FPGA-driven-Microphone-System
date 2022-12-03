from flask import Flask, render_template, url_for, request

from generator import generator
from tone import frequency
from filter import filter_func
from play import playAudio

app = Flask(__name__)

 

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/generator',methods=['POST', 'GET'])
def wav_convert():
    ret = request.form.to_dict()
    print(ret)
    src = ret["src"]
    dst = ret["dst"]
    generator(str(src), str(dst))
    
    return render_template('index.html', converted = 1)

@app.route('/audio_filter',methods=['POST', 'GET'])
def filter_frequecy():
    ret = request.form.to_dict()
    print(ret)
    src = ret["src"]
    low = ret["low"]
    high = ret["high"]
    filter_func(str(src), int(low), int(high))
    
    return render_template('index.html', low = low, high = high)
    

@app.route('/pitch',methods=['POST', 'GET'])
def change_pitch():
    ret = request.form.to_dict()
    print(ret)
    src = ret["src"]
    pitch = ret["pitch"]
    frequency(str(src), int(pitch))
    
    return render_template('index.html', pitch = pitch)
    

@app.route('/play',methods=['POST', 'GET'])
def play_audio():
    ret = request.form.to_dict()
    #print(ret)
    playAudio()
    
    return render_template('index.html', status = 1)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
    #port=8000