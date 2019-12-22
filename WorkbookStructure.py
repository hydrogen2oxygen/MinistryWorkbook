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

class Color:
	"A class representing a color"
	def __init__(self,r=0,g=0,b=0):
		self.red = r
		self.green = g
		self.blue = b
	def toString(self):
		content = "color(" + str(self.red) + ","
		content += str(self.green) + "," + str(self.red) + ")" 
		return content
		
class Detail:
	time = datetime.datetime.now()
	topic = "Song 55"
	name = None
	color = None
	def toString(self):
		content = self.time.strftime("%H:%M") + " | "
		content += self.topic
		if self.name is not None:
			content += " | by " + self.name
		if self.color is not None:
			content += " - (" + self.color.toString() + ")"
		return content