# Flight Delay Visualization Project  

## Project Overview  
This project analyzes flight delay data in the United States, offering insights into the causes and patterns of delays. The analysis combines bar charts, pie charts, and an interactive map to provide a comprehensive understanding of delays across cities and carriers.  

---

## Data Sources  
1. **Flight Delay Data**:  
   - Source: **T_ONTIME_REPORTING.csv** (https://transtats.bts.gov/Fields.asp?gnoyr_VQ=FGK)  
   - Description: A CSV file containing details such as carrier, origin, destination, and delay information.  

2. **Geographical Data**:  
   - Source: **united-states-international-airports.geojson** (https://github.com/codeforgermany/click_that_hood/tree/main/public/data)  
   - Description: A GeoJSON file with U.S. city geographical coordinates for mapping purposes.  

---

## Python Code and Workflow  

### 1. Preprocessing (`premap.py`)  
- Extracts departure city coordinates from the dataset (`T_ONTIME_REPORTING.csv`).  
- Saves processed data to `city_coordinates.csv` for faster access during mapping.  

### 2. Bar Chart Analysis (`bar.py`)  
- Visualizes average carrier delays across different airlines using Matplotlib.  
- Highlights variability in delays among carriers.
- **average_delay_by_cause.png**

### 3. Pie Chart Analysis (`pie.py`)  
- Displays the proportion of delay causes (e.g., late aircraft, weather, NAS) in a pie chart.  
- Identifies late aircraft as the dominant contributor.
- **delay_causes_pie_chart.png**

### 4. Interactive Map (`map.py`)  
- Uses Folium to create an interactive map showing delay hotspots.  
- Color-coded markers represent delay durations:  
  - Green: Delays < 20 minutes  
  - Yellow: Delays between 20–50 minutes  
  - Red: Delays > 50 minutes  
- Includes popups for detailed flight information (carrier and delay time).
- **average_flight_delays_map_with_custom_popup.html**

---

## Methods  
1. **Data Aggregation**:  
   - Calculated total delays for each flight by summing delays from various causes (e.g., weather, NAS, late aircraft).  

2. **Visualization**:  
   - Bar and pie charts created using Matplotlib to summarize carrier performance and delay causes.  
   - Interactive map created using Folium to provide geographic insights into delays.  

3. **Color Coding**:  
   - Delays were categorized into three levels for clear visual distinction.  

4. **Optimization**:  
   - Preprocessed city coordinates to enhance map rendering efficiency.  

---

## GitHub Pages  
The project, along with the Python scripts, data sources, and report documentation, is archived on a GitHub Page.  
**Link**: [Interactive Flight Delay Visualization](https://yourusername.github.io/Flight-Delay-Visualization/)  

---

## Significance  
By combining statistical analysis and interactive visualizations, this project bridges raw data with actionable insights, enhancing both personal and industry-level decision-making.  
