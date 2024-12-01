class Result:
    def __init__(self, bangla_marks, english_marks, math_marks):
        self.bangla = bangla_marks
        self.english = english_marks
        self.math = math_marks


    def get_average(self):
        average = (self.bangla + self.english + self.math) / 3
        return average
    

    def get_grade(self):
        average = self.get_average()
        if average >= 80:
            return "A+"
        elif 50 <= average <80:
            return "B+"
        elif 33 <= average < 50:
            return "C+"
        else: 
            return "F"


    
res1 = Result(84, 97, 75)

avg = (res1.math + res1.english + res1.bangla) / 3

print(res1.math)
print(res1.get_average())
print(res1.get_grade())