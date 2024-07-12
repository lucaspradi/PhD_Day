import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="ICN PhD Day 2024", 
    page_icon="icn.png", 
    layout="centered", 
    initial_sidebar_state="auto", 
    menu_items=None
)

if "information_button_clicked" not in st.session_state:
    st.session_state.information_button_clicked = False

if "book_of_abstracts_button_clicked" not in st.session_state:
    st.session_state.book_of_abstracts_button_clicked = True

with st.sidebar:
    st.image("Logo_ICN.png", use_column_width="auto")

    st.write("This is the official website for the PhD day of the ICN - Universite Cote D'Azur. Here you can find the book of abstracts and the schedule of the event, as well as more information. Hope you Enjoy!")
    st.markdown("**19th of July 2024** - From 09:00 to 13:30")
    st.write("Please select what you would like to see:")
    information = st.button("Information", use_container_width=True)
    abstracts = st.button("Book of abstracts", use_container_width=True)

if information:
    st.session_state.information_button_clicked = True
    st.session_state.book_of_abstracts_button_clicked = False

if abstracts:
    st.session_state.information_button_clicked = False
    st.session_state.book_of_abstracts_button_clicked = True

st.title('ICN PhD Day 2024')

if st.session_state.book_of_abstracts_button_clicked == True:
    # Path to the PDF file
    pdf_file = 'Book_of_abstracts.pdf'

    pdf_viewer(pdf_file)

if st.session_state.information_button_clicked == True:

    st.subheader('Information', divider="blue")
    st.markdown("The PhD Day of the ICN - Universite Cote D'Azur will take place on the 19th of July 2024 at Villa Arson in Nice. The event will start at 9:00 and will end at 13:30. The event will be a great opportunity to meet other PhD students and to learn about the research that is being done at the ICN. We hope to see you there!")
    st.markdown("Please arrive at the location at least 15 minutes before the start of the event.")
    st.markdown("The event will also hold a Small Coffee Break at 10:30 and a Lunch Buffet at 12:30.")

    st.subheader('Schedule', divider="blue")
    c = st.container()
    c.write("**08:45 - 09:00:** Registration")
    c.write("**09:00 - 10:30:** Student Presentations: Keyu MAO, Alex WASCHTSHC, Alice RAVEZ, Fakhri-Eddin LAHFAIDH, Anastasiia PIDVOROTNIA")
    c.write("**10:30 - 11:00:** Small Coffee Break")
    c.write("**11:00 - 11:45:** Student Presentations: Matthieu JORANDON, Sandra LITWIN, Jean-Baptiste COFFIN")
    c.write("**11:45 - 12:15:** Invited Speaker: Dr. Hervé RAPS")
    c.write("**12:15 - 12:25:** Awards - Closing Ceremony")
    c.write("**12:25 - 13:30:** Lunch Buffet")

    st.subheader('Location', divider="blue")

    st.write('The event will take place at <a href="https://maps.app.goo.gl/sA1bDTkCePrknuZo8" target="_blank">Villa Arson</a> in Nice. The address is: 20 Av. Stephen Liegeard, 06100 Nice. You can find the location on the map below.', unsafe_allow_html=True)

    m = folium.Map(location=[43.721745150171614, 7.252915797843882], zoom_start=16)
    folium.Marker([43.721745150171614, 7.252915797843882], popup='See Villa Arson on <a href="https://maps.app.goo.gl/sA1bDTkCePrknuZo8" target="_blank">Google Maps</a>', tooltip='Villa Arson, 20 Av. Stephen Liegeard, 06100 Nice').add_to(m)
    
    st.data = st_folium(m, width=700)