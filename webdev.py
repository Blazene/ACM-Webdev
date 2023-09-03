import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
def quad_plot(a,b,c):
    x= np.linspace(-10, 10)
    y= a*x**2 + b*x + c

    fig, ax = plt.subplots()
    ax.plot(x,y)
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title(f"Quadratic equation: {a}x^2 + {b}x + {c}")

    st.pyplot(fig)

def main():

    st.title("Math visualization: Quadratic equation")
    st.sidebar.header("Quadratic equation coefficients")
    a = st.sidebar.slider("Coefficient of a", -10,10,0)
    b= st.sidebar.slider("Coefficient of b", -10,10,0)
    c= st.sidebar.slider("Coefficient of c", -10,10,0)
    quad_plot(a,b,c)
if __name__=="__main__":
    main()