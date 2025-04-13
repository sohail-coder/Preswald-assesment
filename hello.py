from preswald import text, plotly, connect, get_df, table, query, slider
import pandas as pd
import plotly.express as px

text("# Welcome to Preswald!")
text("This is your first app. 🎉")

# Load the CSV
connect()
df = get_df('sugar_consumption_dataset_csv')

text("# My Data Analysis App")
text("## 🇫🇷 France Sugar Consumption Over Time")

# Slider for user control
threshold = slider("Minimum Total Sugar Consumption (tons)", min_val=0, max_val=5000000, default=1000000)


# # country_search = text_input("Enter Country Name", default="France")
# # show_france = checkbox(label="France", default=True)
# # show_germany = checkbox(label="Germany", default=False)
# # show_italy = checkbox(label="Italy", default=False)
# # if show_france:
# #     selected_country = "France"
# # elif show_germany:
# #     selected_country = "Germany"
# # elif show_italy:
# #     selected_country = "Italy"
# # else:
# #     selected_country = "India"  



# SQL query to get France's data
sql = """
SELECT Year, Total_Sugar_Consumption
FROM sugar_consumption_dataset_csv
WHERE Country = 'France'
ORDER BY Year ASC
"""
filtered_df = query(sql, "sugar_consumption_dataset_csv")

# Apply the slider filter
filtered_df = filtered_df[filtered_df["Total_Sugar_Consumption"] > threshold]

# Display the table
table(filtered_df, title=f"France - Total Sugar Consumption Over Years (>{threshold} tons)")


filtered_df["Year"] = pd.to_numeric(filtered_df["Year"], errors="coerce")
filtered_df["Total_Sugar_Consumption"] = pd.to_numeric(filtered_df["Total_Sugar_Consumption"], errors="coerce")

# Plot with Plotly
fig = px.line(
    filtered_df,
    x="Year",
    y="Total_Sugar_Consumption",
    title="France - Total Sugar Consumption Over Time",
    markers=True
)

# Display plot
plotly(fig)


