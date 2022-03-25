import sys
import argparse
import re
from math_4nec2 import *

unit_names = ['CM', 'MM', 'IN', 'FT', 'PF', 'NF', 'UF', 'NH', 'UH']

def process_units(a):
    t_list = []
    string_len = len(a)
    for index, u in enumerate(unit_names):
        last = 0
        nmatches = 0
        pattern = re.compile(r'(=\s*|\s+|(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?)'+u+'(?!\w)|([+\-*/]|\s+|$)*?')
        while last <= len(a):
#            result = re.search(r'(=\s*|\s+|(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?)'+u+r'(?!\w)|([+\-*/]|\s+|$)*?',a, last)
            result = pattern.search(a, last)
            if result is None:
                break
            first, last = result.span()
            if last == first:
                last = first+1
            else:
                t_list.append(tuple((first,last,index)))
                nmatches=nmatches+1
#       print(u, end=' ')
#       print(a, end=' ')
#       print(nmatches)
#   print(t_list)
    t_list.sort()
#   print(t_list)
    ret_string = ''
    start = 0
    for t in t_list:
        first, last, index = t
        if start < first:
            ret_string += a[start:first]
        start = last
        if a[first] == '=':
            part = a[first:last]
        else:
            part = '(' + a[first:last -2] + '*'+ unit_names[index]+ ')'
        ret_string += part
    ret_string += a[start:string_len]
    return ret_string

def process_command_line(a):
    t_list = []
    string_len = len(a)
    pattern = re.compile(r'\S+')
    last = 0
    while last <= len(a):
        result = pattern.search(a, last)
        if result is None:
            break
        first, last = result.span()
        if last == first:
            last = first+1
        else:
            t_list.append(tuple((first,last)))
    t_list.sort()
    ret_string = ''
    start = 0
    for t in t_list:
        first, last = t
        if start < first:
            ret_string += a[start:first]
        start = last
        partial = process_units(a[first:last])
        part = str(eval(partial))
        ret_string += part
    ret_string += a[start:string_len]
#   print('Values: ',ret_string)
    return ret_string

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input_file', type=argparse.FileType('rt'), required=True, help='input file')
parser.add_argument('-j', '--processors', type=int, required=False, help='number of processors in SMP machine')
parser.add_argument('-o', '--output_file', type=argparse.FileType('w'), required=False, help='output file (defalts to stdout)')
args = parser.parse_args()
print('Processing file: ',args.input_file.name, file=sys.stderr)
stdout_fileno = sys.stdout
remember_to_close = False
if args.output_file is not None:
    args.output_file.close()
    sys.stdout = open(args.output_file.name, 'w')
    remember_to_close = True
with args.input_file: 
    sy_pattern = re.compile('^SY\s+',flags=re.IGNORECASE)
    comment_pattern = re.compile('^C[EM]\s+',flags=re.IGNORECASE)
    gx_pattern = re.compile('^GX\s+', flags=re.IGNORECASE)
    apex_comment_pattern = re.compile("^'")
    for line in args.input_file:
        if sy_pattern.search(line):
            myline = sy_pattern.sub('', line)
            lines_without_comments = (myline.split("'")[0]).split(",")
            for l in lines_without_comments:
                l1 = l.strip().upper().replace('^','**')
                str_out = process_units(l1)
                exec(str_out)
        elif apex_comment_pattern.search(line):
            pass
        elif comment_pattern.search(line):
            print(line, end='')
        elif gx_pattern.search(line):
            print('Warning: GX card found! It will be copied verbatim.', file=sys.stderr)
            gx_list = line.upper().split("'") # remove apex comments anyway
            if len(gx_list) == 1:
                print(gx_list[0], end='')
            else:
                print(gx_list[0])
        else:
            if len(line) <= 3:
                print(line, end='')
            else:
                print(line[0:3], end = '')
                command_list = line[3:len(line)].upper().split("'")
                l1 = process_command_line(command_list[0].replace('^','**').replace(',',' '))
                if len(command_list) == 1:
                    print(l1, end='')
                else:
                    print(l1)

#           print(line)
# Close stdout file
if remember_to_close:
    sys.stdout.close()
    sys.stdout = stdout_fileno
print('End of processing', file=sys.stderr)
