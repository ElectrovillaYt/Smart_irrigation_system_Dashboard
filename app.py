from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

temperature_data = 0
moisture_data = 0
humidity_data = 0

@app.route('/moisture_data', methods=['POST'])
def receive_moisture():
    if request.method=='POST':
     global moisture_data
     data = request.form
     moisture_data = float(data['data'])
     return 'Data received successfully!'
    
@app.route('/temperature_data', methods=['POST'])
def receive_temperature():
    if request.method=='POST':
     global temperature_data
     data = request.form
     temperature_data = float(data['data'])
     return 'Data received successfully!'
    
@app.route('/humidity_data', methods=['POST'])
def receive_humidity():
    if request.method=='POST':
     global humidity_data
     data = request.form
     humidity_data = float(data['data'])
     return 'Data received successfully!'

@app.route('/')

def display_web():
    global temperature_data
    global moisture_data
    global humidity_data

    return render_template('index.html', moisture_data = moisture_data, temperature_data_C = temperature_data, humidity_data = humidity_data)

def get_data():
    global temperature_data
    global moisture_data
    global humidity_data

    if moisture_data is not None:
        return moisture_data
   
    if temperature_data is not None:
        return temperature_data
    
    if humidity_data is not None:
        return humidity_data
    
@app.route("/about")
def about_page():
   return render_template('about.html')

# if __name__ == '__main__':
#     app.run()
