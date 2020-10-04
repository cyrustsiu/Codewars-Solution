def multiplication_table(row,col):
    table = []
    for num in range(1,row+1):
        row = []
        table.append(row)     
        for column in range(1,col+1):
            row.append(num*column)
    return table
