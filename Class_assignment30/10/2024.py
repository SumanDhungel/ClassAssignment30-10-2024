class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        return f"I am {self.name}, {self.age}, {self.gender}"

class Member(Person):
    def __init__(self, name, age, gender, membership_id):
        Person.__init__(self,name, age, gender)
        self.membership_id = membership_id

    def introduce(self):
        return f"I am {self.name}, {self.age}, {self.gender} with membership ID {self.membership_id}"

class Author(Person):
    def __init__(self, name, age, gender, books_written):
        Person.__init__(self,name, age, gender)
        self.books_written = books_written

    def list_books(self):
        return f"Books written: {','.join(self.books_written)}"

class AuthorMember(Member, Author):
    def __init__(self, name, age, gender, membership_id, books_written):
        Member.__init__(self,name, age, gender, membership_id)
        Author.__init__(self,name, age, gender, books_written)

    def introduce(self):
        return f"I am {self.name}, {self.age}, {self.gender} with membership ID {self.membership_id}. Books written: {','.join(self.books_written)}"

am1 = AuthorMember("Albert", 45, "Male", 1234, ["Bright Day", "Silly Mistakes", "Lost in Helsinki"])

print(am1.introduce())
