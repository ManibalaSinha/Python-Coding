def solution(X,Y,D):
   return (Y-X+D-1)//D #distance = Y-X, each jump covers D distance, num of jumps= disatnce/D . ceiling division
X=10 #start at 10, after 1 jump X+D=40, after 2 jump 40+D= 70, after 3 jump 70 +D=100
Y=85 #
D=30
print(solution(X,Y,D))