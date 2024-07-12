import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

def main():
    st.title('PDF Display in Streamlit')

    # Path to the PDF file
    pdf_file = 'Book_of_abstracts.pdf'

    pdf_viewer(pdf_file)

if __name__ == "__main__":
    main()