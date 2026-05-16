import os

from dotenv import load_dotenv


load_dotenv()


class Config:

    SUBMIT_ASSIGNMENT_URL = os.getenv(
        "SUBMIT_ASSIGNMENT_URL"
    )

    FETCH_SUMMARY_URL = os.getenv(
        "FETCH_SUMMARY_URL"
    )