from flask import Flask
from multiprocessing import Process
import makeProcess
import sendEndmessage

app = Flask(__name__)

@app.route('/start/<pid>')
def start_recording(pid):
    makeProcess.run(pid)
    print("main.py_pid : " + pid)
    return 'Recording started'

@app.route('/end/<pid>')
def stop_recording(pid):
    sendEndmessage.run(pid)
    return 'Recording stopped'

if __name__ == '__main__':
    # MQTT 대신 Flask 웹 서버 시작
    app.run(host='0.0.0.0', port=8000, threaded=True, debug=True)
