#graphic user interface


from tkinter import *

w = Tk() #윈도우 객체 생성
w.title("레이블 실습")

#라벨생성
lbl_1 = Label(w, text='파이썬을')
lbl_2 = Label(w, text='열심히', font=("맑은 고딕",20),fg="red")
lbl_3 = Label(w, text='공부합니다.', fg="blue",bg="green",width=20,height=10,anchor= S)

#라벨 보이기 생성시에 어디에 라벨을 붙일지 w를 넣었기 때문에 추가 x
lbl_1.pack()
lbl_2.pack()
lbl_3.pack()


# w.geometry('600x150')#가로 세로 크기 지정
# w.resizable(width=True,height=False)#resize값을 false 주게 되면 사이즈 조정 불가
w.mainloop()#Tkinter 마무리 코드











#안주 추첨 프로그램 v0.7
# import random
#
# alcohols_foods= {}
# a = input('술의 종류를 보관하고 있는 파일?')
# f = input('안주의 종류를 보관하고 있는 파일?')
#
# try:
#     with open(a,encoding="UTF-8") as fp1:
#         with open(f,encoding="UTF-8") as fp2:
#             alcohols = fp1.readlines()
#             foods = fp2.readlines()
#             for k in range(len(alcohols)):
#                 alcohols_foods[alcohols[k].strip('\n')] = foods[k][0:-1] #마지막 역슬래쉬 제거
# except FileNotFoundError:
#     print('파일이 없거나, 폴더의 경로가 잘못되었습니다.')
# else:
#     while True:
#         alcohol = input('주문하실 술(' + '/'.join([alcohol.rstrip('\n') for alcohol in alcohols]) + '/아무거나/결제)은?')
#         if alcohol == '결제':
#             break
#         if alcohol in alcohols_foods.keys():
#             print('{0}에 어울리는 안주는 {1}입니다.'.format(alcohol, alcohols_foods[alcohol]))
#         elif alcohol == '아무거나':
#             alcohol = str(random.choice(list(alcohols_foods)))
#             print('{0}을 추천합니다. 안주는 {1}입니다.'.format(alcohol, alcohols_foods[alcohol]))
#         else:
#             print('{0}는 판매하지 않습니다.메뉴에서 골라주세요'.format(alcohol))
# finally:
#     print('다음에 또 만나요')

