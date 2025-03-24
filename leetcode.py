from collections import Counter
import math 
def find_duplicates(lst):
    return list({item for item in lst if lst.count(item) > 1})
#medium 
def find_dup2(lst):
    dup=set()
    for item in lst:
        if lst.count(item)>1:
            dup.add(item)
    print(dup)
    return len(dup)
def topFreq2(nums, k):
    lst= find_duplicates(nums)
    if not lst:
        return None
    return([lst[i] for i in range(0,k)])
#easy 
def containDup(lst):
    r= list({item for item in lst if lst.count(item) > 1})
    if not r :
        return False
    else: 
        return True
#easy 
def disappearingNums(nums):
    # range 1 to len(nums)
    # if dict is created with keys 1 to len(nums)
    # loop through, if its there add it if not then its 0 
    missing=[]
    keys= range(1,len(nums)+1)
    my_dict= dict.fromkeys(keys,0)
    print(my_dict)
    idx=1
    for i in range(1,len(nums)+1):
        if i in my_dict and (i in nums):
            my_dict[i]= my_dict[i]+1
        else:
            print("here")
            missing.append(i)
    print(my_dict)
    print(missing)
def longestSubstring(s):
    # longest substring without repeating characters 
    # sting like aaaaa would jsut be a 
    # string with ababc would be ab 
    '''
    while the character and its neighbor are not the same save the length of the number of characters
    that qualify whichever one is the longest save it and return it
    s="p w w k e w"
       1 2 3 4 5 6

    '''
    i = 0 
    j = 1
    #length= len(s)
    substr=""
    substr2=""
    while i < len(s) and j < len(s):
        print("1st line in while", i, j)
        if s[i] == s[j]:
            substr= s[0:j] 
            s = s[j:] # reset s to be the rest of the string 
            i = j
            j += 1
            print("in ==",i, j)
            print("substr",substr)
            substr2=substr
            substr=""
            print("substr2 ,s ",substr2, s)
        else: 
            print("nothing",i,j)
            j = j +1
           
            print("i,j ", i,j)
    i=i+1
    
    if len(substr)> len(substr2):
        print("finals ", substr)
    else:
        print("final ", substr2)        
def longSub(s):
    #gpt answer
    i=0
    visited=set()
    longest =""
    current=""

    for j in range(len(s)):
        while s[j] in visited:
            visited.remove(s[i])
            current = current[1:]
            i+=1
        visited.add(s[j])
        current += s[j]
        if len(current)> len(longest):
            longest=current
    return longest
def mergeSortedLists(lst1, lst2):
    lst3= lst1+lst2
    lst3=sorted(lst3)
    return lst3
def twoSum(lst, sum):
    for i in range(0, len(lst)):
        for j in range(1,len(lst)):
            if lst[i] + lst[j] == sum:
                return i, j 
def sum_func(lst):
    sum_val =0
    for i in lst:
        sum_val = sum_val + i 
    return sum_val
def prod(lst):
    prod=1
    for i in lst:
        prod= prod*i
    return prod
def isPallindrome(str1):
    boole= False
    str2=""
    str2= str1[::-1]
    if (str2 or str1 ) == "":
        return False
    if str1== str2:
        boole=True
    
    return boole
def pallindromeFinder(str1):
    pallindrome_list=[]
    length= len(str1)
    j=1
    for i in range(0,length):
        
        for k in range(0,length+1):
            #print("i k", i,k)
            str2=str1[i:k]
            if isPallindrome(str2):
                pallindrome_list.append([str2])
    return pallindrome_list
def letterCombos(str_1):
    num1 = ""
    num2=""
    dict_letters= {2:["a","b","c"],3:["d","e","f"],4:["g","h","i"],5:["j","k","l"],6:["m","n","o"],7:["p","q","r","s"],8:["t","u","v"],9:["w","x","y","z"]}    

    final_list=[]
    if str_1=="":
        return final_list
    elif len(str_1)==1:
        num1=int(str_1[0])
        return dict_letters[num1]
    else:
        num1=int(str_1[0])
        num2=int(str_1[1])
        for i in dict_letters[num1]:
            for j in dict_letters[num2]:
                i=str(i)
                j=str(j)
                final_list.append(i+j)
    return final_list
def robHouses(lst1):
    sum1= 0
    sum2=0
    length=len(lst1)
    for a in range(0, length):
        if a%2 ==1:
            sum1 = sum1+lst1[a]
        elif a%2 ==0:
            sum2= sum2+lst1[a]
    if sum1>sum2:
       return sum1
    else:
        return sum2
