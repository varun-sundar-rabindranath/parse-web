
# This file contains  all the modules used to get/parse  information from a
# webpage. We will split the file into packages later, as each module grows

import urllib.request # Get raw data from a webpage

html = urllib.request.urlopen("https://www.yelp.com/careers/job-openings/0aa8d9cb-776a-44d4-9fba-f9ed632e6ead?description=Software-Engineer-Data-Mining-NLP_Engineering_San-Francisco-CA").read()

print(html)
