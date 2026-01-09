Workforce Calculator — Quick README (1 page)

Purpose
- Provide a simple, transparent model to estimate staffing needs based on volume and handling time.

Inputs
- Daily_Volume: total units expected per day
- Avg_Handle_Time_min: average time in minutes to process one unit
- Shrinkage_percent: expected non-productive time fraction (breaks, meetings, training)
- Shifts: number of shifts per day

Core logic (simplified)
1. Total_minutes_required = Daily_Volume * Avg_Handle_Time_min
2. Available_minutes_per_FTE_per_day = Shift_length_minutes * (1 - Shrinkage_percent)
   - Use 480 minutes for an 8-hour shift as a default
3. Required_FTEs_total = ceil(Total_minutes_required / Available_minutes_per_FTE_per_day)
4. Suggested_FTEs_per_shift = ceil(Required_FTEs_total / Shifts)

Example
- Daily_Volume = 10,000
- Avg_Handle_Time_min = 0.5
- Total_minutes_required = 5,000
- With 8-hour shifts and 10% shrinkage: Available_minutes_per_FTE = 480*(1-0.10)=432
- Required_FTEs_total = ceil(5000/432) = 12
- For 3 shifts -> Suggested_FTEs_per_shift = ceil(12/3) = 4

What to improve next
- Add variability by hour-of-day to model peaks
- Add time-and-motion derived handle times per SKU
- Convert to an interactive Google Sheet with input cells and formulas

Micro-task (5 minutes)
- Open this repo in GitHub and download Workforce_Calculator.csv, then open it in Excel or Google Sheets and confirm header row is visible.