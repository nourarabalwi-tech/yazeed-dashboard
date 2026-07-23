import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import datetime

# ---------------------------------------------------------
# 1. إعدادات الصفحة والهوية البصرية (Page Config & Styling)
# ---------------------------------------------------------
st.set_page_config(
    page_title="مشروع يزيد الراجحي — لوحة القيادة الاستراتيجية",
    page_icon="🏎️",
    layout="wide",
    initial_sidebar_state="expanded"
)

/* Custom Card Style */
    .kpi-card {
        background-color: #1E293B;
        border-left: 4px solid #D4AF37;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 15px;
        color: #F8FAFC !important;
    }
    .kpi-card ul li {
        color: #F8FAFC !important;
        font-size: 1rem;
}
    
    /* Header Container */
    .header-box {
        background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
        border: 1px solid #D4AF37;
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0px 4px 20px rgba(212, 175, 55, 0.15);
    }
    .header-box h1 {
        color: #D4AF37;
        font-weight: 700;
        margin-bottom: 8px;
    }
    .header-box p {
        color: #94A3B8;
        font-size: 1.1rem;
    }

    /* Metric Cards */
    div[data-testid="stMetricValue"] {
        color: #D4AF37 !important;
        font-weight: bold !important;
    }
    div[data-testid="stMetricLabel"] {
        color: #CBD5E1 !important;
    }
    
    /* Custom Card Style */
    .kpi-card {
        background-color: #1E293B;
        border-left: 4px solid #D4AF37;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 15px;
    }
    .kpi-card h4 {
        color: #94A3B8;
        margin: 0 0 5px 0;
        font-size: 0.9rem;
    }
    .kpi-card h2 {
        color: #D4AF37;
        margin: 0;
        font-size: 1.8rem;
    }
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #1E293B;
        border-radius: 6px;
        color: #94A3B8;
        padding: 10px 20px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #D4AF37 !important;
        color: #0F172A !important;
        font-weight: bold;
    }
    
    /* General Text Right to Left */
    p, h1, h2, h3, h4, h5, h6, div {
        text-align: right;
        direction: rtl;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. تحميل البيانات المدمجة (Data Loading)
# ---------------------------------------------------------
@st.cache_data
def load_data():
    rally_data = [
        {"Rally_ID": "R2021-01", "Date": "2021-01-15", "Event_Name": "Rally Dakar", "Location": "Saudi Arabia", "Category": "T1 Ultimate", "Final_Position": 3, "Stage_Wins": 2, "Status": "Finished"},
        {"Rally_ID": "R2021-02", "Date": "2021-03-20", "Event_Name": "Sharqiyah Baja", "Location": "Saudi Arabia", "Category": "T1 Ultimate", "Final_Position": 1, "Stage_Wins": 4, "Status": "Finished"},
        {"Rally_ID": "R2022-01", "Date": "2022-01-14", "Event_Name": "Rally Dakar", "Location": "Saudi Arabia", "Category": "T1 Ultimate", "Final_Position": 3, "Stage_Wins": 1, "Status": "Finished"},
        {"Rally_ID": "R2022-02", "Date": "2022-11-12", "Event_Name": "Saudi Baja Hail", "Location": "Saudi Arabia", "Category": "T1 Ultimate", "Final_Position": 1, "Stage_Wins": 3, "Status": "Finished"},
        {"Rally_ID": "R2023-01", "Date": "2023-01-15", "Event_Name": "Rally Dakar", "Location": "Saudi Arabia", "Category": "T1 Ultimate", "Final_Position": 85, "Stage_Wins": 1, "Status": "Finished"},
        {"Rally_ID": "R2023-02", "Date": "2023-03-18", "Event_Name": "Abu Dhabi Desert Challenge", "Location": "UAE", "Category": "T1 Ultimate", "Final_Position": 1, "Stage_Wins": 3, "Status": "Finished"},
        {"Rally_ID": "R2023-03", "Date": "2023-10-18", "Event_Name": "Rallye du Maroc", "Location": "Morocco", "Category": "T1 Ultimate", "Final_Position": 1, "Stage_Wins": 2, "Status": "Finished"},
        {"Rally_ID": "R2024-01", "Date": "2024-01-19", "Event_Name": "Rally Dakar", "Location": "Saudi Arabia", "Category": "T1 Ultimate", "Final_Position": 2, "Stage_Wins": 2, "Status": "Finished"},
        {"Rally_ID": "R2024-02", "Date": "2024-02-10", "Event_Name": "Hail Saudi Baja", "Location": "Saudi Arabia", "Category": "T1 Ultimate", "Final_Position": 1, "Stage_Wins": 3, "Status": "Finished"},
        {"Rally_ID": "R2025-01", "Date": "2025-01-17", "Event_Name": "Rally Dakar", "Location": "Saudi Arabia", "Category": "T1 Ultimate", "Final_Position": 2, "Stage_Wins": 2, "Status": "Finished"}
    ]

    biz_data = [
        {"Transaction_ID": "B2021-01", "Date": "2021-03-15", "Sector": "Real Estate", "Project_Name": "مجمع الملقى الفندقي", "Investment_Amount_SAR": 45000000, "Revenue_SAR": 58500000, "ROI_Percentage": 0.30},
        {"Transaction_ID": "B2021-02", "Date": "2021-08-10", "Sector": "Retail & F&B", "Project_Name": "توسع سلسلة الكافيهات", "Investment_Amount_SAR": 12000000, "Revenue_SAR": 15600000, "ROI_Percentage": 0.30},
        {"Transaction_ID": "B2022-01", "Date": "2022-02-01", "Sector": "Real Estate", "Project_Name": "مركز النخيل التجاري", "Investment_Amount_SAR": 80000000, "Revenue_SAR": 108000000, "ROI_Percentage": 0.35},
        {"Transaction_ID": "B2022-02", "Date": "2022-06-20", "Sector": "Automotive", "Project_Name": "مركز الصيانة والسباقات", "Investment_Amount_SAR": 25000000, "Revenue_SAR": 31250000, "ROI_Percentage": 0.25},
        {"Transaction_ID": "B2023-01", "Date": "2023-01-10", "Sector": "Tech & VC", "Project_Name": "تطبيق الخدمات اللوجستية", "Investment_Amount_SAR": 15000000, "Revenue_SAR": 22500000, "ROI_Percentage": 0.50},
        {"Transaction_ID": "B2023-02", "Date": "2023-09-15", "Sector": "Real Estate", "Project_Name": "أبراج حطين السكنية", "Investment_Amount_SAR": 120000000, "Revenue_SAR": 156000000, "ROI_Percentage": 0.30},
        {"Transaction_ID": "B2024-01", "Date": "2024-04-10", "Sector": "Retail & F&B", "Project_Name": "العلامات التجارية الفاخرة", "Investment_Amount_SAR": 30000000, "Revenue_SAR": 40500000, "ROI_Percentage": 0.35},
        {"Transaction_ID": "B2024-02", "Date": "2024-11-05", "Sector": "Automotive", "Project_Name": "أكاديمية تطوير السيارات", "Investment_Amount_SAR": 18000000, "Revenue_SAR": 22500000, "ROI_Percentage": 0.25},
        {"Transaction_ID": "B2025-01", "Date": "2025-02-12", "Sector": "Tech & VC", "Project_Name": "منصة الذكاء الاصطناعي", "Investment_Amount_SAR": 22000000, "Revenue_SAR": 33000000, "ROI_Percentage": 0.50}
    ]

    df_rally = pd.DataFrame(rally_data)
    df_biz = pd.DataFrame(biz_data)
    
    df_rally['Date'] = pd.to_datetime(df_rally['Date'])
    df_biz['Date'] = pd.to_datetime(df_biz['Date'])
    
    df_biz['Profit_SAR'] = df_biz['Revenue_SAR'] - df_biz['Investment_Amount_SAR']
    
    return df_rally, df_biz

df_rally, df_biz = load_data()

# ---------------------------------------------------------
# 3. الهيدر وشريط التحكم الجانبي (Header & Sidebar Filters)
# ---------------------------------------------------------
st.markdown("""
<div class="header-box">
    <h1>🏎️ المنصة التحليلية المتكاملة — يزيد الراجحي</h1>
    <p>دمج التميز الرياضي بالريادة الاستثمارية عبر تحليلات البيانات المتقدمة</p>
</div>
""", unsafe_allow_html=True)

st.sidebar.title("🔍 تصفية البيانات")
selected_years = st.sidebar.multiselect(
    "اختر السنة:",
    options=[2021, 2022, 2023, 2024, 2025],
    default=[2021, 2022, 2023, 2024, 2025]
)

# Apply filter
df_rally_filtered = df_rally[df_rally['Date'].dt.year.isin(selected_years)]
df_biz_filtered = df_biz[df_biz['Date'].dt.year.isin(selected_years)]

# ---------------------------------------------------------
# 4. التبويبات الرئيسية (Main Tabs)
# ---------------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 لوحة القيادة (Dashboard)",
    "🏎️ تحليل الرالي (Rally Analytics)",
    "💼 إمبراطورية الأعمال & SWOT",
    "🎤 سيناريو العرض التقديمي"
])

