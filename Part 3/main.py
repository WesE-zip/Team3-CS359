import sys


class SQLHandler:
    def __init__(self, question_num, param1):
        self.question_num = question_num
        self.param1 = param1

    def question_one(self):
        print("Question One...")
        
    def question_two(self):
        print("Question Two...")
        
    def question_three(self):
        print("Question Three...")
        p1 = self.param1
        print("Parameter: ", p1)
        
    def question_four(self):
        print("Question Four...")
        p1 = self.param1
        print("Parameter: ", p1)
        
    def question_five(self):
        print("Question Five...")
        
    def question_six(self):
        print("Question Six...")
        p1 = self.param1
        print("Parameter: ", p1)
        
    def question_seven(self):
        print("Question Seven...")
        
    def question_eight(self):
        print("Question Eight...")
        
    def question_nine(self):
        print("Question Nine...")
        p1 = self.param1
        print("Parameter: ", p1)
        
    def question_ten(self):
        print("Question Ten...")
        
    def error_msg(self):
        print("Query failed...")
        
    # Executes the question according to number
    # and validates if parameter value has been passed
    def exec(self):
        q_num = self.question_num
        p1 = self.param1
        
        if q_num == 1: self.question_one()
        elif q_num == 2: self.question_two()
        elif q_num == 3 and p1: self.question_three()
        elif q_num == 4 and p1: self.question_four()
        elif q_num == 5: self.question_five()
        elif q_num == 6 and p1: self.question_six()
        elif q_num == 7: self.question_seven()
        elif q_num == 8: self.question_eight()
        elif q_num == 9 and p1: self.question_nine()
        elif q_num == 10: self.question_ten()
        else: self.error_msg()
    
# Main method
# Validates the question number type (ex. Int)
# Checks if a parameter value has been passed
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing question number.")
        sys.exit()
        
    try:
        question_num = int(sys.argv[1])
    except ValueError:
        print("Invalid question number.")
        sys.exit(1)

    param1 = None
    if len(sys.argv) > 2:
        param1 = sys.argv[2]

    sql_handler = SQLHandler(question_num, param1)
    sql_handler.exec()
    