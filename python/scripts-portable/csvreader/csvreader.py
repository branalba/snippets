import csv

def disp_csv_prev ( csvfile ):
    print(csvfile)
    with open( csvfile, newline='' ) as f:
        reader = csv.reader(f, delimiter=';')
        count = 0
        for row in reader:
            print(row)
            count += 1
            if count > 20:
                break

def get_csv_cols ( csvfile, colnum ):
    out = []
    with open ( csvfile, newline = '' ) as f:
        reader = csv.reader(f, delimiter=';')
        f.readline()
        for row in reader:
            out.append(float(row[colnum]))

    return out
    
