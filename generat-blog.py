# This program reads all the directories under the archive folder
# Regenerate the html file based on whether the file is up to date
# Finally generate a list file
#
# -f force convert
# -p print html
#
# -n not write to {blog_path_name}/index.txt
# -s <blog_path_name> force covert this md file, NOT update /archive/index.txt
#

from distutils.file_util import write_file
import sys
import getopt
import os
from markdown_it import MarkdownIt
from pyquery import PyQuery
import datetime

md = MarkdownIt("commonmark").enable('table').enable('strikethrough')
import re

from colorama import Fore
from colorama import Style

archives_path = os.path.join('./', 'archive')
html_file_name          = 'index.txt'
md_file_name            = 'index.md'

stat_cov = 0
stat_err = 0
stat_wip = 0
stat_str = 0
stat_cov_file_name = []

def main(argv):
    force_covert    : bool      = False
    print_html      : bool      = False
    single_file     : os.path   = ""
    save_to_file    : bool      = True

    try:
        opts, args = getopt.getopt(argv,"fps:n")
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-f':
            force_covert = True
        elif opt == '-p':
            print_html = True
        elif opt == '-s':
            single_file = arg
        elif opt == '-n':
            save_to_file = False
    
    if single_file != "":
        process_single_file(force_covert, print_html, single_file, save_to_file)
    else:
        html_text = process_archives(force_covert, print_html, save_to_file)
        print_stat()
        write_html(os.path.join(archives_path, html_file_name), html_text)
    return

