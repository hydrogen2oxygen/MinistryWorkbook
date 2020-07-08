import WorkbookStructure as wb

class MinistryWorkbook:
	"MinistryWorkbook main class"
	workbook = None
	
	def printHelp(self):
		print("Welcome to MinistryWorkbook v1.0")
		print("--------------------------------")
		print("Commands:")
		print("new book      - new ministry workbook")
		print("new week      - creates a new week for the workbook")
		print("open book     - opens a saved book")
		print("show          - overview of the entire workbook")
		print("show week     - overview of the week")
		print("list books    - list of all saved books")
		print("add detail    - creates details")
		print("update detail - change the detail")
		print("delete detail - deletes the specific detail")
		print("exit          - quit the program")
		print("--------------------------------")

	def newBook(self):
		self.workbook = wb.WorkbookStructure()

	def cli_transformDateFromString(self,dateString):
		dateObject = None
		#try:
		#	dateObject = datetime.datetime.strptime(dateString, '%Y-%m-%d')
		#except error:
		#	print("Date " + dateString + " cannot be transformed into an object (does not have the right format like yyyy-mm-dd)!"
		return dateObject

	def show(self):
		print(self.workbook.toString())

	# CLI Input Output Loop
	def commandLoop(self):
		finished = False

		while finished is False:
			command = input('> ')
			
			if command == "exit":
				finished = True
			
			if command == "new book":
				self.newBook()
				newTitle = input("> TITLE [" +self.workbook.title + "] = ")
				newDate = input("> START DATE [Format " + self.workbook.startDate.strftime("%Y-%m-%d") + "]:")
				if len(newTitle) > 0:
					self.workbook.title = newTitle
				if newDate is not None:
					newDateObject = self.cli_transformDateFromString(newDate)
					if newDateObject is not None:
						self.workbook.startDate = newDateObject

				print("new book inserted")
				self.show()

			if command == "show":
				self.show()

mw = MinistryWorkbook()
mw.printHelp()
mw.commandLoop()