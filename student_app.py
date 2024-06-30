import streamlit as st
import pandas as pd
from data_preprocessing import data_preprocessing
from prediction import prediction

#options
Marital_status_opt = ['1 - single', '2 - married', '3 - widower', '4 - divorced', '5 - facto union', '6 - legally separated']
Application_mode_opt = ['1 - 1st phase-general contingent', '2 - Ordinance No. 612/93', '5 - 1st phase-special contingent (Azores Island)', '7 - Holders of other higher courses', '10 - Ordinance No. 854-B/99', '15 - International student (bachelor)', '16 - 1st phase-special contingent (Madeira Island)', '17 - 2nd phase-general contingent', '18 - 3rd phase-general contingent', '26 - Ordinance No. 533-A/99, item b2 (Different Plan)', '27 - Ordinance No. 533-A/99, item b3 (Other Institution)', '39 - Over 23 years old', '42 - Transfer', '43 - Change of course', '44 - Technological specialization diploma holders', '51 - Change of institution/course', '53 - Short cycle diploma holders', '57 - Change of institution/course (International)']
Course_opt = ['33 - Biofuel Production Technologies', '171 - Animation and Multimedia Design', '8014 - Social Service (evening attendance)', '9003 - Agronomy', '9070 - Communication Design', '9085 - Veterinary Nursing', '9119 - Informatics Engineering', '9130 - Equinculture', '9147 - Management', '9238 - Social Service', '9254 - Tourism', '9500 - Nursing', '9556 - Oral Hygiene', '9670 - Advertising and Marketing Management', '9773 - Journalism and Communication', '9853 - Basic Education', '9991 - Management (evening attendance)']
Prev_qualification_opt = ["1 - Secondary education", "2 - Higher education-bachelor's degree", "3 - Higher education-degree", "4 - Higher education-master's", "5 - Higher education-doctorate", "6 - Frequency of higher education", "9 - 12th year of schooling-not completed", "10 - 11th year of schooling-not completed", "12 - Other-11th year of schooling", "14 - 10th year of schooling", "15 - 10th year of schooling-not completed", "19 - Basic education 3rd cycle (9th/10th/11th year) or equiv.", "38 - Basic education 2nd cycle (6th/7th/8th year) or equiv.", "39 - Technological specialization course", "40 - Higher education-degree (1st cycle)", "42 - Professional higher technical course", "43 - Higher education-master (2nd cycle)"]
Nationality_opt = ['1 - Portuguese', '2 - German', '6 - Spanish', '11 - Italian', '13 - Dutch', '14 - English', '17 - Lithuanian', '21 - Angolan', '22 - Cape Verdean', '24 - Guinean', '25 - Mozambican', '26 - Santomean', '32 - Turkish', '41 - Brazilian', '62 - Romanian', '100 - Moldova (Republic of)', '101 - Mexican', '103 - Ukrainian', '105 - Russian', '108 - Cuban', '109 - Colombian']
Mothers_qualification_opt = ["1 - Secondary Education-12th Year of Schooling or Eq.", "2 - Higher Education-Bachelor's Degree", "3 - Higher Education-Degree", "4 - Higher Education-Master's", "5 - Higher Education-Doctorate", "6 - Frequency of Higher Education", "9 - 12th Year of Schooling-Not Completed", "10 - 11th Year of Schooling-Not Completed", "11 - 7th Year (Old)", "12 - Other-11th Year of Schooling", "14 - 10th Year of Schooling", "18 - General commerce course", "19 - Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.", "22 - Technical-professional course", "26 - 7th year of schooling", "27 - 2nd cycle of the general high school course", "29 - 9th Year of Schooling-Not Completed", "30 - 8th year of schooling", "34 - Unknown", "35 - Can't read or write", "36 - Can read without having a 4th year of schooling", "37 - Basic education 1st cycle (4th/5th year) or equiv.", "38 - Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.", "39 - Technological specialization course", "40 - Higher education-degree (1st cycle)", "41 - Specialized higher studies course", "42 - Professional higher technical course", "43 - Higher Education-Master (2nd cycle)", "44 - Higher Education-Doctorate (3rd cycle)"]
Fathers_qualification_opt = ["1 - Secondary Education-12th Year of Schooling or Eq.", "2 - Higher Education-Bachelor's Degree", "3 - Higher Education-Degree", "4 - Higher Education-Master's", "5 - Higher Education-Doctorate", "6 - Frequency of Higher Education", "9-12th Year of Schooling-Not Completed", "10 - 11th Year of Schooling-Not Completed", "11 - 7th Year (Old)", "12 - Other-11th Year of Schooling", "13 - 2nd year complementary high school course", "14 - 10th Year of Schooling", "18 - General commerce course", "19 - Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.", "20 - Complementary High School Course", "22 - Technical-professional course", "25 - Complementary High School Course-not concluded", "26 - 7th year of schooling", "27 - 2nd cycle of the general high school course", "29 - 9th Year of Schooling-Not Completed", "30 - 8th year of schooling", "31 - General Course of Administration and Commerce", "33 - Supplementary Accounting and Administration", "34 - Unknown", "35 - Can't read or write", "36 - Can read without having a 4th year of schooling", "37 - Basic education 1st cycle (4th/5th year) or equiv.", "38 - Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.", "39 - Technological specialization course", "40 - Higher education-degree (1st cycle)", "41 - Specialized higher studies course", "42 - Professional higher technical course", "43 - Higher Education-Master (2nd cycle)", "44 - Higher Education-Doctorate (3rd cycle)"]
Mothers_occupation_opt = ['0 - Student', '1 - Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers', '2 - Specialists in Intellectual and Scientific Activities', '3 - Intermediate Level Technicians and Professions', '4 - Administrative staff', '5 - Personal Services, Security and Safety Workers and Sellers', '6 - Farmers and Skilled Workers in Agriculture, Fisheries and Forestry', '7 - Skilled Workers in Industry, Construction and Craftsmen', '8 - Installation and Machine Operators and Assembly Workers', '9 - Unskilled Workers', '10 - Armed Forces Professions', '90 - Other Situation', '99 - (blank)', '122 - Health professionals', '123 - teachers', '125 - Specialists in information and communication technologies (ICT)', '131 - Intermediate level science and engineering technicians and professions', '132 - Technicians and professionals, of intermediate level of health', '134 - Intermediate level technicians from legal, social, sports, cultural and similar services', '141 - Office workers, secretaries in general and data processing operators', '143 - Data, accounting, statistical, financial services and registry-related operators', '144 - Other administrative support staff', '151 - personal service workers', '152 - sellers', '153 - Personal care workers and the like', '171 - Skilled construction workers and the like, except electricians', '173 - Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like', '175 - Workers in food processing, woodworking, clothing and other industries and crafts', '191 - cleaning workers', '192 - Unskilled workers in agriculture, animal production, fisheries and forestry', '193 - Unskilled workers in extractive industry, construction, manufacturing and transport', '194 - Meal preparation assistants']
Fathers_occupation_opt = ['0 - Student', '1 - Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers', '2 - Specialists in Intellectual and Scientific Activities', '3 - Intermediate Level Technicians and Professions', '4 - Administrative staff', '5 - Personal Services, Security and Safety Workers and Sellers', '6 - Farmers and Skilled Workers in Agriculture, Fisheries and Forestry', '7 - Skilled Workers in Industry, Construction and Craftsmen', '8 - Installation and Machine Operators and Assembly Workers', '9 - Unskilled Workers', '10 - Armed Forces Professions', '90 - Other Situation', '99 - (blank)', '101 - Armed Forces Officers', '102 - Armed Forces Sergeants', '103 - Other Armed Forces personnel', '112 - Directors of administrative and commercial services', '114 - Hotel, catering, trade and other services directors', '121 - Specialists in the physical sciences, mathematics, engineering and related techniques', '122 - Health professionals', '123 - teachers', '124 - Specialists in finance, accounting, administrative organization, public and commercial relations', '131 - Intermediate level science and engineering technicians and professions', '132 - Technicians and professionals, of intermediate level of health', '134 - Intermediate level technicians from legal, social, sports, cultural and similar services', '135 - Information and communication technology technicians', '141 - Office workers, secretaries in general and data processing operators', '143 - Data, accounting, statistical, financial services and registry-related operators', '144 - Other administrative support staff', '151 - personal service workers', '152 - sellers', '153 - Personal care workers and the like', '154 - Protection and security services personnel', '161 - Market-oriented farmers and skilled agricultural and animal production workers', '163 - Farmers, livestock keepers, fishermen, hunters and gatherers, subsistence', '171 - Skilled construction workers and the like, except electricians', '172 - Skilled workers in metallurgy, metalworking and similar', '174 - Skilled workers in electricity and electronics', '175 - Workers in food processing, woodworking, clothing and other industries and crafts', '181 - Fixed plant and machine operators', '182 - assembly workers', '183 - Vehicle drivers and mobile equipment operators', '192 - Unskilled workers in agriculture, animal production, fisheries and forestry', '193 - Unskilled workers in extractive industry, construction, manufacturing and transport', '194 - Meal preparation assistants', '195 - Street vendors (except food) and street service providers']


