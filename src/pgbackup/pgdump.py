import subprocess, sys

def dump(url):
    '''
    >>> from pgbackup import pgdump
    >>> dump = pgdump.dump('postgres://demo:secure_password@34.221.194.232:80/sample')
    >>> f = open('dump.sql', 'w+b')
    >>> f.write(dump.stdout.read())
    56979
    >>> f.close()
    '''
    try:
        return subprocess.Popen(['pg_dump', url], stdout=subprocess.PIPE)
    except OSError as err:
        print(f"Error: {err}")
        sys.exit(1)
