#!/usr/bin/env python3

import datetime as dt
import json, sys

from googleapiclient.discovery import build
import pprint

if __name__ == '__main__':
    # Create an output file name in the format "srch_res_yyyyMMdd_hhmmss.json"
    now_sfx = dt.datetime.now().strftime('%Y%m%d_%H%M%S')
    output_dir = './output/'
    output_fname = output_dir + 'srch_res_' + now_sfx + '.json'
    search_term = sys.argv[1]
    num_requests = int(sys.argv[2])
    
    # Key codes we created earlier for the Google CustomSearch API
    my_api_key = "AIzaSyB7kcLf8SHrfaChqG5l275y4vi-9Ufn6UI"
    my_cse_id = "011658049436509675749:gkuaxghjf5u"

    output_f = open(output_fname, 'a+')

    service = build("customsearch", "v1", developerKey=my_api_key)

    #Function to perform google search.
    def google_search(search_term, cse_id, start_val, **kwargs):
        res = service.cse().list(q=search_term, cx=cse_id, start=start_val, **kwargs).execute()
        output = json.dumps(res, sort_keys=True, indent=2)
        output_f.write(output)
        print('Wrote 10 search results...')

    for i in range(0, num_requests):
        # This is the offset from the beginning to start getting the results from
        start_val = 1 + (i * 10)
        # Make an HTTP request object
        results = google_search(search_term,
            my_cse_id,
            start_val,
            num=10
        )
 
    output_f.close()
    print('Output file "{}" written.'.format(output_fname)) 