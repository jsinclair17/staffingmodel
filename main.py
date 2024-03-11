import streamlit as st
import staffingdb as stdb

st.set_page_config(layout="centered")
st.title("Project Staffing")

customer_name = st.text_input("Customer Name", key='customer')
customer_address = st.text_input("Customer Address", key='address')

project_name = st.text_input("Project Name", key='projectname')
project_type = st.selectbox("Project Type", ["Data Engineering","Data Migration","Pipelines and Intergration","Data Story Telling"
,"Application Development","Testing/ Functional UAT"], key='projecttype')
st.divider()
project_area_names_cost = st.slider("Cost", min_value=1, max_value=10, help='lower rating is higher funding availability; higher is less costly', key='cost')
project_area_names_speed = st.select_slider("Time to Market", options=['Flexible', 'Average', 'Rapid'], value=('Flexible'), key='speed')
project_area_names_criticallity = st.slider("Criticallity (Org Impact)", min_value=1, max_value=10, key='critical')
project_area_names_tz = st.slider("Time Zone Alignment", min_value=1, max_value=10, key='timezone')
if project_area_names_tz <=3:
    st.write('time zone is less important based on this')
elif project_area_names_tz >3 and project_area_names_tz <=6:
    st.write('time zone is important but not critical')
else:
    st.write('time zone is critical')
project_area_names_complexity = st.slider("Complexity", min_value=1, max_value=10, key='complex')
project_area_names_expertise = st.slider("Expertise", min_value=1, max_value=10, key='expert')
project_area_names_laws = st.slider("Laws & Regulation", min_value=1, max_value=10, key='laws')
project_area_names_accessibility = st.slider("FTE Availabilty", min_value=1, max_value=10, key="accessible")
project_area_names_innovate = st.slider("Innovation & Process Maturity", min_value=1, max_value=10, key='innovate')
project_area_names_scalabilty = st.slider("Scalability", min_value=1, max_value=10, key='scalable')
#staff_name = st.text_input("Staff Name")
#staff_type_name = st.selectbox("Staff Type", ["Engineer", "Manager", "Designer"])
#staff_level_name = st.selectbox("Staff Level", ["Senior", "Junior", "MidLevel"])
#staff_location_name = st.selectbox("Staff Location", ["New York", "Los Angeles", "Chicago"])
st.divider()


customer1 = stdb.ProjectAdd(customer_name, customer_address, project_name, project_type, project_area_names_cost, project_area_names_speed, project_area_names_criticallity
                            , project_area_names_tz, project_area_names_complexity, project_area_names_expertise, project_area_names_laws, project_area_names_accessibility, project_area_names_innovate
                            , project_area_names_scalabilty)
#customer1.save()
def set_value():
    customer1.save()
    st.session_state['customer'] = ''
    st.session_state['address'] = ''
    st.session_state['projectname'] = ''
    st.session_state['projecttype'] = 'Data Engineering'
    st.session_state['cost'] = 1
    st.session_state['speed'] = 'Flexible'
    st.session_state['critical'] = 1
    st.session_state['timezone'] = 1
    st.session_state['complex'] = 1
    st.session_state['expert'] = 1
    st.session_state['laws'] = 1
    st.session_state['accessible'] = 1
    st.session_state['innovate'] = 1
    st.session_state['scalable'] = 1

testresult = st.button(label="Submit", on_click=set_value)

#if testresult:
#    customer1.save()
