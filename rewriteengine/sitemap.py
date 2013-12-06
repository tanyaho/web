from BeautifulSoup import BeautifulStoneSoup as Soup
from urlparse import urlparse
from google import search
import re
import requests

def mk_nice_domain(domain):
    """
    convert domain into a nicer one (eg. www3.google.com into google.com)
    """
    domain = re.sub("^www(\d+)?\.", "", domain)
    # add more her
    return domain


def sitemap_parse(sitemap_option, astring, google_results, website_url):
    not_indexed = []
    not_sitemap = []
    error = ''
    sitemap_results = []
    website_host = urlparse(website_url).scheme
    if website_host != '':
        website_url = urlparse(website_url).scheme + "://" + urlparse(website_url).netloc
    if website_url[-1] != '/':
        website_url += '/'
    if astring != '':
        if sitemap_option == 'sitemap':

            resp = requests.get(astring)
            soup = Soup(resp.content)

        elif sitemap_option == 'upload_sitemap':

            soup = Soup(astring)
        urls = soup.findAll('url')
        for u in urls:
            loc = u.find('loc').string
            sitemap_results.append(loc)
            if loc not in google_results:
                not_indexed.append(loc)
        for loc in google_results:
            if loc not in sitemap_results:
                not_sitemap.append(loc)
    return not_indexed, not_sitemap, error


def googlesearch(website_url):
    google_results = []
    error = ''
    try:
        website_schema = urlparse(website_url).scheme
        if website_schema != '':
            website_url = urlparse(website_url).netloc
        website_url = 'site:'+mk_nice_domain(website_url)
        if website_schema == 'site:':
            error = 'Cannot resolve the URL'
        else:
            for url in search(website_url, stop=100):

                google_results.append(url)

    except:
        error = 'Cannot query to Google'

    return error, google_results