data = []

col1, col2 = st.columns([1, 5])
with col1:
    st.image('logo.png', width=130, use_column_width='auto')
with col2:
    st.header('**Jaya Jaya Institut Specialized Counseling App (Prototype)**')



col1, col2 = st.columns([1, 5])
with col1:
    st.image('personal_info.png', width=80)
with col2:
    st.markdown(
        "<div style='display: flex; align-items: center; justify-content: flex-start; height: 80px;'>"
        "<h3 style='margin-bottom: 0;'>General Information</h3>"
        "</div>",
        unsafe_allow_html=True
    )

#col1, col2, col3 = st.columns(3)

#with col3:
    #Application_order = int(st.number_input(label='Application Order', value=0, max_value=9))
    #data[-1]["Application_order"] = Application_order


col1, col2, col3 = st.columns(3)
with col1:
    Gender = st.selectbox(label='Gender', options=['Male','Female'],index=0)
    data.append({"Gender": 1 if Gender == "Male" else 0})

with col2:
    Marital_status = st.selectbox(label='Marital Status', options=Marital_status_opt,index=0)
    data[-1]["Marital_status"] = Marital_status.split(" - ")[0]

with col3:
    Nationality = st.selectbox(label='Nationality', options=Nationality_opt,index=0)
    data[-1]['Nationality'] = Nationality.split(" - ")[0]


