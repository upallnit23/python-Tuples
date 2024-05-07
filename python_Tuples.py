import itertools

#1 Tuple Mastery in Python
#Task 1:Formatting Flight Itineraries

itinlist = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
"""for section in itinlist:
    for itin in section:
        print(itinlist)"""
"""for tuple in itinlist:
    sepitinlist = tuple
    print(sepitinlist)"""
count = 0
for tuple in itinlist:
    name, fromdest, todest = tuple
    count += 1
    print(f"Itinerary: {count}: {name} from {fromdest} to {todest}")

#2 Python Data Structures Challenges in Real-World Scenarios
#Task 1: Library System Enhancement

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
addtup = ("The Girl Who Kicked the Hornet's Nest", "Stieg Larsson")

library.append(addtup)
print(library)

#3 Python Loops and Tuples in Analytical Applications
#Task 1:Stock Market Data Analysis

stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0)]

listy = []
for element in stock_data:
    listy.append(element[-1])
print(listy)
sumlisty = round(sum(listy) / len(listy))
print(sumlisty)

#4. Mastering Tuple Packing and Unpacking in Python
#Task 1:Customer Order Processing

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2)]   
print(orders)

for element in orders:
    ordname, ordproduct, ordnum = element
    print(f"{ordname} has ordered {ordnum} {ordproduct}(s).")

#Advanced Tuple Techniques: Joining and Nesting in Python
#Task 1:Product Catalog Merging

catalog1 = (("Laptop", 1000), ("Camera", 500))
catalog2 = (("Smartphone", 800), ("Tablet", 450))

def joinfunc(a, b):
    c = a + b
    print(c)

joinfunc(catalog1, catalog2)




