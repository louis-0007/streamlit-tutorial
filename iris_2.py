# import altair as alt
# import matplotlib.pyplot as plt
# import pandas as pd
# import seaborn as sns
import streamlit as st
# from PIL import Image


# def show_description(species: str) -> None:
#     @st.cache(suppress_st_warning=True)
#     def _read_descriptions(species: str) -> str:
#         with open(f'{species.lower()}_descriptions.txt', 'r') as f:
#             return f.read()

#     @st.cache(suppress_st_warning=True)
#     def _load_images():
#         st.write('Cache miss')
#         images = {
#             'Setosa': Image.open('setosa.jpg'),
#             'Versicolor': Image.open('versicolor.jpg'),
#             'Virginica': Image.open('virginica.jpg'),
#         }
#         return images

#     # col1, col2 = st.beta_columns(2)
#     col1, col2 = st.columns(2)
#     description = _read_descriptions(species)
#     images = _load_images()
#     col1.header(species)
#     col1.image(images[species], use_column_width=True)
#     col2.header('Description')
#     col2.write(description, unsafe_allow_html=True)


def show_description1(species: str) -> None:
    @st.cache(suppress_st_warning=True)
    def _read_descriptions(species: str) -> str:
        k=species + '이것의 description'
   
        return k

    # @st.cache(suppress_st_warning=True)
    # def _load_images():
    #     st.write('Cache miss')
    #     images = {
    #         'Setosa': Image.open('setosa.jpg'),
    #         'Versicolor': Image.open('versicolor.jpg'),
    #         'Virginica': Image.open('virginica.jpg'),
    #     }
    #     return images

    # col1, col2 = st.beta_columns(2)
    col1, col2 = st.columns(2)
    description = _read_descriptions(species)
    # images = _load_images()
    col1.header(species)
    # col1.image(images[species], use_column_width=True)
    col2.header('Description')
    col2.write(description, unsafe_allow_html=True)    
    st.write('니가 골랐어 아랫 것을')    
    st.write(species)    


def show_description2(species: str) -> None:
    @st.cache(suppress_st_warning=True)
    def _read_descriptions(species: str) -> str:
        k=species + '이것의 description'
   
        return k

    # @st.cache(suppress_st_warning=True)
    # def _load_images():
    #     st.write('Cache miss')
    #     images = {
    #         'Setosa': Image.open('setosa.jpg'),
    #         'Versicolor': Image.open('versicolor.jpg'),
    #         'Virginica': Image.open('virginica.jpg'),
    #     }
    #     return images

    # col1, col2 = st.beta_columns(2)
    description = _read_descriptions(species)
    # images = _load_images()
    st.header(species)
    # col1.image(images[species], use_column_width=True)
    st.header('Description')
    st.write(description, unsafe_allow_html=True)    
    st.write('니가 골랐어 아랫 것을')    
    st.write(species)   

    


def home_page() -> None:
    st.title('Looking into Iris Dataset')
    # st.image('all_three.jpg', caption='Three types of Iris flowers.')
    # with st.beta_expander('Show raw data'):
    with st.expander('Show raw data'):
        st.write(df)
    st.header('General Information')
    selected_sepecies = st.radio('Select species', ['Setosa', 'Versicolor', 'Virginica'])
    show_description1(selected_sepecies)


def dataset_page() -> None:
    st.title('Dataset')
    st.header('Statistics')
    

def graphs_page() -> None:
    st.title('Graphs')

    st.header('Seaborn (Matplotlib)')
    st.header('*Can also support Plotly and Bokeh')



def control_page() -> None:
    st.title('Control')

    st.header('Spot test control')
    selected_sepecies = st.radio('Select species', ['Setosa', 'Versicolor', 'Virginica'])
    show_description2(selected_sepecies)

    if selected_sepecies ==  'Setosa' : print('세토사')
    elif selected_sepecies ==  'Versicolor' : 
        {print('베지칼러')}

    st.write('*Spot get robot state')



if __name__ == '__main__':
    # df = pd.read_csv('iris.csv')
    df = '''니가 나를 모르는데
    난들 너를 알겠느냐
    한 치 앞도 ...'''

    selected_page = st.sidebar.selectbox(
        'Select Page',
        ('Control','Dataset', 'Graphs', 'Home' )
    )

    if selected_page == 'Home':
        home_page()
    elif selected_page == 'Dataset':
        dataset_page()
    elif selected_page == 'Graphs':
        graphs_page()
    else:
        control_page()
