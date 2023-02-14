import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df = pd.read_csv("gapminder_with_codes.csv")
#get data for the year 2007
df_2007 = df[df['year']==2007]

#streamlit title
st.title('Gap Minder')

st.set_option('deprecation.showPyplotGlobalUse', False)
#plot a violinplot for the population dataset
sns.violinplot(data = df_2007, x= 'pop')
# plt.show()
st.pyplot()

sns.violinplot(data = df_2007, x = 'gdpPercap')
# plt.show()
st.pyplot()


sns.violinplot(data = df_2007, x = 'lifeExp')
# plt.show()
st.pyplot()
