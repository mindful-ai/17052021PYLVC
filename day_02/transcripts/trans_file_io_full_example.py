Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> path = r"C:\Users\Purushotham\Desktop\oracle\day_02\transcripts\data.txt"
>>> f = open(path)
>>> content = f.readlines()
>>> content
['OrderDate\n', '\n', 'Region\n', '\n', 'Rep\n', '\n', 'Item\n', '\n', 'Units\n', '\n', 'UnitCost\n', '\n', 'Total\n', '\n', '1/6/2020\n', '\n', 'East\n', '\n', 'Jones\n', '\n', 'Pencil\n', '\n', '95\n', '\n', '1.99\n', '\n', '189.05\n', '\n', '1/23/2020\n', '\n', 'Central\n', '\n', 'Kivell\n', '\n', 'Binder\n', '\n', '50\n', '\n', '19.99\n', '\n', '999.50\n', '\n', '2/9/2020\n', '\n', 'Central\n', '\n', 'Jardine\n', '\n', 'Pencil\n', '\n', '36\n', '\n', '4.99\n', '\n', '179.64\n', '\n', '2/26/2020\n', '\n', 'Central\n', '\n', 'Gill\n', '\n', 'Pen\n', '\n', '27\n', '\n', '19.99\n', '\n', '539.73\n', '\n', '3/15/2020\n', '\n', 'West\n', '\n', 'Sorvino\n', '\n', 'Pencil\n', '\n', '56\n', '\n', '2.99\n', '\n', '167.44\n', '\n', '4/1/2020\n', '\n', 'East\n', '\n', 'Jones\n', '\n', 'Binder\n', '\n', '60\n', '\n', '4.99\n', '\n', '299.40\n', '\n', '4/18/2020\n', '\n', 'Central\n', '\n', 'Andrews\n', '\n', 'Pencil\n', '\n', '75\n', '\n', '1.99\n', '\n', '149.25\n', '\n', '5/5/2020\n', '\n', 'Central\n', '\n', 'Jardine\n', '\n', 'Pencil\n', '\n', '90\n', '\n', '4.99\n', '\n', '449.10\n', '\n', '5/22/2020\n', '\n', 'West\n', '\n', 'Thompson\n', '\n', 'Pencil\n', '\n', '32\n', '\n', '1.99\n', '\n', '63.68\n', '\n', '6/8/2020\n', '\n', 'East\n', '\n', 'Jones\n', '\n', 'Binder\n', '\n', '60\n', '\n', '8.99\n', '\n', '539.40\n', '\n', '6/25/2020\n', '\n', 'Central\n', '\n', 'Morgan\n', '\n', 'Pencil\n', '\n', '90\n', '\n', '4.99\n', '\n', '449.10\n', '\n', '7/12/2020\n', '\n', 'East\n', '\n', 'Howard\n', '\n', 'Binder\n', '\n', '29\n', '\n', '1.99\n', '\n', '57.71\n', '\n', '7/29/2020\n', '\n', 'East\n', '\n', 'Parent\n', '\n', 'Binder\n', '\n', '81\n', '\n', '19.99\n', '\n', '1,619.19\n', '\n', '8/15/2020\n', '\n', 'East\n', '\n', 'Jones\n', '\n', 'Pencil\n', '\n', '35\n', '\n', '4.99\n', '\n', '174.65\n', '\n', '9/1/2020\n', '\n', 'Central\n', '\n', 'Smith\n', '\n', 'Desk\n', '\n', '2\n', '\n', '125.00\n', '\n', '250.00\n', '\n', '9/18/2020\n', '\n', 'East\n', '\n', 'Jones\n', '\n', 'Pen Set\n', '\n', '16\n', '\n', '15.99\n', '\n', '255.84\n', '\n', '10/5/2020\n', '\n', 'Central\n', '\n', 'Morgan\n', '\n', 'Binder\n', '\n', '28\n', '\n', '8.99\n', '\n', '251.72\n', '\n', '10/22/2020\n', '\n', 'East\n', '\n', 'Jones\n', '\n', 'Pen\n', '\n', '64\n', '\n', '8.99\n', '\n', '575.36\n', '\n', '11/8/2020\n', '\n', 'East\n', '\n', 'Parent\n', '\n', 'Pen\n', '\n', '15\n', '\n', '19.99\n', '\n', '299.85\n', '\n', '11/25/2020\n', '\n', 'Central\n', '\n', 'Kivell\n', '\n', 'Pen Set\n', '\n', '96\n', '\n', '4.99\n', '\n', '479.04\n', '\n', '12/12/2020\n', '\n', 'Central\n', '\n', 'Smith\n', '\n', 'Pencil\n', '\n', '67\n', '\n', '1.29\n', '\n', '86.43\n', '\n', '12/29/2020\n', '\n', 'East\n', '\n', 'Parent\n', '\n', 'Pen Set\n', '\n', '74\n', '\n', '15.99\n', '\n', '1,183.26\n', '\n', '1/15/2021\n', '\n', 'Central\n', '\n', 'Gill\n', '\n', 'Binder\n', '\n', '46\n', '\n', '8.99\n', '\n', '413.54\n', '\n', '2/1/2021\n', '\n', 'Central\n', '\n', 'Smith\n', '\n', 'Binder\n', '\n', '87\n', '\n', '15.00\n', '\n', '1,305.00\n', '\n', '2/18/2021\n', '\n', 'East\n', '\n', 'Jones\n', '\n', 'Binder\n', '\n', '4\n', '\n', '4.99\n', '\n', '19.96\n', '\n', '3/7/2021\n', '\n', 'West\n', '\n', 'Sorvino\n', '\n', 'Binder\n', '\n', '7\n', '\n', '19.99\n', '\n', '139.93\n', '\n', '3/24/2021\n', '\n', 'Central\n', '\n', 'Jardine\n', '\n', 'Pen Set\n', '\n', '50\n', '\n', '4.99\n', '\n', '249.50\n', '\n', '4/10/2021\n', '\n', 'Central\n', '\n', 'Andrews\n', '\n', 'Pencil\n', '\n', '66\n', '\n', '1.99\n', '\n', '131.34\n', '\n', '4/27/2021\n', '\n', 'East\n', '\n', 'Howard\n', '\n', 'Pen\n', '\n', '96\n', '\n', '4.99\n', '\n', '479.04\n', '\n', '5/14/2021\n', '\n', 'Central\n', '\n', 'Gill\n', '\n', 'Pencil\n', '\n', '53\n', '\n', '1.29\n', '\n', '68.37\n', '\n', '5/31/2021\n', '\n', 'Central\n', '\n', 'Gill\n', '\n', 'Binder\n', '\n', '80\n', '\n', '8.99\n', '\n', '719.20\n', '\n', '6/17/2021\n', '\n', 'Central\n', '\n', 'Kivell\n', '\n', 'Desk\n', '\n', '5\n', '\n', '125.00\n', '\n', '625.00\n', '\n', '7/4/2021\n', '\n', 'East\n', '\n', 'Jones\n', '\n', 'Pen Set\n', '\n', '62\n', '\n', '4.99\n', '\n', '309.38\n', '\n', '7/21/2021\n', '\n', 'Central\n', '\n', 'Morgan\n', '\n', 'Pen Set\n', '\n', '55\n', '\n', '12.49\n', '\n', '686.95\n', '\n', '8/7/2021\n', '\n', 'Central\n', '\n', 'Kivell\n', '\n', 'Pen Set\n', '\n', '42\n', '\n', '23.95\n', '\n', '1,005.90\n', '\n', '8/24/2021\n', '\n', 'West\n', '\n', 'Sorvino\n', '\n', 'Desk\n', '\n', '3\n', '\n', '275.00\n', '\n', '825.00\n', '\n', '9/10/2021\n', '\n', 'Central\n', '\n', 'Gill\n', '\n', 'Pencil\n', '\n', '7\n', '\n', '1.29\n', '\n', '9.03\n', '\n', '9/27/2021\n', '\n', 'West\n', '\n', 'Sorvino\n', '\n', 'Pen\n', '\n', '76\n', '\n', '1.99\n', '\n', '151.24\n', '\n', '10/14/2021\n', '\n', 'West\n', '\n', 'Thompson\n', '\n', 'Binder\n', '\n', '57\n', '\n', '19.99\n', '\n', '1,139.43\n', '\n', '10/31/2021\n', '\n', 'Central\n', '\n', 'Andrews\n', '\n', 'Pencil\n', '\n', '14\n', '\n', '1.29\n', '\n', '18.06\n', '\n', '11/17/2021\n', '\n', 'Central\n', '\n', 'Jardine\n', '\n', 'Binder\n', '\n', '11\n', '\n', '4.99\n', '\n', '54.89\n', '\n', '12/4/2021\n', '\n', 'Central\n', '\n', 'Jardine\n', '\n', 'Binder\n', '\n', '94\n', '\n', '19.99\n', '\n', '1,879.06\n', '\n', '12/21/2021\n', '\n', 'Central\n', '\n', 'Andrews\n', '\n', 'Binder\n', '\n', '28\n', '\n', '4.99\n', '\n', '139.72\n', '\n']
>>> f.seek(0)
0
>>> c2 = f.read()
>>> f.close()
>>> c2
'OrderDate\n\nRegion\n\nRep\n\nItem\n\nUnits\n\nUnitCost\n\nTotal\n\n1/6/2020\n\nEast\n\nJones\n\nPencil\n\n95\n\n1.99\n\n189.05\n\n1/23/2020\n\nCentral\n\nKivell\n\nBinder\n\n50\n\n19.99\n\n999.50\n\n2/9/2020\n\nCentral\n\nJardine\n\nPencil\n\n36\n\n4.99\n\n179.64\n\n2/26/2020\n\nCentral\n\nGill\n\nPen\n\n27\n\n19.99\n\n539.73\n\n3/15/2020\n\nWest\n\nSorvino\n\nPencil\n\n56\n\n2.99\n\n167.44\n\n4/1/2020\n\nEast\n\nJones\n\nBinder\n\n60\n\n4.99\n\n299.40\n\n4/18/2020\n\nCentral\n\nAndrews\n\nPencil\n\n75\n\n1.99\n\n149.25\n\n5/5/2020\n\nCentral\n\nJardine\n\nPencil\n\n90\n\n4.99\n\n449.10\n\n5/22/2020\n\nWest\n\nThompson\n\nPencil\n\n32\n\n1.99\n\n63.68\n\n6/8/2020\n\nEast\n\nJones\n\nBinder\n\n60\n\n8.99\n\n539.40\n\n6/25/2020\n\nCentral\n\nMorgan\n\nPencil\n\n90\n\n4.99\n\n449.10\n\n7/12/2020\n\nEast\n\nHoward\n\nBinder\n\n29\n\n1.99\n\n57.71\n\n7/29/2020\n\nEast\n\nParent\n\nBinder\n\n81\n\n19.99\n\n1,619.19\n\n8/15/2020\n\nEast\n\nJones\n\nPencil\n\n35\n\n4.99\n\n174.65\n\n9/1/2020\n\nCentral\n\nSmith\n\nDesk\n\n2\n\n125.00\n\n250.00\n\n9/18/2020\n\nEast\n\nJones\n\nPen Set\n\n16\n\n15.99\n\n255.84\n\n10/5/2020\n\nCentral\n\nMorgan\n\nBinder\n\n28\n\n8.99\n\n251.72\n\n10/22/2020\n\nEast\n\nJones\n\nPen\n\n64\n\n8.99\n\n575.36\n\n11/8/2020\n\nEast\n\nParent\n\nPen\n\n15\n\n19.99\n\n299.85\n\n11/25/2020\n\nCentral\n\nKivell\n\nPen Set\n\n96\n\n4.99\n\n479.04\n\n12/12/2020\n\nCentral\n\nSmith\n\nPencil\n\n67\n\n1.29\n\n86.43\n\n12/29/2020\n\nEast\n\nParent\n\nPen Set\n\n74\n\n15.99\n\n1,183.26\n\n1/15/2021\n\nCentral\n\nGill\n\nBinder\n\n46\n\n8.99\n\n413.54\n\n2/1/2021\n\nCentral\n\nSmith\n\nBinder\n\n87\n\n15.00\n\n1,305.00\n\n2/18/2021\n\nEast\n\nJones\n\nBinder\n\n4\n\n4.99\n\n19.96\n\n3/7/2021\n\nWest\n\nSorvino\n\nBinder\n\n7\n\n19.99\n\n139.93\n\n3/24/2021\n\nCentral\n\nJardine\n\nPen Set\n\n50\n\n4.99\n\n249.50\n\n4/10/2021\n\nCentral\n\nAndrews\n\nPencil\n\n66\n\n1.99\n\n131.34\n\n4/27/2021\n\nEast\n\nHoward\n\nPen\n\n96\n\n4.99\n\n479.04\n\n5/14/2021\n\nCentral\n\nGill\n\nPencil\n\n53\n\n1.29\n\n68.37\n\n5/31/2021\n\nCentral\n\nGill\n\nBinder\n\n80\n\n8.99\n\n719.20\n\n6/17/2021\n\nCentral\n\nKivell\n\nDesk\n\n5\n\n125.00\n\n625.00\n\n7/4/2021\n\nEast\n\nJones\n\nPen Set\n\n62\n\n4.99\n\n309.38\n\n7/21/2021\n\nCentral\n\nMorgan\n\nPen Set\n\n55\n\n12.49\n\n686.95\n\n8/7/2021\n\nCentral\n\nKivell\n\nPen Set\n\n42\n\n23.95\n\n1,005.90\n\n8/24/2021\n\nWest\n\nSorvino\n\nDesk\n\n3\n\n275.00\n\n825.00\n\n9/10/2021\n\nCentral\n\nGill\n\nPencil\n\n7\n\n1.29\n\n9.03\n\n9/27/2021\n\nWest\n\nSorvino\n\nPen\n\n76\n\n1.99\n\n151.24\n\n10/14/2021\n\nWest\n\nThompson\n\nBinder\n\n57\n\n19.99\n\n1,139.43\n\n10/31/2021\n\nCentral\n\nAndrews\n\nPencil\n\n14\n\n1.29\n\n18.06\n\n11/17/2021\n\nCentral\n\nJardine\n\nBinder\n\n11\n\n4.99\n\n54.89\n\n12/4/2021\n\nCentral\n\nJardine\n\nBinder\n\n94\n\n19.99\n\n1,879.06\n\n12/21/2021\n\nCentral\n\nAndrews\n\nBinder\n\n28\n\n4.99\n\n139.72\n\n'
>>> type(c2)
<class 'str'>
>>> type(content)
<class 'list'>
>>> print(c2)

