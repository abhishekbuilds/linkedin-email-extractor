#!/usr/bin/env python3

from googleapiclient.discovery import build                     #For using Google Custom Search Engine API
import datetime as dt                                           #Importing system date for the naming of the output file.
import sys                                                      
from xlwt import Workbook                                       #For working on xls file.
import re                                                       #For email search using regex.

if __name__ == '__main__':
    # Create an output file name in the format "srch_res_yyyyMMdd_hhmmss.xls in output folder"
    now_sfx = dt.datetime.now().strftime('%Y%m%d_%H%M%S')
    output_dir = './output/'
    output_fname = output_dir + 'srch_res_' + now_sfx + '.xls'
    search_term = sys.argv[1]
    num_requests = int(sys.argv[2])
    
    my_api_key = "replace_with_you_api_key"                 #Read readme.md to know how to get you api key.
    my_cse_id = "011658049436509675749:gkuaxghjf5u"         #Google CSE which searches possible LinkedIn profile according to query.

    service = build("customsearch", "v1", developerKey=my_api_key)

    wb=Workbook()
    sheet1 = wb.add_sheet(search_term)                      #Excel sheet created with name of the search term.
    wb.save(output_fname)
    sheet1.write(0,0,'Name')
    sheet1.write(0,1,'Profile Link')
    sheet1.write(0,2,'Snippet')
    sheet1.write(0,3,'Present Organisation')
    sheet1.write(0,4,'Location')
    sheet1.write(0,5,'Role')
    sheet1.write(0,6,'Email')
    sheet1.col(0).width = 256 * 20
    sheet1.col(1).width = 256 * 50
    sheet1.col(2).width = 256 * 100
    sheet1.col(3).width = 256 * 20
    sheet1.col(4).width = 256 * 20
    sheet1.col(5).width = 256 * 50
    sheet1.col(6).width = 256 * 50
    wb.save(output_fname)

    row = 1                                                 #To insert the data in the next row.

    #Function to perform google search.
    def google_search(search_term, cse_id, start_val, **kwargs):
        res = service.cse().list(q=search_term, cx=cse_id, start=start_val, **kwargs).execute()
        return res

    for i in range(0, num_requests):
        # This is the offset from the beginning to start getting the results from
        start_val = 1 + (i * 10)
        # Make an HTTP request object
        results = google_search(search_term,
            my_cse_id,
            start_val,
            num=10                                          #num value can be 1 to 10. It will give the no. of results. 
        )

        for profile in range (0, 10):
            title = results['items'][profile]['title']
            link = results['items'][profile]['link']
            snippet = results['items'][profile]['snippet']
            # org = results['items'][profile]['pagemap']['person'][0]['org']
            # location = results['items'][profile]['pagemap']['person'][0]['location']
            # role = results['items'][profile]['pagemap']['person'][0]['role']
            #All three are set to be null as some profiles don't contains the person key.
            #I am trying to resolve this issue.
            org="Null"
            location="Null"
            role="Null"
            myList = [item for item in snippet.split('\n')]
            newSnippet = ' '.join(myList)
            contain = re.search(r'[\w\.-]+@[\w\.-]+', newSnippet)
            if contain is not None:
                print(title[:-23])
                sheet1.write(row,0,title[:-23])
                sheet1.write(row,1,link)
                sheet1.write(row,2,newSnippet)
                sheet1.write(row,3,org)
                sheet1.write(row,4,location)
                sheet1.write(row,5,role)
                sheet1.write(row,6,contain[0])
                print('Wrote {} search result(s)...'.format(row))
                row = row + 1

    wb.save(output_fname)
    print('Output file "{}" written.'.format(output_fname)) 