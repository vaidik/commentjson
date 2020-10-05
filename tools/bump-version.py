import re
import sys


VERSION_RE = r'\'(([0-9]+\.){2}[0-9])\''


if __name__ == '__main__':
    cmd = sys.argv[1]

    if cmd == '--get-current':
        with open('setup.py') as fp:
            for line in fp.readlines():
                if '__version__' in line:
                    match = re.search(VERSION_RE, line)
                    if match:
                        print(match.groups()[0])
    elif cmd == '--set-version':
        stdin_input = input()
        if not len(stdin_input):
            print('No input provided on stdin.')
            sys.exit(1)

        lines = []
        with open('setup.py') as fp:
            for line in fp.readlines():
                if '__version__' in line:
                    line = re.sub(VERSION_RE, '\'%s\'' % stdin_input, line)
                lines.append(line)

        with open('setup.py', 'w') as fp:
            fp.write(''.join(lines))

    else:
        print('Invalid command')
        sys.exit(1)
