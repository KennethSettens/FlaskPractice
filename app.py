from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey 

app = Flask(__name__)
app.config['SECRET_KEY'] = "purp"

KEY = "responses"

@app.route('/')
def index():
    return render_template('/home.html', survey=survey)


@app.route('/questions/<int:num>')
def render_question(num):

    responses = session.get(KEY)

    if (responses is None):
        return redirect("/")

    if (len(responses) == len(survey.questions)):
        return redirect("/complete")

    if (len(responses) != num): 
        flash(f"Invalid question id: {num}.")
        return redirect(f"/questions/{len(responses)}")

    question = survey.questions[num]
    return render_template("/question.html", index=num, question=question)


@app.route("/answer", methods=["POST"])
def store_answer():
    answer = request.form["answer"] 
    responses = session[KEY]
    responses.append(answer)
    session[KEY] = responses

    if (len(responses) == len(survey.questions)):
        return redirect("/completed")
    else:
        return redirect(f"/questions/{len(responses)}")


@app.route('/start', methods=["POST"])
def start_survey():
    session[KEY] = []
    return redirect("/questions/0")


@app.route("/completed")
def complete():
    return render_template("/completion.html")