
import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

#Page title
st.set_page_config(layout="wide", page_title='ACOM CORP', page_icon='💻')
st.title('💻 Config to OLT ACOM')
st.info('Cấu hình tự động OLT các dự án của ACOM trên toàn quốc và kiểm tra số lượng thuê bao đang tồn tại.')

with st.expander('Giới thiệu về app'):
  st.markdown('**Bạn có thể làm gì với App?**')
  st.info('Cấu hình các dự án của ACOM toàn quốc, Xem data của đang hoạt động ở các dự án.')
  st.markdown('**Bạn sử dụng như thế nào?**')
  st.warning('1. Chọn dự án cần sử dụng\n2. Chọn trên list thông tin cần xử lý\n3. Nhập các thông tin cần xử lý\n4. Thông báo trả kết quả.')
  
st.subheader('WELCOME TO ACOM CORPORATION OLT CONFIGURATION WEBSITE!')

# tabs = st.tabs(['Cấu hình', 'Check thông tin dự án'])

#with tabs[0]:
project_options = ['Vinhomes Grand Park PK2', 'Vinhomes Grand Park PK3', 'Lavida Plus', 'Lux5 Bason', 'EcoxuanBD', 'TCL Tham Lương', 'HP One', 'AriaVT', 'BaryaVT', 'Hacom', 'Global City', 'Vin Hưng Yên', 'Vin Tây Mỗ', 'Vin Bắc Giang']
selected_project = st.selectbox('Chọn dự án', project_options)

if selected_project:
    options = ['Config', 'Check', 'Clear', 'Reboot', 'Bridge', 'thoai', 'iptv']
    st.write(f'Bạn đã chọn dự án: {selected_project}')
    st.write('Đang chuyển đến giao diện cấu hình OLT...')
    congthuc = st.text_input('Nhập công thức theo hướng dẫn của Chiến ACOM (Nếu không biết vui lòng liên hệ: 0932277923 Phone/Zalo Chiến ACOM)')
    if selected_project == 'Vinhomes Grand Park PK2':
        choice = st.selectbox('Bạn muốn gì?', options)
        if choice:
            st.write('Bạn muốn {} OLT Vinhomes Grand Park PK2'.format(choice))
