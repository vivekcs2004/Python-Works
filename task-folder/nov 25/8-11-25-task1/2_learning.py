#2. Extract a Word from a Sentence 

s = "MachineLearningModel"

start = s.find("L")             
end = s.find("M", start)        

print(s[start:end])
