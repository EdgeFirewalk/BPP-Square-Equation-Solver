from flask import Flask, render_template, request
import math

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/', methods=['post'])
def form():
    if request.method == 'POST':
        a = int(request.form.get('a'))
        b = int(request.form.get('b'))
        c = int(request.form.get('c'))

        # Если ошибка ввода
        if a == 0 or b == 0 or c == 0:
            return render_template('error.html')

        D = (b*b) - (4 * a * c)

        if D > 0:
            x1 = ((-b) + math.sqrt(D)) / (2 * a)
            x2 = ((-b) - math.sqrt(D)) / (2 * a)
            return render_template('two-roots.html', a=a, b=b, c=c, D=D, x1=x1, x2=x2)

        if D == 0:
            x = (-b) / (2 * a)
            return render_template('one-root.html', a=a, b=b, c=c, D=D, x=x)

        if D < 0:
            return render_template('no-roots.html', a=a, b=b, c=c, D=D)

def run():
    app.run()
