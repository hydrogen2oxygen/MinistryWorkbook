import datetime

class WorkbookStructure:
	# Description of the entire class
	"The class representing the entire data of one PDF for the Ministry Workbook"
	
	# The title is valid for all weeks
	title = "Our Christian Life and Ministry"
	
	# An array of weeks (each containing one MinistryWeek)
	weeks = []
	
	def toString(self):
		content = "WorkbookStructure:\n" + self.title 
		content += "\n----------------------------\n"
		for week in self.weeks:
			content += week.toString()
			content += "\n"
		return content

class MinistryWeek:
	"One week"
	date = datetime.datetime.now()
	scripture = "Genesis 1-3"
	president = "Smith"
	
	# We know at least 2 types of elements (Detail and Section)
	elements = []
	def toString(self):
		content = "";
		for element in self.elements:
			if len(content) > 0:
				content += "\n"
			content += element.toString()
		return content

class Detail:
	time = datetime.datetime.now()
	topic = "Song 55"
	name = "Johnson"
	def toString(self):
		return self.time.strftime("%H:%M") + " | " + self.topic + " | by " + self.name

class Color:
	"A class representing a color"
	def __init__(self,r=0,g=0,b=0):
		self.red = r
		self.green = g
		self.blue = b
	def toString(self):
		return "color(" + str(self.red) + "," + str(self.green) + "," + str(self.red) + ")"

class Section:
	name = "TREASURES FROM GOD'S WORD"
	# The color of the section is by default a light gray
	color = Color(64,64,64)
	def toString(self):
		return "# " + self.name + " - (" + self.color.toString() + ")"


# We test what we have so far
workbook = WorkbookStructure()
# Insert one week with details and sections
week_one = MinistryWeek()
week_one.scripture = "Revelation 17-19"
week_one.president = "Abraham"
detail_first_song = Detail()
detail_first_song.time = datetime.datetime.strptime('2019-12-27 19:00', '%Y-%m-%d %H:%M')
detail_first_song.name = "Prayer: Davis"
week_one.elements.append(detail_first_song)

# The first section already contains
# the right name and color per default
detail_first_section = Section()
week_one.elements.append(detail_first_section)

#Last but not least we append the first week
# to the workbook object
workbook.weeks.append(week_one)

print(workbook.toString())