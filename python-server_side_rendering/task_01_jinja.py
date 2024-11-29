from flask import Flask, render_template

app = Flask(__name__)

# Route  la page d'accueil
@app.route('/')
def home():
    return render_template('index.html')

# Route qui va la page "À propos"
@app.route('/about')
def about():
    return render_template('about.html')

# Route  la page de contact
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
