import person


class Child(person):
    def calculate_bmi(self):
        return self.weight / (self.height ** 2) * 1.3

    def get_bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 114:
            return "Underweight"
        elif 14 <= bmi < 18:
            return "Normal Weight"
        elif 14 <= bmi < 24:
            return "Overweight"
        else:
            return "Obese"