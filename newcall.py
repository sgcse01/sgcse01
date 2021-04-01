import os, sys, callee, time, signal, logging


def run():
#start the daemon    
    callee.testfunc()
    while True:
        time.sleep(1)

def stop():

    """Stop the daemon."""
    logging.basicConfig(filename='kill.log',format='%(asctime)s %(message)s', encoding='utf-8', level=logging.DEBUG)
    # Get the pid from the pidfile
    try:
        with open('/tmp/pidfile','r') as pf:
            pid = int(pf.read().strip())
    except IOError:
        pid = None

    if not pid:
        logging.error("pid file does not")
        return # not an error in a restart

        # Try killing the daemon process
    try:
        while 1:
            os.kill(pid, signal.SIGTERM)
            time.sleep(0.1)
            os.remove('/tmp/pidfile')
            logging.info("daemon is stopped")
    except OSError as err:
        e = str(err.args)
        if e.find("No such process") > 0:
            if os.path.exists('/tmp/pidfile'):
                os.remove('/tmp/pidfile')
        else:
            print (str(err.args))
            sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            run()
        elif 'stop' == sys.argv[1]:
            stop()
    else:
        print("usage is newcall.py start|stop")
   
