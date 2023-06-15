import streamlit as st
from scipy.stats import binom
import plotly.graph_objects as go
import numpy as np
import pandas as pd

# Dataframe을 csv형태로 변환
def convert_df(df):
    return df.to_csv(index=False, float_format='%.6f').encode('utf-8')

# main 함수(프로그램 동작하는 몸통)
def main():
    st.title('이항 분포 시뮬레이터')
    n = st.number_input('총 시도 횟수를 입력해주세요! (1, 2, 3...)', 1, help='시도 횟수는 음수값을 입력하지 말아주세요!')
    # 소수점 입력 시 소수점 아래 4자리를 넘어갈 경우 제대로 입력되지 않는 부분 보정하고자
    # string형태로 확률 값을 받고 string to int로 변환하여 사용함
    p_string = st.text_input('성공 확률을 입력해주세요! (100% = 1.0)', '0.1', help='확률값에 들어갈 수 없는 값(예: 음수)을 입력하지 말아주세요!')
    p = float(p_string)

    xList = np.arange(n+1)

    if st.checkbox('누적 분포') :
        yList = np.array(np.array([binom.cdf(k, n, p) for k in range(n + 1)]))
    else :
        yList = np.array(np.array([binom.pmf(k, n, p) for k in range(n + 1)]))

    # 그래프 객체 생성
    fig = go.Figure()
    fig.add_trace(go.Bar(x=xList, y=yList))
    st.plotly_chart(fig)

    helptip = '- 표의 우측 하단을 잡고 당기거나 표 영역에서 스크롤을 내리면 더 많은 정보를 볼 수 있어요!'
    st.title('※ 확률값 상세', help=helptip)
    
    # 표로 표현해줄 데이터 형태 정의
    df = pd.DataFrame({
        'SuccessCount':xList,
        'SuccessProb':yList,
        })
    
    csv = convert_df(df)
    fName = st.text_input('저장될 csv의 파일명을 입력하세요!', 'ResultSimul', help='파일 확장자(.csv)는 붙이지 않아도 됩니다') + '.csv'

    st.download_button(
        label='Download data', 
        data=csv, 
        file_name=fName,
        mime='text/csv')
    
    st.write(df.style.format())

if __name__ == "__main__":
    main()