>>> 
>>> 
>>> # ------------------ process c2
>>> 
>>> clean2 = c2.split("\n\n")
>>> clean2
['OrderDate', 'Region', 'Rep', 'Item', 'Units', 'UnitCost', 'Total', '1/6/2020', 'East', 'Jones', 'Pencil', '95', '1.99', '189.05', '1/23/2020', 'Central', 'Kivell', 'Binder', '50', '19.99', '999.50', '2/9/2020', 'Central', 'Jardine', 'Pencil', '36', '4.99', '179.64', '2/26/2020', 'Central', 'Gill', 'Pen', '27', '19.99', '539.73', '3/15/2020', 'West', 'Sorvino', 'Pencil', '56', '2.99', '167.44', '4/1/2020', 'East', 'Jones', 'Binder', '60', '4.99', '299.40', '4/18/2020', 'Central', 'Andrews', 'Pencil', '75', '1.99', '149.25', '5/5/2020', 'Central', 'Jardine', 'Pencil', '90', '4.99', '449.10', '5/22/2020', 'West', 'Thompson', 'Pencil', '32', '1.99', '63.68', '6/8/2020', 'East', 'Jones', 'Binder', '60', '8.99', '539.40', '6/25/2020', 'Central', 'Morgan', 'Pencil', '90', '4.99', '449.10', '7/12/2020', 'East', 'Howard', 'Binder', '29', '1.99', '57.71', '7/29/2020', 'East', 'Parent', 'Binder', '81', '19.99', '1,619.19', '8/15/2020', 'East', 'Jones', 'Pencil', '35', '4.99', '174.65', '9/1/2020', 'Central', 'Smith', 'Desk', '2', '125.00', '250.00', '9/18/2020', 'East', 'Jones', 'Pen Set', '16', '15.99', '255.84', '10/5/2020', 'Central', 'Morgan', 'Binder', '28', '8.99', '251.72', '10/22/2020', 'East', 'Jones', 'Pen', '64', '8.99', '575.36', '11/8/2020', 'East', 'Parent', 'Pen', '15', '19.99', '299.85', '11/25/2020', 'Central', 'Kivell', 'Pen Set', '96', '4.99', '479.04', '12/12/2020', 'Central', 'Smith', 'Pencil', '67', '1.29', '86.43', '12/29/2020', 'East', 'Parent', 'Pen Set', '74', '15.99', '1,183.26', '1/15/2021', 'Central', 'Gill', 'Binder', '46', '8.99', '413.54', '2/1/2021', 'Central', 'Smith', 'Binder', '87', '15.00', '1,305.00', '2/18/2021', 'East', 'Jones', 'Binder', '4', '4.99', '19.96', '3/7/2021', 'West', 'Sorvino', 'Binder', '7', '19.99', '139.93', '3/24/2021', 'Central', 'Jardine', 'Pen Set', '50', '4.99', '249.50', '4/10/2021', 'Central', 'Andrews', 'Pencil', '66', '1.99', '131.34', '4/27/2021', 'East', 'Howard', 'Pen', '96', '4.99', '479.04', '5/14/2021', 'Central', 'Gill', 'Pencil', '53', '1.29', '68.37', '5/31/2021', 'Central', 'Gill', 'Binder', '80', '8.99', '719.20', '6/17/2021', 'Central', 'Kivell', 'Desk', '5', '125.00', '625.00', '7/4/2021', 'East', 'Jones', 'Pen Set', '62', '4.99', '309.38', '7/21/2021', 'Central', 'Morgan', 'Pen Set', '55', '12.49', '686.95', '8/7/2021', 'Central', 'Kivell', 'Pen Set', '42', '23.95', '1,005.90', '8/24/2021', 'West', 'Sorvino', 'Desk', '3', '275.00', '825.00', '9/10/2021', 'Central', 'Gill', 'Pencil', '7', '1.29', '9.03', '9/27/2021', 'West', 'Sorvino', 'Pen', '76', '1.99', '151.24', '10/14/2021', 'West', 'Thompson', 'Binder', '57', '19.99', '1,139.43', '10/31/2021', 'Central', 'Andrews', 'Pencil', '14', '1.29', '18.06', '11/17/2021', 'Central', 'Jardine', 'Binder', '11', '4.99', '54.89', '12/4/2021', 'Central', 'Jardine', 'Binder', '94', '19.99', '1,879.06', '12/21/2021', 'Central', 'Andrews', 'Binder', '28', '4.99', '139.72', '']
>>> 
>>> 
>>> # ----------------------- process content
>>> 
>>> clean1 = []
>>> for item in content:
	if(item != '\n'):
		clean1.append(item.strip())

		
