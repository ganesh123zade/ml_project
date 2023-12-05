import streamlit as st
import pickle
lin_model=pickle.load(open('lin_model.pkl','rb'))
log_model=pickle.load(open('log_model.pkl','rb'))
svc_model=pickle.load(open('svc_model.pkl','rb'))


def classify(num):
    if num <0.5:
        return'Satosa'
    elif num<1.5:
        return'Vercicolor'
    else:
        return 'Verginica'

# Create function 
def main():
    st.title('Classification of Flower')
    activities=['Linear Regression','Logistic Regression','SVM']
    options=st.sidebar.selectbox('',activities)
    st.subheader(options)
    sl=st.slider('Select Sepal Length',0.0,10.0)
    sw=st.slider('Select Sepal width',0.0,10.0)
    pl=st.slider('Select petal Length',0.0,10.0)
    pw=st.slider('Select petal width',0.0,10.0)
    input=[[sl,sw,pl,pw]]

    if st.button('classify'):
        if (options=='Linear Regression'):
            st.success(classify(lin_model.predict(input)))
        elif(options== 'Logistic Regression'):
            st.success(classify(log_model.predict(input)))
        else:
            st.success(classify(svc_model.predict(input)))

if __name__=='__main__':
    main()