from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def my_home():
    return render_template("index.html")

@app.route("/<page>.html")
def page(page):
    full_page = page + ".html"
    return render_template(full_page)

def write_to_file(data):
    try:
        with open("database.txt", mode="a") as my_file:
            my_file.write(data["email"] + "," + data["subject"] + "," + data["message"] + "\n")
    except FileNotFoundError as err:
        print("file not found")
        raise err

def write_to_csv(data):
    try:
        with open("database.csv", mode="a", newline='') as database2:
            email = data["email"]
            subject = data["subject"]
            message = data["message"]
            csv_writer = csv.writer(database2, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([email,subject,message])
    except FileNotFoundError as err:
        print("file not found")
        raise err

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect("thankyou.html")
    else:
        return "something is not right. Try again"