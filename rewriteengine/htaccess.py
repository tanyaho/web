from urlparse import urlparse
import re
from rewriteengine.models import htaccess
import tempfile
import shutil
from website.settings import FILE_UPLOAD_DIR


def handle_uploaded_file(source):
    fd, filepath = tempfile.mkstemp(prefix=source.name, dir=FILE_UPLOAD_DIR)
    with open(filepath, 'wb') as dest:
        shutil.copyfileobj(source, dest)
    return filepath


def remove_temp_file():
    shutil.rmtree(FILE_UPLOAD_DIR)


def get_code(directing_url, directed_url):

    directed_host = ''
    directing_query = ''
    if directing_url != '':
        directing_query = re.escape(urlparse(directing_url).query)
        directing_url = re.escape(urlparse(directing_url).path[1:])

    full_directed_url = directed_url
    if directed_url != '':
        directed_host = urlparse(directed_url).scheme + "://" + urlparse(directed_url).netloc
        directed_url = urlparse(directed_url).path[1:]
    return directing_query, directing_url, directed_host, full_directed_url, directed_url


def get_htaccess_rules(rule_name, get_rules, htaccess_error, directing_url, directed_url, is_redirection, is_rewrite):
    directing_query, directing_url, directed_host, full_directed_url, directed_url = get_code(directing_url, directed_url)
    get_rules = []
    if is_redirection:
        get_rules = htaccess.objects.all().filter(name=rule_name, redirection=is_redirection)
        if is_rewrite:
            get_rules = htaccess.objects.all().filter(name=rule_name)
    if is_rewrite:
        get_rules = htaccess.objects.all().filter(name=rule_name, rewrite=is_rewrite)
    for idx, item in enumerate(get_rules):
        if '[Old URL]' in item.rule:
            if directing_url == '':
                htaccess_error += 'Redirecting URL requires path. '
            else:
                get_rules[idx].rule = get_rules[idx].rule.replace('[Old URL]', directing_url)
        if '[Old Query]' in item.rule:
            if directing_query == '':
                htaccess_error += 'Redirecting URL requires query. '
            else:
                get_rules[idx].rule = get_rules[idx].rule.replace('[Old Query]', directing_query)

        if '[New URL]' in item.rule:
            if directed_url == '':
                htaccess_error += 'Redirected/Rewritten URL requires path. '
            else:
                get_rules[idx].rule = get_rules[idx].rule.replace('[New URL]', directed_url)
        if '[New Host]' in item.rule:
            if directed_host == '':
                htaccess_error += 'Redirected/Rewritten URL requires host. '
            else:
                get_rules[idx].rule = get_rules[idx].rule.replace('[New Host]', directed_host)
        if '[Full New URL]' in item.rule:
            if full_directed_url == '':
                htaccess_error += 'Redirected/Rewritten URL requires path. '
            else:
                get_rules[idx].rule = get_rules[idx].rule.replace('[Full New URL]', full_directed_url)
    return get_rules, htaccess_error


def get_rules_name(directing_url, directed_url):
    directing_query, directing_url, directed_host, full_directed_url, directed_url = get_code(directing_url, directed_url)
    get_rules = htaccess.objects.all().filter(redirection=True)
    rule_check = ''
    htaccess_error = ''
    rule_name = ''
    if directing_url != '':
        rule_check += '[Old URL]'
    if directing_query != '':
        rule_check += '[Old Query]'
    if full_directed_url != '':
        rule_check += '[Full New URL]'
    for item in get_rules:
        a_rule = ''
        if '[Old URL]' in item.rule:
            a_rule += '[Old URL]'
        if '[Old Query]' in item.rule:
            a_rule += '[Old Query]'
        if '[Full New URL]' in item.rule:
            a_rule += '[Full New URL]'
        if rule_check == a_rule:
            rule_name = item.name

    if rule_name == '':
        htaccess_error += 'Cannot find the suitable rule. Please select from the drop down rule'

    return rule_name, htaccess_error