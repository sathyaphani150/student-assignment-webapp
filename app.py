from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session
)

import requests

from Config import Config


app = Flask(__name__)

app.secret_key = "student_assignment_secret_key"


submit_api_url = Config.SUBMIT_ASSIGNMENT_URL

fetch_summary_url = Config.FETCH_SUMMARY_URL


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        action = request.form.get("action")

        # SUBMIT ASSIGNMENT

        if action == "submit":

            try:

                payload = {

                    "student_name": request.form.get(
                        "student_name"
                    ),

                    "roll_number": int(
                        request.form.get("roll_number")
                    ),

                    "subject": request.form.get(
                        "subject"
                    ),

                    "assignment_link": request.form.get(
                        "assignment_link"
                    )
                }

                response = requests.post(
                    submit_api_url,
                    json=payload
                )

                session["response_message"] = response.json()

            except Exception as error:

                session["response_message"] = {
                    "success": False,
                    "message": str(error)
                }

        # FETCH SUMMARY

        elif action == "fetch_summary":

            try:

                response = requests.get(
                    fetch_summary_url
                )

                session["summary_data"] = response.json()

            except Exception as error:

                session["summary_data"] = {
                    "success": False,
                    "message": str(error)
                }

        return redirect(
            url_for("index")
        )

    response_message = session.pop(
        "response_message",
        None
    )

    summary_data = session.pop(
        "summary_data",
        None
    )

    return render_template(
        "index.html",
        response_message=response_message,
        summary_data=summary_data
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )