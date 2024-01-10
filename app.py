from flask import render_template, request, session, flash, redirect, url_for
from settings import expert_creation_key,app
import json
import models
# def login_required(func):
#     if not "user" in session:
#         flash("Login First", category="error")
#         return redirect(url_for("login"))
#     return func



@app.route('/', methods = ["GET","POST"])
def index():
    if request.method == "POST":
        issue_id = request.form['issue']
        issue_id = int(issue_id)
        return redirect(url_for("troubleshoot",id=issue_id)+"?step=1")
    else:
        solution = models.Solution.query.all()
        issues = []
        for object in solution:
            for issue in object.issues:
                issues.append((object.id,issue.title))
        return render_template('index.html', issues = issues)

@app.route("/signup",methods=['GET','POST'])
def signup():
    if request.method == "POST":
        data = request.form
        name = data['name']
        email = data['email']
        password = data['password']
        key = data['admin_key']

        if key.strip() != expert_creation_key:
            flash("Invalid Admin Key",category="error")
            return redirect(url_for("signup"))

        user = models.Admin(name=name,email=email)
        user.set_password(password)
        models.db.session.add(user)
        models.db.session.commit()
        
        flash("Expert Created Successful","success")
        return redirect(url_for("login"))
        
    else:
        return render_template("signup.html")


@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == "POST":
        data = request.form
        email = data['email']
        password = data['password']
        user = models.Admin.query.filter_by(email = email).first()
        if not user:
            flash("Email does not exist","error")
            return redirect(url_for("user"))
        if user.check_password(password):
            session['user'] = user.id
            flash("Login Successful","success")
            return redirect(url_for("dashboard"))
        else:
            flash("Password is Incorrect","error")
            return redirect(url_for("login"))
    else:
        return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if not "user" in session:
        flash("You are not an expert","error")
        return redirect(url_for("login"))
    context = {}
    user = models.Admin.query.filter_by(id = session['user']).first()
    context['user'] = user
    solutions = models.Solution.query.all()
    context['solutions'] = solutions
    return render_template("dashboard.html",**context)

@app.route("/add-to-knowledge-base",methods=['GET','POST'])
def add_knowledge():
    if not "user" in session:
        flash("You are not an expert","error")
        return redirect(url_for("login"))
    if request.method == "POST":
        solution_name = request.form['solution_name']
        issues = request.form.getlist("issues")
        steps = request.form.getlist("steps")
        step_order = request.form.getlist('order')
        solution = models.Solution(name = solution_name)
        solution.save()
        for issue in issues:
            iss = models.Issue(title=issue)
            iss.save()
            solution.issues.append(iss)
        models.minor_save()
        for step,order in zip(steps,step_order):
            st = models.Step(step = step,order = order, solutions = solution)
            st.save()
        flash("Knowledge Added to Knowledge Base")
        return redirect(url_for("dashboard"))
    else:
        return render_template("add-to-base.html")

#Helper Function
def create_knowledge(data):
    for object in data:
        issues = [models.Issue(title=title).save() for title in object["issues"]]
        solution = models.Solution(name=object['name'])
        solution.save()
        for issue in issues:
            solution.issues.append(issue)
        models.minor_save()
        for id,step in enumerate(object['solutions']):
            models.Step(step = step, order = id + 1, solutions = solution).save()



@app.route("/add-from-file",methods=['GET','POST'])
def add_from_file():
    if not "user" in session:
        flash("You are not an expert","error")
        return redirect(url_for("login"))
    if request.method == "POST":
        file = request.files['file']
        # print()
        
        data = json.loads(file.read())
        create_knowledge(data['data'])
        flash("Knowledge Base Updated Successfully",category="success")
        return redirect(url_for("dashboard"))
    else:
        return render_template("add-from-file.html")
            
    

@app.route("/troubleshoot/<id>")
def troubleshoot(id):
    solution = models.db.get_or_404(models.Solution,int(id))
    steps = list(solution.steps)
    steps.sort(key=lambda x: x.order)
    step_number = request.args.get('step')
    if step_number and step_number.isnumeric():
        print("Yes")
        step_number = int(step_number)
        if step_number >= len(steps):
            return render_template("troubleshoot.html",solution=solution,steps = steps, step_number = len(steps), last=True)
        steps = steps[:step_number]
        return render_template("troubleshoot.html",solution = solution, steps = steps, step_number = step_number,last=False)
    else:
        return render_template("troubleshoot.html",solution=solution,steps = steps, step_number = len(steps), last=True)

@app.route("/solution/<id>/delete",methods=["POST"])
def delete_solution(id):
    solution = models.db.get_or_404(models.Solution,int(id))
    models.db.session.delete(solution)
    models.db.session.commit()
    flash("Solution Deleted Successfully",category="success")
    return redirect(url_for("dashboard"))

@app.route("/logout")
def logout():
    if "user" in session:
        del session['user']
        flash("User Logged Out Successfully", category="success")
        return redirect(url_for("login"))
    else:
        flash("User is not logged in",category="error")
        return redirect(url_for("login"))






# if __name__ == '__main__':
#     app.run(debug=True)
