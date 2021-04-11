#!/usr/bin/env python3

import requests
import argparse

def main():
    try:
        with open(args.file) as fp:
            song_txt = fp.read()
    except FileNotFoundError as e:
        print(f'Unable to access {args.file}: {e}')
        return -1

    song_lines = song_txt.split('\n')
    
    if  requests.get(args.url).status_code != 200:
        print(f'{args.url} does not resolve to a valid HTTP server.')
        return -2

    try:
        print(f'Pumping {args.file} to {args.url}')
        while True:
            for line in song_lines:
                requests.get(f'{args.url}/{"/".join(line.split(" "))}')
    except KeyboardInterrupt:
        print('Exiting...')
    finally:
        pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()  
    parser.add_argument('url', help='URL to target')
    parser.add_argument('-f', '--file', help='Path to the lyrics file.', default='lyrics.txt')
    args = parser.parse_args()
    main()