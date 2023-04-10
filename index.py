from flask import Flask, render_template, request, flash
# from flask_mail import Mail
# from flask.ext.message import Message


app = Flask(__name__)
# mail = Mail(app)


@app.route("/")
def index():

    if request.method == "POST":
    #     name = request.form["name"]
    #     subject = request.form["subject"]
    #     sender_email = request.form["email"]
    #     message = request.form["message"]

    #     subject = "From YDM WEBSITE"
    #     to = "adamabdulrafik@gmail.com"
    #     # template = render_template("index")
    #     template = f"""
    #         You have a Message from: {name},<br>
    #         With Email: {sender_email},<br>
    #         And Subject: {subject},<br>
            
    #         Saying: {message}
    #     """


    #     msg = Message(
    #         subject,
    #         recipients=[to],
    #         html=template,
    #         sender=sender_email
    #     )

    #     mail.send(msg)
        flash("Your Message has been sent Successfully, Thank you for contacting Us", "success")

    return render_template("index.html")
    

if __name__=="__main__":
    app.run(debug=True)