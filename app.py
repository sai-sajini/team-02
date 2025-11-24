import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import numpy as np

# Page config
st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for sleek dark theme
# st.markdown("""
#     <style>
#         /* Main theme */
#         :root {
#             --primary: #0ea5e9;
#             --dark-bg: #0f172a;
#             --card-bg: #1e293b;
#             --border: #334155;
#             --text-primary: #f1f5f9;
#             --text-secondary: #cbd5e1;
#         }
        
#         body {
#             background-color: var(--dark-bg);
#             color: var(--text-primary);
#         }
        
#         .main {
#             background-color: var(--dark-bg);
#             padding: 0;
#         }
        
#         /* Title bar styling */
#         .title-bar {
#             display: flex;
#             justify-content: space-between;
#             align-items: center;
#             padding: 1rem 2rem;
#             background-color: var(--card-bg);
#             border-bottom: 1px solid var(--border);
#             margin-bottom: 2rem;
#             border-radius: 8px;
#         }
        
#         .title-bar h1 {
#             margin: 0;
#             font-size: 1.75rem;
#             font-weight: 700;
#             color: var(--text-primary);
#         }
        
#         /* Card styling */
#         [data-testid="stContainer"] {
#             background-color: transparent;
#         }
        
#         .card {
#             background-color: var(--card-bg);
#             border: 1px solid var(--border);
#             border-radius: 8px;
#             padding: 1.5rem;
#             box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
#         }
        
#         /* Streamlit component overrides */
#         .stSelectbox, .stTextArea, .stButton {
#             border-radius: 8px;
#         }
        
#         .stButton > button {
#             background-color: var(--primary);
#             color: white;
#             border: none;
#             border-radius: 6px;
#             font-weight: 600;
#             padding: 0.5rem 1.5rem;
#             transition: all 0.3s ease;
#         }
        
#         .stButton > button:hover {
#             background-color: #0284c7;
#             transform: translateY(-2px);
#         }
        
#         .stTextArea > textarea {
#             background-color: var(--card-bg);
#             color: var(--text-primary);
#             border: 1px solid var(--border);
#             border-radius: 6px;
#         }
        
#         .stSelectbox > div > div {
#             background-color: var(--card-bg);
#             border-radius: 6px;
#         }
        
#         /* Table styling */
#         .stDataFrame {
#             border-radius: 8px;
#             overflow: hidden;
#         }
        
#         /* Metrics styling */
#         .metric-card {
#             background-color: var(--card-bg);
#             border: 1px solid var(--border);
#             border-radius: 8px;
#             padding: 1rem;
#             text-align: center;
#         }
        
#         .metric-value {
#             font-size: 1.5rem;
#             font-weight: 700;
#             color: var(--primary);
#         }
        
#         .metric-label {
#             font-size: 0.875rem;
#             color: var(--text-secondary);
#             margin-top: 0.5rem;
#         }
        
#         h2, h3 {
#             color: var(--text-primary);
#             font-weight: 700;
#         }
        
#         h3 {
#             margin-top: 1.5rem;
#             margin-bottom: 1rem;
#             color: var(--text-secondary);
#             font-size: 0.875rem;
#             text-transform: uppercase;
#             letter-spacing: 0.05em;
#         }
#     </style>
# """, unsafe_allow_html=True)

# Title bar with dropdown
col1, col2 = st.columns([1, 0.2])

with col1:
    st.markdown("<div class='title-bar'><h1>🚀 Dashboard</h1></div>", unsafe_allow_html=True)

with col2:
    version = st.selectbox(
        "Version",
        ["v0", "v1", "v2", "v3"],
        key="version_select",
        label_visibility="collapsed"
    )

st.markdown("")  # spacing

# Main layout - 3 columns
left_col, middle_col, right_col = st.columns([0.25, 0.5, 0.25], gap="medium")

# ============ LEFT COLUMN - STATISTICS TABLE ============
with left_col:
    st.markdown("<h3>📊 Statistics</h3>", unsafe_allow_html=True)
    
    # Generate sample statistics data
    stats_data = {
        'Metric': ['Requests', 'Errors', 'Latency', 'Uptime', 'Active Users'],
        'Value': ['2,450K', '12', '125ms', '99.9%', '1,234'],
        'Status': ['↑ +5%', '↓ -2%', '↔ 0%', '✓ OK', '↑ +8%']
    }
    stats_df = pd.DataFrame(stats_data)
    
    st.dataframe(
        stats_df,
        use_container_width=True,
        hide_index=True,
        column_config={
            'Metric': st.column_config.TextColumn(width="medium"),
            'Value': st.column_config.TextColumn(width="small"),
            'Status': st.column_config.TextColumn(width="small"),
        }
    )
    
    # Key metrics
    st.markdown("<h3>Key Metrics</h3>", unsafe_allow_html=True)
    
    m1, m2 = st.columns(2)
    with m1:
        st.metric("CPU", "45%", "+2%")
    with m2:
        st.metric("Memory", "62%", "-1%")
    
    m3, m4 = st.columns(2)
    with m3:
        st.metric("Disk", "78%", "0%")
    with m4:
        st.metric("Network", "234Mb/s", "+12%")

