#! /usr/bin/pyton
#-*-coding: utf-8 -*-
'''
闭包！！！
'''
def counter(strat = 0):
	count = [strat]
	def incr( ):
		count[0] += 1
		return count[0]
	return incr

c1 = counter(0)
print c1()
print c1()

print('*')*5
c2 = counter(0)
print c2()

del c1, c2
