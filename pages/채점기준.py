import streamlit as st
def app():
    st.title('과제, 중간, 기말 채점 기준')

    st.write('''점수 계산:    
                출결점수\*0.1+과제\*0.3+중간\*0.3+기말\*0.3''')

    st.subheader('출결점수(10%)')
    with st.expander("출결점수"):
        st.write("총점: 15  \n 출석 1점, 지각,조퇴:0.5점, 결석 0점   \n 사전에 이야기하고 지각,조퇴하신 경우엔 출석처리 하였습니다. \n")
        
    st.subheader('과제(30%)')
    with st.expander("1주차과제: word2vec, chatgpt활용 과제 (100점 만점)"):
        st.write('**과제 설명**')
        st.image('hw1.JPG')
        
        st.write('-----')
        st.write('**채점 기준**')


        st.write('''
                    - 숙제1(40점), 숙제2(60점)   
                        └숙제1: 모두 만점  
                        └숙제2: 레포트(20), 코드(20), 재밌고 유용한 사례 제안(20)  
                    - 레포트 (있으면 20에서 감점) (없으면 -20)  
                                    - 레포트 없이 gpt 캡처창만 있을 경우 (-1)  
                                    - gpt 그대로 복사 (-1)  
                                    - 서론본론결론 제목 잘 갖추어서 잘 활용한 경우  
                    - 코드 모두 만점
                    - 유용한 사례 (기본점수 20에서 감점)  
                                    - 없으면 (-5)  
                                    - 유용한 사례 알려줘 (-1)  
                ''')
        
    with st.expander("2주차과제: ColabTurtle 이용하여 본인 이름 그리기 (100점 만점)"):
        st.write('모두 잘해서 만점')

    with st.expander("3주차과제: MLP를 활용하여 MNIST 99% 모델 만들기 (100점 만점)"):
        st.write('''
                - 99% 이상이면 100  
                - 97% 이상이면 99  
                - 95% 이상이면 98
                - 정확도 구하는 식 못만들어서 정확도 확인 못하면 90  
                - 정확도 구할 때 test 데이터 이용 안한 경우 95  
                ''')

    with st.expander("NVIDIA-DLI 자격증 제출(100점 만점)"):
        st.write('''
                - 이전에 제출한 92%와 동일한 과제이기 때문에 NVIDIA-DLI 수료하면 100점  
                - 모두 100점  
                ''')

    with st.expander("이상탐지"):
        st.write('''
                - 데이터 나누눈 부분 문제 지시대로 안한 경우 (정도에 따라 -2, -5, -10 감점)
                - 모델 1개당 5점 (1개만 사용한 경우: -10)  
                - 그외 살짝 잘못된 부분들 -2  
                - 과제 시도하다가 문제 못풀고 낸 경우 -50  
                - 다른 사람과 코드가 동일한 경우 0점 처리  
                ''') 
        
    st.subheader("중간고사(30%)")
    st.write('''
            중간고사 평균: 100.9516177    
            중간고사 표준편차: 12.32523455  
            ''')
    with st.expander("leader board (lb)"):
        st.write('''
                - onclass, takehome lb 는 리더보드 상 스코어를 의미함     
                - onclass(당일 10시 캡처), takehome(데드라인 캡처)  
                - 토폴로지(유용균교수님) 점수 기준으로 상대적 점수 계산  
                    - onclass: 0.60697     
                    - takehome: 0.37256    
                    - 계산 방법: (1/자기점수)*기준점수*100   
                    - 기준점수 대비이기 때문에 총점이 100점이 아님   
                ''') 

    with st.expander("code (정성평가)"):
        st.write('''
                **onclass code**
                - 기본점수 80점: 데이콘 베이스라인 돌리기 성공  
                - 모델 학습부분: 10점 (다른 모델 사용, 하이퍼파라미터 변화 등)  
                - EDA 시도: 5점    
                - feature engineering: 5점   
                
                **takehome**    
                - 자신만의 새로운 방식 적용: 100    
                - 다른 사람껄 참고했지만 자신만의 분석이 들어가서: 98    
                - 다른사람꺼 참고해서 올리려는 노력: 95    
                - 참고 안하고 베이스라인/보충 강의만 참고: 90~85    
                - 출처 명시x -1     
                ''')     
        
    st.subheader("기말고사(30%)")
    st.write('''
            기말고사 평균: 95.93421053    
            기말고사 표준편차: 6.141878545  
            ''')

    with st.expander("기말고사"):
        st.write('''
                - 보너스 문제 1개당 3점 -> 총점: 109  
                - 인공지능 이론 문제 1개 틀릴때마다 1점 감점  
                - 100점 기준으로 코드상 오류있으면 감점  
                - 코드1,2(머신러닝,비전) 점수의 경우 보너스점수와 감점 내역이 섞여서 반영됨  
                    - 예시: -1+3-1  
                ''')
        
if __name__ == "__main__":
        app()