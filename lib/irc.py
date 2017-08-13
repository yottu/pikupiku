import sys
import socket
import string


class irc(object):
    ''' source: http://archive.oreilly.com/pub/h/1968 '''
    def __init__(self, host, port, nick, oauth, channel, subtitle):
	self.host = host
	self.port = port
	self.nick = nick
	self.oauth = oauth
	self.channel = channel
	self.subtitle = subtitle

    def connect(self):
        s=socket.socket()
        s.connect((self.host, self.port))
        s.send("PASS " + self.oauth + "\r\n")
        s.send("NICK " + self.nick + "\r\n")
        s.send("JOIN " + self.channel + "\r\n")
        print(s.recv(1024))
        print("Connected to " + str(s.getpeername()))
        readbuffer = ""

        while True:
		readbuffer=readbuffer+s.recv(1024)
#		print(readbuffer)
		temp=string.split(readbuffer, "\n")
		readbuffer=temp.pop( )

		for line in temp:
			line=string.rstrip(line)
			line=string.split(line)

                        try:
    			    if (line[2] == self.channel):
			        comment = ' '.join(line[3:])[1:]
			except Exception as e:
			    print str(e)

			print comment
			self.subtitle.subfile_append(comment)

			if(line[0]=="PING"):
				s.send("PONG %s\r\n" % line[1])
