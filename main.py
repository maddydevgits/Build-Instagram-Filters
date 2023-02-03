
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import cv2

st.title('Build Instagram Filters Here')

def main():
	st.title("FILTER ME")

	menu = ["Image","Dataset","DocumentFiles","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Image":
		st.subheader("Image")


with st.sidebar:
    selected = option_menu("Select Filter", ["HDR", 'invert','greyscale','less_bright','more_bright','pencil_col'], 
        icons=['star','star','star','star','star','star',], menu_icon="image", default_index=1)
    
with st.sidebar.expander("About the App"):
     st.write("""
        Use this simple app to convert your favorite photo to a pencil sketch, a grayscale image or an image with blurring effect many more.  \nHope you enjoy!
     """)

uploaded_file = st.file_uploader("", type=['jpg','png','jpeg'])

if uploaded_file is not None:
    if selected=='HDR':
        with open('test.png','wb') as f:
            f.write(uploaded_file.getbuffer())
        img=cv2.imread('test.png')
        hdr = cv2.detailEnhance(img, sigma_s=12, sigma_r=0.15)
        hdr1=cv2.cvtColor(hdr,cv2.COLOR_BGR2RGB)
        col1,col2=st.columns(2)
        col1.image(Image.open(uploaded_file),width=250)
        col2.image(hdr1,width=250)
        cv2.imwrite('output/HDR.png',hdr)
    elif selected=='invert':
        with open('test.png','wb') as f:
            f.write(uploaded_file.getbuffer())
        img=cv2.imread('test.png')
        inv = cv2.bitwise_not(img)
        inv=cv2.cvtColor(inv,cv2.COLOR_BGR2RGB)
        col1,col2=st.columns(2)
        col1.image(Image.open(uploaded_file),width=250)
        col2.image(inv,width=250)
        cv2.imwrite('output/invert.png',inv)

    
    
    
    
    
