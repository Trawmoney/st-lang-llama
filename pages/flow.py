from barfi import barfi_schemas
import streamlit as st

saved_schemas = barfi_schemas()

select_schema = st.selectbox('Select a saved schema:', saved_schemas)

feed = Block(name='Feed')
feed.add_input()
result = Block(name='Result')
result.add_output()

barfi_result = st_barfi(base_blocks= [feed, result], load_schema=select_schema)
