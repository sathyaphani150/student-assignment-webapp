import os


class Config:

    SUBMIT_ASSIGNMENT_URL = os.environ.get(
        "SUBMIT_ASSIGNMENT_URL"
    )

    FETCH_SUMMARY_URL = os.environ.get(
        "FETCH_SUMMARY_URL"
    )