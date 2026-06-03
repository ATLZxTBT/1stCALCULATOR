from flask import *
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def ProcessResult():
    Result = ""
    if request.method == "POST":
        Num1 = float(request.form.get("num1"))
        Num2 = float(request.form.get("num2"))
        Operation = request.form.get("OPERATION")
        if Operation == "1":
            Result = Num1 + Num2
        elif Operation == "2":
            Result = Num1 - Num2
        elif Operation == "3":
            Result = Num1 * Num2
        elif Operation == "4":
            Result = Num1 / Num2
        else:
            Result = "Invalid values!"
    return render_template("calculator.html", Result=Result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