>>> clean1
['OrderDate', 'Region', 'Rep', 'Item', 'Units', 'UnitCost', 'Total', '1/6/2020', 'East', 'Jones', 'Pencil', '95', '1.99', '189.05', '1/23/2020', 'Central', 'Kivell', 'Binder', '50', '19.99', '999.50', '2/9/2020', 'Central', 'Jardine', 'Pencil', '36', '4.99', '179.64', '2/26/2020', 'Central', 'Gill', 'Pen', '27', '19.99', '539.73', '3/15/2020', 'West', 'Sorvino', 'Pencil', '56', '2.99', '167.44', '4/1/2020', 'East', 'Jones', 'Binder', '60', '4.99', '299.40', '4/18/2020', 'Central', 'Andrews', 'Pencil', '75', '1.99', '149.25', '5/5/2020', 'Central', 'Jardine', 'Pencil', '90', '4.99', '449.10', '5/22/2020', 'West', 'Thompson', 'Pencil', '32', '1.99', '63.68', '6/8/2020', 'East', 'Jones', 'Binder', '60', '8.99', '539.40', '6/25/2020', 'Central', 'Morgan', 'Pencil', '90', '4.99', '449.10', '7/12/2020', 'East', 'Howard', 'Binder', '29', '1.99', '57.71', '7/29/2020', 'East', 'Parent', 'Binder', '81', '19.99', '1,619.19', '8/15/2020', 'East', 'Jones', 'Pencil', '35', '4.99', '174.65', '9/1/2020', 'Central', 'Smith', 'Desk', '2', '125.00', '250.00', '9/18/2020', 'East', 'Jones', 'Pen Set', '16', '15.99', '255.84', '10/5/2020', 'Central', 'Morgan', 'Binder', '28', '8.99', '251.72', '10/22/2020', 'East', 'Jones', 'Pen', '64', '8.99', '575.36', '11/8/2020', 'East', 'Parent', 'Pen', '15', '19.99', '299.85', '11/25/2020', 'Central', 'Kivell', 'Pen Set', '96', '4.99', '479.04', '12/12/2020', 'Central', 'Smith', 'Pencil', '67', '1.29', '86.43', '12/29/2020', 'East', 'Parent', 'Pen Set', '74', '15.99', '1,183.26', '1/15/2021', 'Central', 'Gill', 'Binder', '46', '8.99', '413.54', '2/1/2021', 'Central', 'Smith', 'Binder', '87', '15.00', '1,305.00', '2/18/2021', 'East', 'Jones', 'Binder', '4', '4.99', '19.96', '3/7/2021', 'West', 'Sorvino', 'Binder', '7', '19.99', '139.93', '3/24/2021', 'Central', 'Jardine', 'Pen Set', '50', '4.99', '249.50', '4/10/2021', 'Central', 'Andrews', 'Pencil', '66', '1.99', '131.34', '4/27/2021', 'East', 'Howard', 'Pen', '96', '4.99', '479.04', '5/14/2021', 'Central', 'Gill', 'Pencil', '53', '1.29', '68.37', '5/31/2021', 'Central', 'Gill', 'Binder', '80', '8.99', '719.20', '6/17/2021', 'Central', 'Kivell', 'Desk', '5', '125.00', '625.00', '7/4/2021', 'East', 'Jones', 'Pen Set', '62', '4.99', '309.38', '7/21/2021', 'Central', 'Morgan', 'Pen Set', '55', '12.49', '686.95', '8/7/2021', 'Central', 'Kivell', 'Pen Set', '42', '23.95', '1,005.90', '8/24/2021', 'West', 'Sorvino', 'Desk', '3', '275.00', '825.00', '9/10/2021', 'Central', 'Gill', 'Pencil', '7', '1.29', '9.03', '9/27/2021', 'West', 'Sorvino', 'Pen', '76', '1.99', '151.24', '10/14/2021', 'West', 'Thompson', 'Binder', '57', '19.99', '1,139.43', '10/31/2021', 'Central', 'Andrews', 'Pencil', '14', '1.29', '18.06', '11/17/2021', 'Central', 'Jardine', 'Binder', '11', '4.99', '54.89', '12/4/2021', 'Central', 'Jardine', 'Binder', '94', '19.99', '1,879.06', '12/21/2021', 'Central', 'Andrews', 'Binder', '28', '4.99', '139.72']
>>> 
>>> 
>>> # --------------------------------- format
>>> 
>>> 'My name is {} and age is {}'.format("anil", 35)
'My name is anil and age is 35'
>>> 'My name is {0} and age is {1}'.format("anil", 35)
'My name is anil and age is 35'
>>> 'My name is {0:10} and age is {1:3}'.format("anil", 35)
'My name is anil       and age is  35'
>>> 'My name is {0:>10} and age is {1:<3}'.format("anil", 35)
'My name is       anil and age is 35 '
>>> 'My name is {0:^10} and age is {1:^3}'.format("anil", 35)
'My name is    anil    and age is 35 '
>>> 'My name is {name:^10} and age is {age:^3}'.format(name="anil", age=35)
'My name is    anil    and age is 35 '
>>> 
>>> template = 'My name is {name:^10} and age is {age:^3}'
>>> print(template.format(name="anil", age=35))
My name is    anil    and age is 35 
>>> print(template.format(name="sunil", age=36))
My name is   sunil    and age is 36 
>>> 
>>> 
>>> # -------------------------------------- create a template
>>> 
>>> # 'OrderDate', 'Region', 'Rep', 'Item', 'Units', 'UnitCost', 'Total'
>>> 
>>> template = "{0:12} | {1:8} | {2:8} | {3:8} | {4:8} | {5:8} | {6:8}"
>>> template.format('OrderDate', 'Region', 'Rep', 'Item', 'Units', 'UnitCost', 'Total')
'OrderDate    | Region   | Rep      | Item     | Units    | UnitCost | Total   '
>>> 
>>> template.format('1/6/2020', 'East', 'Jones', 'Pencil', '95', '1.99', '189.05')
'1/6/2020     | East     | Jones    | Pencil   | 95       | 1.99     | 189.05  '
>>> 
>>> 
>>> # -------------------------------- printing the formatted information
>>> 
>>> clean1[0:6]
['OrderDate', 'Region', 'Rep', 'Item', 'Units', 'UnitCost']
>>> template.format(clean1[0:6])
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    template.format(clean1[0:6])
TypeError: unsupported format string passed to list.__format__
>>> a,b,c,d,e,f,g = clean1[0:6]
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    a,b,c,d,e,f,g = clean1[0:6]
ValueError: not enough values to unpack (expected 7, got 6)
>>> a,b,c,d,e,f,g = clean1[0:7]
>>> template.format(a,b,c,d,e,f,g)
'OrderDate    | Region   | Rep      | Item     | Units    | UnitCost | Total   '
>>> a,b,c,d,e,f,g = clean1[0+7:7+7]
>>> template.format(a,b,c,d,e,f,g)
'1/6/2020     | East     | Jones    | Pencil   | 95       | 1.99     | 189.05  '
>>> a,b,c,d,e,f,g = clean1[0+2*7:7+2*7]
>>> template.format(a,b,c,d,e,f,g)
'1/23/2020    | Central  | Kivell   | Binder   | 50       | 19.99    | 999.50  '
>>> len(clean1)
308
>>> 308 / 7
44.0
>>> for i in range(44):
	pass