# ---------------------------------------------------------
# Tab 1: لوحة القيادة العامة
# ---------------------------------------------------------
with tab1:
    st.subheader("💡 مؤشرات الأداء الرئيسية (KPIs)")
    
    col1, col2, col3, col4 = st.columns(4)
    
    total_races = len(df_rally_filtered)
    wins = len(df_rally_filtered[df_rally_filtered['Final_Position'] == 1])
    podiums = len(df_rally_filtered[df_rally_filtered['Final_Position'] <= 3])
    podium_rate = (podiums / total_races * 100) if total_races > 0 else 0
    
    total_inv = df_biz_filtered['Investment_Amount_SAR'].sum()
    total_rev = df_biz_filtered['Revenue_SAR'].sum()
    total_profit = df_biz_filtered['Profit_SAR'].sum()
    avg_roi = (total_profit / total_inv * 100) if total_inv > 0 else 0
    
    col1.metric("إجمالي السباقات", f"{total_races}")
    col2.metric("نسبة التتويج", f"{podium_rate:.1f}%")
    col3.metric("إجمالي الاستثمارات", f"{total_inv/1e6:.1f}M SAR")
    col4.metric("متوسط العائد ROI", f"{avg_roi:.1f}%")
    
    st.divider()
    
    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown("### 📈 الاستثمار مقابل العائد حسب القطاع")
        sector_summary = df_biz_filtered.groupby('Sector')[['Investment_Amount_SAR', 'Revenue_SAR']].sum().reset_index()
        fig_biz = go.Figure()
        fig_biz.add_trace(go.Bar(x=sector_summary['Sector'], y=sector_summary['Investment_Amount_SAR'], name='الاستثمار', marker_color='#334155'))
        fig_biz.add_trace(go.Bar(x=sector_summary['Sector'], y=sector_summary['Revenue_SAR'], name='العائد', marker_color='#D4AF37'))
        fig_biz.update_layout(barmode='group', template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_biz, use_container_width=True)
        
    with c2:
        st.markdown("### 🏆 توزيع المراكز في السباقات")
        pos_counts = df_rally_filtered['Final_Position'].apply(lambda x: 'المركز الأول 🥇' if x == 1 else ('منصة تتويج 🥈🥉' if x <= 3 else 'مراكز أخرى')).value_counts().reset_index()
        fig_pie = px.pie(pos_counts, values='count', names='Final_Position', color_discrete_sequence=['#D4AF37', '#94A3B8', '#334155'], hole=0.4)
        fig_pie.update_layout(template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_pie, use_container_width=True)

