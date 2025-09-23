from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('usuarios/login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Validación simple para simular un login exitoso
        if email and password:
            return redirect(url_for('layout/base.html'))

    return render_template('usuarios/login.html')

if __name__ == '__main__':
    app.run(debug=True)