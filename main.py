import streamlit as st
import staffingdb as stdb
from PIL import Image
import pandas as pd
# You can always call this function where ever you want

def add_logo(logo_path, width, height):
    """Read and return a resized logo"""
    logo = Image.open(logo_path)
    modified_logo = logo.resize((width, height))
    return modified_logo

my_logo = add_logo(logo_path="./TLLogo.png", width=800, height=100)
st.image(my_logo)
#st.set_page_config(layout="centered")
#st.title(':green[Jeff]')


# customer_name = st.text_input("Customer Name", key='customer')
# customer_address = st.text_input("Customer Email Address", key='address')

# project_name = st.text_input("Project Name", key='projectname')
# project_type = st.selectbox("Project Type", ["Data Engineering","Data Migration","Pipelines and Intergration","Data Story Telling"
# ,"Application Development","Testing/ Functional UAT"], key='projecttype') 

#st.divider()
project_area_names_cost = st.slider("Funding Availability", min_value=1, max_value=5, help='Your enagagment funding level has been allocated', key='cost')
# """ if project_area_names_cost <3:
#     st.write('Conservative Spend')
# elif project_area_names_cost >=3 and project_area_names_cost <5:
#     st.write('Business Case Required for Additional Spend')
# elif project_area_names_cost >=5 and project_area_names_cost <7:
#     st.write('Discretionary Budget Available')
# elif project_area_names_cost >=7 and project_area_names_cost <10:
#     st.write('Budget Contingency Available')
# else:
#     st.write('Large Investment Made') """
#st.divider()
project_area_names_speed = st.slider("Go To Market Strategy", min_value=1, max_value=5, help='Describe the level of planning to deliver product', key='speed')
# """ if project_area_names_speed <3:
#     st.write('Proof of Concept')
# elif project_area_names_speed >=3 and project_area_names_speed <5:
#     st.write('Protoytpe Development')
# elif project_area_names_speed >=5 and project_area_names_speed <7:
#     st.write('MVP')
# elif project_area_names_speed >=7 and project_area_names_speed <10:
#     st.write('Scaling Strategy Development')
# else:
#     st.write('Full Feature Launch') """
#st.divider()
#project_area_names_criticallity = st.slider("Criticallity (Org Impact)", min_value=1, max_value=10, key='critical')
project_area_names_tz = st.slider("Time Zone Coordination", min_value=1, max_value=5, help='Describe the need for resources to be time zone aligned' ,key='timezone')
# """ if project_area_names_tz <3:
#     st.write('Minimal Overlap Required')
# elif project_area_names_tz >=3 and project_area_names_tz <5:
#     st.write('Overlap as requested')
# elif project_area_names_tz >=5 and project_area_names_tz <7:
#     st.write('Adaptive Scheduling Required')
# elif project_area_names_tz >=7 and project_area_names_tz <10:
#     st.write('Alignment Required for Most Deliverables')
# else:
#     st.write('Required') """
#st.divider()
project_area_names_complexity = st.slider("Team Size", min_value=1, max_value=5, help='Amount of capacity needed to support the initiative' ,key='complex')
# """ if project_area_names_complexity <3:
#     st.write('Individual Contributor')
# elif project_area_names_complexity >=3 and project_area_names_complexity <5:
#     st.write('Individual Contributor with Advisory Support')
# elif project_area_names_complexity >=5 and project_area_names_complexity <7:
#     st.write('Functional Project Team')
# elif project_area_names_complexity >=7 and project_area_names_complexity <10:
#     st.write('Functional Project Team with Advisory Support')
# else:
#     st.write('Large Program Team') """
#st.divider()
project_area_names_expertise = st.slider("Expertise", min_value=1, max_value=5, help='Skillset necessary for successful delivery of the initiative', key='expert')
# """ if project_area_names_expertise <5:
#     st.write('Functional Expert')
# elif project_area_names_expertise >=5 and project_area_names_expertise <10:
#     st.write('Skilled Practicioner')
# else:
#     st.write('Subject Matter Expert') """
#st.divider()
project_area_names_laws = st.slider("Laws & Regulation", min_value=1, max_value=5, help='Barriers for using offshore resources for work', key='laws')
# """ if project_area_names_laws <3:
#     st.write('Lenient')
# elif project_area_names_laws >=3 and project_area_names_laws <5:
#     st.write('Moderate Oversight')
# elif project_area_names_laws >=5 and project_area_names_laws <7:
#     st.write('Enhanced Oversight')
# elif project_area_names_laws >=7 and project_area_names_laws <10:
#     st.write('Highly Regulated')
# else:
#     st.write('Restrictive') """
#st.divider()
project_area_names_accessibility = st.slider("Immediate Response Tolerance", min_value=1, max_value=5, help='Communication promptness required', key="accessible")
# """ if project_area_names_accessibility <3:
#     st.write('Within 1-2 Business Days')
# elif project_area_names_accessibility >=3 and project_area_names_accessibility <5:
#     st.write('Within 6-8 hours during Operating Hours')
# elif project_area_names_accessibility >=5 and project_area_names_accessibility <7:
#     st.write('Within 4-6 hours during Operating Hours')
# elif project_area_names_accessibility >=7 and project_area_names_accessibility <10:
#     st.write('Within 2-4 hours during Operating Hours')
# else:
#     st.write('Fully accessible during Operating Hours') """
#st.divider()
project_area_names_innovate = st.slider("Innovation & Process Maturity", min_value=1, max_value=5, help='Describe the need to be more Strategic or Tactical', key='innovate')
# """ if project_area_names_innovate <3:
#     st.write('Routine')
# elif project_area_names_innovate >=3 and project_area_names_innovate <5:
#     st.write('Flexible Process')
# elif project_area_names_innovate >=5 and project_area_names_innovate <7:
#     st.write('Strategic Innovation')
# elif project_area_names_innovate >=7 and project_area_names_innovate <10:
#     st.write('Transformational Innovation')
# else:
#     st.write('Disruptor') """
#st.divider()
#project_area_names_scalabilty = st.slider("Scalability", min_value=1, max_value=10, key='scalable')
#staff_name = st.text_input("Staff Name")
#staff_type_name = st.selectbox("Staff Type", ["Engineer", "Manager", "Designer"])
#staff_level_name = st.selectbox("Staff Level", ["Senior", "Junior", "MidLevel"])
#staff_location_name = st.selectbox("Staff Location", ["New York", "Los Angeles", "Chicago"])
#st.divider()


