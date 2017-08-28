#! /usr/bin/env python
#

import os
import sys
from pubMedSearch import pubMedSearch

def main():

    ### Need to add arbitrarily long argument list for search terms
    if len(sys.argv) != 4:
        print('Usage: pubmed.py <search_term> <number_of_articles> <email_address>')
        raise SystemExit(1)

    (combined_results, number_returned) = pubMedSearch(sys.argv[1], sys.argv[2], sys.argv[3])

    if  not number_returned:
        print "\n No articles found for", sys.argv[1], ".\n"

    bold = '\033[1m'
    unbold = '\033[0m'

    for i in range(number_returned):
        print
        print bold + 'PubMed ID: ' + unbold, combined_results[i][0]
        print bold + 'Title:     ' + unbold, combined_results[i][1]
        print bold + "Date:      " + unbold, combined_results[i][2]
        print bold + "Authors:   " + unbold, combined_results[i][3]
        print bold + 'Abstract:  ' + unbold, unicode(combined_results[i][4][0])

    print "\n", number_returned, "articles returned. \n\n"


if __name__ == '__main__':
    main()
