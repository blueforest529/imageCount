import csv
import copy

# csv 파일 이름 입력
CSVFILEPATH = 'count.csv'
# 단가
UNITPRICE = 110

with open(CSVFILEPATH, newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)
    count_png = 0
    count_jpg = 0 

    first_row = None
    last_row = None
    for i, row in enumerate(csv_reader) :
        if i == 1:
            first_row = row  
        last_row = row  

        for colum in row :
            if (".png" in colum) :
                count_png += colum.count('.png')

            if (".jpg" in colum) :
                count_jpg += colum.count('.jpg')
        
        

    print("[첫 행] : ", first_row[0])
    print("[마지막 행] : ", last_row[0])
    print("[이미지 갯수] : ", count_png + count_jpg)
    # 최종 금액
    print("[최종 금액] : ", (count_png + count_jpg) // UNITPRICE)