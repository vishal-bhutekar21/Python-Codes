class Student:
    def __init__(self, name, marks):
        print("Constructor for the student is created.")
        self.name = name
        self.marks = marks

    def avg_marks(self):
        total = sum(self.marks)  # Calculate the sum of marks
        average = total / len(self.marks)  # Calculate the average
        print(f"Hey Champ {self.name}! Your average marks are: {average:.2f}")
        print("Hey Champ {}! Your average marks are: {:.2f}".format(self.name,average))

# Create an instance of the Student class
vishal = Student("Vishal Bhutekar", [98, 23, 53, 98])
vishal.avg_marks()
