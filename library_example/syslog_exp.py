import syslog, os

def initsyslog():
    syslog.openlog("%s[%d]" % (os.path.basename(sys.argv[0]), os.getpid()), 0, syslog.LOG_DAEMON)
    syslog.syslog("Started")

initsyslog()