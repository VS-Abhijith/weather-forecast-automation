

# Weather Forecast Extractor

This project fetches **weather forecast data** for a given city using the **BBC Weather Broker API**, **transforms** the data, and **saves** it as a structured JSON file.

## 📋 Project Structure

- **API Integration**: Connects to the BBC Weather Broker API using an API key.
- **Data Extraction**: Retrieves detailed weather forecast information for a given `location_id`.
- **Data Transformation**: Simplifies the response to keep only the **issue date** and **enhanced weather description**.
- **Data Storage**: Saves the cleaned data into a **JSON file** for future use or analysis.

---

## 🛠️ Requirements

Before running the code, make sure you have the following Python packages installed:

```bash
pip install requests
```

> `requests` is used for making HTTP requests to the weather API.

---

## 📦 How to Run

1. **Clone or download** this repository.

2. **Set your API Key**:
   - Replace the value of `API_KEY` in the script with your valid API key.

3. **Execute the script**:

```bash
python your_script_name.py
```

4. The output will be saved as a file named:

```
karachi_weather_forecast.json
```

---

## ⚙️ Functions Breakdown

- **`get_weather_forecast(location_id)`**
  - Fetches weather data for the given location.
  - Takes a `location_id` (e.g., Karachi's `1174872`) as input.
  - Returns the **raw JSON response**.

- **`transform_weather_data(weather_data)`**
  - Processes the raw weather data.
  - Extracts the **issue date** and **enhanced weather description**.
  - Returns a **clean dictionary**.

- **`main()`**
  - Controls the flow: fetches data, transforms it, and saves it to a JSON file.

---

## 🌟 Example Output

```json
{
    "2025-04-26T06:00:00Z": "Sunny Intervals",
    "2025-04-26T12:00:00Z": "Light Rain Showers",
    "2025-04-27T06:00:00Z": "Cloudy"
}
```

---

## 📈 Potential Extensions

- Add **error handling** for failed API requests.
- Make **location ID** a **user input** instead of hardcoding.
- Schedule the script to run **daily** to collect historical weather data.
- Visualize the forecasts using **Matplotlib** or **Power BI**.

---

## 💬 Notes

- **BBC Weather Broker API** may require special access permissions; check their usage policy.
- This code currently works only for **known location IDs**.
- Always **keep your API keys safe** — avoid pushing them into public repositories.

---

## 🙌 Author

*Developed with curiosity and enthusiasm.*

---
