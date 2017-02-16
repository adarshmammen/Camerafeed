from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

def get_frame():
	frames = open('stream.jpg','r')
	ret =  frames.read()
	frames.close()
	return ret

@app.route('/')
def index():
    return render_template('index.html')

def gen():
	while True:
	    frame = get_frame()
	    yield (b'--frame\r\n'
	           b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=33507)