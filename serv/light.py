from flask import Flask, send_file
import RPi.GPIO as GPIO

led = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
 
app = Flask('lightControl')
 
 
@app.route('/')
def index():
    return send_file('light.html')
 
 
@app.route('/images/<filename>')
def get_image(filename):
    return send_file('images/' + filename)
 
 
@app.route('/turnOn')
def turnOn():
    GPIO.output(led, GPIO.HIGH)
    return 'turnedOn'
 
 
@app.route('/turnOff')
def turnOff():
    GPIO.output(led, GPIO.LOW)
    return 'turnedOff'
 
try: 
    app.run(port=3000, host='0.0.0.0')
finally:
    GPIO.cleanup()
    print('GPIO cleanup completed.')