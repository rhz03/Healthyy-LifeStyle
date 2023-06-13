import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import hydralit_components as hc 

from streamlit_lottie import st_lottie
import json
# Set page configuration
st.set_page_config(
    page_title="Healthy Lifestyle Application",
    page_icon= "✅",
    layout='wide'
)
t1, t2 = st.columns(2)
with t1:
    st.markdown('')
with t2:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("""
    **Health Care Analytics**
    
    by Rim Zeaiter
    """)


# Tab layout
menu_data = [
    {'label': "Introduction", 'icon': '🌟'},
    {'label': 'Rank & Life Expectancy','icon': '📈'},
    {'label': 'Cities', 'icon': '🏙️'},
    {'label': "Overview", 'icon': '🔍'}
]
over_theme = {'txc_inactive': 'white','menu_background':'rgb(0,153,76)', 'option_active':'white'}

menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    hide_streamlit_markers=True,
    sticky_nav=True, #at the top or not
    sticky_mode='sticky', #jumpy or not-jumpy, but sticky or pinned
)
#page 1:Introduction
if menu_id=="Introduction":
 st.title('Healthy LifeStyle')
 st.write("""
        In today's fast-paced world, maintaining a healthy lifestyle has become increasingly 
        important. Adopting healthy habits not only improves our overall well-being but also 
        reduces the risk of various chronic diseases. This interactive dashboard provides valuable insights 
        into the factors that contribute to a healthy lifestyle, allowing you to explore the connections 
        between different variables and their impact on individual health outcomes. By leveraging a comprehensive dataset 
        on healthy lifestyle indicators, including diet, physical activity, sleep patterns, and stress levels, this dashboard
        aims to empower individuals to make informed decisions and take proactive steps towards achieving 
        and maintaining a healthy lifestyle. Whether you're a health enthusiast, a researcher, or simply curious about 
        the factors that influence our well-being, this dashboard is designed to provide you with valuable information 
        and inspire positive changes in your daily routine. Let's embark on a journey to discover the keys to a healthy lifestyle together!
       """)


# Load the dataset (replace 'your_dataset.csv' with the actual filename)
 data = data = pd.read_csv("/Users/macbook/Desktop/rim zeaiter streamlit /healthy_lifestyle_city_2021 copy.csv")
 # Display a message
 st.markdown('<p style="color: green;"><strong>Click the button to display the data</strong></p>', unsafe_allow_html=True)
 #st.dataframe(data.head())
 if st.button('Healthy lifestyle Data'):
    # Display the data frame
    st.dataframe(data.head())
 else:
    # Display a message
    st.write("")
 st.image('/Users/macbook/Desktop/png-clipart-ecg-and-healthy-living-ecg-healthy-lifestyle.png')
elif menu_id=='map':
  st.title('Correlation Matrix Analysis 📊')
  data = data = pd.read_csv("/Users/macbook/Desktop/rim zeaiter streamlit /healthy_lifestyle_city_2021 copy.csv")


