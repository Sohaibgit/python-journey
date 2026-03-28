# EXERCISE 1: Translate this Java to Python
# Java: public static void main(String[] args) { System.out.println("Hello"); }
# Python:
def main():
    print("Hello")

if __name__ == "__main__":
    main()

# EXERCISE 2: Translate this Java to Python
# Java: for (int i = 0; i < 10; i++) { System.out.println(i); }
# Python:
for i in range(10):
    print(i)

# EXERCISE 3: Translate a Java ArrayList
# Java: List<String> names = new ArrayList<>(); names.add("Sohaib");
# Python:
names: list[str] = []
names.append("Sohaib")