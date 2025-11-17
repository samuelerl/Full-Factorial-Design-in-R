# Factorial Design of Paper Airplanes

This repository contains a full factorial design study that examines how paper clip placement affects paper airplane flight distance. The primary analysis is written in R Markdown, supported by helper scripts for design randomization and power estimation.

## Repository structure
- `Final Project.Rmd` – R Markdown report that describes the experiment and performs the analysis.
- `excel_sheets/` – Excel files with the pilot and full study run orders and recorded distances.
- `pictures/` – Photos of the airplane design and experimental setup referenced in the report.
- `useful_functions/` – Helper scripts used during the project:
  - `excel_writer.py` generates randomized full-factorial run orders and saves them to Excel.
  - `power_factorial_23.R` estimates power for a $2^3$ factorial design via simulation.

## Reproducing the report
1. Open `Final Project.Rmd` in RStudio (or run `rmarkdown::render("Final Project.Rmd")`).
2. Ensure the following R packages are installed: `ggplot2`, `readxl`, `dplyr`, and `knitr`.
3. The report expects the Excel files in `excel_sheets/` and images in `pictures/` to remain in their current relative locations.
4. Knit the document to PDF to recreate the analysis, figures, and narrative.

## Generating a new randomized design (optional)
If you want to run additional experiments, you can create a new randomized run order with Python:

```bash
python useful_functions/excel_writer.py
```

By default this writes a factorial design spreadsheet to `~/excel_sheets/factorial.xlsx`. Adjust the `OUTFILE` constant or call `generate_random_design` directly to customize factors, replicates, or output path.
