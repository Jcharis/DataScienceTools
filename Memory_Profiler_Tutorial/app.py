# Core Pkgs
import streamlit as st 
from memory_profiler import profile  



@profile
def main():
 	st.title("Memeory Profiling Streamlit Apps")
 	menu = ["Home","Text Analysis","About"]

 	choice = st.sidebar.selectbox("Menu",menu)

 	if choice == "Home":
 		st.subheader("Home")

 	elif choice == "Text Analysis":
 	    st.subheader("Text Analysis")

 	else:
 		st.subheader("About") 



if __name__ == '__main__':
	main()


# How to Run
# python3 -m memory_profiler app.py
# mprof run app.py
# mprof plot