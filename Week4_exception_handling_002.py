#exception handling

# def midterm():
#     score = int(input('1에서 10사이 정수 입력: '))
#     if score < 0 or score > 20:
#         raise Exception("중간고사 점수 입력 범위를 벗어났습니다. {}".format(score))
#     else:
#         print('{0}점 입니다.'.format(score))
#
#
# try:
#     midterm()
# except Exception as e:
#     print('예외 발생 :{0}'.format(e))
#
#
#
# # try:
#     a = [1,2,3]
#     # print(5/0)
#     print(a[3])
# except ZeroDivisionError as e:
#     print('분모에 0이 올 수없습니다.:{0}'.format(e))
# except IndexError as e:
#     print('인덱스 범위를 벗어났습니다.: {0}'.format(e))
# except Exception as e:
#     print('무언가 에러가 발생했습니다. :{0}'.format(e))


#안주 프로그램 V 0.6
import random

alcohols_foods= {}
with open("alcohols.txt", encoding="UTF-8") as fp1:
    with open("foods.txt",encoding="UTF-8") as fp2:
        alcohols = fp1.readlines()
        foods = fp2.readlines()
        for k in range(len(alcohols)):
            alcohols_foods[alcohols[k].strip('\n')] = foods[k][0:-1] #마지막 역슬래쉬 제거
print(alcohols_foods)

while True:
    alcohol = input('주문하실 술(' + '/' .join([alcohol.rstrip('\n') for alcohol in alcohols]) +  '/아무거나/결제)은?')
    if alcohol == '결제':
        break
    if alcohol in alcohols_foods.keys():
        print('{0}에 어울리는 안주는 {1}입니다.'.format(alcohol, alcohols_foods[alcohol]))
    elif alcohol == '아무거나':
        alcohol = str(random.choice(list(alcohols_foods)))
        print('{0}을 추천합니다. 안주는 {1}입니다.'.format(alcohol, alcohols_foods[alcohol]))
    else:
        print('{0}는 판매하지 않습니다.메뉴에서 골라주세요'.format(alcohol))
