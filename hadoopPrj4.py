#! /usr/bin/python

# This hadoopHW4.py python program is designed and created
# to perform the automation of the installation
# and execution of hadoop instance on a Ubuntu 14.04
# Trusty Tahr cloud operating system, offered and 
# initialized through Google Cloud Compute Engine.
# author:GeoWade 

from subprocess import call
 
def scriptGet():

    # part 1: create a bash script to download the 
    # jdk and framework tar archives from dropbox

    # part 1a: a list that contains the commands to be printed
    # to the script and that will be executed by the script
    gtscrp = ['#! /bin/sh', 'mkdir -p -m0755 fetchTmp',
              'cd fetchTmp', 
              'wget https://www.dropbox.com/s/'
              'h6bw3tibft3gs17/jdk-7u21-linux-x64.tar.gz',
              'wget https://www.dropbox.com/s/'
              'znonl6ia1259by3/hadoop-1.1.2.tar.gz', 
              'wget https://www.dropbox.com/s/'
              'gp6t7616wsypkdo/chiu-wordcount2.jar', 
              'wget https://www.dropbox.com/s/'
              'w6yvyg1p57sf6sh/gettysburg.txt', 'cd -',
              'exit']

    gtscrpOpn = open('wgtArchives.sh', 'w')
    for gtscrp1 in gtscrp:
        gtscrpOpn.write(gtscrp1 + "\n\n")
    gtscrpOpn.close()    

    # part 1b: change mode of execution on the script and
    # execute the script
    chsrp = 'chmod 0755 wgtArchives.sh'
    exscrp = './wgtArchives.sh'

    call(chsrp, shell=True)
    call(exscrp, shell=True)

    # part 1c: make the archiveTmp directory
    # move the contents of the fetchTmp diretory to archiveTmp
    # and delete the fetchTmp directory
    mvfetch = ['sudo updatedb',
               'mv fetchTmp/* $HOME/', 
               'rm -rf $HOME/fetchTmp',
               'rm -rf $HOME/wgtArchives.sh',
               'sudo updatedb']

    for fetchmv in mvfetch:
        call(fetchmv, shell=True)

    print 'The archives have been fetched!'
    print 'The archives reside in the archiveTmp dir\n'

def installJdk():
    
    # part 2: create a list of commands to install the jdk,
    # and install the Oracle jdk7u21.

    # part 2a: create a list of commands
    oraLst = ['sudo mkdir -p -m0755 /usr/lib/jvm/jdk1.7.0',
              'tar xvf $HOME/jdk-7u21-linux-x64.tar.gz',
              'sudo updatedb', 
              'sudo mv jdk1.7.0_21/* /usr/lib/jvm/jdk1.7.0/']

    # part 2b: iterate through the oraextlst perform the tasks
    for ora in oraLst:
        call(ora, shell=True)
    
    # part 2c: create variables to run update-alternatives
    ualts = 'sudo update-alternatives --install \"/usr/bin/'
    ualts1 = ' \"'
    ualts2 = ' \"/usr/lib/jvm/jdk1.7.0/bin/'
    ualts3 = ' 1'

    # a list for the individual jdk binaries,
    # each binary followed by a char slash double qoute
    # to encapsulate the in quotation marks
    jdora = ['java\"', 'javac\"', 'jar\"']

    # part 2d: execute the comands to update the alternatives
    for ojdk in jdora:
        call(ualts + ojdk + ualts1 + ojdk + ualts2 + ojdk + ualts3, shell=True)

    # part 2e: remove the extracted folder owned by root
    remjdk = 'sudo rm -rf jdk1.7.0_21'
    call(remjdk, shell=True)
    
    print 'The Oracle 7u21 JDK has been installed and '

    orajdk = ['java', 'javac', 'jar', 'java -version']

    for dora in orajdk:
        call(dora, shell=True)
    
    print 'The Oracle 7u21 JDK has been installed and tested\n'

def confSyCtl():

    # part 3: open the /etc/sysctl.conf file
    ctconsy = 'cat /etc/sysctl.conf > $HOME/sysctl.conf.bak'
    call(ctconsy, shell=True)
    
    confsyLst = ['# disable ipv6', 'net.ipv6.conf.all.disable_ipv6 = 1',
                 'net.ipv6.conf.default.disable_ipv6 = 1',
                 'net.ipv6.conf.lo.disable_ipv6 = 1']

    # DO NOT OVERWRITE THE FILE!! append to the list the file
    confsyOpn = open('sysctl.conf.bak', 'a')
    for confsy1 in confsyLst:
        confsyOpn.write(confsy1 + "\n")
    confsyOpn.close()

    rmold = 'sudo rm -rf /etc/sysctl.conf'

    mvnw = 'sudo mv sysctl.conf.bak /etc/sysctl.conf'

    call(rmold, shell=True)

    call(mvnw, shell=True)

    print 'Print the sysctl configuration\n'

    # to avoid rebooting, the sysctl --system statement
    # will be executed to load the new settings.
    confsyLoad = 'sudo sysctl --system'
    call(confsyLoad, shell=True)

    # print the sysctl.conf configuration
    confsyPrnt = 'sudo sysctl -p'
    call(confsyPrnt, shell=True)  

