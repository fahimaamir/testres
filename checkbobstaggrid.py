
import streamlit as st
from st_aggrid import AgGrid,GridOptionsBuilder
import pandas as pd
from time import sleep
#htmlmin==0.1.12
#@st.cache_resource
def load_data():
    df = pd.DataFrame({'name' : ['User1', 'User2', 'User3'],
                    'role' : ['member', 'admin', 'moderator'],
                    'sfee' : [0, 0, 0]})
    return df


df = load_data()
gd = GridOptionsBuilder.from_dataframe(df)
gd.configure_pagination(enabled=False)
gd.configure_default_column(editable=True, filter=True, resizable=True, sortable=True, value=True, enableRowGroup=True,
enablePivot=True, enableValue=True, floatingFilter=True, aggFunc='sum', flex=1, minWidth=150, width=150, maxWidth=200)
gd.configure_selection(selection_mode='multiple', use_checkbox=True)
    
gd.configure_column('Passengerid', headerCheckboxSelection = True)
gridoptions = gd.build()
tabla = AgGrid(df, editable=True,height=300,width='100%',
    update_on=['cellValueChanged'],
    reload_data=False,
    gridOptions=gridoptions)

# Step2: Select some rows
b2 = st.checkbox("Filter")
if b2:
    sel_row = tabla["selected_rows"]
    if sel_row:
        df_filter = pd.DataFrame(sel_row)
# Step 3: Print rows selected
        AgGrid(df_filter)
        
        
