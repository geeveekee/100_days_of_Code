from prettytable import PrettyTable

my_table = PrettyTable(field_names=['Student Name', 'Class', 'Section', 'Percentage'])

my_table.add_row(['Leonard', 'X', 'B', '91.2%'])
my_table.add_row(['Harry', 'X', 'C', '63.5%'])
my_table.add_row(['Ron', 'X', 'A', '90.23%'])
my_table.add_row(['Sheldon', 'X', 'B', '92.7%'])
my_table.add_row(['Hermione', 'X', 'D', '98.2.2%'])
my_table.add_row(['Oswald', 'X', 'B', '95.0%'])

print(my_table)