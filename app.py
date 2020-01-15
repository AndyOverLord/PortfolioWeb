from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_database(data)
        return redirect("/thankyou.html")
    else:
        return 'Something went wrong'

def write_to_database(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        content = data['content']
        file = database.write(f'\n{email},{subject},{content}')