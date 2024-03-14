score = int(input('What is your score: '));

# if(score >= 90 and score <= 100):
#   print('Grade: A');
# elif(score >= 80 and score < 90):
#   print('Grade: B');
# elif(score >= 70 and score < 80):
#   print('Grade: C');
# elif(score >= 60 and score < 70):
#   print('Grade: D');
# elif(score >= 50 and score < 60):
#   print('Grade: E');
# else:
#   print('Grade: F');
# if(90 <=score <= 100):
#   print('Grade: A');
# elif(80 <= score < 90):
#   print('Grade: B');
# elif(70 <= score < 80):
#   print('Grade: C');
# elif(60 <= score < 70):
#   print('Grade: D');
# elif(50 <= score < 60):
#   print('Grade: E');
# else:
#   print('Grade: F');

# what happens here at below code is that using if aand elif only one condition is check if it is true and program stops after right condition but instead of elif only if is used than every single condition will be checked
if(score >= 90):
  print('Grade: A');
elif(score >= 80):
  print('Grade: B');
elif(score >= 70):
  print('Grade: C');
elif(score >= 60):
  print('Grade: D');
elif(score >= 50):
  print('Grade: E');
else:
  print('Grade: F');