from __future__ import division
import time

class subtitle(object):
	def __init__(self, subfile_location):
		self.subfile = subfile_location
		self.subfile_start = None
		self.subfile_lasttime = None # Time last sub got displayed
		self.append_to_subfile = True # Write new comment to subfile
		self.subfile_count = 0 # Number of comments in live subfile

                self.create_sub(self.subfile)



	def subfile_append(self, com):
		''' Output comment to subfile when streaming a video '''
		if self.append_to_subfile:
			
			with open(self.subfile, 'a',) as fh:
			        #print("Appending " + com)
				# FIXME replace hardcoded 5 with subtitle display duration
				xpos = str((self.subfile_count*100+20)%1024)
				
				# ceil of comment length divided by 50 # FIXME hard coded 50
				try:
    				    for i in range(0, -(-len(com))//50+1):
				            #print("In for loop for " + com)
				            fh.write("Dialogue: 0," + self.subfile_time(time.time()+1*i) +"," + self.subfile_time(int(time.time())+4*(i+1)) + ",testStyle,,")
					    fh.write('0000,0000,0000,,{\\move(1440,'
							+ xpos + ',-512,' + xpos + ')}{\\fad(1000,1000)}')
					    fh.write(com[i*50:(i+1)*50]) # TODO FIXME Security
					    fh.write("\n")
				except Exception as e:
				    print str(e)
					
				self.subfile_count += 1
		
	
	def subfile_time(self, thetime):
		''' return time formatted for subtitle file (HH:MM:SS.MS) '''
		
		# seconds since last subtitle was displayed
		self.subfile_lasttime = int(thetime) - int(self.subfile_start)
		
		sec_format = str("%02i" % ((self.subfile_lasttime)%60))
		min_format = str("%02i" % ((self.subfile_lasttime/60)%60))
		hour_format = str("%02i" % ((self.subfile_lasttime/60/60)%99))
        	ms_shift = str("%02i" % ((self.subfile_count*30)%99))
		time_formatted = hour_format + ":" + min_format + ":" + sec_format + "." + ms_shift
		return time_formatted
	

	def create_sub(self, subfile):
		''' create a subfile for overlaying comments over webm '''
		self.subfile = subfile
		self.subfile_start = time.time()
		try:
				with open(subfile, 'w') as fh:
					fh.write(u"[Script Info]\n# Thank you Liisachan from forum.doom9.org\n".encode('utf-8'))
					fh.write("ScriptType: v4.00+\nCollisions: Reverse\nPlayResX: 1280\n")
					fh.write("PlayResY: 1024\nTimer: 100.0000\n\n")
					fh.write("[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, ")
					fh.write("SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, ")
					fh.write("StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, ")
					fh.write("Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\n")
					fh.write("Style: testStyle,Verdana,48,&H40ffffff,&H00000000,&Hc0000000")
					fh.write(",&H00000000,-1,0,0,0,100,100,0,0.00,1,1,0,8,0,0,0,0\n")
					fh.write("[Events]\nFormat: Layer, Start, End, Style, Actor, MarginL, ")
					fh.write("MarginR, MarginV, Effect, Text\n")
					fh.write("Dialogue: 0,00:00:00.00,00:00:05.00,testStyle,,")
					fh.write('0000,0000,0000,,{\\move(1440,120,-512,120)}{\\fad(1000,1000)}')
					fh.write("pikupiku \o/")
					fh.write("\n") 
		except Exception as e:
		        print str(e)
		
		return True
