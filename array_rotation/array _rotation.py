def rotate_array(A,B):
    start=0
    end=len(A)-1
    k=B-1
    for i in range(len(A)//2):
        A[start],A[end]=A[end],A[start]
        start+=1
        end-=1 
    partial=0
    for i in range(partial,k):
        A[partial],A[k]=A[k],A[partial]
        partial+=1
        k-=1
    partial_end=len(A)-1
    for i in range(B,partial_end):
        A[B],A[partial_end]=A[partial_end],A[B]
        B+=1
        partial_end-=1
    return A
A=list(map(int,input("Enter the array Elements: ").split()))
B=int(input("Enter the number of times the array should rotate: "))
output=rotate_array(A,B)
print("Rotated Array: ")
for i in range(len(A)):
    print(A[i],end=" ")