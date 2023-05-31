import streamlit as st
import plotly.graph_objects as go
import numpy as np
from math import factorial

# 누적 분포를 위해 임시값으로 저장할 데이터 선언
global total_prob

# 이산 확률 분포
def bin_dist(k, n, p):
    nck = factorial(n) / (factorial(k) * factorial(n-k))
    pd = nck * p**k * (1-p)**(n-k)
    return pd

# 이산 확률 변수의 누적 분포 함수
def cum_dist(k, n, p):
    global total_prob
    total_prob = total_prob + bin_dist(k, n, p)
    return total_prob

def main():
    st.title('이항 분포 시뮬레이터')
    n = st.number_input('총 시도 횟수를 입력해주세요! (1, 2, 3...)', 1, 1000, help='1000이 넘어갈 경우 overflow가 발생하기때문에 1000까지만 입력 가능합니다!')
    # 소수점 입력 시 소수점 아래 4자리를 넘어갈 경우 제대로 입력되지 않는 부분 보정하고자
    # string형태로 확률 값을 받고 string to int로 변환하여 사용함
    p_string = st.text_input('성공 확률을 입력해주세요! (100% = 1.0)', '0.1', help='확률값에 들어갈 수 없는 값(예: 음수)을 입력하지 말아주세요!')
    p = float(p_string)

    xList = np.arange(n+1)

    if st.checkbox('누적 분포') :
        # 전역 변수로 설정한 값 사용 선언 및 초기화(누적 분포)
        global total_prob
        total_prob = 0.0
        yList = np.array(np.array([cum_dist(k, n, p) for k in range(n + 1)]))
    else :
        yList = np.array(np.array([bin_dist(k, n, p) for k in range(n + 1)]))

    # 그래프 객체 생성
    fig = go.Figure()
    fig.add_trace(go.Bar(x=xList, y=yList))
    st.plotly_chart(fig)

    helptip = '- 표의 우측 하단을 잡고 당기거나 표 영역에서 스크롤을 내리면 더 많은 정보를 볼 수 있어요!'
    st.title('※ 확률값 상세', help=helptip)
    st.write(yList)

if __name__ == "__main__":
    main()