col1, col2 = st.columns([1, 5])
with col1:
    st.image('parents.png', width=80)
with col2:
    st.markdown(
        "<div style='display: flex; align-items: center; justify-content: flex-start; height: 80px;'>"
        "<h3 style='margin-bottom: 0;'>Parents Information</h3>"
        "</div>",
        unsafe_allow_html=True
    )

st.markdown('##### Qualification')
col1, col2 = st.columns(2)
with col1:
    Mothers_qualification = st.selectbox(label="Mother's Qualification", options=Mothers_qualification_opt,index=0)
    data[-1]['Mothers_qualification'] = Mothers_qualification.split(" - ")[0]

with col2:
    Fathers_qualification = st.selectbox(label="Father's Qualification", options=Fathers_qualification_opt,index=0)
    data[-1]['Fathers_qualification'] = Fathers_qualification.split(" - ")[0]

st.markdown('##### Occupation')
col1, col2 = st.columns(2)
with col1:
    Mothers_occupation = st.selectbox(label="Mother's Occupation", options=Mothers_occupation_opt,index=0)
    data[-1]['Mothers_occupation'] = Mothers_occupation.split(" - ")[0]

with col2:
    Fathers_occupation = st.selectbox(label="Father's Occupation", options=Fathers_occupation_opt,index=0)
    data[-1]['Fathers_occupation'] = Fathers_occupation.split(" - ")[0]


st.markdown('### Others')

Daytime_evening_attendance = st.selectbox(label='Attendance', options=['Daytime', 'Evening'],index=0)
data[-1]["Daytime_evening_attendance"] = 1 if Daytime_evening_attendance == "Day" else 0

col1, col2 = st.columns(2)
with col1:
    Prev_qualification = st.selectbox(label="Previous Qualification", options=Prev_qualification_opt,index=0)
    data[-1]['Previous_qualification'] = Prev_qualification.split(" - ")[0] 

