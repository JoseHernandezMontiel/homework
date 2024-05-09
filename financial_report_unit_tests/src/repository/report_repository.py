from patterns import csv_utils
from patterns import web_report
    
class ReportRepository():
    
  def __init__(self):
    self.source_data = None
    
  def uploadFile(self, file_path: str):    
    if not file_path:
      return False

    self.source_data = csv_utils.parse_file(file_path)
    return True

  def createReport(self):
    html_report = web_report.create_content(self.source_data)
    return web_report.create_file(html_report)