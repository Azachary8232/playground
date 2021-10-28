from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Next page please'

@app.route('/play')
def box_3():
    return render_template('index.html')

@app.route('/play/<int:num>')
def box_x(num):
    return render_template('index.html', num=num)

@app.route('/play/<int:num>/<string:color>')
def box_x_color(num, color):
    return render_template('index.html', num=num, color=color)

if __name__=="__main__":
    app.run(debug=True)