# ============================================================
# STUDENT LEARNING PORTAL
# PROG211 - OBJECT-ORIENTED PROGRAMMING 1
# ============================================================


class Student:
    def __init__(self, student_id, name, programme, email):
        self.student_id = student_id
        self.name = name
        self.programme = programme
        self.email = email

    def display_details(self):
        print("Student ID:", self.student_id)
        print("Student Name:", self.name)
        print("Programme:", self.programme)
        print("Email:", self.email)


class LearningRecord:
    total_records = 0

    def __init__(self, record_id, student, course_name, learning_status):
        self.record_id = record_id
        self.student = student
        self.course_name = course_name
        self.learning_status = learning_status

        LearningRecord.total_records += 1

    def display_record(self):
        print("\n----------------------------------------")
        print("LEARNING RECORD DETAILS")
        print("----------------------------------------")
        print("Record ID:", self.record_id)
        self.student.display_details()
        print("Course Name:", self.course_name)
        print("Learning Status:", self.learning_status)
        print("----------------------------------------")

    def update_status(self, new_status):
        self.learning_status = new_status

    @classmethod
    def get_total_records(cls):
        return cls.total_records

    @staticmethod
    def validate_status(status):
        if status == "Not Started":
            return True
        elif status == "In Progress":
            return True
        elif status == "Completed":
            return True
        else:
            return False


class LearningPortal:
    def __init__(self):
        # One dictionary stores multiple LearningRecord objects.
        self.learning_records = {}

    def register_learning_record(self):
        print("\n========================================")
        print("REGISTER LEARNING RECORD")
        print("========================================")

        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        programme = input("Enter Programme: ")
        email = input("Enter Email: ")

        student = Student(student_id, name, programme, email)

        course_name = input("Enter Course Name: ")

        print("\nSelect Learning Status")
        print("1. Not Started")
        print("2. In Progress")
        print("3. Completed")

        choice = input("Enter choice: ")

        if choice == "1":
            learning_status = "Not Started"
        elif choice == "2":
            learning_status = "In Progress"
        elif choice == "3":
            learning_status = "Completed"
        else:
            print("Invalid learning status selection.")
            return

        if LearningRecord.validate_status(learning_status):
            number = LearningRecord.get_total_records() + 1
            record_id = "LRN" + str(number).zfill(3)

            record = LearningRecord(
                record_id,
                student,
                course_name,
                learning_status
            )

            self.learning_records[record_id] = record

            print("\nLearning record registered successfully.")
            print("Record ID:", record_id)
            print("Student:", student.name)
            print("Course:", course_name)
            print("Learning Status:", learning_status)

    def search_record(self):
        print("\n========================================")
        print("SEARCH LEARNING RECORD")
        print("========================================")

        record_id = input("Enter Record ID: ").upper()
        record = self.learning_records.get(record_id)

        if record:
            record.display_record()
        else:
            print("Learning record not found.")

    def update_learning_status(self):
        print("\n========================================")
        print("UPDATE LEARNING STATUS")
        print("========================================")

        record_id = input("Enter Record ID: ").upper()
        record = self.learning_records.get(record_id)

        if record:
            print("Current Learning Status:", record.learning_status)
            print("\n1. Not Started")
            print("2. In Progress")
            print("3. Completed")

            choice = input("Enter choice: ")

            if choice == "1":
                new_status = "Not Started"
            elif choice == "2":
                new_status = "In Progress"
            elif choice == "3":
                new_status = "Completed"
            else:
                print("Invalid learning status selection.")
                return

            if LearningRecord.validate_status(new_status):
                record.update_status(new_status)
                print("Learning status updated successfully.")
                print("New Learning Status:", record.learning_status)
        else:
            print("Learning record not found.")

    def display_all_records(self):
        print("\n========================================")
        print("ALL LEARNING RECORDS")
        print("========================================")

        if len(self.learning_records) == 0:
            print("No learning records available.")
        else:
            for record_id in self.learning_records:
                record = self.learning_records[record_id]
                record.display_record()

    def display_total_records(self):
        total = LearningRecord.get_total_records()
        print("\n========================================")
        print("TOTAL LEARNING RECORDS")
        print("========================================")
        print("Total Learning Records:", total)


def main():
    portal = LearningPortal()

    while True:
        print("\n================================================")
        print("             STUDENT LEARNING PORTAL")
        print("================================================")
        print("1. Register Learning Record")
        print("2. Search Learning Record")
        print("3. Update Learning Status")
        print("4. Display All Records")
        print("5. Display Total Records")
        print("6. Exit")
        print("================================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            portal.register_learning_record()
        elif choice == "2":
            portal.search_record()
        elif choice == "3":
            portal.update_learning_status()
        elif choice == "4":
            portal.display_all_records()
        elif choice == "5":
            portal.display_total_records()
        elif choice == "6":
            print("\nThank you for using the Student Learning Portal.")
            print("Program closed.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