with col2:
    Educational_special_needs = st.selectbox(label='Needs Special Educational?', options=['Yes', 'No'],index=0)
    data[-1]["Educational_special_needs"] = 1 if Educational_special_needs == "Yes" else 0


col1, col2 = st.columns(2)
with col1:
    Application_mode = st.selectbox(label='Application Mode', options=Application_mode_opt,index=0)
    data[-1]['Application_mode'] = Application_mode.split(" - ")[0]

with col2:
    Displaced = st.selectbox(label='Displaced?', options=['Yes', 'No'],index=0)
    data[-1]["Displaced"] = 1 if Displaced == "Yes" else 0


col1, col2 = st.columns(2)
with col1:
    Course = st.selectbox(label='Course', options=Course_opt,index=0)
    data[-1]['Course'] = Course.split(" - ")[0]

with col2:
    International = st.selectbox(label='International Student?', options=['Yes', 'No'],index=0)
    data[-1]["International"] = 1 if International == "Yes" else 0  


col1, col2 = st.columns(2)
#with col1:
    #Application_order = int(st.number_input(label='Application Order', value=0, max_value=9))
    #data[-1]["Application_order"] = Application_order

with col1:
    Previous_qualification_grade = float(st.number_input(label='Prev. Qualification Grade', min_value=1.000, max_value=200.00))
    data[-1]['Previous_qualification_grade'] = Previous_qualification_grade

with col2:
    Admission_grade = float(st.number_input(label='Admission Grade', min_value=0.000, max_value=200.00))
    data[-1]['Admission_grade'] = Admission_grade


#col1, col2, col3, col4 = st.columns(4)
col1, col2, col3 = st.columns(3)    
with col1:
    Debtor = st.selectbox(label='Debtor?', options=['Yes', 'No'],index=0)
    data[-1]["Debtor"] = 1 if Debtor == "Yes" else 0


with col2:
    Scholarship_holder = st.selectbox(label='Scholarship', options=['Yes', 'No'],index=0)
    data[-1]["Scholarship_holder"] = 1 if Scholarship_holder == "Yes" else 0

with col3:
    Tuition_fees_up_to_date = st.selectbox(label='Tuition Fees Up to Date?', options=['Yes', 'No'],index=0)
    data[-1]["Tuition_fees_up_to_date"] = 1 if Tuition_fees_up_to_date == "Yes" else 0


#with col4:
    #Application_order = int(st.number_input(label='Application Order', value=0, max_value=9))
    #data[-1]["Application_order"] = Application_order


#col1, col2 = st.columns(2)
#with col1:
#Previous_qualification = st.selectbox(label="Previous Qualification", options=Prev_qualification_opt,index=0)
#data[-1]['Previous_qualification'] = Previous_qualification.split(" - ")[0]    

#with col2:
    #Previous_qualification_grade = float(st.number_input(label='Previous Qualification Grade', min_value=1.000, max_value=200.00))
    #data[-1]['Previous_qualification_grade'] = Previous_qualification_grade

col1, col2 = st.columns([1, 5])
with col1:
    st.image('transcript.png', width=60)
with col2:
    st.markdown(
        "<div style='display: flex; align-items: center; justify-content: flex-start; height: 60px;'>"
        "<h3 style='margin-bottom: 0;'>Study Tracer</h3>"
        "</div>",
        unsafe_allow_html=True
    )


#col1, col2, col3 = st.columns(3)
#with col1:
    #Admission_grade = float(st.number_input(label='Admission Grade', min_value=0.000, max_value=200.00))
    #data[-1]['Admission_grade'] = Admission_grade

#with col2:
    #Age_at_enrollment = int(st.number_input(label='Age at Enrollment', min_value=1, format="%d"))
    #data[-1]['Age_at_enrollment'] = Age_at_enrollment

#with col3:
#Daytime_evening_attendance = st.selectbox(label='Attendance', options=['Daytime', 'Evening'],index=0)
#data[-1]["Daytime_evening_attendance"] = 1 if Daytime_evening_attendance == "Day" else 0

