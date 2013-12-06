from django.shortcuts import render
from rewriteengine.htaccess import get_htaccess_rules, handle_uploaded_file, get_rules_name, remove_temp_file
from rewriteengine.models import htaccess
from xlrd import open_workbook
from rewriteengine.sitemap import googlesearch, sitemap_parse

def htaccessrules(request):
    htaccess_error = ''
    all_rules = htaccess.objects.all()
    show_rules = False
    get_rules = None
    directing_url = ''
    directed_url = ''

    if request.method == 'POST':
        show_rules = True
        is_chooseforme = request.POST.get('chooseforme', False)
        is_redirection = request.POST.get('redirection', False)
        is_rewrite = request.POST.get('rewrite', False)
        if request.POST['Directing_URL'] != '':
            directing_url = request.POST['Directing_URL']
        if request.POST['Directed_URL'] != '':
            directed_url = request.POST['Directed_URL']
        if is_chooseforme:
            rule_name, htaccess_error_temp = get_rules_name(directing_url, directed_url)
            htaccess_error += htaccess_error_temp
            if is_rewrite:
                htaccess_error = 'This option is for redirections only'
                rule_name = ''
        else:
            rule_name = request.POST['name']
        if rule_name == '':
            if htaccess_error == '':
                htaccess_error = 'Please select rule type'
            show_rules = False
        else:


            get_rules, htaccess_error_temp = get_htaccess_rules(rule_name, get_rules, htaccess_error, directing_url, directed_url, is_redirection, is_rewrite)
            htaccess_error += htaccess_error_temp
            if htaccess_error != '':
                get_rules = None
                show_rules = False

    return render(request, 'rewriteengine/htaccess.html',  {'all_rules': all_rules,
                                                            'get_rules': get_rules,
                                                            'show_rules': show_rules,
                                                            'htaccess_error': htaccess_error,
                                                            'directing_url': directing_url,
                                                            'directed_url': directed_url})


def bulk_redirections(request):
    htaccess_error = ''
    all_rules = htaccess.objects.all().filter(bulk_upload=True)
    show_rules = False
    get_rules = []
    if request.method == 'POST':

        is_chooseforme = request.POST.get('chooseforme', False)
        if is_chooseforme:
            rule_name = 'chooseforme'
        else:
            rule_name = request.POST['name']
        if rule_name == '':
            htaccess_error = 'Please select rule type'
        else:
            afile = request.FILES.get('filedocs', '')
            if (afile != '') and ('.xls' in afile.name):
                path = handle_uploaded_file(afile)
                aString = open(path, 'rb').read()
                wb = open_workbook(file_contents=aString)
                sheet = wb.sheet_by_index(0)
                for row_index in range(sheet.nrows):
                    if row_index != 0:
                        for col_index in range(sheet.ncols):
                            if col_index == 0:
                                directing_url = sheet.cell(row_index, col_index).value
                            elif col_index == 1:
                                directed_url = sheet.cell(row_index, col_index).value
                        if is_chooseforme:
                            rule_name, htaccess_error_temp = get_rules_name(directing_url, directed_url)
                        if rule_name != "":
                            get_rules_temp, htaccess_error_temp = get_htaccess_rules(rule_name, get_rules, htaccess_error, directing_url, directed_url, True, False)
                            get_rules += get_rules_temp
                        if htaccess_error_temp != '':
                            htaccess_error += 'Redirection from ' + directing_url + ' to ' + directed_url + ' failed. Reason: '+ htaccess_error_temp
            else:
                htaccess_error = 'Invalid file, please upload excel file with the example template.'

    return render(request, 'rewriteengine/bulk-redirections.html',  {'all_rules': all_rules,
                                                            'get_rules': get_rules,
                                                            'show_rules': show_rules,
                                                            'htaccess_error': htaccess_error})


def sitemap_indexed(request):
    google_results = []
    not_indexed = []
    error = ''
    not_sitemap = []
    astring = ''
    website_url=''
    if request.method == 'POST':
        sitemap_option = request.POST['sitemap_option']
        if sitemap_option == 'sitemap':
            astring = request.POST['sitemap_url']
            if '.xml' not in astring:
                error = "Please upload xml file"
        elif sitemap_option == 'upload_sitemap':
            afile = request.FILES.get('filedocs', '')
            path = ""
            if afile != "":
                path = handle_uploaded_file(afile)
                if '.xml' in path:
                    astring = open(path, 'rb').read()
        else:
            error = "Please select option to get the sitemap"

        if astring:
            if request.POST['website_url'] != '':
                website_url = request.POST['website_url']
                error_temp, google_results = googlesearch(website_url)
                if error:
                    error += error_temp
                else:
                    not_indexed, not_sitemap, error_temp = sitemap_parse(sitemap_option, astring, google_results, website_url)
                    error += error_temp
        else:
            error += "Please upload xml file"

    return render(request, 'rewriteengine/sitemap-indexed.html',  {'error': error, 'not_indexed':not_indexed, 'not_sitemap': not_sitemap})

