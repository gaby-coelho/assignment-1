import streamlit as st
from starter import COSTS, TIME_BLOCKS, ZONES
from logic import avg_delivery_time, best_promise, cost_per_late_order, late_rate


st.set_page_config(page_title="Rosa's Pizza")
st.title("Rosa's Pizza")
st.caption("Find the delivery promise with the highest net profit.")

zone_column, time_column = st.columns(2)
with zone_column:
    zone = st.selectbox("Zone", options=ZONES)
with time_column:
    time_block = st.selectbox("Time block", options=TIME_BLOCKS)

st.subheader("Promise range")
range_start_column, range_end_column = st.columns(2)
with range_start_column:
    promise_start = st.number_input(
        "First promise (minutes)", min_value=5, max_value=90, value=5, step=5
    )
with range_end_column:
    promise_end = st.number_input(
        "Last promise (minutes)", min_value=5, max_value=90, value=90, step=5
    )

st.subheader("Order economics")
margin_column, churn_column, refund_column = st.columns(3)
with margin_column:
    margin = st.number_input(
        "Profit margin per order",
        min_value=0.0,
        value=float(COSTS["margin"]),
        step=0.5,
        format="%.2f",
    )
with churn_column:
    churn_orders = st.number_input(
        "Churn per late order",
        min_value=0.0,
        value=float(COSTS["churn_orders"]),
        step=0.1,
        format="%.2f",
    )
with refund_column:
    refund = st.number_input(
        "Refund per late order",
        min_value=0.0,
        value=float(COSTS["refund"]),
        step=0.5,
        format="%.2f",
    )

valid_range = promise_start <= promise_end
if not valid_range:
    st.warning("The first promise must be less than or equal to the last promise.")

if st.button("Recommend promise", disabled=not valid_range):
    promises = range(int(promise_start), int(promise_end) + 1, 5)
    costs = {
        "margin": margin,
        "churn_orders": churn_orders,
        "refund": refund,
    }
    recommended_promise, net_profit = best_promise(
        zone, time_block, promises, costs
    )
    st.session_state.recommendation = {
        "zone": zone,
        "time_block": time_block,
        "promise": recommended_promise,
        "net_profit": net_profit,
    }

if "recommendation" in st.session_state:
    recommendation = st.session_state.recommendation
    st.subheader(
        f"Recommendation for {recommendation['zone']} / {recommendation['time_block']}"
    )
    result_column, profit_column = st.columns(2)
    result_column.metric("Promised delivery time", f"{recommendation['promise']} min")
    profit_column.metric("Net profit", f"${recommendation['net_profit']:,.2f}")