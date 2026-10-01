This is a Streamlit app for BUSADMIN O712 Assignment 1 (Rosa's Pizza).

## Commands

- `pip install -r requirements.txt` to install dependencies.
- App: `streamlit run app.py`

## Architecture

- `starter.py` (installed from the rosa-starter package) provides
  ZONES, TIME_BLOCKS, COSTS, PROMISE, and delivery_times. Do not
  edit or reimplement any of these.
- `logic.py` holds all pure computation, ported from the notebook:
  late_rate, avg_delivery_time, cost_per_late_order, best_promise.
  No Streamlit imports, no printing — these should be usable and
  testable outside the app.
- `app.py` is a thin wrapper. It builds widgets, reads user input,
  calls functions from logic.py, and displays results. It does not
  contain any zone/time-block/cost calculation logic of its own.
- A change to logic.py must not require changing how app.py calls it,
  unless the function's signature genuinely changes.

## Constraints

- Standard library, numpy, and streamlit only, plus the rosa-starter
  package. Ask before adding any other dependency.
- Preserve the behavior verified in the notebook — logic.py should
  produce the same results as the tested notebook functions, not new
  implementations.
- Reuse existing functions rather than duplicating logic in app.py.