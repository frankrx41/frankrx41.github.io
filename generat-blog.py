# This program reads all the directories under the archive folder
# Regenerate the html file based on whether the file is up to date
# Finally generate a list file
#
# -f force convert
# -p print html
#
# -s <blog_path_name> force covert this md file, NOT update /archive/index.txt and {blog_path_name}/index.txt, should use for debug only
#

import sys
import getopt
import os
from xmlrpc.client import boolean
import markdown
import re

from colorama import Fore
from colorama import Style

archives_path = os.path.join('./', 'archive')
html_file_name          = 'index.txt'
md_file_name            = 'index.md'
todo_mark_file_name     = '.wip'

stat_cov = 0
stat_err = 0
stat_wip = 0
stat_str = 0
stat_cov_file_name = []

def main(argv):
    force_covert    : bool      = False
    print_html      : bool      = False
    single_file     : os.path   = ""

    try:
        opts, args = getopt.getopt(argv,"fps:")
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
    
    if single_file != "":
        process_single_file(force_covert, print_html, single_file, False)
    else:
        html_text = process_archives(force_covert, print_html)
        print_stat()
        write_html(os.path.join(archives_path, html_file_name), html_text)
    return


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

    if os.path.exists(os.path.join(archive_full_path, todo_mark_file_name)):
        print(f'{Fore.YELLOW}[WIP]:\tRemove {todo_mark_file_name} to continue {Style.RESET_ALL}')
        stat_wip += 1
        return ""

    if not os.path.exists(os.path.join(archive_full_path, md_file_name)):
        print(f'{Fore.YELLOW}[WIP]:\tFile {md_file_name} is miss {Style.RESET_ALL}')
        stat_wip += 1
        return ""

    if is_need_covert == False:
        if not os.path.exists(os.path.join(archive_full_path, html_file_name)):
            is_need_covert = True
        # no latest
        elif os.path.getmtime(os.path.join(archive_full_path, html_file_name)) < os.path.getmtime(os.path.join(archive_full_path, md_file_name)):
                is_need_covert = True

    # Covert md to html
    if is_need_covert:
        coverted_html = ""
        with open(os.path.join(archive_full_path, md_file_name), 'r', encoding='UTF-8') as f:
            text = f.read()
            coverted_html = markdown.markdown(text, extensions=['fenced_code', 'tables'])

        # './' => '/{blog_dir}/'
        coverted_html = coverted_html.replace('src="./', 'src="/archive/' + blog_dir + "/")

        # Do not use './'
        re_found = re.search('src="[^\./]', coverted_html)
        if re_found:
            print(f'{Fore.RED}[ERR]:\t {re_found} {Style.RESET_ALL}')
            stat_err += 1
            return ""

        # `KEY` => <kbd>KEY</kbd>
        key_list = [{1: 'Ctrl', 2: 'Ctrl'},  {1: 'Shift', 2: '⇧'},  {1: 'Esc', 2: 'Esc'},  {1: 'Win', 2: 'Win'},  {1: 'Cmd', 2: 'Cmd'},  {1: 'Enter', 2: '⏎'},  {1: 'PgUp', 2: 'PgUp'},  {1: 'PgDn', 2: 'PgDn'},  {1: 'Home', 2: 'Home'},  {1: 'End', 2: 'End'},  {1: 'Backspace', 2: '⌫'},  {1: '&lt;-', 2: '←'}, {1:'-&gt;', 2: '→'}, {1: '\^\|', 2:'↑'}, {1: 'v\|', 2:'↓'}, {1: 'Tab', 2: 'Tab'},  {1: 'A', 2: 'A'},  {1: 'B', 2: 'B'},  {1: 'C', 2: 'C'},  {1: 'D', 2: 'D'},  {1: 'E', 2: 'E'},  {1: 'F', 2: 'F'},  {1: 'G', 2: 'G'},  {1: 'H', 2: 'H'},  {1: 'I', 2: 'I'},  {1: 'J', 2: 'J'},  {1: 'K', 2: 'K'},  {1: 'L', 2: 'L'},  {1: 'M', 2: 'M'},  {1: 'N', 2: 'N'},  {1: 'O', 2: 'O'},  {1: 'P', 2: 'P'},  {1: 'Q', 2: 'Q'},  {1: 'R', 2: 'R'},  {1: 'S', 2: 'S'},  {1: 'T', 2: 'T'},  {1: 'U', 2: 'U'},  {1: 'V', 2: 'V'},  {1: 'W', 2: 'W'},  {1: 'X', 2: 'X'},  {1: 'Y', 2: 'Y'},  {1: 'Z', 2: 'Z'},  {1: 'Up', 2: '↑'},  {1: 'Down', 2: '↓'},  {1: 'Left', 2: '←'}, {1: 'Right', 2: '→'}]
        for key_name in key_list:
            coverted_html = re.sub(f'<code>({key_name[1]})</code>', f'<kbd>{key_name[2]}</kbd>', coverted_html, flags=re.IGNORECASE)

        if print_html:
            print(coverted_html)

        if save_to_file:
            with open(os.path.join(archive_full_path, html_file_name), 'w', encoding='UTF-8') as f:
                f.write(coverted_html)
        print(f'{Fore.GREEN}[COV]:\t{html_file_name} {Style.RESET_ALL}')
        stat_cov_file_name.append(blog_dir)
        stat_cov += 1

    print(f'[END]:\t')
    return f'<li><a href="?{blog_dir}">{blog_dir}</a></li>\n'


def process_archives(force_covert: bool, print_html: bool):
    output_html = '<ul>\n'
    for blog_dir in os.listdir(archives_path):
        if os.path.isdir(os.path.join(archives_path, blog_dir)):
           output_html += process_single_file(force_covert, print_html, blog_dir, True)

    output_html += '</ul>'

    
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
