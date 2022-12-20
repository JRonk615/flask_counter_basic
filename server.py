from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = '389342daa3687119287f180abf4ef12e0a08120d2d34840ed0aa0e13aaaea958'

# is the intial home page/ sets the total to 1 when reset

@app.route('/')
def index():
    if 'total' not in session:
        session['total'] = 1
    return render_template('index.html')

#once button is hit it directs to the /counter and increments

@app.route('/counter', methods = ['POST'])
def counter():
    if 'total' not in session:
        session['total'] = 0
    session['total'] += 1
    return redirect('/')

#increments the counter by 2

@app.route('/plus2')
def plus_2():
    if 'total' not in session:
        session['total'] = 0
    session['total'] += 2
    return redirect('/')

#increments counter by certain number

@app.route('/morenums', methods = ['POST'])
def do_more_nums():
    session['total'] += int(request.form['increment'])
    return redirect('/')


#resets current count

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)