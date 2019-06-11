# -*- coding: utf-8 -*-
__author__ = 'Administrator'
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
plt.plot(squares, linewidth=1)

plt.title("Square Numbers",fontsize=24)
plt.savefig('tt.png')
# plt.show()

if __name__ == '__main__':
    pass