# ============ MIDDLE COLUMN - CHARTS ============
with middle_col:
    st.markdown("<h3>📈 Logs & Metrics</h3>", unsafe_allow_html=True)
    
    # Generate sample time series data
    dates = [datetime.now() - timedelta(hours=i) for i in range(24, 0, -1)]
    requests = np.random.randint(1500, 3000, 24) + np.linspace(0, 500, 24)
    errors = np.random.randint(5, 30, 24)
    
    # Chart 1 - Requests over time
    fig1 = go.Figure()
    
    fig1.add_trace(go.Scatter(
        x=dates,
        y=requests,
        name='Requests',
        mode='lines',
        line=dict(color='#0ea5e9', width=3),
        fill='tozeroy',
        fillcolor='rgba(14, 165, 233, 0.2)'
    ))
    
    fig1.update_layout(
        title="Requests (Last 24 Hours)",
        xaxis_title="Time",
        yaxis_title="Count",
        hovermode='x unified',
        template='plotly_dark',
        margin=dict(l=0, r=0, t=30, b=0),
        height=300,
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(color='#f1f5f9'),
        xaxis=dict(gridcolor='#334155'),
        yaxis=dict(gridcolor='#334155')
    )
    
    st.plotly_chart(fig1, use_container_width=True)
    
    # Chart 2 - Error rate
    fig2 = go.Figure()
    
    fig2.add_trace(go.Scatter(
        x=dates,
        y=errors,
        name='Errors',
        mode='lines+markers',
        line=dict(color='#ef4444', width=2),
        marker=dict(size=6)
    ))
    
    fig2.update_layout(
        title="Error Rate (Last 24 Hours)",
        xaxis_title="Time",
        yaxis_title="Errors",
        hovermode='x unified',
        template='plotly_dark',
        margin=dict(l=0, r=0, t=30, b=0),
        height=250,
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(color='#f1f5f9'),
        xaxis=dict(gridcolor='#334155'),
        yaxis=dict(gridcolor='#334155')
    )
    
    st.plotly_chart(fig2, use_container_width=True)
    
    # Chart 3 - Distribution
    categories = ['API', 'Web', 'Mobile', 'Desktop', 'Other']
    values = [35, 28, 18, 12, 7]
    
    fig3 = go.Figure(data=[
        go.Pie(
            labels=categories,
            values=values,
            marker=dict(colors=['#0ea5e9', '#06b6d4', '#10b981', '#f59e0b', '#ef4444'])
        )
    ])
    
    fig3.update_layout(
        title="Traffic Distribution",
        template='plotly_dark',
        margin=dict(l=0, r=0, t=30, b=0),
        height=250,
        paper_bgcolor='#ffffff',
        font=dict(color='#f1f5f9')
    )
    
    st.plotly_chart(fig3, use_container_width=True)

# ============ RIGHT COLUMN - SYSTEM PROMPT ============
with right_col:
    st.markdown("<h3>⚙️ System Prompt</h3>", unsafe_allow_html=True)
    
    # Default system prompt
    default_prompt = """You are an AI assistant helping with system monitoring and analytics. Your role is to:

1. Analyze system metrics and provide insights
2. Identify performance issues and anomalies
3. Suggest optimization strategies
4. Help interpret log data

Context:
- Monitor CPU, Memory, Disk usage
- Track request rates and error patterns
- Analyze user behavior trends"""
    
    # System prompt textarea
    system_prompt = st.text_area(
        "Edit System Prompt",
        value=default_prompt,
        height=300,
        label_visibility="collapsed",
        key="system_prompt"
    )
    
    st.markdown("")  # spacing
    
    # Submit button
    if st.button("💾 Submit", use_container_width=True, key="submit_btn"):
        st.success(f"✅ System prompt updated successfully!")
        st.session_state.last_prompt = system_prompt
        st.session_state.prompt_updated = True
    
    # Display last update info
    if 'prompt_updated' in st.session_state and st.session_state.prompt_updated:
        st.caption(f"Last updated: {datetime.now().strftime('%H:%M:%S')}")
    else:
        st.caption("Last updated: Never")

st.markdown("")
st.markdown("---")
st.caption(f"Dashboard Version: {version} | Last refresh: {datetime.now().strftime('%H:%M:%S')}")