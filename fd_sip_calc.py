import streamlit as st
import math
import pandas as pd
import matplotlib.pyplot as plt

st.title("📈 FD & SIP Calculator")

tab1, tab2 = st.tabs(["💰 Fixed Deposit Calculator", "📊 SIP Calculator"])

# ---------------------- FD Calculator -----------------------
with tab1:
    st.header("Fixed Deposit (FD) Calculator")

    principal = st.number_input("Principal Amount (₹)", min_value=1000.0, step=500.0)
    rate = st.slider("Annual Interest Rate (%)", min_value=1.0, max_value=12.0, value=7.0)
    years = st.slider("Tenure (in years)", min_value=1, max_value=10, value=3)
    frequency = st.selectbox("Compounding Frequency", ["Annual", "Half-Yearly", "Quarterly", "Monthly"])

    freq_map = {
        "Annual": 1,
        "Half-Yearly": 2,
        "Quarterly": 4,
        "Monthly": 12
    }

    n = freq_map[frequency]
    r = rate / 100

    maturity = principal * (1 + r / n) ** (n * years)
    interest_earned = maturity - principal

    st.success(f"💼 Maturity Amount: ₹{maturity:,.2f}")
    st.info(f"💸 Total Interest Earned: ₹{interest_earned:,.2f}")

# ---------------------- SIP Calculator -----------------------
with tab2:
    st.header("Systematic Investment Plan (SIP) Calculator")

    monthly_investment = st.number_input("Monthly Investment (₹)", min_value=100.0, step=100.0)
    expected_return = st.slider("Expected Annual Return (%)", min_value=5.0, max_value=20.0, value=12.0)
    sip_years = st.slider("Investment Duration (Years)", min_value=1, max_value=30, value=10)

    months = sip_years * 12
    r = expected_return / 100 / 12

    # SIP Future Value Formula
    future_value = monthly_investment * (((1 + r) ** months - 1) * (1 + r)) / r
    invested_amount = monthly_investment * months
    estimated_return = future_value - invested_amount

    st.success(f"📈 Future Value: ₹{future_value:,.2f}")
    st.info(f"💸 Total Invested: ₹{invested_amount:,.2f}")
    st.info(f"📊 Estimated Returns: ₹{estimated_return:,.2f}")

    # Optional chart
    if st.checkbox("📊 Show Growth Chart"):
        data = []
        fv = 0
        for i in range(1, months + 1):
            fv += monthly_investment * ((1 + r) ** (months - i + 1))
            data.append(fv)

        df = pd.DataFrame(data, columns=["Value"])
        st.line_chart(df)