st.markdown('##### Curricular Units in the 1st Semester')
col1, col2, col3, col4 = st.columns(4)
with col1:
    Curricular_units_1st_sem_enrolled = int(st.number_input(label='Enrolled 1st Sem.', min_value=0, value=0, step=1, format="%d"))
    data[-1]['Curricular_units_1st_sem_enrolled'] = Curricular_units_1st_sem_enrolled

with col2:
    Curricular_units_1st_sem_evaluations = int(st.number_input(label='Evaluated 1st Sem.', min_value=0, value=0, step=1, format="%d"))
    data[-1]['Curricular_units_1st_sem_evaluations'] = Curricular_units_1st_sem_evaluations

with col3:
    Curricular_units_1st_sem_approved = int(st.number_input(label='Approved 1st Sem.', min_value=0, value=0, step=1, format="%d"))
    data[-1]['Curricular_units_1st_sem_approved'] = Curricular_units_1st_sem_approved

with col4:
    Curricular_units_1st_sem_grade = float(st.number_input(label='Grade 1st Sem.', min_value=0.000))
    data[-1]['Curricular_units_1st_sem_grade'] = Curricular_units_1st_sem_grade

st.markdown('##### Curricular Units in the 2nd Semester')
col1, col2, col3, col4 = st.columns(4)
with col1:
    Curricular_units_2nd_sem_enrolled = int(st.number_input(label='Enrolled 2nd Sem.', min_value=0, value=0, step=1, format="%d"))
    data[-1]['Curricular_units_2nd_sem_enrolled'] = Curricular_units_2nd_sem_enrolled

with col2:
    Curricular_units_2nd_sem_evaluations = int(st.number_input(label='Evaluated 2nd Sem.', min_value=0, value=0, step=1, format="%d"))
    data[-1]['Curricular_units_2nd_sem_evaluations'] = Curricular_units_2nd_sem_evaluations

with col3:
    Curricular_units_2nd_sem_approved = int(st.number_input(label='Approved 2nd Sem.', min_value=0, value=0, step=1, format="%d"))
    data[-1]['Curricular_units_2nd_sem_approved'] = Curricular_units_2nd_sem_approved

with col4:
    Curricular_units_2nd_sem_grade = float(st.number_input(label='Grade 2nd Sem.', min_value=0.000))
    data[-1]['Curricular_units_2nd_sem_grade'] = Curricular_units_2nd_sem_grade


st.markdown('### Additional Information')
#col1, col2 = st.columns(2)
#with col1:
    #Application_order = int(st.number_input(label='Application Order', value=0, max_value=9))
    #data[-1]["Application_order"] = Application_order

#with col1:
    #Previous_qualification_grade = float(st.number_input(label='Prev. Qualification Grade', min_value=1.000, max_value=200.00))
    #data[-1]['Previous_qualification_grade'] = Previous_qualification_grade

#with col2:
    #Admission_grade = float(st.number_input(label='Admission Grade', min_value=0.000, max_value=200.00))
    #data[-1]['Admission_grade'] = Admission_grade

#with col4:
    #Age_at_enrollment = int(st.number_input(label='Age at Enrollment', min_value=1, format="%d"))
    #data[-1]['Age_at_enrollment'] = Age_at_enrollment



col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    Application_order = int(st.number_input(label='Application Order', value=0, max_value=9))
    data[-1]["Application_order"] = Application_order

with col2:
    Age_at_enrollment = int(st.number_input(label='Age at Enrollment', min_value=1, format="%d"))
    data[-1]['Age_at_enrollment'] = Age_at_enrollment

with col3:
    Unemployment_rate = float(st.number_input(label='Unemployment Rate'))
    data[-1]['Unemployment_rate'] = Unemployment_rate

with col4:
    Inflation_rate = float(st.number_input(label='Inflation Rate'))
    data[-1]['Inflation_rate'] = Inflation_rate

with col5:
    GDP = float(st.number_input(label='GDP'))
    data[-1]['GDP'] = GDP



with st.expander('### **View the Raw Data**'):
    data_df = pd.DataFrame(data)
    st.dataframe(data=data_df, width=800)


if st.button('Predict'):
    new_data = data_preprocessing(data=data_df)
    with st.expander('#### **View the Preprocessed Data**'):
        st.dataframe(data=new_data, width=800)
    st.write('### **Status: {}'.format(prediction(new_data)))