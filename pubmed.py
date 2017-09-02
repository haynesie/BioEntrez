#! /usr/bin/env python3
#

import os
import sys
from pubMedSearch import pubMedSearch

PUBMED_EMAIL = os.environ.get('PUBMED_EMAIL') or 'someone@email.com'

def usage_and_exit():
    print('\nUsage: pubmed.py <search_term> <number_of_articles> <email_address>')
    print('If <search_term> is multi-word phrase or comination of terms, use quotes.')
    raise SystemExit(1)


def main():

    if len(sys.argv) == 3:
        (combined_results, number_returned) = pubMedSearch(sys.argv[1], sys.argv[2], PUBMED_EMAIL)
    elif len(sys.argv) == 4 and "@" in sys.argv[3]:
        (combined_results, number_returned) = pubMedSearch(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        usage_and_exit()


    if  not number_returned:
        print("\n No articles found for", sys.argv[1], ".\n")

    bold = '\033[1m'
    unbold = '\033[0m'

    for i in range(number_returned):
        print('\n')
        print (bold + 'PubMed ID: ' + unbold, combined_results[i][0])
        print (bold + 'Title:     ' + unbold, combined_results[i][1])
        print (bold + "Date:      " + unbold, combined_results[i][2])
        print (bold + "Authors:   " + unbold, combined_results[i][3])
        print (bold + 'Abstract:  ' + unbold, combined_results[i][4][0])

    print("\n", number_returned, "articles returned. \n\n")


if __name__ == '__main__':
    main()
