
from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['lab'] == '2':
            font = 'hangshu'
        elif request.form['lab'] == '1':
            font = 'kaishu'
        else:
            font = ''
        text = request.form['text']
        return render_template('index.html', text=text, font=font)
    return render_template('index.html')



if __name__ == '__main__':
    app.debug = True
    app.run()
    
