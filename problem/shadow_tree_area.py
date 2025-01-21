'''You are developing a feature for an environmental awareness app that helps users to know how much area their tree's shadow covers. You have the distance D from a tree's trunk to the edge of the shadow. Your task is to calculate and return an integer value representing the shadow area of the canopy.
Note - Round of the result to nearest integer.
Input Specification:
inputi: An inteRer value D, representing the distance from the tree trunks to the
edge of shadow
Output Specification:
Return an integer value representing the shadow area of the canopy.'''


D = float(input("Enter the distance 'D' cover by tree shadow: "))

def area(D):
    area = 3.14*(D*D)
    return int(area) 

print(area(D))