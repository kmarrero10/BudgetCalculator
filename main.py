from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
	id = db.Column(db.Integer, primary_key=True)

	income = db.Column(db.Integer, default=0)
	item = db.Column(db.String(200))
	cost = db.Column(db.Integer, default=0, nullable=False)
	completed = db.Column(db.Integer, default=0)
	date_created = db.Column(db.DateTime, default=datetime.utcnow)

	def __repr__(self):
		return '<Cost %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def home():
	return render_template("home.html")
# 	if request.method == 'POST':
# 		task_content = request.form['content']
# 		new_task = Todo(content=task_content)

# 		try:
# 			db.session.add(new_task)
# 			db.session.commit()
# 			return redirect('/')

# 		except:
# 			return 'There was an issue adding your task!'

# 	else:
# 		tasks = Todo.query.order_by(Todo.date_created).all()
# 		return render_template("home.html", tasks=tasks)

# @app.route('/delete/<int:id>')
# def delete(id):
# 	task_to_delete = Todo.query.get_or_404(id)

# 	try:
# 		db.session.delete(task_to_delete)
# 		db.session.commit()
# 		return redirect('/')
# 	except:
# 		return 'There was a problem deleting that task'

# @app.route('/update/<int:id>', methods=['GET', 'POST'])
# def update(id):
# 	task = Todo.query.get_or_404(id)


# 	if request.method == 'POST':
# 		task.content = request.form['content']

# 		try:
# 			db.session.commit()
# 			return redirect('/')
# 		except:
# 			return 'There was an issue updating your task!'
# 	else:
# 		return render_template('update.html', task=task)


@app.route("/calculator")
def calculator():
	return render_template("calculator.html")



@app.route("/calculator/add", methods=['POST', 'GET'])
def add_item():

	if request.method == 'POST':
		#item_val = request.form['item']
		cost_val = request.form['cost']
		new_item= Todo(cost=cost_val)

		# try:
		db.session.add(cost_val)
		db.session.commit()
		return redirect('/calculator')



		# except:
		# 	return 'errrrorrrr'



if __name__ == "__main__":
	app.run(debug=True) 


