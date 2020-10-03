from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def create_user():
    name_from_form = request.form['name']
    dojo_from_form = request.form['dojo']
    favLang_from_form = request.form['favLang']
    comment_from_form = request.form['comment']
    gender_from_form = request.form['gender']
    check_from_form = request.form['check']
    return render_template("show.html", name_on_template=name_from_form, dojo_on_template=dojo_from_form, favLang_on_template=favLang_from_form, comment_on_template=comment_from_form, gender_on_template=gender_from_form, check_on_template=check_from_form)

if __name__ == "__main__":
    app.run(debug=True)