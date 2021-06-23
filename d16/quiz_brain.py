class QuizBrain:
    def __init__(self, q_list):
        self.q_num = 0
        self.q_list = q_list
        self.score = 0

    def check_answer(self, ans, c_ans):
        if ans.lower() == c_ans.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong!")
        print(f"Your score is {self.score}/{self.q_num}")
        
    def still_has_questions(self):
        return self.q_num < len(self.q_list)
      
    def next_question(self):
        current_q = self.q_list[self.q_num]
        self.q_num +=1
        user_answer = input(f"Q.{self.q_num}: {current_q.text} (True/False): ")
        self.check_answer(user_answer, current_q.answer)