# Page 2.2: Life Expectancy
elif menu_id == "Rank & Life Expectancy":

    
    col1, col2, col3 = st.columns(3)

    with col1:
     st.markdown(
        """
        <div class="metric-container" style="border: 2px solid green; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <h3 class="metric-title">Rank 🥇</h3>
            <p class="metric-value">Amsterdam </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    with col2:
     st.markdown(
        """
        <div class="metric-container" style="border: 2px solid green; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <h3 class="metric-title">Total Cities</h3>
            <p class="metric-value">44</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    with col3:
      st.markdown(
    """
    <style>
    .metric-container {
        border: 2px solid green;
        padding: 25px; /* Increase the padding value to create more space inside the border */
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .metric-value {
        font-size: 18px; /* Adjust the font size as desired */
    }
    </style>
    <div class="metric-container">
        <p class="metric-value">As <strong>happiness level</strong> 😊↑</p>
        <p class="metric-value"><strong>life expectancy</strong> 📈↑</p>
    </div>
    """,
    unsafe_allow_html=True
)

    st.header('Rank🥇')
    df= pd.read_csv("/Users/macbook/Desktop/rim zeaiter streamlit /healthy_lifestyle_city_2021 copy.csv")


# Sort DataFrame by Rank in ascending order
    df = df.sort_values('Rank')

# Create checkbox for selecting display option
    display_option = st.checkbox('Display All Cities', value=True)

    if display_option:
    # Display all cities in ascending order based on rank
     selected_rank = None  # Assigning a default value when all cities are selected
    else:
    # Create number input for selecting rank
     selected_rank = st.number_input('Select Rank', min_value=1, max_value=len(df), value=1, step=1)

# Filter DataFrame based on selected rank
    if selected_rank is not None:
      filtered_dfd = df[df['Rank'] <= selected_rank]
    else:
     filtered_dfd = df
# Create horizontal bar plot
    fig6 = px.bar(filtered_dfd, x='Rank', y='City', orientation='h')

# Set plot title and axis labels
    fig6.update_layout(title='City Rankings', xaxis_title='Rank', yaxis_title='City')
# Set the size of the plot
    fig6.update_layout(height=700, width=1000)
# Show the plot
    st.plotly_chart(fig6)
    st.header("Life Expectancy")
   
    data= pd.read_csv("/Users/macbook/Desktop/rim zeaiter streamlit /healthy_lifestyle_city_2021 copy.csv")

    # Available cities
    available_cities = data['City'].unique()

# Multiselect for selecting cities including 'All' option (default selected)
    selected_cities = st.multiselect('Select Cities', ['All'] + list(available_cities), default='All', key='city_select')


    # Check if 'All' is selected and update the selected cities accordingly
    if 'All' in selected_cities:
        selected_cities = available_cities

    # Filter the dataset based on selected cities
    filtered_data = data[data['City'].isin(selected_cities)]

    # Create subplots
    fig = make_subplots(rows=2, cols=2, subplot_titles=("Obesity vs Life Expectancy", "Happiness Level vs Life Expectancy",
                                                      "Cost of Bottle of Water vs Life Expectancy", "Sunshine Hours vs Life Expectancy"))

    # Encode cities as categorical values with numeric codes
    city_codes = pd.Categorical(filtered_data['City'], categories=selected_cities).codes

    # Scatterplot 1: Obesity vs Life Expectancy
    fig.add_trace(go.Scatter(x=filtered_data['Obesity levels(Country)'], y=filtered_data['Life expectancy(years) (Country)'],
                             mode='markers', marker=dict(color=city_codes), hovertext=filtered_data['City']),
                  row=1, col=1)

    # Scatterplot 2: Happiness Level vs Life Expectancy
    fig.add_trace(go.Scatter(x=filtered_data['Happiness levels(Country)'], y=filtered_data['Life expectancy(years) (Country)'],
                             mode='markers', marker=dict(color=city_codes), hovertext=filtered_data['City']),
                  row=1, col=2)

    # Scatterplot 3: Cost of Bottle of Water vs Life Expectancy
    fig.add_trace(go.Scatter(x=filtered_data['Cost of a bottle of water(City)'], y=filtered_data['Life expectancy(years) (Country)'],
                             mode='markers', marker=dict(color=city_codes), hovertext=filtered_data['City']),
                  row=2, col=1)

    # Scatterplot 4: Sunshine Hours vs Life Expectancy
    fig.add_trace(go.Scatter(x=filtered_data['Sunshine hours(City)'], y=filtered_data['Life expectancy(years) (Country)'],
                             mode='markers', marker=dict(color=city_codes), hovertext=filtered_data['City']),
                  row=2, col=2)

    # Update subplot titles and layout
    #fig.update_layout(title_text='Scatterplots', showlegend=False)
    # Update subplot titles and layout
    fig.update_layout(showlegend=False, height=700, width=1300)

    # Adjust the size of scatterplots
    #fig.update_layout(
        #height=1000,  # Update the height
       # width=1500,  # Update the width
        #autosize=False,  # Disable autosize
 #   )
    
    # Update x-axis and y-axis titles
    fig.update_xaxes(title_text='Obesity levels(Country)', row=1, col=1)
    fig.update_yaxes(title_text='Life expectancy(years) (Country)', row=1, col=1)

    fig.update_xaxes(title_text='Happiness levels(Country)', row=1, col=2)
    fig.update_yaxes(title_text='Life expectancy(years) (Country)', row=1, col=2)

    fig.update_xaxes(title_text='Cost of a bottle of water(City)', row=2, col=1)
    fig.update_yaxes(title_text='Life expectancy(years) (Country)', row=2, col=1)

    fig.update_xaxes(title_text='Sunshine hours(City)', row=2, col=2)
    fig.update_yaxes(title_text='Life expectancy(years) (Country)', row=2, col=2)

    # Display the scatterplots
    st.plotly_chart(fig)


#page3:visualizations of top and least
# Get the column names from the DataFrame
elif menu_id=="Cities":
 st.title('Cities🏙️')
 
 
 st.markdown('<h1 style="color: green;">Top 5 cities</h1>', unsafe_allow_html=True)
 data = data = pd.read_csv("/Users/macbook/Desktop/rim zeaiter streamlit /healthy_lifestyle_city_2021 copy.csv")

# Option to select bars to display
 columns = data.columns[2:]
 selected_bars = st.multiselect('Select bars to display',['All']+ list(columns),default=['All'],key='select bar')


# Filter dataframe based on selected bars
 if 'All' in selected_bars:
    selected_bars = columns.tolist()
 else:
    data = data[['City'] + selected_bars]

# Draw bar plots for selected bars
 if selected_bars:
    rows = 5
    cols = 2
    num_plots = len(selected_bars)
    fig4 = make_subplots(rows=rows, cols=cols, subplot_titles=selected_bars)
    plot_index = 0
    for row in range(1, rows + 1):
        for col in range(1, cols + 1):
            if plot_index >= num_plots:
                break
            column = selected_bars[plot_index]
            top_cities = data.nlargest(5, column)
            trace = go.Bar(x=top_cities['City'], y=top_cities[column])
            fig4.add_trace(trace, row=row, col=col)
            plot_index += 1
            fig4.update_xaxes(title_text='City', row=row, col=col)
            fig4.update_yaxes(title_text=column, row=row, col=col)

    fig4.update_layout(height=1200, width=1200, showlegend=False)
    st.plotly_chart(fig4)



 st.markdown('<h1 style="color: green;">Least 5 cities</h1>', unsafe_allow_html=True)
 # Get the column names from the DataFrame
 data = data = pd.read_csv("/Users/macbook/Desktop/rim zeaiter streamlit /healthy_lifestyle_city_2021 copy.csv")

# Option to select bars to display
 columnss = data.columns[2:]
 selected_barss = st.multiselect('Select bars to display',['All']+ list(columnss),default=['All'],key='selected bar')

# Filter dataframe based on selected bars
 # Filter dataframe based on selected bars
 if 'All' in selected_barss:
    selected_barss = columnss.tolist()
 else:
    data = data[['City'] + selected_barss]

# Draw bar plots for selected bars
 if selected_barss:
    rows = 5
    cols = 2
    num_plots = len(selected_barss)
    fig5 = make_subplots(rows=rows, cols=cols, subplot_titles=selected_barss)
    plot_index = 0
    for row in range(1, rows + 1):
        for col in range(1, cols + 1):
            if plot_index >= num_plots:
                break
            column = selected_barss[plot_index]
            top_cities = data.nsmallest(5, column)
            trace = go.Bar(x=top_cities['City'], y=top_cities[column])
            fig5.add_trace(trace, row=row, col=col)
            plot_index += 1
            fig5.update_xaxes(title_text='City', row=row, col=col)
            fig5.update_yaxes(title_text=column, row=row, col=col)

    fig5.update_layout(height=1200, width=1200, showlegend=False)
    st.plotly_chart(fig5)



#page 4:overview
elif menu_id=='Overview':
 st.title("Overview")


# Display the header in the center with green color
 st.markdown('<h1 class="center" style="color: green;">Recommendation</h1>', unsafe_allow_html=True)



# Recommendation 1: Obesity
#st.markdown("<h3 style='text-align: center; color: blue;'>Obesity: .</h1>", unsafe_allow_html=True)
#defining lottie function to visualize animated pictures
 def load_lottiefile(filepath: str):
     with open(filepath) as f:
         return json.load(f)
 col1, col2, col3, col4 = st.columns(4)

 with col1:
    # Animation 1 for Obesity
    lottie_obesity = load_lottiefile("/Users/macbook/Desktop/obesity.json")
    st_lottie(lottie_obesity)
    st.caption("""
        <div>
            <div style="vertical-align:left;font-size:16px;padding-left:5px;padding-top:5px;margin-left:0em";>
                <strong style="color: #333333">Obesity:</strong>Implement programs and initiatives to promote healthy eating habits, increase awareness about the importance of maintaining a balanced diet, and encourage regular physical activity. Provide access to affordable and nutritious food options and promote portion control.
            </div>
        </div>
    """, unsafe_allow_html=True)

# Recommendation 2: Happiness Level

 with col2:
    # Animation 2 for Happiness Level
     lottie_happiness = load_lottiefile("/Users/macbook/Desktop/happ.json")
     st_lottie(lottie_happiness)
     st.caption("""
        <div>
            <div style="vertical-align:left;font-size:16px;padding-left:5px;padding-top:5px;margin-left:0em";>
                <strong style="color: #333333">Happiness Level:</strong> Implement programs for stress management, positive thinking, and mental health support. Encourage social connections and community engagement for happiness.
            </div>
        </div>
    """, unsafe_allow_html=True)

# Recommendation 3: Cost of Bottle of Water
#st.markdown("<h3 style='text-align: center; color: blue;'>Cost of Bottle of Water: Improve access to clean drinking water and promote water conservation. Raise awareness about hydration and benefits of clean water.</h1>", unsafe_allow_html=True)

 with col3:
    # Animation 3 for Cost of Bottle of Water
     lottie_water = load_lottiefile("/Users/macbook/Desktop/water.json")
     st_lottie(lottie_water)
     st.caption("""
        <div>
            <div style="vertical-align:left;font-size:16px;padding-left:5px;padding-top:5px;margin-left:0em";>
                <strong style="color: #333333">Cost of Bottle of Water:</strong>Improve access to clean drinking water and promote water conservation. Raise awareness about hydration and benefits of clean water.
            </div>
        </div>
     """, unsafe_allow_html=True)

# Recommendation 4: Sunshine Hours
#st.markdown("<h3 style='text-align: center; color: blue;'>Sunshine Hours: Provide safe and well-maintained recreational areas, parks, and green spaces. Promote the benefits of sunlight exposure for overall well-being.</h1>", unsafe_allow_html=True)
 with col4:
  # Animation 4 for Sunshine Hours
  lottie_water = load_lottiefile("/Users/macbook/Desktop/sun.json")
  st_lottie(lottie_water)
  st.caption("""
     <div>
         <div style="vertical-align:left;font-size:16px;padding-left:5px;padding-top:5px;margin-left:0em";>
             <strong style="color: #333333">Sunshine Hours:</strong> Provide safe and well-maintained recreational areas, parks, and green spaces. Promote the benefits of sunlight exposure for overall well-being.
         </div>
     </div>
  """, unsafe_allow_html=True)

 st.write("")

 st.markdown('<h1 class="center" style="color: green;">Data Source:</h1>', unsafe_allow_html=True)
 st.markdown('<p style="text-align: left;"><a href="https://www.kaggle.com/datasets/prasertk/healthy-lifestyle-cities-report-2021" style="color: black;">https://www.kaggle.com/datasets/prasertk/healthy-lifestyle-cities-report-2021</a></p>', unsafe_allow_html=True)



