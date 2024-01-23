import streamlit as st
import requests
from PIL import Image
import subprocess
import sys



st.title("PixelCraft AI")
st.caption("Draw anything you like and see if you can outsmart AI!")


API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "ENTER YOUR HUGGINGFACE AUTHENTICATOR"}


    
def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()


if 'player_points' not in st.session_state:
    st.session_state.player_points = 0

if 'ai_points' not in st.session_state:
    st.session_state.ai_points = 0
try:
   subprocess_executed=st.button("Draw image")
   if subprocess_executed==True:
        subprocess.run([f"{sys.executable}", "pypaint.py"])
        subprocess_executed = True
   path=st.text_input("Enter File name")
   trunc_path=path[28:]
   output = query(trunc_path)
   st.write("You Drew")
   st.image(trunc_path)
   st.write("My guess is.......")
   st.write(output[0]['generated_text'])
        
   add_selectbox = st.selectbox("Did the AI guess correctly?", ["Yes", "No"])
   with st.sidebar:
      st.write(f"Player points : {st.session_state.player_points}")
      st.write(f"AI points : {st.session_state.ai_points}") 
   reset=st.button("Reset scores")

   if reset==True:
      st.session_state.ai_points =0
      st.session_state.player_points = 0
           
   if add_selectbox=='Yes':   
       st.session_state.ai_points +=100
   else:      
       st.session_state.player_points += 100

        
except:
    st.write("Please input a valid file")
    
    



