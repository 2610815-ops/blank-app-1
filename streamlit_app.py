import streamlit as st

menu = ['1.아메리카노', '2.카페라떼', '3.바닐라라떼', '4.딸기라떼']
price = [4000, 5000, 5500, 6000]

# 스트림릿 텍스트 출력
st.title('********* msgb cafe ***********')
st.write('========================================')

# input() 대신 스트림릿 컴포넌트 사용
# selectbox는 메뉴 이름을 직접 고르게 하므로 index를 바로 가져올 수 있습니다.
selected_menu = st.selectbox('메뉴를 선택해 주세요:', menu)
count = st.number_input('수량을 입력하세요:', min_value=1, value=1, step=1)

# 선택한 메뉴의 인덱스 번호 찾기
idx = menu.index(selected_menu)

# 결과 출력
st.success(f'선택하신 메뉴는 {menu[idx]}입니다. 결제금액은 {price[idx] * count}원입니다.')

st.write('msgb 카페를 이용해 주셔서 감사합니다.')