# Return home page single archive html text
def process_single_file(force_covert: bool, print_html: bool, blog_dir: os.path, save_to_file: bool):
    archive_full_path = os.path.join(archives_path, blog_dir)

    global stat_cov
    global stat_err
    global stat_wip
    global stat_str

    print()
    print(f'[STR]:\t{blog_dir}')
    stat_str += 1
    is_need_covert = force_covert

    if not os.path.exists(os.path.join(archive_full_path, md_file_name)):
        print(f'{Fore.YELLOW}[WIP]:\tFile {md_file_name} is miss {Style.RESET_ALL}')
        stat_wip += 1
        return ""

    if is_need_covert == False:
        # Not exist html file
        if not os.path.exists(os.path.join(archive_full_path, html_file_name)):
            is_need_covert = True
        # We update md file
        elif os.path.getmtime(os.path.join(archive_full_path, html_file_name)) < os.path.getmtime(os.path.join(archive_full_path, md_file_name)):
            is_need_covert = True

    md_text = ''
    # Get md text
    if is_need_covert:
        with open(os.path.join(archive_full_path, md_file_name), 'r', encoding='UTF-8') as f:
            md_text = f.read()
        md_firstline = md_text.split('\n', maxsplit=1)[0]
        # This md is wip
        if md_firstline == '' or md_firstline[0] != '#':
            print(f'{Fore.YELLOW}[WIP]:\tMake first line be H1 mark to continue {Style.RESET_ALL}')
            stat_wip += 1
            return ""

    coverted_html = ''
    # Covert md to html
    if is_need_covert:
        coverted_html = md.render(md_text)

        # './' => '/{blog_dir}/'
        coverted_html = coverted_html.replace('src="./', 'src="/archive/' + blog_dir + "/")

        # Do not use './'
        re_found = re.search('src="[^\./]', coverted_html)
        if re_found:
            print(f'{Fore.RED}[ERR]:\t {re_found} {Style.RESET_ALL}')
            print(coverted_html)
            stat_err += 1
            return ""

        # `KEY` => <kbd>KEY</kbd>
        key_list = [{0: 'Alt', 1: 'Alt'}, {0: 'Ctrl', 1: 'Ctrl'}, {0: 'Shift', 1: '⇧'}, {0: 'Esc', 1: 'Esc'}, {0: 'Win', 1: 'Win'}, {0: 'Cmd', 1: 'Cmd'}, {0: 'Enter', 1: '⏎'}, {0: 'PgUp', 1: 'PgUp'}, {0: 'PgDn', 1: 'PgDn'}, {0: 'Home', 1: 'Home'}, {0: 'End', 1: 'End'}, {0: 'Backspace', 1: '⌫'}, {0: '&lt;-', 1: '←'}, {0:'-&gt;', 1: '→'}, {0: 'Tab', 1: '↹'}, {0: 'A', 1: 'A'}, {0: 'B', 1: 'B'}, {0: 'C', 1: 'C'}, {0: 'D', 1: 'D'}, {0: 'E', 1: 'E'}, {0: 'F', 1: 'F'}, {0: 'G', 1: 'G'}, {0: 'H', 1: 'H'}, {0: 'I', 1: 'I'}, {0: 'J', 1: 'J'}, {0: 'K', 1: 'K'}, {0: 'L', 1: 'L'}, {0: 'M', 1: 'M'}, {0: 'N', 1: 'N'}, {0: 'O', 1: 'O'}, {0: 'P', 1: 'P'}, {0: 'Q', 1: 'Q'}, {0: 'R', 1: 'R'}, {0: 'S', 1: 'S'}, {0: 'T', 1: 'T'}, {0: 'U', 1: 'U'}, {0: 'V', 1: 'V'}, {0: 'W', 1: 'W'}, {0: 'X', 1: 'X'}, {0: 'Y', 1: 'Y'}, {0: 'Z', 1: 'Z'}, {0: 'Up', 1: '↑'}, {0: 'Down', 1: '↓'}, {0: 'Left', 1: '←'}, {0: 'Right', 1: '→'}, {0: 'Space', 1: 'Space'}]
        for key_name in key_list:
            coverted_html = re.sub(f'<code>({key_name[0]})</code>', f'<kbd>{key_name[1]}</kbd>', coverted_html, flags=re.IGNORECASE)

        # Alerts tip note important
        str_list = [    {0: '<blockquote>\n<p><strong>tip:*</strong>', 1: '<blockquote class="alerts alerts-tip"> '},
                        {0: '<blockquote>\n<p><strong>note:*</strong>', 1: '<blockquote class="alerts alerts-note"> '},
                        {0: '<blockquote>\n<p><strong>important:*</strong>', 1: '<blockquote class="alerts alerts-important"> '}]
        for str_name in str_list:
            coverted_html = re.sub(str_name[0], str_name[1], coverted_html, flags=re.IGNORECASE)

        # Checkbox
        coverted_html = coverted_html.replace("[ ] ", '<input type="checkbox" />')
        coverted_html = coverted_html.replace("[x] ", '<input type="checkbox" checked="checked" />')


        if print_html:
            print(coverted_html)

        if save_to_file:
            with open(os.path.join(archive_full_path, html_file_name), 'w', encoding='UTF-8') as f:
                f.write(coverted_html)
        print(f'{Fore.GREEN}[COV]:\t{html_file_name} {Style.RESET_ALL}')
        stat_cov_file_name.append(blog_dir)
        stat_cov += 1
    else:
        with open(os.path.join(archive_full_path, html_file_name), 'r', encoding='UTF-8') as f:
            coverted_html = f.read()

    print(f'[END]:\t')

    # To main page div
    output_html = ''
    pq = PyQuery(coverted_html)
    output_html += f'<div class="archive-list" onClick="location.href=\'?{blog_dir}\'">'
    output_html += f'<h1>{pq("h1").html()}</h1>'
    output_html += f'<p>{pq("p").html()}</p>'

    md_file_full_name_path = os.path.join(archive_full_path, md_file_name)
    time_create = os.path.getctime(md_file_full_name_path)
    time_modify = os.path.getmtime(md_file_full_name_path)
    time_format = "%Y-%m-%d"
    time_create_str = datetime.datetime.fromtimestamp(time_create).strftime(time_format)
    time_modify_str = datetime.datetime.fromtimestamp(time_modify).strftime(time_format)
    if time_create_str == time_modify_str:
        time_modify_str = ''
    output_html += f'<div class="archive-info">{len(coverted_html)} | {time_create_str} {time_modify_str}</div>'
    output_html +='</div>\n'
    return output_html


def process_archives(force_covert: bool, print_html: bool, save_to_file: bool):
    output_html = ''
    for blog_dir in os.listdir(archives_path):
        if os.path.isdir(os.path.join(archives_path, blog_dir)):
           output_html += process_single_file(force_covert, print_html, blog_dir, save_to_file)

    output_html += ''

    
    return output_html


def print_stat():
    print()
    print(f'stat_str: {stat_str}')
    print(f'stat_wip: {stat_wip}')
    print(f'stat_cov: {stat_cov}')
    print(f'Covert files: {stat_cov_file_name}')
    if stat_err > 0:
        print(f'{Fore.RED}stat_err: {stat_err} {Style.RESET_ALL}')
    else:
        print(f'{Fore.GREEN}Success!!{Style.RESET_ALL}')
    return


def write_html(file_full_path, html_text):
    print('--- output ---')
    print(html_text)

    file1 = open(file_full_path, 'w', encoding='UTF-8')
    file1.write(html_text)
    file1.close()
    return


if __name__ == "__main__":
    main(sys.argv[1:])
