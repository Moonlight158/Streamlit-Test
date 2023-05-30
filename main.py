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
    st.title('이항 분포 시뮬레이터')
    n = st.number_input('총 시도 횟수를 입력해주세요! (1, 2, 3...)', 1, help='ex) 1, 10')
    # 소수점 입력 시 소수점 아래 4자리를 넘어갈 경우 제대로 입력되지 않는 부분 보정하고자
    # string형태로 확률 값을 받고 string to int로 변환하여 사용함
    p_string = st.text_input('성공 확률을 입력해주세요! (100% = 1.0)', '0.1', help='ex) 0.1, 0.3')
    p = float(p_string)

    x = np.arange(n + 1)
    pd1 = np.array([bin_dist(k, n, p) for k in range(n + 1)])
    fig, ax = plt.subplots()
    ax.plot(x, pd1)
    ax.set_title('n = {}, p={}'.format(n, p))
    ax.set_xlabel('Success Count')
    ax.set_ylabel('Prob')

    # 그래프의 x축 간격 조정
    xDist = 1
    if(n > 10) :
        xDist = int((n+1)/10)

    ax.set_xticks(np.arange(0,n+1,xDist))
    st.pyplot(fig)

    helptip = '- 표의 우측 하단을 잡고 당기거나 표 영역에서 스크롤을 내리면 더 많은 정보를 볼 수 있어요!'
    st.title('※ 확률값 상세', help=helptip)
    st.write(pd1)

if __name__ == "__main__":
    main()