>>> start = 0
>>> end = 7
>>> m = 0
>>> n = 7
>>> for i in range(len(clean1)/7):
	a,b,c,d,e,f,g = clean1[0+i*7:7+i*7]
	template.format(a,b,c,d,e,f,g)

	
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    for i in range(len(clean1)/7):
TypeError: 'float' object cannot be interpreted as an integer
>>> for i in range(int(len(clean1)/7)):
	a,b,c,d,e,f,g = clean1[0+i*7:7+i*7]
	template.format(a,b,c,d,e,f,g)

	
'OrderDate    | Region   | Rep      | Item     | Units    | UnitCost | Total   '
'1/6/2020     | East     | Jones    | Pencil   | 95       | 1.99     | 189.05  '
'1/23/2020    | Central  | Kivell   | Binder   | 50       | 19.99    | 999.50  '
'2/9/2020     | Central  | Jardine  | Pencil   | 36       | 4.99     | 179.64  '
'2/26/2020    | Central  | Gill     | Pen      | 27       | 19.99    | 539.73  '
'3/15/2020    | West     | Sorvino  | Pencil   | 56       | 2.99     | 167.44  '
'4/1/2020     | East     | Jones    | Binder   | 60       | 4.99     | 299.40  '
'4/18/2020    | Central  | Andrews  | Pencil   | 75       | 1.99     | 149.25  '
'5/5/2020     | Central  | Jardine  | Pencil   | 90       | 4.99     | 449.10  '
'5/22/2020    | West     | Thompson | Pencil   | 32       | 1.99     | 63.68   '
'6/8/2020     | East     | Jones    | Binder   | 60       | 8.99     | 539.40  '
'6/25/2020    | Central  | Morgan   | Pencil   | 90       | 4.99     | 449.10  '
'7/12/2020    | East     | Howard   | Binder   | 29       | 1.99     | 57.71   '
'7/29/2020    | East     | Parent   | Binder   | 81       | 19.99    | 1,619.19'
'8/15/2020    | East     | Jones    | Pencil   | 35       | 4.99     | 174.65  '
'9/1/2020     | Central  | Smith    | Desk     | 2        | 125.00   | 250.00  '
'9/18/2020    | East     | Jones    | Pen Set  | 16       | 15.99    | 255.84  '
'10/5/2020    | Central  | Morgan   | Binder   | 28       | 8.99     | 251.72  '
'10/22/2020   | East     | Jones    | Pen      | 64       | 8.99     | 575.36  '
'11/8/2020    | East     | Parent   | Pen      | 15       | 19.99    | 299.85  '
'11/25/2020   | Central  | Kivell   | Pen Set  | 96       | 4.99     | 479.04  '
'12/12/2020   | Central  | Smith    | Pencil   | 67       | 1.29     | 86.43   '
'12/29/2020   | East     | Parent   | Pen Set  | 74       | 15.99    | 1,183.26'
'1/15/2021    | Central  | Gill     | Binder   | 46       | 8.99     | 413.54  '
'2/1/2021     | Central  | Smith    | Binder   | 87       | 15.00    | 1,305.00'
'2/18/2021    | East     | Jones    | Binder   | 4        | 4.99     | 19.96   '
'3/7/2021     | West     | Sorvino  | Binder   | 7        | 19.99    | 139.93  '
'3/24/2021    | Central  | Jardine  | Pen Set  | 50       | 4.99     | 249.50  '
'4/10/2021    | Central  | Andrews  | Pencil   | 66       | 1.99     | 131.34  '
'4/27/2021    | East     | Howard   | Pen      | 96       | 4.99     | 479.04  '
'5/14/2021    | Central  | Gill     | Pencil   | 53       | 1.29     | 68.37   '
'5/31/2021    | Central  | Gill     | Binder   | 80       | 8.99     | 719.20  '
'6/17/2021    | Central  | Kivell   | Desk     | 5        | 125.00   | 625.00  '
'7/4/2021     | East     | Jones    | Pen Set  | 62       | 4.99     | 309.38  '
'7/21/2021    | Central  | Morgan   | Pen Set  | 55       | 12.49    | 686.95  '
'8/7/2021     | Central  | Kivell   | Pen Set  | 42       | 23.95    | 1,005.90'
'8/24/2021    | West     | Sorvino  | Desk     | 3        | 275.00   | 825.00  '
'9/10/2021    | Central  | Gill     | Pencil   | 7        | 1.29     | 9.03    '
'9/27/2021    | West     | Sorvino  | Pen      | 76       | 1.99     | 151.24  '
'10/14/2021   | West     | Thompson | Binder   | 57       | 19.99    | 1,139.43'
'10/31/2021   | Central  | Andrews  | Pencil   | 14       | 1.29     | 18.06   '
'11/17/2021   | Central  | Jardine  | Binder   | 11       | 4.99     | 54.89   '
'12/4/2021    | Central  | Jardine  | Binder   | 94       | 19.99    | 1,879.06'
'12/21/2021   | Central  | Andrews  | Binder   | 28       | 4.99     | 139.72  '
>>> 
>>> # ----------------------------- use the logic to send this info to a file
>>> 
>>> path = r"C:\Users\Purushotham\Desktop\oracle\day_02\transcripts\report.txt"
>>> f = open(path, 'w')
>>> a,b,c,d,e,f,g = clean1[0:7]
>>> f.write(template.format(a,b,c,d,e,f,g) + '\n')
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    f.write(template.format(a,b,c,d,e,f,g) + '\n')
AttributeError: 'str' object has no attribute 'write'
>>> file = open(path, 'w')
>>> a,b,c,d,e,f,g = clean1[0:7]
>>> f.write(template.format(a,b,c,d,e,f,g) + '\n')
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    f.write(template.format(a,b,c,d,e,f,g) + '\n')
AttributeError: 'str' object has no attribute 'write'
>>> file.write(template.format(a,b,c,d,e,f,g) + '\n')
79
>>> file.write("-"*80+"\n")
81
>>> for i in range(int(len(clean1)/7)-1):
	a,b,c,d,e,f,g = clean1[8+i*7:15+i*7]
	file.write(template.format(a,b,c,d,e,f,g) + "\n")

	
80
79
80
80
79
80
79
80
79
80
80
80
80
79
80
80
81
80
81
81
81
80
79
80
79
80
80
80
80
80
80
79
80
79
80
80
80
81
81
81
80
81
Traceback (most recent call last):
  File "<pyshell#93>", line 2, in <module>
    a,b,c,d,e,f,g = clean1[8+i*7:15+i*7]
ValueError: not enough values to unpack (expected 7, got 6)
>>> file
<_io.TextIOWrapper name='C:\\Users\\Purushotham\\Desktop\\oracle\\day_02\\transcripts\\report.txt' mode='w' encoding='cp1252'>
>>> for i in range(int(len(clean1)/7)):
	a,b,c,d,e,f,g = clean1[0+i*7:7+i*7]
	file.write(template.format(a,b,c,d,e,f,g) + "\n")

	
79
79
79
79
79
79
79
79
79
79
79
79
79
79
79
79
79
79
79
79
79
79
79
79
79
79
79
79
79
79
79
79
79
79
79
79
79
79
79
79
79
79
79
79
>>> file.close()
>>> 
