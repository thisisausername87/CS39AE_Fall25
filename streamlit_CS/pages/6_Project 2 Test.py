import streamlit as st
import pandas as pd
import plotly.express as px
import os

data_path = os.path.join(os.getcwd(), "streamlit_CS", "data", "degrees_that_pay_back.csv")
df = pd.read_csv(data_path)
df_sorted = df.sort_values(by="Starting Median Salary")

fig = px.bar(df_sorted, x="Undergraduate Major", y="Starting Median Salary", title="Starting Salary by Major")
fig.show()
st.write("This bar graph shows the starting median salaries for each undergraduate major. The graph is understood by looking at the value on the left of the graph and correlating it with the major on the bottom under the bar.") 
st.write("This data shows that some of the highest paying majors are physicians assistant, chemical engineering, computer engineering, and electrical engineering. There are no outliers or otherwise unusual data points in the graph. One conclusion that can be found from the information is that STEM related majors that are more mathematically and scientifically technical tend to have higher paying positions as opposed to the more humanitarian jobs such as journalism and music.")

fig = px.histogram(df_sorted, x="Starting Median Salary", nbins=20, title="Counts of Starting Salaries")
fig.update_layout(
    xaxis_title="Starting Median Salary",
    yaxis_title="Count"
)
fig.show()
st.write("This histogram shows the number of jobs that are in each slary range.")

fig = px.scatter(df_sorted, x="Starting Median Salary", y="Percent change from Starting to Mid-Career Salary", title="Percent Salary Increase Based on Starting Salary")
fig.update_layout(
    xaxis_title="Starting Median Salary",
    yaxis_title="Salary Percent Increase"
)
fig.show()

fig = px.line(df_sorted, x="Starting Median Salary", y="Mid-Career 90th Percentile Salary", title="Upper Salary Limit Based On Starting Salary")
fig.show()
