import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
	"""Simple Iris EDA App"""
	st.title("Iris EDA App with Streamlit")
	st.subheader("Streamlit Deployed App")
	st.subheader("EDA Aspect")
		# Preview Dataset

	df = pd.read_csv("iris.csv")

	if st.checkbox("Preview Dataset"):
		number = st.number_input("Select Number of Rows To View",value=1)
		st.dataframe(df.head(number))

	if st.checkbox("Shape of Dataset"):
		st.write(df.shape)
		data_dim = st.radio("Show Dimensions By ",("Rows","Columns"))
		if data_dim == 'Rows':
			st.text("Showing the Rows")
			st.write(df.shape[0])
		if data_dim == 'Columns':
			st.text("Showing the Columns")
			st.write(df.shape[1])

	if st.checkbox("Select Columns"):
		all_columns = df.columns.tolist()
		selected_columns = st.multiselect("Select Columns",all_columns)
		new_df = df[selected_columns]
		st.dataframe(new_df)

	if st.button("Summary of Dataset"):
		st.write(df.describe())

	if st.button("Value Counts"):
		st.text("Value Counts By Target")
		st.write(df.iloc[:,-1].value_counts())

	st.subheader("Data Visualization")
	# Correlation Plot
	if st.checkbox("Correlation Plot with Matplotlib"):
		plt.matshow(df.corr())
		st.pyplot()

	if st.checkbox("Correlation Plot with Seaborn"):
		st.write(sns.heatmap(df.corr(),annot=True))
		st.pyplot()

	if st.checkbox("Pie Chart"):
		if st.button("Generate Pie Chart"):
			st.write(df.iloc[:,-1].value_counts().plot.pie(autopct="%1.1f%%"))
			st.pyplot()

	if st.checkbox("Plot Value Counts"):
		st.write(df.iloc[:,-1].value_counts().plot(kind='bar'))
		st.pyplot()


	if st.checkbox("Plot Value Counts By Columns"):
		st.text("Value Counts By Target/Class")

		all_columns_names = df.columns.tolist()
		primary_col = st.selectbox('Select Primary Column To Group By',all_columns_names)
		selected_column_names = st.multiselect('Select Columns Names',all_columns_names)
		if st.button("Plot"):
			st.text("Generating Plot for: {} and {}".format(primary_col,selected_column_names))
			if selected_column_names:
				vc_plot = df.groupby(primary_col)[selected_column_names].count()		
			else:
				vc_plot = df.iloc[:,-1].value_counts()
			st.write(vc_plot.plot(kind='bar'))
			st.pyplot()



if __name__ == '__main__':
	main()