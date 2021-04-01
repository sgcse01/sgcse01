import os, sys, logging 
from pathlib import Path

def testfunc():
    

    logging.basicConfig(filename='run.log', format='%(asctime)s %(message)s', encoding='utf-8', level=logging.DEBUG)
    if Path('/tmp/pidfile').exists():
        logging.info("pid file exists, exiting")
        sys.exit(1)

    print(os.getuid())
    try:
        pid = os.fork()
        logging.info("pid is %s",  pid)
        if pid > 0:
            sys.exit(0)
    except OSError as err:
        logging.error('fork #1 failed: %s'.format(err))
        sys.exit(1)
    
    os.chdir('/')
    os.setsid()
    os.umask(0)


    try:
        pid = os.fork()
        logging.info("pid of second fork is %s",  pid)
        if pid > 0:
            sys.exit(0)
    except OSError as err:
        logging.error('fork #2 failed: %s'.format(err))
        sys.exit(1)
# becoming daemon
    sys.stdout.flush()
    sys.stderr.flush()
    si = open(os.devnull, 'r')
    so = open(os.devnull, 'a+')
    se = open(os.devnull, 'a+')
    os.dup2(si.fileno(), sys.stdin.fileno())
    os.dup2(so.fileno(), sys.stdout.fileno())
    os.dup2(se.fileno(), sys.stderr.fileno())
    logging.info("daemon created")

#   write the pid file 
    pid = str(os.getpid())
    with open('/tmp/pidfile', 'w+') as f:
        f.write(pid + '\n')
    logging.info(" daemon done")


