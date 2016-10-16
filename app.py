from flask import Flask,render_template ,redirect , url_for
from flask_wtf import Form
from wtforms.fields import RadioField , SubmitField

app = Flask(__name__)
app.config['SECRET_KEY']='secret!'
questions = ['Is it compiled?','Does it run on a VM?']
guesses = ['Python','Java','C++']


class YesNoQuestionForm(Form): # predefined python form as a replacement of manually created html form
	answer = RadioField('Your answer', choices=[('yes','Yes'),('no','No')]) # yes is input field and Yes is label which is displayed on screen
	submit =SubmitField('Submit')


@app.route('/') # @ is a decorator and app.route maps the funtion with the server
def index():
	return render_template('index.html') #to pickup html file


@app.route('/question/<int:id>' , methods=['GET', 'POST']) # if browser sends the request it is get and if user sends it is get
def question(id):
	form = YesNoQuestionForm()
	if form.validate_on_submit(): # a predefined function which returns true if data is valid
		if form.answer.data == 'yes':
			return redirect(url_for('question',id=id+1)) # to redirect to the given page
		else:
			return redirect(url_for('question',id=id))
	return render_template('question.html', question=questions[id] , form=form)


@app.route('/guess/<int:id>') #id is the argument passed my user used to extract the element from the list named guesses
def guess(id):
	return render_template('guess.html',guess=guesses[id])


if __name__ == '__main__': # to run the file as main
	app.run(host='0.0.0.0', port=80000, debug=True)
