#No more sys calls 
n = int(input("Enter your number:"))
guess = n/2
temp = 0.0
handylist = []

for x in range(7):
    temp = n/guess
    guess = (guess + temp) / 2
    handylist.append(guess)
res = n**0.5
print(f"Actual answer: {res:.3f}")
print(f"Fifth iteration: {(handylist[4]):.3f} Accuracy: {res/handylist[4]:.3f}")
print(f"Sixth iteration: {handylist[5]:.3f} Accuracy: {res/handylist[5]:.3f}")
print(f"Seventh iteration: {handylist[6]:.3f} Accuracy: {res/handylist[6]:.3f}")
