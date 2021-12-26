from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cervical_traction', methods=['GET', 'POST'])
def cervical_traction():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('cervical_traction.html')


@app.route('/lumbar_traction', methods=['GET', 'POST'])
def lumbar_traction():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('lumbar_traction.html')


@app.route('/documentation', methods=['GET', 'POST'])
def documentation():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('documentation.html')


@app.route('/emergency', methods=['GET', 'POST'])
def emergency():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('emergency.html')


@app.route('/medical_card', methods=['GET', 'POST'])
def medical_card():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('medical_card.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
