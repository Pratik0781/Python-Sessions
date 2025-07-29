try:
    score=0
    correct_ans=0
    ques=["Who Is PM Of India","What Is The Capital Of India","Who Is The President Of India"]
    ans=["Modi","Delhi","Draupadi"]
    for i in range(len(ques)):
        print(ques[i])
        answer=input("Inter The Answer :").lower().strip()
        if answer==ans[i].lower():
            print("Correct Answer")
            score=score+1
            correct_ans=correct_ans+1
        else:
            print("Wrong Answer")
except Exception as e:
    print(e)
print("Final Score",score)
print("Correct Answers",correct_ans)
        
        
    
