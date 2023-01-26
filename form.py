from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def formFunction():
    if request.method == "POST":
        first_name = request.form.get('fname')
        last_name = request.form.get('lname')
        return  "Your Name is " + first_name + last_name
    return render_template('form.html')



if __name__ == '__main__':
    app.run(debug=True)