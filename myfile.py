import pickle
import streamlit as st
model1 = pickle.load(open("model.pkl", "rb"))

def myf1():
    sepal_length = st.number_input('Sepal length')
    sepal_width= st.number_input('Sepal width')
    petal_length = st.number_input('Petal length')
    petal_width = st.number_input('Petal width')
    pred = st.button('PREDICT')

    if(pred):
        op = model1.predict([[sepal_length, sepal_width, petal_length, petal_width]])
        st.write('The class belong to:',op)
    

myf1()
    
