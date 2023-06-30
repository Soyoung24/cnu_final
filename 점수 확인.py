import streamlit as st

import streamlit as st
import pandas as pd

def app():

    grade_df=pd.read_excel('grade.xlsx')
    grade_df = grade_df.drop(['Unnamed: 0', 'No'], axis=1)
    grade_df=grade_df.fillna(0)


    st.title('과제, 중간, 기말 점수 확인')

    student_id = st.number_input('학번 9자리 입력', 200000000)
    name = st.text_input('이름')
    google_id = st.text_input('구글 클래스룸 계정 (예시: cnu__@gmail.com)')
    phone_number = st.text_input('핸드폰 번호 (예시: 000-0000-0000)')


    def find_my_score(student_id, name, google_id, phone_number, grade_df):
        return grade_df[(student_id==grade_df['학번']) & (name==grade_df['이름']) & (google_id==grade_df['구글 클래스룸 계정']) & (phone_number==grade_df['핸드폰번호'])]

    if st.button('점수 확인하기'):


        my_df = find_my_score(student_id, name, google_id, phone_number, grade_df)

        st.subheader('출결 점수 (10%)')
        st.write('출석 1, 지각/조퇴:0.5, 결석 0')
        attendance_df = my_df[['출결점수']]
        st.dataframe(attendance_df)

        st.subheader('과제 점수 (30%)')
        hw_df=my_df[['1주차 과제','2주차 과제','3주차 과제','NVIDIA-DLI','이상탐지 ','과제 소계']]
        st.dataframe(hw_df)

        st.subheader('중간고사 점수(30%)')
        st.write('lb: 리더보드 score')
        st.write('점수: 리더보드 score 토폴로지 기준 상대점수')
        st.write('code: 제출 코드 정성평가')

        mid_df = my_df[['mid_onclass_lb', 'mid_home_lb',
            'mid_onclass_점수', 'mid_home_점수',]] 
        mid_df2 = my_df[['mid_onclass_code', 'mid_home_code',
            '보너스_공유(5)', '보너스_피인용(5)', '중간고사']]
        st.dataframe(mid_df)
        st.dataframe(mid_df2)

        st.subheader('기말고사 점수(30%)')
        st.write('보너스 문제 1개당 3점 -> 총점: 109')
        st.write('인공지능 이론 문제 1개 틀릴때마다 1점 감점')
        st.write('만점 기준으로 코드상 오류있으면 감점')

        final_df = my_df[['인공지능 이론', '코드1,2(머신러닝, 비전)',
            '코드3(이상탐지)', '기말고사']]
        st.dataframe(final_df)

if __name__ == "__main__":
        app()