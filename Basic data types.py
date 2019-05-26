## Basic Data types
#---------------------------------------------------------------Nested lists--------------------------------------------------

if __name__ == '__main__':
    marksheet = []
    i = 999
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score > i:
            i = i
        else:
            i = score           
        marksheet+=[[name,score]]
    print (min(marksheet[]))


#--------------------------------------------------List Comprehensions------------------------------------------------------

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])

#-------------------------------------------------Find the Runner-Up Score!----------------------------------------------------

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    m = max(arr)
    while max(arr) == m:
        arr.remove(m)
    print(max(arr))

#-----------------------------------------------------------Find the percentage-----------------------------------------

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    a = sum(student_marks[query_name])
    print("%.2f"%(a/3))

#-------------------------------------------------------List-------------------------------------------------------------

if __name__ == '__main__':
    N = int(input())
    result = []
    for n in range(N):
        x = input().split(" ")
        command = x[0]
        if command == 'append':
            result.append(int(x[1]))
        if command == 'print':
            print(result)
        if command == 'insert':
            result.insert(int(x[1]), int(x[2]))
        if command == 'reverse':
            result = result[::-1]
        if command == 'pop':
            result.pop()
        if command == 'sort':
            result = sorted(result)
        if command == 'remove':
            result.remove(int(x[1]))
        #   print(result)

#---------------------------------------------------------Tuples-------------------------------------------------------------

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))

#-----------------------------------------------------------