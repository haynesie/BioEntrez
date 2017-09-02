from Bio import Entrez
from Bio.Entrez import efetch, read

def pubMedSearch(query, numberOfArticles=5, email='someone@email.com'):

    Entrez.email = email

    if int(numberOfArticles) > 20:
        numberOfArticles = 20

    handle1 = Entrez.esearch(db='pubmed', sort='relevance', retmax=numberOfArticles, retmode='xml', term=query)

    results = Entrez.read(handle1)
    if not results['IdList']:
        combined_results = []
        failed_search = 0
        return((combined_results, failed_search))
    ids = ','.join(results['IdList'])
    handle2 = Entrez.efetch(db='pubmed',retmode='xml',id=ids)
    papers = Entrez.read(handle2)

    ##  Set up data for results page
    titles = []
    dates = []
    authors = []
    abstracts = []

    for i in range(0, len(papers['PubmedArticle'])):

        ##  Titles (easy)
        titles.append(papers['PubmedArticle'][i]['MedlineCitation']['Article']['ArticleTitle'])

        ##  Dates
        date = papers['PubmedArticle'][i]['MedlineCitation']['Article']['ArticleDate']
        if date:
            (month, day, year) = date[0]['Month'], date[0]['Day'], date[0]['Year']
            printdate = "(" + str(month) + "/" + str(day) + "/" + str(year) +")"
        else:
            printdate = "(unknown date)"
        dates.append(printdate)

        ##  Authors
        authorlist = []
        for j in range(0, len(papers['PubmedArticle'][i]['MedlineCitation']['Article']['AuthorList'])):
            if 'LastName' in papers['PubmedArticle'][i]['MedlineCitation']['Article']['AuthorList'][j].keys():
                lastname = papers['PubmedArticle'][i]['MedlineCitation']['Article']['AuthorList'][j]['LastName']
                lastname = lastname.encode('utf-8', errors='ignore')
            else:
                pass
            if 'Initials' in papers['PubmedArticle'][i]['MedlineCitation']['Article']['AuthorList'][j].keys():
                initial = papers['PubmedArticle'][i]['MedlineCitation']['Article']['AuthorList'][j]['Initials']
                initial = initial.encode('utf-8', errors='ignore')
            else:
                pass
            authorlist.append("{}, {}., ".format(lastname, initial))
        authors.append(authorlist)

        ##  Abstracts  (some PubMed articles don't have them!!!)
        if 'Abstract' in papers['PubmedArticle'][i]['MedlineCitation']['Article']:
#            abstract = papers['PubmedArticle'][i]['MedlineCitation']['Article']['Abstract']['AbstractText'][0]
            abstract = papers['PubmedArticle'][i]['MedlineCitation']['Article']['Abstract']['AbstractText']
            abstracts.append(abstract)
        else:
            abstract = '(No abstract.)'
            abstracts.append(abstract)

    combined_results = list(zip(results['IdList'], titles, dates, authors, abstracts))
    number_returned = len(combined_results)

    return((combined_results, number_returned))
