# EXERCISE 1: List comprehensions (Python's killer feature vs Java streams)
# Java: list.stream().filter(x -> x > 5).map(x -> x * 2).collect(Collectors.toList())
# Python:
numbers = [1, 3, 5, 7, 9, 11]
result = [x * 2 for x in numbers if x > 5]  # [14, 18, 22]

# EXERCISE 2: Dictionaries (like Java HashMap but way cleaner)
# Build a contact book
contacts = {"Sohaib": "916-555-0001", "Khalid": "916-555-0002", "Shamim": "916-555-0003"}
# Dict comprehension
area_codes = {name: phone[:3] for name, phone in contacts.items()}
print(f"Area codes: {area_codes}")

# EXERCISE 3: Tuples (immutable, like Java records)
# Useful for returning multiple values (Java can't do this easily)
def get_user():
    # returns tuple like ('Sohaib', 'Sacramento', 'IT Specialist')
    return "Sohaib", "Sacramento", "IT Specialist"

name, city, title = get_user()  # Tuple unpacking
print(f"Name: {name}, City: {city}, Title: {title}")

# EXERCISE 4: Sets
skills_java = {"Spring Boot", "REST APIs", "OOP", "SQL"}
skills_python = {"FastAPI", "REST APIs", "OOP", "SQL", "AI"}
common = skills_java & skills_python          # Intersection
print(f"Common skills: {common}")
all_skills = skills_java | skills_python      # Union
print(f"All skills: {all_skills}")
only_python = skills_python - skills_java     # Difference
print(f"Only in Python: {only_python}")