def hdoopExct():

    # part 4: Extract and move the hadoop frame work
    # part 4a: create a list of commands to perform the extraction
    hdoopLst = ['tar xvf $HOME/hadoop-1.1.2.tar.gz',
                'sudo mv hadoop-1.1.2 /usr/local/hadoop',
                'sudo updatedb']

    for hdoop1 in hdoopLst:
        call(hdoop1, shell=True)

    print 'The hadoop framework has extracted and moved\n'

def bshAdmn():

    # part 5: A list holding the $HOME/.bash_admin source script for
    # hadoop user environment variables  
    bshadmin = ['# ~/.bash_admin for user, admin, and other environment'
                ' variables to be used by bash',
                '# Set Hadoop-related environment variables',
                'export HADOOP_HOME=/usr/local/hadoop',
                'export PIG_HOME=/usr/local/pig',
                'export PIG_CLASSPATH=/usr/local/hadoop/conf',
                '# Set JAVA_HOME (we will also configure JAVA_HOME '
                'directly for Hadoop later on)',
                'export JAVA_HOME=/usr/lib/jvm/jdk1.7.0/',
                '# Some convenient aliases and functions '
                'for running Hadoop-related commands',
                'unalias fs &> /dev/null', 'alias fs="hadoop fs"',
                'unalias hls &> /dev/null', 'alias hls="fs -ls"',
                '# If you have LZO compression enabled in your ' 
                'Hadoop cluster and',
                '# compress job outputs with LZOP '
                '(not covered in this tutorial):',
                '# Conveniently inspect an LZOP compressed file from '
                'the command', '# line; run via:', '#', '# $ lzohead '
                '/hdfs/path/to/lzop/compressed/file.lzo',  '#',
                '# Requires installed \'lzop\' command.', '#', 'lzohead () {', 
                'hadoop fs -cat $1 | lzop -dc | head -1000 | less', '}',
                '# Add Hadoop bin/ directory to PATH',
                'export PATH=$PATH:$HADOOP_HOME/bin',
                'export PATH=$PATH:$PIG_HOME/bin']

    bshadmOpn = open('.bash_admin', 'w')

    for bshadm in bshadmin:
        bshadmOpn.write(bshadm + "\n")
    bshadmOpn.close()
    
    print 'The ~/.bash_admin alias file has been created!\n'

def bshrcAlias():

    bshrcOpn = open('.bashrc', 'a')
    bshrcLst = ['if [ -f \"$HOME/.bash_admin\" ]; then',
                '. "$HOME/.bash_admin"', 'fi']

    for bshr in bshrcLst:
        bshrcOpn.write(bshr + "\n")
    bshrcOpn.close()

def hdoopEnvSh():

     # part 6: append the JAVA_HOME variable to the hdoopEnvSh file
     hdenvshLst = ['# The java implementation to use. Required.',
                   'export JAVA_HOME=/usr/lib/jvm/jdk1.7.0/']

     # DO NOT OVERWRITE! append to the file
     hdenvshOpn = open('/usr/local/hadoop/conf/hadoop-env.sh', 'a')
     for hdenv1 in hdenvshLst:
         hdenvshOpn.write(hdenv1 + "\n")
     hdenvshOpn.close()

     print 'The JAVA_HOME variable has been configured\n'

def coreSite():

    # part 7: create a list for the hadoop/conf/core-site.xml file
    confLst = ['<?xml version=\"1.0\"?>'
               '<?xml-stylesheet type=\"text/xsl\"'
               ' href=\"configuration.xsl\"?>',
               '<!-- Put site-specific property overrides '
               'in this file. -->\n',
               '<configuration>', '<property>',
               ' <name>hadoop.tmp.dir</name>',
               ' <value>/app/hadoop/tmp</value>',
               ' <description>A base for other temporary'
               ' directories.</description>',
               '</property>\n',
               '<property>',
               ' <name>fs.default.name</name>',
               ' <value>hdfs://localhost:54310</value>',
               ' <description>The name of the default file system.'
               ' A URI whose',
               ' scheme and authority determine the'
               ' FileSystem implementation. The',
               ' uri\'s scheme determines the config '
               ' property (fs.SCHEME.impl) naming',
               ' the FileSystem implementation class. '
               ' The uri\'s authority is used to',
               ' determine the host, port, etc. for a'
               ' filesystem.</description>',
               '</property>','</configuration>']

    # part 7a: write the contents of the list to the file
    corsit = open('/usr/local/hadoop/conf/core-site.xml', 'w')
    for corsit1 in confLst:
        corsit.write(corsit1+"\n") 
    corsit.close()

    print 'The core-site.xml file has been configured.\n'

