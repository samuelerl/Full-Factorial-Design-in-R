import pandas as pd
import itertools
import numpy as np

OUTFILE = "~/excel_sheets/factorial.xlsx"


def generate_random_design(factors, n_reps=1, out_file="design.xlsx", sheet_name="Design"):
    """
    Generate a randomized full‐factorial design and write to Excel doc

    Params
    ----------
    factors : dict
        A dict mapping factor names to lists of levels, e.g.
        {"Nose": ["Yes", "No"], "Middle": ["Yes", "No"], "Rear": ["Yes", "No"]}
    n_reps : int
        Number of replicates per treatment combination
    out_file : str
        Path to output Excel file.
    sheet_name : str
        Name of the sheet in the Excel file

    Returns
    -------
    pd.DataFrame
        The randomized design (invisibly returned)
    """
    level_lists = [factors[f] for f in factors]
    combos = list(itertools.product(*level_lists))
    df = pd.DataFrame(combos, columns=list(factors.keys()))

    df = pd.concat([df] * n_reps, ignore_index=True)

    df = df.sample(frac=1, random_state=None).reset_index(drop=True)

    df.insert(0, "RunOrder", range(1, len(df) + 1))

    df["Distance"] = ""

    with pd.ExcelWriter(out_file, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name=sheet_name)

    print(f"Design written to: {out_file}")
    return df


# Example usage:
if __name__ == "__main__":
    my_factors = {
        "Nose": ["Yes", "No"],
        "Middle": ["Yes", "No"],
        "Rear": ["Yes", "No"]
    }
    design_df = generate_random_design(my_factors, n_reps=7, out_file="$OUTFILE")
    print(design_df.head())
