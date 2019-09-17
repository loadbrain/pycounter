import pycounter.sushi
import datetime
report = pycounter.sushi.get_report(wsdl_url='https://ams.brill.com/all/services/SushiService',    start_date=datetime.date(2019,1,1), end_date=datetime.date(2019,4,30), requestor_id="20778", customer_reference="6651", report="JR1",    release=4)
report.write_tsv("/home/wera/brill.tsv")
for journal in report:
    print(journal.title)



# https://github.com/pitthsls/pycounter

### Output of report as TSV:
# >>> report.write_tsv("/tmp/counterreport.tsv")

# 	report = pycounter.sushi.get_report(wsdl_url='http://www.example.com/SushiService',
# start_date=datetime.date(2015,1,1), end_date=datetime.date(2015,1,31),
# ...     requestor_id="myreqid", customer_reference="refnum", report="JR1",
# ...     release=4)