def maxSubarray(lst):
    length= len(lst)
    curr_sum=0
    sum_greater=0
    if length == 1:
        return lst[0]
    elif length== 0:
        return curr_sum
    else:
        for i in range(0,length):
            for j in range(1,length+1):
                curr_sum= sum_func(lst[i:j])
                if curr_sum>sum_greater:
                    sum_greater=curr_sum
    return sum_greater
def maxProduct(lst):
    length= len(lst)
    curr_prod=0
    prod_greater=0
    if length == 1:
        return lst[0]
    elif length== 0:
        return curr_prod
    else:
        for i in range(0,length):
            for j in range(1,length+1):
                if i < j:
                    curr_prod= prod(lst[i:j])
                   # print(i,j,"list: ",lst[i:j],curr_prod)
                    if curr_prod>prod_greater:
                        prod_greater=curr_prod
                else:
                    prod_greater=0
    return prod_greater
def longestIncreasingSub(lst):
    longest=1
    length=len(lst)
    if length == 1:
        return 1 
    else:
        i=0
        while i<length-1:
            if lst[i]<lst[i+1]:
                longest=longest+1
                i = i + 1
            else:
                i = i +1
        print(longest)
def wordbreak(s,wordDict):
    # split by spaces can the word be split by space to make this word
    boole= False
    for items in wordDict:
        if all(items in s for items in wordDict):
            boole=True
    return boole
def majorityElement(nums):
    # find which one has at least n/2 number of the elements 
    dup=set()
    size =(len(nums)/2)
    for item in nums:
        if nums.count(item)>= size:
            dup.add(item)
    return dup
