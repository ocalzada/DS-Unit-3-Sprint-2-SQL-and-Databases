#PART TWO
# establish connection with DB
sl3_conn = sqlite3.connect('northwind_small.sqlite3')

# create connection cursor
sl3_curs = sl3_conn.cursor()

sl3_curs.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY
name;").fetchall()

[('Category',), ('Customer',), ('CustomerCustomerDemo',), ('CustomerDemographic',), ('Employee',), 
('EmployeeTerritory',), ('Order',), ('OrderDetail',), ('Product',), ('Region',), ('Shipper',), ('Supplier',), 
('Territory',)]

# Q1: What are the ten most expensive items (per unit price) in the database?
sl3_curs.execute('SELECT ProductName, UnitPrice FROM product ORDER BY UnitPrice DESC LIMIT 10;').fetchall()

# Top 10 most expensive items per unit price.
[('Côte de Blaye', 263.5), ('Thüringer Rostbratwurst', 123.79), ('Mishi Kobe Niku', 97), ("Sir Rodney's Marmalade", 81), 
('Carnarvon Tigers', 62.5), ('Raclette Courdavault', 55), ('Manjimup Dried Apples', 53), ('Tarte au sucre', 49.3), 
('Ipoh Coffee', 46), ('Rössle Sauerkraut', 45.6)]

#Q2: What is the average age of an employee at the time of their hiring?
sl3_curs.execute('SELECT AVG(HireDate - BirthDate) AS avg_age FROM Employee;').fetchall()

# average age of employees when hired
[(37.22222222222222,)]

#Q3: (Stretch) How does the average age of employee at hire vary by city?
sl3_curs.execute('SELECT city, AVG(HireDate - BirthDate) AS avg_age FROM Employee GROUP BY city;').fetchall()

# average age when hired by city
[('Kirkland', 29.0), ('London', 32.5), ('Redmond', 56.0), ('Seattle', 40.0), ('Tacoma', 40.0)]


# PART THREE
# Q1: What are the ten most expensive items (per unit price) in the database and their suppliers?
sl3_curs.execute('SELECT p.id, p.productname, p.unitprice, s.companyname FROM product as p, supplier as')

# TOP 10 most expensive items and their suppliers
[(29, 'Thüringer Rostbratwurst', 123.79, "Forêts d'érables"), (9, 'Mishi Kobe Niku', 97, 'PB Knäckebröd AB'), 
(20, "Sir Rodney's Marmalade", 81, 'Leka Trading'), (18, 'Carnarvon Tigers', 62.5, 'Aux joyeux ecclésiastiques'), 
(28, 'Rössle Sauerkraut', 45.6, 'Gai pâturage'), (27, 'Schoggi Schokolade', 43.9, 'Escargots Nouveaux'), 
(8, 'Northwoods Cranberry Sauce', 40, 'Specialty Biscuits, Ltd.'), (17, 'Alice Mutton', 39, 'Svensk Sjöföda AB'), 
(12, 'Queso Manchego La Pastora', 38, 'Plutzer Lebensmittelgroßmärkte AG'), (26, 'Gumbär Gummibärchen', 31.23, 'Pasta Buttini s.r.l.')]

# Q2: What is the largest category (by number of unique products in it)?
sl3_curs.execute('SELECT c.CategoryName, COUNT(DISTINCT p.ProductName) AS num_products FROM category AS c, product AS p WHERE c.Id = p.CategoryId GROUP BY c.CategoryName ORDER BY num_products DESC LIMIT 1;').fetchall()

# Largest Category by number of unique products in it
[('Confections', 13)]

# Q3: (Stretch) Who's the employee with the most territories?
sl3_curs.execute('SELECT Employee.Id, Employee.LastName, Employee.FirstName, COUNT(EmployeeTerritory.TerritoryID) as num_territory FROM Employee, EmployeeTerritory WHERE Employee.Id = EmployeeTerritory.EmployeeId GROUP BY Employee.ID ORDER BY num_territory DESC LIMIT 1;').fetchall()
# Employee with most Territories:
[(7, 'King', 'Robert', 10)]

