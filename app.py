from flask import Flask, render_template, request
from scanner import scan_target
import json

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    results = []
    target = ""
    error = ""

    if request.method == "POST":

        target = request.form.get("target", "").strip()

        if not target:
            error = "Please enter a target."

        else:

            try:

                results = scan_target(target)

                with open("report.json", "w") as file:
                    json.dump(results, file, indent=4)

            except Exception as e:

                error = str(e)

    return render_template(
        "index.html",
        results=results,
        target=target,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)