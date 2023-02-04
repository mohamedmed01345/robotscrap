#!/bin/python3
import requests
import argparse
import os

## TODO: Make it output in dir or file that has the full output
parser = argparse.ArgumentParser(prog='python3 robotscrap.py',usage='%(prog)s [domains file] -od [output directory]')
parser.add_argument('filename')
parser.add_argument('-od',default=None,help='specify the output directory')
args = parser.parse_args()
if os.path.isdir(args.od):
    pass
elif args.od:
    os.mkdir(args.od)
path = args.od or '.'
try:
    with open(args.filename, 'r') as file:
        for link in file.readlines():
            print(f'   {link.strip()}   '.center(10,'#'))
            file_out = open(f'{path}/{link}','w')
            request = requests.get(f'https://{link.strip()}/robots.txt')
            response_all = request.text
            for response in response_all.split('\n'):
                if 'Disallow' in response:
                    final = f'https://{link.strip()}{response.split("Disallow: ")[1]}'
                    file_out.write(f'{final}\n')
                    print(final)
            file_out.close()
except FileNotFoundError as e:
    print('File not found',args.filename)
