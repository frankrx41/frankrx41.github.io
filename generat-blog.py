# This program reads all the directories under the archive folder
# Regenerate the html file based on whether the file is up to date
# Finally generate a list file
#
# -f force convert
# -p print html

import sys
import getopt
import os
import markdown

archives_path = os.path.join('./', 'archive')
html_file_name          = 'index.txt'
md_file_name            = 'index.md'
todo_mark_file_name     = '.wip'

def main(argv):
    force_covert = False
    print_html = False
    try:
        opts, args = getopt.getopt(argv,"fp")
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-f':
            force_covert = True
        elif opt == '-p':
            print_html = True
    
    html_text = process_archives(force_covert, print_html)
    write_html(os.path.join(archives_path, html_file_name), html_text)
    return

def process_archives(force_covert, print_html):


    output_html = '<ul>\n'

    for blog_dir in os.listdir(archives_path):
        archive_full_path = os.path.join(archives_path, blog_dir)
        if os.path.isdir(archive_full_path):
            # check md
            print("")
            print(f'[STR]:\t{blog_dir}')
            is_need_covert = force_covert

            if os.path.exists(os.path.join(archive_full_path, todo_mark_file_name)):
                print(f'[WIP]:\tRemove {todo_mark_file_name} to continue')
                continue

            if not os.path.exists(os.path.join(archive_full_path, md_file_name)):
                print(f'[ERR]:\t{md_file_name} file is miss!')
                continue

            if is_need_covert == False:
                if not os.path.exists(os.path.join(archive_full_path, html_file_name)):
                    is_need_covert = True
                elif os.path.getmtime(os.path.join(archive_full_path, html_file_name)) < os.path.getmtime(os.path.join(archive_full_path, md_file_name)):
                        is_need_covert = True

            # covert md to html
            if is_need_covert:
                coverted_html = ""
                with open(os.path.join(archive_full_path, md_file_name), 'r', encoding='UTF-8') as f:
                    text = f.read()
                    coverted_html = markdown.markdown(text, extensions=['fenced_code'])
                coverted_html = coverted_html.replace('src="./', 'src="/archive/' + blog_dir + "/")
                if print_html:
                    print(coverted_html)

                with open(os.path.join(archive_full_path, html_file_name), 'w', encoding='UTF-8') as f:
                    f.write(coverted_html)
                print(f'[COV]:\t{html_file_name}')

            output_html += f'<li><a href="?{blog_dir}">{blog_dir}</a></li>\n'
            print(f'[END]:\t')

    output_html += '</ul>'
    return output_html


def write_html(file_full_path, html_text):
    print('--- output ---')
    print(html_text)

    file1 = open(file_full_path, 'w', encoding='UTF-8')
    file1.write(html_text)
    file1.close()
    return


if __name__ == "__main__":
    main(sys.argv[1:])
