import WorkbookStructure as wb

class MinistryWorkbook:
	"MinistryWorkbook main class"
	workbook = wb.WorkbookStructure()
	finished = False
	
	print("Welcome to MinistryWorkbook v1.0")
	print("--------------------------------")
	print("Commands:")
	print("exit - quit the program")
	print("--------------------------------")
	
	# CLI Input Output Loop
	while finished is False:
		command = input('> ')
		
		if command == "exit":
			finished = True

			
			


			