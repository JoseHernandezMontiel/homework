from repository.report_repository import ReportRepository

report = ReportRepository()

CSV_FILE = "taxi-data.csv"

def main():
    is_uploaded = report.uploadFile(CSV_FILE)

    if not is_uploaded:
        print("File not uploaded")
        return
    
    report.createReport()

if __name__ == '__main__':
    main()
