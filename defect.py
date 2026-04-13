import streamlit as st
from dotenv import load_dotenv
load_dotenv()


import google.generativeai as genai
from PIL import Image

st.set_page_config('DEFECT AI',page_icon='🪐',layout='wide')
st.title("AI POWERED DEFECT ANALYSER 🚀")
st.header(":blue[Prototype of automated structural defect analyser using ai]")
st.subheader(":red[AI powered structural defect analysis using streamlit that allows users to upload the image of any structural defects and to get suggestions and recommendations for repair and rebuilt]")


with st.expander('➤about the app'):
    st.markdown(f'''this app helps to detect the defects like cracks,misallignments etc and provide
                **Defect Detection**
                **recommendation**
                **suggestions for improvements**''')
    
    
import os 
key=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=key)

input_image=st.file_uploader("upload your file here",type=['png','jpeg','jpg'])
img=''
if input_image:
    img=Image.open(input_image).convert('RGB')
    st.image(img,caption="uploaded successfully")
    
    
prompt=f'''You are a quality engineer and civil engineer .you need to 
analyse the input image and provide necessary details for the below questions in bullet points
(max 3 points for each questions)

1.Identify the type of structural defect in given image like cracks ,bends,misallignments
2.identify the causes for the defect
3.what is the intensity of the cracks
4.what is the probablity that building will collapse
5.give some measures to counter the defect
6.provide some recommendations for these defects to not happen in future
7.is it worth to repair the defect
8.provide summary of the analysis
9.identify any potential safety hazard associated with this image
10.whether the defect will cause any defect to neighbouring areas
'''
model=genai.GenerativeModel('gemini-2.5-flash-lite')
def generate_result(prompt,img):
    result=model.generate_content(f''' using the given {prompt}
                                  and given {img}
                                  analyse the image and give the
                                  results as per the given prompt''')
    return result.text

submit=st.button('analyse the image')
if submit:
    with st.spinner('results loading'):
        response=generate_result(prompt,img)
        st.markdown('## :green[Results]')
        st.write(response)