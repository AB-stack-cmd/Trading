Input = "PAYPALISHIRING"
numRows = 3
Output= "PAHNAPLSIIGYIR"


def zigzag(s,numsRows):
    rows  = [""] * numsRows
    goDown = False
    current = 0

    print(rows)
    for char in s:

        rows[current] += char
        if current ==0 and current == numRows-1 :
            goDown = not goDown
            current +=1 if goDown else 1     

zigzag(Input,numRows)
