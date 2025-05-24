import numpy as np
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, DataReturnMode
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
import streamlit as st
import numpy as np
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode
from collections import defaultdict
#from st_aggrid.shared import getAllColumnProps, getAllGridOptions
#from st_aggrid import getAllColumnProps, getAllGridOptions
from st_aggrid import AgGrid, GridOptionsBuilder


def generate_sales_data():
        """Generate dataset simulating sales data."""
        np.random.seed(42)
        rows = 50

        # Create a more complex dataset
        df = pd.DataFrame({
            'Product ID': range(1, rows + 1),
            'City': np.random.choice(['Karachi', 'Islamabad', 'Quata', 'Pishawar'], rows),
            'Category': np.random.choice(['Electronics', 'Clothing', 'Home', 'Sports'], rows),
            'Base Price': np.random.uniform(10, 500, rows).round(2),
            'Quantity Sold': np.random.randint(1, 100, rows),
        })

        return df


def configure_grid_options(df):
        """Configure advanced grid options with multiple features."""
        gb = GridOptionsBuilder.from_dataframe(df)
        # Configure row grouping and aggregation
        gb.configure_default_column(
                    groupable=True,
                    value=True,
                    enableRowGroup=True,
                    aggFunc='sum'
                )

                # Add filter and sort options
        gb.configure_grid_options(
                    enableRangeSelection=True,
                    enableRangeHandle=True,
                    suppressColumnMoveAnimation=False,
                    suppressRowClickSelection=False
                )
        # Make some columns editable
#        gb.configure_columns(['Base Price', 'Quantity Sold'], editable=True)

        # Add a virtual column (This will be calculated on the client side)
#        gb.configure_column(
#            'Total Revenue',
#            valueGetter="Number(data['Base Price']) * Number(data['Quantity Sold'])",
#            cellRenderer="agAnimateShowChangeCellRenderer",
#            type=["numericColumn"],
#            editable=False,
#            valueFormatter="x.toLocaleString('en-US', {style: 'currency', currency: 'USD'})"
 #       )
        
        return gb.build()


    # Generate data
sales_data = generate_sales_data()




    #testing 



    # Configure grid options
grid_options = configure_grid_options(sales_data)
gb = GridOptionsBuilder()
gb.configure_default_column(
                    groupable=True,
                    value=True,
                    enableRowGroup=True,
                    aggFunc='sum'
                )

                # Add filter and sort options
gb.configure_grid_options(
                    enableRangeSelection=True,
                    enableRangeHandle=True,
                    suppressColumnMoveAnimation=False,
                    suppressRowClickSelection=False)
gb.build()

        

    #st.subheader('Interactive Sales Data Grid')
st.markdown("""
    **Features:**
    - Edit Base Price and Quantity Sold
    - Automatic Total Revenue calculation
    """)





    # AgGrid with custom options
ag_return = AgGrid(
        sales_data,
        gridOptions=grid_options,
        height=500,
        theme='alpine',
        allow_unsafe_jscode=True,
        fit_columns_on_grid_load=True,
        reload_data=False
    )
