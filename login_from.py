st.header("Nethi Bhavesh")




#Headddder
st.header("Streamlit  Application")





#Title
st.title("Welcome to Std management App")





#subHeader
st.subheader("Management of Students data")





#Text
st.text("Text ")





#Markdown Horizontal Line
st.markdown("---------------------------------------")





#text method to display info 
st.text("This is a simple Streamlit application to manage student data.")





#Write allows 
st.write("Hello")
st.write(123)
a=69
b=420
st.write(a,"This number is a variable",b)
st.write([1,2,3])
st.write({"name":"John", "age":30})





#Markdown
st.markdown("### This is a markdown header")
st.markdown("**This text is bold**")
st.markdown("*This text is italic*")
st.markdown("- Item 1\n- Item 2\n- Item 3")
st.markdown("<h3 style = color:blue> This is a blue header </h3>", unsafe_allow_html=True)
st.markdown("<h3 style = color:red> This is a red header </h3>", unsafe_allow_html=True)




# to display code snippets
st.code('''
        def add(a,b):
            return(a+b)
        ''',language='python')




# Dispaly math Equations
st.latex(r'''
         E = mc^2,
         a^2 + b^2 = c^2
    ''')




# Divider line virtually divides data
st.divider()





#Button
if st.button("Click me"):
    st.text("Button Clicked!")
    st.success("Success Message")
    st.balloons()
else:
    st.write("Button not clicked yet.")
    st.error("Connection Error!!")
name=st.text_input("Enter your name:")
st.write("Hello,\n",name)
st.write(f"Hello,{name}!!")
if name == "":
    st.warning("Please enter your name")
Marks=st.number_input("Enter marks",0,100)
if Marks>100:
    st.warning("Marks cannot be greater than 100")
    
else:
    st.success(f"Marks entered: {Marks}")
st.divider()




#Text Area
if st.checkbox("I agree"):
    st.write("Thank you for agreeing!")
st.divider()




#Radio buttons
gender=st.radio("Select Gender",("Male","Female","Other"))
st.write(f"You have selected: {gender}")
st.divider()




#Select Box
country=st.selectbox("Select Country",["USA","Canada","UK","Australia","India"])
st.write(f"You have selected: {country}")
st.divider()




#MultiSelect
skills=st.multiselect("Select Skills",["Python","Java","C"])
st.write(f"Your skills are: {skills}")
st.divider()





#Slider
age=st.slider("Select YYour Age:",0,100,10)
st.write(f"your age is: {age}")
st.divider()




# File Uploader
st.file_uploader("Upload a file")
st.divider()




# Creation of form 
with st.form("my_form"):
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age",0,120)   
    submit = st.form_submit_button("Submit") # buttons inside form
if submit:
    st.write(f"Name: {name}")
    st.write(f"Age: {age}")

with st.form("Login_Form"):
    username = st.text_input("Username")
    password = st.text_input("Password",type='password')
    login = st.form_submit_button("Login")
if login:
    st.write(f"Welcome, {username}!")
    st.success("Login Successful")
st.divider()



#columns
col1,col2,col3=st.columns(3)
with col1:
    st.header("Column 1")
    st.markdown("---------------------------------------")
    st.write("Column 1")

with col2:
    st.header("Column 2")
    st.markdown("---------------------------------------")
    st.write("Column 2")
with col3:
    st.header("Column 3")
    st.markdown("---------------------------------------")
    st.write("Column 3")    
st.divider()




#Container 
container=st.container()
container.write("This is inside the container")
container.button("Container Button")
st.divider()
data = {
    'Name': ['Anurag', 'Sumit', 'Rohit'],
    'Age': [21, 22, 20],
    'Course': ['B.Tech', 'M.Tech', 'BBA']
}
st.table(data)
st.divider()



# Sidebar
st.sidebar.title("Sidebar Title")
option = st.sidebar.radio("Select an option", ["Home", "About", "Help"])
st.sidebar.write(f"You selected:\n {option}")
st.divider()

@st.cache_data
def load_data():
    return [1,2,3,4]
data=load_data()
st.write(data)
st.divider()
