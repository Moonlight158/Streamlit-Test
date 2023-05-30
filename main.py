# main.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from math import factorial

def bin_dist(k, n, p):
    nck = factorial(n) / (factorial(k) * factorial(n-k))
    pd = nck * p**k * (1-p)**(n-k)
    return pd

def main():
    # input number
    plt.rcParams['font.family'] = 'Malgun Gothic'

    st.title('이항 분포 시뮬레이터')
    n = st.number_input('총 시도 횟수를 입력해주세요! (1, 2, 3...)', 1, help='ex) 1, 10')
    p = st.number_input('성공 확률을 입력해주세요! (100% = 1.0)', 0.5, help='ex) 0.1, 0.3')

    x = np.arange(n + 1)
    pd1 = np.array([bin_dist(k, n, p) for k in range(n + 1)])
    fig, ax = plt.subplots()
    ax.plot(x, pd1)
    ax.set_title('n = {}, p={}'.format(n, p))
    ax.set_xlabel('성공 횟수',fontdict={'fontname':'Malgun Gothic'})
    ax.set_ylabel('기대 확률',fontdict={'fontname':'Malgun Gothic'})
    st.pyplot(fig)

    helptip = '- 표의 우측 하단을 잡고 당기거나 표 영역에서 스크롤을 내리면 더 많은 정보를 볼 수 있어요!'
    st.title('※ 확률값 상세', help=helptip)
    st.write(pd1)

if __name__ == "__main__":
    main()