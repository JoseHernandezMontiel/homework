from flask import Flask, redirect, request, render_template, url_for
app = Flask(__name__)



# POST

@app.route('/login', methods=['POST'])
def login():
    
  username = request.form.get('username')
  password = request.form.get('password')

  if username[0].isupper() and any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
    return redirect(url_for('home'))
  else:
    return render_template('login.html', error="Invalid username or password")



# GET

# TEMPLATES
@app.route('/')
def loginFile():
  return render_template('login.html')

@app.route('/home')
def home():
  return render_template('home.html')



if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True, port=8081)