general_transcript ={"python":{"score":97, "grade":1},
              "comp_essentials":{"score":90, "grade":1},
              "mathematics_4_eng1":{"score":80, "grade":1},
              "physics_4_eng1":{"score":60, "grade":1},
              "english_4_general_purpose":{"score":85, "grade":1}}
print(general_transcript)

average_score = 0
total_grade = 0
total_score = 0

for i in general_transcript :

    total_score += general_transcript[i]["score"]
    total_grade += general_transcript[i]["grade"]
    average_score = total_score / 5
print("Your Total Score =",total_score)
print("Your Total Grade =",total_grade)
print("Your Average Score =",average_score,"%")
    
