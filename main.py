from flask import Flask,redirect,url_for, render_template
app = Flask(__name__)

# @app.route('/')
# def hello_world():
# 	# return render_template('index.html', content = "như đầu bòi quấn rẻ")
# 	return "<h1>lò thị vi sóng</h1>"

# @app.route('/<name>')
# def xxx(name):
# 	if name == 'admin':
# 		return redirect(url_for(''))
# 	return f"<h1> hello {name}!</h1>"

# @app.route('/blog/<int:blog_id>')
# def blog(blog_id):
# 	return f"<h1> blog {blog_id}!</h1>"


@app.route("/")
def hello_world():
	return render_template('index.html')


if __name__ == '__main__':
	app.run()


