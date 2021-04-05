
def stableMatch (col,stu,pref_s,pref_c,available,pairs):

    resultStr = checkFree(col,available) #find first available college

    while( resultStr != "-" ):

        studentMatch = returnMatch(resultStr,pref_c,available) #find the first available student for college

        if available[studentMatch] == 0: #that is also free

            available[studentMatch] = 1 #match the student with college
            available[resultStr] = 1
            pairs[studentMatch] = resultStr
            pairs[resultStr] = studentMatch

        else:  #if that student is already matched with some other college

            otherCol = pairs[studentMatch]  #return the other college that student has matched

            if pref_s[studentMatch].index(resultStr) < pref_s[studentMatch].index(otherCol): #determine which college student loves most

                available[otherCol] = 0 # unmatch the student with college and match it with new college
                pairs[otherCol] = 0

                pairs[studentMatch] = resultStr

            #else

                #remains the same

        resultStr = checkFree(col, available) #check the next available college





def returnMatch (resultStr, pref_c, available):  #determine the available student for the college

    for i in pref_c[resultStr]:

        if available[i] == 0:

            return i

    return "-"


def checkFree(colleges,available):  #determine the first available college

    for i in colleges:

        if available[i] == 0:
            return i

    return "-"


colleges = ["c1","c2","c3","c4"]

students = ["s1","s2","s3","s4"]

pref_s = {"s1":["c1","c4","c3","c2"],"s2":["c3","c2","c4","c1"],"s3":["c2","c4","c1","c3"],"s4":["c1","c2","c3","c4"]}

pref_c = {"c1":["s3","s2","s1","s4"],"c2":["s4","s3","s2","s1"],"c3":["s2","s1","s3","s4"],"c4":["s1","s2","s4","s3"]}

available = {"s1":0,"s2":0,"s3":0,"s4":0,"c1":0,"c2":0,"c3":0,"c4":0}
# 0 means it is free

pairs = {"s1":0,"s2":0,"s3":0,"s4":0,"c1":0,"c2":0,"c3":0,"c4":0}

stableMatch(colleges,students,pref_s,pref_c,available,pairs)

print("Stable Matches:")

for key in pairs:  #print the pairs

    if key[0] == "s":
        print (key,"-", pairs[key])