def productArrayExceptSelf(lst):
    length = len(lst)
    # product of all elements except current element at curr index 
    prod= []
    total=1
    for i in lst:
        total = total * i
    #print(total)
    for j in range(0,length):
       # print(lst[j])
        prod.append(total//lst[j])
    return prod
def findTheDuplicates(lst):
    dup= set()
    for i in lst:
        if lst.count(i)>1:
            dup.add(i)
    item = list(dup)
    
    return item[0]
def findTheDuplicatesArray(lst):
    dup= set()
    for i in lst:
        if lst.count(i)>1:

            dup.add(i)
    item = list(dup)
    return item
def matrixZeroes(lst):
    m = len(lst)
    n = len(lst[0])
    x=0
    y=0
    for i in range(0,m):
        for j in range(0,n):
            if lst[i][j]== 0:
                x= i 
                y = j 
                lst[i]=[0 for _ in lst]
    for i in range(0,m):
        for j in range(0,n):
            if j == y:
                lst[i][j]=0
    return lst

def swapLoc(lst,x,y):
    m = len(lst)
    node = lst[x][y] # node contains the value at that position 
    print(x,y)
    print("node", node)
    if x == 0: 
        print("node in x==0", node)
        lst[y][m-1]=node
        print(" lst[y][m-1]",y, m-1,  lst[y][m-1])
    elif y == (m-1):
        print("node in y==n-1", node)
        lst[y][0]=node
        print(" lst[y][0]", y, lst[y][0])
    else:
        print("node in else", node)
        lst[y][x] = node # now the swapped position contains that value 
        print("  lst[y][x]",y,x,   lst[y][x])
    # return a node 

    return lst
def rotateMatrix(lst):
    m= len(lst)
    n = len(lst[0])
    col = []
    print(m,n)
    i = 0 
    while i < m:
        first_col = [row[0] for row in lst]
        col[i] = [row[i] for row in lst]
        i = i +1

    # for i in range (0,n):
    #     for j in range(0,m):
    #         if j == 0:
    #             print(i,j, lst[i][j])
    #             col[i][j]=lst[i][j]

    print(col)
    
def longestSequence(lst):
    lst_set=set()
    lst_set=set(lst)
    return len(lst_set)
def subsets():
    subset=[[]]
    length= len(lst)
    i =1 
    if length == 1:
        subset.append(lst)
    else: 
        subset.append(lst[:2])
        while i != length+1:
            sublidt=lst[0:length:i]
            print(sublidt,lst)
            subset.append(sublidt)
            i= i+1
    print(subset)
def tryCounter():
    c = Counter()
    c= Counter('supercalafrajalisticexpialadocious')
    print(c)
    d = Counter({'red':4, 'blue':2})
    print(d)
    e= Counter(cats=4, dogs=2)
    print(e)
    print(d['red'])
    print(e['cats'])
    print(c)
def mergeIntervals(lst):
    # input [[1,5],[2,7],[9,11]]
    # output [[1,7],[9,11]]
    output=[]
    lst.sort()
    first_interval= lst[0]
    start_f, end_f= first_interval
    for start, end  in lst[1:]:
       # start_f, end_f= first_interval
        if (start <= end_f):
            end_f = max(end,end_f)
        else:
            output.append([start,end])
            start_f, end_f = start, end
    output.append([start_f,end_f])
        
        
    return output
def numberOfIslands(lst1):
    # input is grid of 0s and 1s 
    # output is a number 
    # traverse 
    if not lst1:
        return 0
    x= len(lst1)
    y = len(lst1[0])
    count = 0 
    for i in range(x):
        for j in range(y):
            if lst1[i][j] =='1':
                dfs(lst1, i , j)
                # every time dfs is returned it increases the count and then 
                # checks again 
                count = count +1
    return count 
def dfs(lst1, i , j):
    x= len(lst1)
    y = len(lst1[0])
    # statement checks for out of bounds or for the ocean 0 
    # keeps checking until reach the end of the board or the ocean 
    if i < 0 or j < 0 or i >= x or j >= y or lst1[i][j] != '1':
        return 
    lst1[i][j] = '@' # marks as visited 
    # recursively calls dfs in each direction of current position 
    dfs(lst1, i+1, j)
    dfs(lst1, i-1, j)
    dfs(lst1, i, j+1)
    dfs(lst1, i, j-1)
def minRotatedArray(lst):
    length= len(lst)
    if length== 0:
        min= None
    else: 
        min = lst[0]
        for i in range(0,length):
            if lst[i] < min:
                min = lst[i] 
                idx= i 
                print("min is ", min, "rotated ", idx, " times")
        
    return min
def distanceFunc(pt1, pt2):
    x1= pt1[0]
    x2= pt2[0]
    y1= pt1[1]
    y2=pt2[1]
    return math.sqrt((pow((x1-x2),2)) + (pow((y1-y2),2)))
def kclosestToOrigin(lst, k):
    origin=[0,0]
    distance_lst=[]
    min_dist=100000
    length= len(lst)
    distance=0
    d2=[]
    for i in range(0,length):
        distance=distanceFunc(lst[i],origin)
        distance_lst.append([i,distance])
    distance_lst.sort(key=lambda x:x[1])
    distance_lst= distance_lst[:k]
    for i in distance_lst:
        print(lst[i[0]])
def isPallindrome(lst):
    rev_lst= lst[::-1]
    #print(rev_lst)
    if rev_lst == lst:
        return True
    else:
        return False
def longestPallindromicSub(lst):
    length= len(lst)
    p_len=0
    idx=0
    idy=0
   # print(lst)
    for i in range(0,length):
        for j in range(i+1,length):
            #print(i,j)
            #print(lst[i:j])
            if isPallindrome(lst[i:j]):
               # print("smth")
                if p_len < len(lst[i:j]):
                  #  print(len(lst[i:j]))
                    p_len= len(lst[i:j])
                    idx=i
                    idy=j
    return(lst[idx:idy])
def rotateList(lst,k):
    length= len(lst)
    last= lst[length-1]
    i = 0
    while k > 0 and i < length :
        lst[i+1]= lst[i]
    lst
    print(lst)
def rotateImage(m):
    length= len(m)
    row1= m[0]
    row_n= m[length-1]
    #print(row1, row_n)
    row_copy=[]
    row_copy=row1 # copy holds row1 
    row1= row_n # row 1 has value of n 
    row_n=row_copy # now n has value of ``
    m[0]= row1
    m[length-1]= row_n
    #for row in m:
       # print(row)
    rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    print("\n")
    m= rez
    print(m)
def spiralMatrix(m):
    num_rows= len(m)
    num_cols= len(m[0])
    top = 0 
    bottom = num_cols-1
    up= num_rows
    down= 0 
    res = []
    # first row 
    # to the right 
    for i in range(0, num_cols):
        res.append(m[0][i])
        m[0][i] ='#'
    # to the down 
    for i in range(0,num_rows):
        print('down',i, bottom )
        if m[i][bottom] != '#':
            res.append(m[i][bottom])
            m[i][bottom] ='#'
    # to the left 
    for i in range(num_cols-1,0,-1):
        print(i, num_rows-1)
        if m[num_rows-1][i] != '#':
            res.append(m[num_rows-1][i])
            m[num_rows-1][i]= '#'
    # to the up 
    for i in range(num_rows-1,0,-1):
        if m[i][down] != '#':
            res.append(m[i][down])
            m[i][down] ='#'
    for i in range(0, num_rows):
        for j in range(0, num_cols):
            if m[i][j] != '#':
                res.append(m[i][j])
    return res
            
    # if at the left edge so y =0  then go right 

    idx = word.find(current_letter)
    a=0
    b=0
    if j>0: 
        if board[i][j-1]== next_letter:
            a=i
            b=j
            checkLeft(board,i,j-1,word[idx+1],word)
        else:
            return a,b
    else:
        return False
def longestConsecutiveSequence(nums):
    sortedlst= sorted(nums)
    firstElem= nums[0]
    consequtive=[]
    
    for i in range(0,len(nums)-1):
       
        if sortedlst[i+1]-1 == sortedlst[i]:
            consequtive.append(sortedlst[i])
            consequtive.append(sortedlst[i+1])
    consequtive=set(consequtive)
    return len(consequtive)
   
def checkRight(board,i,j,word,idx):
    if board[i][j] == word[idx]:
        if idx+1 <len(word) and j+1 < len(board[0]):
            checkRight(board,i, j+1, word, idx+1)
        else: 
            return i,j,idx
def wordSearch(board, word):
    hasWord = True
    idx = 0 
    # current_letter= board[i][j]
    num_rows = len(board)
    num_cols = len(board[0])
    i=0
    j=0
    current_letter= word[0]
    found_letters=[]
    list_word= list(word)
    length= len(word)
    while i < num_rows and j < num_cols and idx< length :
       if board[i][j] == word[idx]:
            print("here",i,j,word[idx+1])
            if i == 0 and idx < length:
                print("here2")
                i = i + 1
                if board[i][j] == word[idx+1]:
                    print("her22")
                    found_letters.append(word[idx+1])
                    i = i +1
                else:
                    i = i + 1
                    continue
                # no up 
            elif i == num_rows-1 and idx < length :
                i = i - 1
                if board[i][j] == word[idx+1]:
                    found_letters.append(word[idx+1])
                    i = i -1
                # no down 
            elif j == 0 and idx < length :
                # no left
                j = j+1
                if board[i][j] == word[idx+1]:
                    found_letters.append(word[idx+1])
                    j=j+1
            elif j == num_cols-1 and idx< length :
                # no right 
                j = j-1
                if board[i][j] == word[idx+1]:
                    found_letters.append(word[idx+1])
                    j=j-1

def newList(nums,i):
    # remove i from list 
    newlist=[]
    if len(newlist) == 1: 
        return newlist
    else: 
        newlist=[]
        for k in nums:
            if k != i : 
                newlist.append(k)
        newList(newlist,i)
    return newlist 
def permute(nums):
    result = []
    backtrack(nums, [], result)
    return result

def backtrack(nums, path, result):
    if len(path) == len(nums):
        result.append(path[:])
        return
    
    for num in nums:
        if num not in path:
            path.append(num)
            backtrack(nums, path, result)
            path.pop()

def subset(nums):
    output=[[]]
    length = len(nums)
    j = 1
    if length == 1: 
        output.append(nums)
    elif length == 2: 
        output.append([nums[0]])
        output.append([nums[1]])
        output.append(nums)
    else:
        for i in range(length):
            temp = []  # Temporary list to store new subsets
            for sub in output:  # Iterate over existing subsets
                temp.append(sub + [nums[i]])  # Add current element to each subset
            output.extend(temp)  # Add new subsets to output
    return output
def letterCasePermutation(s):
    newString=""
    lst=[s]
    
    for i in range(0,len(s)):
        print("here")
        if s[i].isalpha():
            for j in range(0, len(lst)):
                print("here 2")
                print(i,lst[j],len(lst))
                newString = list(lst[j])
                newString[i]= newString[i].swapcase()
                lst.append("".join(newString))
    return lst
def combinations(n,k):
    output=[]
    combineBacktrack(1,[], k,n,output)
    expected = math.factorial(n)//((math.factorial(n-k))* (math.factorial(k)))
    if len(output)!= expected:
        return False
    else:
        return output
def combineBacktrack(first,curr,k,n,output):
    if len(curr)==k:
        output.append(curr[:])
        return 
    for i in range(first, n+1):
        curr.append(i)
        combineBacktrack(i+1, curr,k,n,output)
        curr.pop()
def comboSum(nums, target):
    length = len(nums)
    nums = sorted(nums)
    output=[]
    comboDFS(0,[],target,nums,0,output)
    return output
def comboDFS(index, path, target,nums,currSum,output):
    if currSum>target:
        return 
    if currSum== target:
        output.append(path)
        return 
        # this return is the reason that it stops and goes back 
        # then it starts over and checks again but how does it do
    for i in range(index, len(nums)):
        if i > index and nums[i]== nums[i-1]:
            continue
        comboDFS(i+1,path+[nums[i]],target,nums,currSum+nums[i],output)
def targetSum(lst,target):
    count =0 
    length= len(lst)
    
    return count
def targetSumbacktrack(lst,target,sum,count):
    if sum == target:
        count = count +1
        return count
def coinChange(coins, amount):
    # the coins in the array are the values 
    if amount == 0:
        return 0
    if len(coins) == 1 and (amount //coins[0] !=0):
        return -1
    coins= coins[::-1]
    print(coins)
    curr=0
def containDuplicate(lst):
    hasDup = False
    for i in range(0,len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i] == lst[j]:
                print(lst[i], lst[j])
                hasDup = True
    return hasDup
def missingNum(lst):
    length = len(lst)
    for i in range(0,length+1):
        if i not in lst:
            return i
def missingArray(lst):
    length = len(lst)
    lst2=[]
    for i in range(1,length+1):
        if i not in lst:
            lst2.append(i)
    return lst2
def singleNumber(lst):
    lst = sorted(lst)
    lst2=[]
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i] == lst[j]:
                lst2.append(lst[i])
    for i in lst:
        if i not in lst2:
            return i
def climbingStairs(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        
    # n = 3 means

def main():
  #  print("Hello, World!")
    nums=[1]
    lst=[[1,2,3],[4,5,6],[7,8,9]]
   # print(missingNum(nums))
   # print(missingArray(nums))
    print(singleNumber(nums))
    #print(containDuplicate(nums))
    longestsequence= [0,3,7,2,5,8,4,6,0,1]
    #print(longestSequence(longestsequence))
    merge_lst= [[1,10],[2,12],[9,15]]
    s="a1b2"
    #print(comboSum([10,1,2,7,6,1,5],8))
   # print(combinations(4,2))
    #print(letterCasePermutation(s))
#     island= [
#             ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]]
    practiceStr= "babad"
    str2="joey"
    subset1=[1,2,1]
    #coinChange([1,2,5],11)
    #print(targetSum([2,1],1))
   # print(permute(subset1))
    #print(subset(subset1))
    #print(longestConsecutiveSequence([1,0,1,2]))
   # print(wordSearch([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABC"))
    #print(wordSearch([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
    #print(spiralMatrix([[1,2,3,11],[4,5,6,12],[7,8,9,13]]))
   # rotateImage([[1,2,3],[4,5,6],[7,8,9]])
    #rotateList([1,2,3,4,5],2)
    #print(isPallindrome(practiceStr))
    #print(isPallindrome(str2))
    #print(longestPallindromicSub(practiceStr))
   # print(numberOfIslands(island))
   # kclosestToOrigin([[3,3],[5,-1],[-2,4]],2)
   # subsets([1,2,3,4,5])
    #print(minRotatedArray([4,5,6,7,0,1,2]))
   # tryCounter()
    #print(merge(merge_lst))
   # print(mergeIntervals(merge_lst))
    # should return [] 1 2 3 4 5 12 13 14 15 23 24 25 34 35 45 123 124 125 134 135 234 235 245 345 1234 2345 1345 12345
    # [1,2,3] [] 1 2 3, 12 13 23 123
    #rotateMatrix(lst)
    #print(spiralMatrix(lst))
    #print(matrixZeroes(lst))
    #print(findTheDuplicatesArray(nums))
    #print(productArrayExceptSelf(nums))
   # print(wordbreak(s,wordDict))
    # print(majorityElement(nums))
    # longestIncreasingSub(thirdlist)
    # print(maxSubarray(sum2))
    # print(maxProduct(prod2))
    #print(robHouses(lst2)) # print 6
    #isPallindrome(str1)
    #print(pallindromeFinder(str1))
    #print(letterCombos(""))
    # print(topFreq2(nums,k))
    # print(containDup(nums))
    # disappearingNums(nums)
    # print(find_duplicates(nums))
    # print(find_dup2(nums))
    # print(longSub(s))
    #print("count:",targetSum(lst1,1))
    #dict_test={1:"racecar",2:"yogurt"}
    # s2= "racecar"
    # r_s2= s2[::-1]
    # print(r_s2)
if __name__ == "__main__":
    main()

   
