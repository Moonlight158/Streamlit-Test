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
    st.title('이항 분포 시뮬레이터')
    number = st.number_input('값을 입력해주세요!', 1, help='ex) 1, 10')
    p = st.number_input('확률 값을 입력해주세요!', 0.3, help='ex) 0.1, 0.3')

    x = np.arange(number + 1)
    pd1 = np.array([bin_dist(k, number, p) for k in range(number + 1)])
    fig, ax = plt.subplots()
    ax.plot(x, pd1)
    ax.set_title('n = {}, p={}'.format(number, p))
    st.pyplot(fig)

if __name__ == "__main__":
    main()