def mapRed():

    # part 8: write the xml configuration to the hadoop/conf/mapred-site.xml
    mapRedList = ['<?xml version=\"1.0\"?>'
                  '<?xml-stylesheet type=\"text/xsl\"'
                  ' href=\"configuration.xsl\"?>',
                  '<!-- Put site-specific property '
                  'overrides in this file. -->\n',
                  '<configuration>', ' <property>',
                  ' <name>mapred.job.tracker</name>',
                  ' <value>localhost:54311</value>',
                  ' <description>The host and port that the MapReduce '
                  'job tracker runs',
                  ' at. If \"local\", then jobs are run in-process '
                  'as a single map and reduce task.',
                  ' </description>',
                  '</property>', '</configuration>']

    mapredFila = open('/usr/local/hadoop/conf/mapred-site.xml', 'w')
    for mapred1 in mapRedList:
        mapredFila.write(mapred1 + "\n")
    mapredFila.close()

    print 'The mapred-site.xml file has been configured.'

def hdfsSite():

    # part 9: write the xml configuration for the hdfs-site.xml file
    hdfsLst = ['<?xml version=\"1.0\"?>'
               '<?xml-stylesheet type=\"text/xsl\"'
               ' href=\"configuration.xsl\"?>',
               '<!-- Put site-specific property '
               'overrides in this file. -->\n',
               '<configuration>', ' <property>',
               ' <name>dfs.replication</name>',
               ' <value>1</value>',
               ' <description>Default block replication.',
               ' The actual number of replications can be '
               'specified when the file is created.',
               ' The default is used if replication is not '
               'specified in create time.',
               ' </description>', '</property>', '</configuration>']

    hdfsFila = open('/usr/local/hadoop/conf/hdfs-site.xml', 'w')
    for hdfs1 in hdfsLst:
        hdfsFila.write(hdfs1 + "\n")
    hdfsFila.close()

    print 'The hdfs-site.xml file has been configured.'

def hdoopUsr():
    
    # part 10: create a tmp directory for the hadoop user
    doopUsrLst = ['sudo updatedb', 'sudo groupadd hadoop',
                  'sudo mv chiu-wordcount2.jar /usr/local/hadoop/bin/',
                  'sudo mkdir -p /app/hadoop/tmp',
                  'sudo chown -R hduser:hadoop /app/hadoop/tmp',
                  'sudo chmod 755 /app/hadoop/tmp',
                  'sudo chown -R hduser:hadoop /usr/local/hadoop',
                  'sudo updatedb']

    for doopUsr1 in doopUsrLst:
        call(doopUsr1, shell=True)

def hdoopStart():

    # part 11: get the gettysburg file and run hadoop
    formLst = ['/usr/local/hadoop/bin/hadoop namenode -format',
               '/usr/local/hadoop/bin/start-all.sh',
               '/usr/local/hadoop/bin/hadoop fs -put gettysburg.txt'
               ' /user/hduser/getty/gettysburg.txt',
               '/usr/local/hadoop/bin/hadoop'
               ' fs -rmr /user/hduser/getty/gettysburg.txt']

    for lstForm in formLst:
        call(lstForm, shell=True)

def gettysburg():
              
    burgLst = ['#! /bin/bash',
               'wrdcnt=\"/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/bin/chiu-wordcount2.jar WordCount /user/'
               'hduser/getty/gettysburg.txt /user/hduser/getty/out\"',
               'cntout=\"/usr/local/hadoop/bin/hadoop fs -cat /user/hduser/getty/out/part-r-00000\"',
               '/usr/local/hadoop/bin/hadoop fs -put gettysburg.txt /user/hduser/getty/gettysburg.txt',
               'sudo updatedb',
               '$wrdcnt', '$cntout', 'cd -', 
               'exit']

    getout1 = open('gettysburg.sh', 'w')

    for gett1 in burgLst:
        getout1.write(gett1 + "\n\n")
    getout1.close()

    # chmsh = 'chmod +x runburg.sh'
    # call(chmsh, shell=True)
   
    print 'Hadoop has been retrieved, installed, and configured!\ndone.'

def main():

    scriptGet()

    installJdk()

    confSyCtl()

    hdoopExct()

    bshAdmn()

    bshrcAlias()
    
    hdoopEnvSh()
    
    coreSite()
    
    mapRed()
    
    hdfsSite()

    hdoopUsr()

    hdoopStart()
    
    gettysburg()
    
    print 'To test hadoop and mapreducePlease run the runburg.sh script!'

main()

