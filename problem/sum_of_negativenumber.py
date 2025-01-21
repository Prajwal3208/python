'''Problem Statement
You are given four integers a, b, c, and d. Find the sum
 of negative numbers out of these four numbers and print the same.
Note: Print 0 if no negative number is present.
Input Format:
The input consists of a single line:
• The line contains four integers a, b, c, and d.
The input will be read from the STDIN by the candidate
Output Format:
Print the sum of negative numbers out of these four numbers.
The output will be matched to the candidate's output printed on the STDOUT
Constraints:
-103 ≤ a $ 103.
-103 ≤ b≤ 10}
-10ª ≤ c ≤ 10ª
-103 ≤ d ≤ 10°.
V. Easy
Example:
Input:
2-3-147
Output:
-17
Explanation:
Sum of '-3' and -14' is '-17, thus output is '-17,'''

def sum_negative(a,b,c,d):
    sum = 0
    if (a < 0):
        sum += a
    if (b<0):
        sum+=b
    if (c<0):
        sum+=c
    if(d<0):
        sum+=d
    
    else:
        sum+= 0
    return sum

a = int(input("enter the number A:"))
b = int(input("enter the number B:"))
c = int(input("enter the number C:"))
d = int(input("enter the number D:"))

print(sum_negative(a,b,c,d))