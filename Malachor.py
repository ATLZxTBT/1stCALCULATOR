from flask import *

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def SIS():
    print("\033[33;2m--~~==| Investing Simulator |==~~--\033[0m\n")
    Result = 0
    if request.method == "POST":
        MainValue = float(request.form.get("MV"))
        Taxes = float(request.form.get("MT"))
        Time = float(request.form.get("Months"))

        Result = MainValue * (1 + Taxes / 100) ** Time

    return render_template("Malachor.html", Result=f"{Result:.2f}")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