customer1 = stdb.ProjectAdd(
    #customer_name, customer_address, project_name, project_type, 
    project_area_names_cost, project_area_names_speed
                            #, project_area_names_criticallity
                            , project_area_names_tz, project_area_names_complexity, project_area_names_expertise, project_area_names_laws, project_area_names_accessibility, project_area_names_innovate
                            #, project_area_names_scalabilty
                            )
#customer1.save()
spread_val = customer1.getspread()
def set_value():
    customer1.save()
    st.session_state['customer'] = ''
    st.session_state['address'] = ''
    st.session_state['projectname'] = ''
    st.session_state['projecttype'] = 'Data Engineering'
    st.session_state['cost'] = 1
    st.session_state['speed'] = 1
    #st.session_state['critical'] = 1
    st.session_state['timezone'] = 1
    st.session_state['complex'] = 1
    st.session_state['expert'] = 1
    st.session_state['laws'] = 1
    st.session_state['accessible'] = 1
    st.session_state['innovate'] = 1
    #st.session_state['scalable'] = 1
    st.write(f'Submission was added successfully')
st.divider()
df = pd.DataFrame(spread_val[0], columns=['Location','Spread'])
st.bar_chart(df,  x='Location', color=['#384268'])
st.write(f"Potential Savings utilizing Thought Logic's Ignition Staffing Model is {spread_val[1][0]} to {spread_val[1][1]}")

#st.write('Please submit selections if you would like to be contacted about your engagement')
#testresult = st.button(label="Submit", on_click=set_value)
#if testresult:
#    customer1.save()
