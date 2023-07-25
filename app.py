from flask import Flask,render_template,redirect,request,url_for,jsonify
from flask_mail import Mail, Message
import configparser
import smtplib
from flask_sqlalchemy import SQLAlchemy
from chatgpt2 import faissbot2
from flask_ngrok import run_with_ngrok
from pyngrok import ngrok

app=Flask(__name__)
run_with_ngrok(app=app)
config = configparser.ConfigParser()
config.read('config.txt')
mail_password = config.get('EMAIL', 'MAIL_PASSWORD')


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587  # or the port number used by your SMTP server
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'mrpolymathematica@gmail.com'
app.config['MAIL_PASSWORD'] = mail_password

mail = Mail(app)

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///email.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db=SQLAlchemy(app)


class news_letter(db.Model):
    sno= db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String,nullable=False)
    description=db.Column(db.String,nullable=False)
    piler=db.Column(db.String,nullable=True)
    bootcamp=db.Column(db.String,nullable=True)

    def __repr__(self)-> str:
        return f"{self.sno}-{self.email}"
    




@app.route("/", methods=["GET","POST","DELETE","PUT","PATCH"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")
        

        msg = Message('Contact Form Submission', sender=email, recipients=['mrpolymathematica@gmail.com'])
        msg.body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
        mail.send(msg)
        try:
            mail.send(msg)
            print("THANK YOU FOR FORM SUBMISSION")
            return redirect("/")
        except Exception as e:
            return f"An error occurred while sending the email: {str(e)}"
        
    

    return render_template("index.html")

@app.route('/newsletter', methods=["POST","GET"])
def newsletter():
    if request.method=="POST":
        description=request.form.get("description")
        email = request.form.get("email")
        piler = request.form.get("piler")
        bootcamp = request.form.get("bootcamp")

        alldata = news_letter(description=description,email=email,piler=piler,bootcamp=bootcamp)
        db.session.add(alldata)
        db.session.commit()
        return redirect("/")
    return render_template("newsletter.html")

@app.route('/chatbot',methods=["GET","POST"])
def openChat():
    if request.method == 'POST':
        user_input = request.form['user_input']
        # Call your chatbot function to get the chatbot's response
        # Replace `get_chatbot_response` with your actual chatbot function
        chatbot_response = faissbot2(user_input)
        return jsonify({'response': chatbot_response})
    return render_template('chatbot.html')

# def get_chatbot_response(user_input):
#     # Replace this with your chatbot logic to generate the chatbot response
#     # For example, you can use if-else statements or a machine learning model
#     # to generate responses based on the user input
#     return "Chatbot: I received your message: " + user_input


if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run()
    # app.run()