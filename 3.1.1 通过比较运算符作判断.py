#coding=utf-8
final_score = input('请输入你的CCNA考试分数：')
if int(final_score) > 811:
	print('恭喜你通过考试。')
elif int(final_score) == 811:
	print('恭喜你压线通过考试。')
else:
	print('成绩不合格。')
