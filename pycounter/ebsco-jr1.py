import pycounter.sushi
import datetime
report = pycounter.sushi.get_report(wsdl_url='https://sushi.ebscohost.com/R4/SushiService.svc',    start_date=datetime.date(2019,1,1), end_date=datetime.date(2019,4,30), requestor_id="4be1b6bc-aab0-4e2c-b664-60504b566ee1", customer_reference="s9094504", report="JR1",    release=4)
report.write_tsv("/home/wera/pycounter/pycounter/ebsco-jr1-counterreport.tsv")
for journal in report:
    print(journal.title)

