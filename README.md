# LinkedIn Email Extractor

LinkedIn Email Extractor is a Python script which provides the LinkedIn profiles whose description contains the email id in it. LEE saves the link to the profile and its information in an excel file including a separate column for the email.
  - No need to search manually for the email-Ids.
  - Saves you from exhausting connection request.
  - Get to the person directly through the mail.

## Features!
  - Uses Google Custom Search Engine API for searching LinkedIn profiles.
  - Just enter the Organisation Name and Job Role to get the linked profiles and email Ids.
  - OR, enter your own search term for getting more optimum results.

## Limitations
  - You have to create your own API key and use it.
  - Google free API usage is limited to 100 search queries per day.
  - And 100 results per search per day.
  - For processing 100 search results for a single search query, Google API makes 10 requests.

## First step before using script
- Go at https://console.developers.google.com/apis.
- SignIn using your google account and create a project named LinkedIn Email Extractor.
- Now search for Google console search, and generate API key for it.
- After getting the key replace "replace_with_you_api_key" with you api key in Lee.py at line 17, and save it.

## How to use?
  - Open terminal and move to LinkedIn Email Extractor directory.
  - Then run following command by replacing your input with <job_role + 'email me at' + company> & <num_request> in the given format:
```sh
python3 lee.py "<job_role + 'email me at' + company>" <no. of request, 1-10>
```
NOTE:
> <num_request> will be between 1 to 10. For 1 request 10 results will be processed for a query.
> For processing 100 result you have to use 10 for the same.
> In processing 100 results for a query 10 credits will be exhausted from your Google API limits.

## Suggestion
If you want to see the whole result without exchausting your credit you can go at http://recruitmentgeek.com/tools/linkedin/ and search the query. You liked the result then you can use the same query with the LEE and get the emails extracted out of it.

## Meta

Abhishek Singh – [@asraisingh](https://twitter.com/asraisingh) – www.iabhishek.me

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/asraisingh/linkedin-email-extractor](asraisingh/linkedin-email-extractor)

## Contribution
1. Fork it (<https://github.com/asraisingh/linkedin-email-extractor/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
