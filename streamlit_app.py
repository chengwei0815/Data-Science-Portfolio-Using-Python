import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Wei Cheng
##### *Portfolio* 
''')

image = Image.open('dp.png')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- A dedicated and an aspiring Software and Technology Engineer with an objective of working in
an organization that provides opportunities for technical and personal advancement.

- Key Skills: Data science, Data analytics, Statistical analysis, Predictive analysis, Problem solving, Machine learning and Project management

''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="" target="_blank">Wei Cheng</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**Diploma in Applied Data Science and Big Data**, *Toronto Institute of Data Science and Technology*, Toronto',
'2023-2024')
st.markdown('''
- GPA: `94%`

''')

txt('**Diploma in Full Stack Software Engineering**, *CodeSquad*, Boston',
'2022-2023')
st.markdown('''
- Over 700 hours of intensive coursework in
software engineering methodologies and technologies. 
- Skilled in front-end and back-end development, data structures,
algorithms, and testing.
- Skills:  Front-End Development · Back-End Web Development · JavaScript · HTML5 · MongoDB · React.js · Node.js · JSON · Express · Software Development · mongoose · CSS
''')

txt('**Masters of Science** (Quantitative Finance), *University of Massachusetts Boston*, Boston',
'2020-2022')
st.markdown('''
- CGPA: `3.98`
- Received graduate scholarship as TA
- Graduated with First Class Honors.
''')

txt('**Masters of Science** (Accounting), *Babson College*, Wellesley',
'2013-2014')
st.markdown('''
- Skills: Mergers & Acquisitions (M&A) · Financial Accounting · logit model · Managerial Finance · Financial Reporting · EViews · QuickBooks · Financial Analysis
''')

txt('**Bachelors of Science** (Double-major of Accounting and Finance), *University of Massachusetts Boston*, Boston',
'2010-2013')
st.markdown('''
- Finance-GPA: `4.00`
- Dean's List
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Data Scientist, Consultant**, Beam Data, Toronto',
'2024-Present')
st.markdown('''
- Design and automated the ETL pipeline with Airflow in Docker on AWS EC2 to get daily job postings from online source, and save data into MySQL database for data wrangling
- Built data analytics pipelines to connect database with Tableau, converted data into actionable insights and prepare visualization reports to stakeholders that interpreting market opportunities, conditions and trends
- Optimized data parsing processes by leveraging a large language model (LLM), leading to a significant improvement in the accuracy of extracting job data, resulting in a 61% reduction in errors.
- Engineered and managed PostgreSQL databases to structure parsed data, enabling more efficient data retrieval and storage, which reduced query times by 30%.
- Developed and automated a data scraping pipeline using Airflow, which streamlined the extraction of company page data and increased data collection efficiency by 75%.
- Enhanced skill extraction processes by creating a robust parsing script using LLM, successfully populating the skills table from job descriptions, and improving the dataset's completeness by 20%.
- Built a golden dataset through the consolidation and refinement of regex-parsed fields, providing a benchmark for evaluating model performance and improving model validation accuracy to 91%.
''')

#####################
st.markdown('''
## Projects
''')

txt('**Sentiment Analysis for Twitter Reviews**',
'2024')
st.markdown('''
- Performed sentiment analysis on over 3 millions raw Twitter reviews using Natural Language Processing (NLP) techniques and machine learning models, leading to actionable insights on public opinion.
  | Skills Used: Python, Natural Language Processing (NLP), Scikit-learn, Pandas, NLTK, SpaCy
- Implemented text preprocessing and feature extraction techniques, including tokenization, stemming, and TF-IDF, to prepare the data for analysis, which improved the model's prediction accuracy.
  | Skills Used: Text Preprocessing, Tokenization, TF-IDF, Data Cleaning
- Applied advanced machine learning algorithms such as Logistic Regression and Support Vector Machines (SVM) to classify sentiment polarity (positive or negative) with an accuracy of 92%.
  | Skills Used: Logistic Regression, Support Vector Machines (SVM), Scikit-learn
- Visualized sentiment trends over time, providing stakeholders with clear insights into customer feedback and emerging topics of interest.
  | Skills Used: Data Visualization, Matplotlib, Seaborn
''')

txt('**Customer Churn Rate Prediction**',
'2024')
st.markdown('''
- Developed a prediction model to estimate customer churn using Python, analyzing a dataset of [specific number] customers and their interaction histories to identify key churn indicators.
| Skills Used: Python, Pandas, Scikit-learn, Data Analysis
- Implemented SMOTE (Synthetic Minority Over-sampling Technique) to balance the dataset, which enhanced the model’s ability to correctly identify potential churn cases.
| Skills Used: SMOTE, Data Balancing, Scikit-learn
- Utilized machine learning frameworks such as Random Forest, Gradient Boosting, and XGBoost, achieving a high ROC AUC score of 0.96, significantly improving the prediction accuracy over baseline models.
| Skills Used: Random Forest, Gradient Boosting, XGBoost, ROC AUC, Python
- Provided actionable insights to the marketing and retention teams, allowing them to target at-risk customers effectively and reduce churn rates by 15% over three months.
| Skills Used: Business Intelligence, Data-driven Decision Making, Python, Data Visualization

''')

txt('**Web Scraping Project for Noon E-commerce Website**',
'2024')
st.markdown('''
- Executed a comprehensive web scraping project on Noon.com, successfully extracting detailed product data including titles, prices, descriptions, SKUs, customer ratings, and stock levels using Python, Beautiful Soup, and Selenium to handle dynamic content.
| Skills Used: Python, Beautiful Soup, Selenium, Web Scraping, Data Extraction
- Implemented advanced error-handling and IP rotation techniques to manage request limits and evade detection, achieving a 98% success rate over 10,000 product pages, ensuring the robustness of the data extraction process.
| Skills Used: Error Handling, IP Rotation, Web Scraping Techniques
- Developed an automated data pipeline for data cleansing, normalization, and storage into a PostgreSQL database, facilitating real-time data analysis and supporting downstream market analysis applications.
| Skills Used: Data Pipeline Development, Data Cleansing, Data Normalization, PostgreSQL, Database Management
- Enhanced data quality and consistency through rigorous preprocessing and validation steps, ensuring that the extracted data was reliable and ready for subsequent analysis.
| Skills Used: Data Preprocessing, Data Validation, Data Quality Assurance
''')



#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `JavaScript`, `Linux`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `Tableau`, `Power BI`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`React`, `Node.js`, `noSOL`, `Flask`, `HTML`, `CSS`, `Express`, `MongoDB`, `Mongoose`')
txt3('Big Data', '`Spark`, `Hive`, `Hadoop`, `AWS (EC2, S3, EMR, Redshift)`, `Airflow`, `Docker`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/weicheng611/')
txt2('GitHub', 'https://github.com/chengwei0815/')
txt2('Portfolio', 'https://wei-cheng.streamlit.app/')
txt2('tableau', 'https://public.tableau.com/app/profile/wei.cheng7743/vizzes')
