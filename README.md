# Loss Tracking Application

A Django-based web dashboard for monitoring and analysing production line losses in a manufacturing environment. The application visualises key metrics such as **Extract Loss**, **Heuft 1** and **Heuft 2** reject losses, and **Other Losses** across different product lines (Can and Bottle). It supports interactive time‑based filtering (weeks/months) and drill‑down to detailed loss breakdowns per product.

---

## Features

- **Interactive Dashboard** – built with Vue.js and Chart.js for real‑time data visualisation.
- **Loss Metrics** – displays Extract Loss, Heuft 1 Loss, Heuft 2 Loss, and calculated Other Losses.
- **Time‑based Aggregation** – switch between weekly and monthly views.
- **Drill‑down Capability** – click on a bar in the Extract Loss chart to view loss deployment details for that period.
- **Product‑line Breakdown** – separate loss charts for Can and Bottle lines.
- **Target Tracking** – shows target values as horizontal lines for comparison.
- **Responsive Design** – uses Bootstrap 4 for a mobile‑friendly layout.

---

## Tech Stack

- **Backend**: Django (with Django REST Framework for API endpoints)
- **Frontend**: Vue.js (with `vue-resource` or `jQuery.ajax`), Chart.js (via `Chart.bundle.min.js`), Bootstrap 4
- **Data Handling**: Custom templatetags (`frontend_tags`, `load_heuft_charts`) for component inclusion
- **Styling**: CSS (custom) and Bootstrap

---

## Installation

### Prerequisites
- Python 3.8+
- Node.js (optional, for frontend asset management)
- PostgreSQL / MySQL / SQLite (any Django‑supported database)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/loss-tracking.git
   cd loss-tracking
