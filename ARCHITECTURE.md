# Architecture

## Tech Stack

Frontend + Backend
Streamlit

Data Processing
Pandas + PyArrow

Visualization
Plotly

Reason:
Streamlit enables rapid development of interactive data visualization tools without needing a full frontend framework.

---

## Data Flow

Raw Telemetry Files (.nakama-0)
↓
Python parsing using Pandas
↓
Combined dataset stored as events.csv
↓
Streamlit loads dataset
↓
Interactive visualization in browser

---

## Coordinate Mapping

Player world coordinates (x,y) are directly plotted on the minimap.

Mapping formula:

mapX = (x - minX) / (maxX - minX)
mapY = (y - minY) / (maxY - minY)

These normalized values are scaled to the minimap image.

---

## Tradeoffs

Option | Decision | Reason
--- | --- | ---
React frontend | Not used | Streamlit faster for prototype
Database | Not used | dataset small enough for CSV
Realtime streaming | Not implemented | not required for test

---

## Future Improvements

- Real-time telemetry streaming
- Player clustering analysis
- Combat zone detection
- Team fight detection