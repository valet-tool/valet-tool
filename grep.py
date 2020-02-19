import os
import re

#
# def grep_file():
#     words = ['password', 'user', 'ip', 'key']
#     rx = re.compile('|'.join(words))
#     for root, dirs, files in os.walk('/Users/sakshikarnawat/PycharmProjects/data/LibreOffice_6.2.8.2_Linux_x86_deb/'):
#         for filename in files:
#             with open(filename) as df:
#                 data = df.read()
#             for match in rx.finditer(data):
#                 print
#                 match.span()
#
# grep_file();