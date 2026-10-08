print("===== PART 1: Two Classes for Area =====")

# Class 1: Trapezoid
# Formula: Area = (a + b) / 2 * h
# a,b are two parallel sides, h is height
class Trapezoid:
    def __init__(self, a, b, h):
        self.a = a # first parallel side
        self.b = b # second parallel side
        self.h = h # height

    def area(self):
        # simple formula for area
        return (self.a + self.b) / 2 * self.h

# Class 2: Parallelogram
# Formula: Area = base * height
class Parallelogram:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        # simple formula for area
        return self.base * self.height

# Testing Part 1
t1 = Trapezoid(a=10, b=6, h=5)
print(f"Trapezoid area (a=10, b=6, h=5) = {t1.area()}")

p1 = Parallelogram(base=10, height=5)
print(f"Parallelogram area (base=10, height=5) = {p1.area()}")

print("\n===== PART 2: Comparison and Dictionary =====")

# Class 3: Comparison Class
# This class will find biggest area
class AreaComparison:
    def find_largest(self, area_dict):
        # area_dict is dictionary like {"shape_name": area_value}
        
        # max() finds key with biggest value
        # key=area_dict.get means compare by value not by name
        largest_shape = max(area_dict, key=area_dict.get)
        largest_area = area_dict[largest_shape]
        
        return largest_shape, largest_area

# Make a dictionary to store results
# format: { "shape name" : area }
results = {}

# Iterate for different dimensions (using loop)
# We will create 5 shapes with different sizes
print("Calculating areas for different dimensions:")

# 1. Trapezoid
trap1 = Trapezoid(10, 6, 5)
results["Trapezoid-1 (10,6,5)"] = trap1.area()

# 2. Parallelogram
para1 = Parallelogram(10, 5)
results["Parallelogram-1 (10x5)"] = para1.area()

# 3. Trapezoid with bigger size
trap2 = Trapezoid(15, 10, 7)
results["Trapezoid-2 (15,10,7)"] = trap2.area()

# 4. Parallelogram with bigger size
para2 = Parallelogram(12, 8)
results["Parallelogram-2 (12x8)"] = para2.area()

# 5. One more
para3 = Parallelogram(20, 6)
results["Parallelogram-3 (20x6)"] = para3.area()

# Print all results from dictionary using loop
print("\nAll Areas stored in Dictionary:")
for name, area in results.items(): # items() gives key and value
    print(f"{name} -> Area = {area}")

# Now use dictionary functions to find largest

# 1. Using max() and get()
largest_name = max(results, key=results.get)
print(f"\nLargest area is: {largest_name} = {results[largest_name]}")

# 2. Using values() to get all areas
all_areas = results.values()
print(f"All area values: {list(all_areas)}")
print(f"Max value from dict values: {max(all_areas)}")

# 3. Using comparison class
checker = AreaComparison()
shape, area = checker.find_largest(results)
print(f"\n[Using Comparison Class] Biggest Shape = {shape} with area = {area}")

# 4. Bonus