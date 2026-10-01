---
name: notebook-to-streamlit
description: Use when turning tested Jupyter notebook functions into
  a Streamlit app. Covers extracting pure logic from a notebook and
  mapping it to widgets and rerun-safe state. Not for building a
  Streamlit app from scratch with no existing logic.
---

## Step 1 — Extract pure logic

Copy the following functions out of the notebook into logic.py,
unchanged: late_rate, avg_delivery_time, cost_per_late_order,
best_promise. No Streamlit imports, no printing. logic.py should
import ZONES, TIME_BLOCKS, COSTS, delivery_times from starter.py.

## Step 2 — Map the interface

| Requirement                          | Streamlit widget                     |
|---------------------------------------|---------------------------------------|
| select a zone                         | st.selectbox(options=ZONES)          |
| select a time block                   | st.selectbox(options=TIME_BLOCKS)    |
| set the range of promised times       | two st.number_input, or st.slider    |
| adjust profit margin per order        | st.number_input, default = COSTS['margin'] |
| adjust churn per late order           | st.number_input, default = COSTS['churn']  |
| adjust refund per late order          | st.number_input, default = COSTS['refund'] |
| get the recommendation                | st.button                            |
| show the recommended promise          | st.write, outside the button's if-block |

Defaults for the cost inputs must match COSTS from starter.py, so
the app behaves like the notebook out of the box.

## Step 3 — State discipline

Streamlit reruns the whole script on every widget interaction.

- The `if st.button(...)` block should only compute the result and
  store it in st.session_state.
- Displaying the result happens outside that block, reading from
  st.session_state unconditionally, so it survives reruns caused by
  touching other widgets (e.g. changing the zone after clicking).

## Done when

- [ ] logic.py functions match the notebook's tested output for at
      least one zone/time-block pair.
- [ ] Changing zone or time block and clicking the button updates
      the recommendation correctly.
- [ ] After clicking the button, the result stays visible when you
      then move a slider or change a dropdown.