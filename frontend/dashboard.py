import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import plotly.express as px
import streamlit as st
from backend import analytics
from backend import preprocess
from backend import topic_detection
from backend import interaction_analysis
from backend import parser as p1
from backend import sentiment_analysis as p2

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="WhatsApp AI Insights", 
    layout="wide", 
    page_icon="📈"
)

# --- CUSTOM CSS FOR ELEGANCE ---
st.markdown("""
    <style>
    /* Main background */
    .main {
        background-color: #0e1117;
    }
    /* Metric Card Styling */
    [data-testid="stMetricValue"] {
        font-size: 28px;
        color: #00d4ff;
    }
    .stMetric {
        background-color: #1e2130;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #31333f;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
    }
    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #1e2130;
        border-radius: 5px 5px 0px 0px;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/124/124034.png", width=60)
    st.title("Insight Controls")
    st.info("Member 3: UI/UX & Visualization")
    if st.button('✨ Celebrate Completion'):
        st.balloons()

# --- HEADER ---
st.title("📱 WhatsApp Group Intelligence")
st.markdown("*Transforming raw conversations into actionable group analytics using AI*")
st.divider()

# --- FILE UPLOADER SECTION ---
st.header("📂 Data Input")
uploaded_file = st.file_uploader("Upload WhatsApp .txt export (Without Media)", type="txt")

if uploaded_file is not None:
    # Read the file content
    content = uploaded_file.getvalue().decode("utf-8")
    
    try:
        # PROCESSING PIPELINE
        with st.spinner("🧠 AI is analyzing messages..."):
            # Call Member 1 logic
            df = p1.parse_chat_data(content)
            # Call Member 2 logic
            df = p2.analyze_all_sentiments(df)
        
        st.success("Analysis Complete!")

        # --- KPI METRICS ---
        st.subheader("Group Snapshot")
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Total Messages", f"{len(df):,}")
        m2.metric("Total Members", df['User'].nunique())
        m3.metric("Most Active", df['User'].value_counts().index[0])
        m4.metric("Dominant Mood", df['Sentiment'].mode()[0])

        st.markdown("###") # Vertical space

        # --- ANALYTICS TABS ---
        tab1, tab2, tab3 = st.tabs(["📊 Activity Leaderboard", "🧠 AI Sentiment Trends", "📑 Data Explorer"])

        with tab1:
            col1, col2 = st.columns([2, 1])
            with col1:
                user_counts = df['User'].value_counts().head(10).reset_index()
                fig_bar = px.bar(
                    user_counts, x='User', y='count', 
                    color='count',
                    title="Leaderboard: Top 10 Contributors",
                    template="plotly_dark", 
                    color_continuous_scale='Viridis'
                )
                st.plotly_chart(fig_bar, use_container_width=True)
            with col2:
                st.markdown("#### Participation Insights")
                st.write("This chart displays the distribution of messages across the most active members of the group.")
                st.info(f"The group has generated an average of **{round(len(df)/df['User'].nunique(), 1)}** messages per person.")

        with tab2:
            c1, c2 = st.columns([1, 1])
            with c1:
                sent_counts = df['Sentiment'].value_counts().reset_index()
                fig_pie = px.pie(
                    sent_counts, values='count', names='Sentiment', 
                    hole=0.6, # Modern Donut Look
                    color='Sentiment',
                    template="plotly_dark",
                    color_discrete_map={'Positive':'#00CC96', 'Neutral':'#636EFA', 'Negative':'#EF553B'}
                )
                fig_pie.update_layout(title_text="Overall Group Sentiment", title_x=0.25)
                st.plotly_chart(fig_pie, use_container_width=True)
            with c2:
                st.markdown("#### AI Sentiment Narrative")
                dominant_sentiment = df['Sentiment'].mode()[0]
                if dominant_sentiment == "Positive":
                    st.success("The AI has detected a highly positive and supportive group atmosphere.")
                elif dominant_sentiment == "Neutral":
                    st.info("The group atmosphere is primarily informative and neutral.")
                else:
                    st.warning("The AI has detected some negative sentiment clusters.")
                
                st.write("Sentiment analysis is performed using Natural Language Processing (NLP) to categorize the tone of each message.")

        with tab3:
            st.markdown("#### Full Dataset")
            st.write("Browse the raw messages and the AI labels assigned to them.")
            st.dataframe(df, use_container_width=True)

    except Exception as e:
        st.error(f"❌ Connection Error: {e}")
        st.info("Please ensure parser.py and sentiment_analysis.py are correctly configured.")

else:
    # Landing page state
    st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&q=80&w=1000", use_container_width=True)
    st.warning("Please upload a WhatsApp .txt file above to begin the analysis.")