# ---------------------------------------------------------
# Tab 2: تحليل الرالي والرياضة
# ---------------------------------------------------------
with tab2:
    st.subheader("🏎️ تحليل الأداء الرياضي والمراحل")
    
    fig_stages = px.bar(
        df_rally_filtered,
        x='Event_Name',
        y='Stage_Wins',
        color='Final_Position',
        color_continuous_scale=['#1E293B', '#D4AF37'],
        title="عدد المراحل المفوز بها لكل سباق",
        labels={'Event_Name': 'اسم البطولة', 'Stage_Wins': 'الفوز بالمراحل'}
    )
    fig_stages.update_layout(template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_stages, use_container_width=True)
    
    st.markdown("### 📋 جدول تفاصيل السباقات")
    st.dataframe(df_rally_filtered, use_container_width=True)

# ---------------------------------------------------------
# Tab 3: الأعمال وتحليل SWOT
# ---------------------------------------------------------
with tab3:
    st.subheader("💼 المحفظة الاستثمارية وتحليل SWOT")
    
    col_swot1, col_swot2 = st.columns(2)
    
    with col_swot1:
        st.markdown("""
        <div class="kpi-card">
            <h3 style="color:#D4AF37;">💪 نقاط القوة (Strengths)</h3>
            <ul>
                <li>علامة تجارية شخصية قوية وواسعة التأثير.</li>
                <li>سرعة وصواب اتخاذ القرار في الظروف الصعبة.</li>
                <li>تنوع مرن بين الأصول العقارية والتجارية.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="kpi-card">
            <h3 style="color:#D4AF37;">🎯 الفرص (Opportunities)</h3>
            <ul>
                <li>التوسع في الشراكات الاستراتيجية الدولية.</li>
                <li>تأسيس أكاديميات للرياضة والقيادة والتطوير.</li>
                <li>الاستثمار في التقنيات الذكية والاستدامة.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col_swot2:
        st.markdown("""
        <div class="kpi-card">
            <h3 style="color:#CBD5E1;">⚠️ نقاط الضعف (Weaknesses)</h3>
            <ul>
                <li>تداخل جدول البطولات المكثف مع وقت إدارة المشاريع.</li>
                <li>الاعتماد على التواجد المباشر في بعض المبادرات.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="kpi-card">
            <h3 style="color:#CBD5E1;">🛡️ التهديدات (Threats)</h3>
            <ul>
                <li>تقلبات الأسواق العقارية والتجارية العالمية.</li>
                <li>المخاطر الميدانية العالية المرتبطة بسباقات الرالي.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.subheader("📊 تفاصيل المشاريع والأرباح")
    st.dataframe(df_biz_filtered, use_container_width=True)

# ---------------------------------------------------------
# Tab 4: سيناريو العرض التقديمي
# ---------------------------------------------------------
with tab4:
    st.subheader("🎤 سيناريو الإلقاء واستراتيجية العرض المباشر")
    
    slides = [
        ("الشريحة 1: الغلاف", "مساء الخير / أهلاً بكم. نسلط الضوء اليوم على نموذج استثنائي يجمع بين إدارة المخاطر في سباقات داكار وبين الحنكة الاستثمارية في الأعمال."),
        ("الشريحة 2: الملخص التنفيذي", "هدفنا تقديم نظرة شمولية تعتمد على البيانات المتقدمة للربط بين اتخاذ القرار السريع والتوسع في تنويع المحفظة."),
        ("الشريحة 3: السيرة والمسيرة", "في الرياضة الميكانيكية، القرار في جزء من الثانية يحدد الفارق بين الفوز والخسارة. تجربة يزيد تحول هذا التركيز إلى منهجية عمل."),
        ("الشريحة 7: لوحة البيانات", "ننتقل الآن للغة الأرقام. تعكس لوحة البيانات علاقة مباشرة بين دقة التخطيط ومعدلات النجاح على الأرض.")
    ]
    
    for title, script in slides:
        with st.expander(title):
            st.write(script)
