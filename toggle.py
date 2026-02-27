import RPi.GPIO as GPIO
from flask import Flask, render_template_string

app = Flask(__name__)

LED = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

html = '''
<html>
<body>
<h1>LED Control</h1>
<a href="/toggle"><button>Toggle LED</button></a>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(html)

@app.route('/toggle')
def toggle():
    current = GPIO.input(LED)
    GPIO.output(LED, not current)
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='192.168.7.215', port=5000)
