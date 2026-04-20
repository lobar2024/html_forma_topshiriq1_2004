from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        ism = request.form.get('ism')
        email = request.form.get('email')
        xabar = request.form.get('xabar')

        if len(ism) > 2 and '@' in email and len(xabar) >= 15:
            res = [ism, email, xabar]
        else:
            res = ["Ma'lumotlar noto'g'ri kiritildi"]

        return render_template('result1.html', res=res)
    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
