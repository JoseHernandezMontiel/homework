import os
from src.repository.report_repository import ReportRepository

report = ReportRepository()
CSV_FILE = "taxi-data.csv"

def test_upload_file():
    assert report.uploadFile(CSV_FILE) == True

def test_html_file_created():
    report.uploadFile(CSV_FILE)

    assert os.path.exists("./financial-report.html") == True
    