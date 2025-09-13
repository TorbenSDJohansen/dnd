from dataclasses import dataclass

import pandas as pd


@dataclass
class Location:
    name: str
    description: str
    notes: str


def add_loc_from_excel_entry(entry: pd.Series) -> Location:
    loc = Location(
        name=str(entry.Name) if pd.notna(entry.Name) else "",
        description=str(entry.Description) if pd.notna(entry.Description) else "",
        notes=str(entry.Notes) if pd.notna(entry.Notes) else "",
    )

    return loc


def get_locations_from_excel(file_path: str) -> list[Location]:
    df = pd.read_excel(file_path, sheet_name='Places')
    locations = [add_loc_from_excel_entry(row) for _, row in df.iterrows()]

    return locations


def sanitize(value: str) -> str:
    # Replace line breaks and excessive whitespace with a single space
    return " ".join(str(value).split())


def make_location_markdown_table(locations: list[Location]) -> str:
    header = (
        "| Name     "
        "| Description                            "
        "| Race    |"
    )
    separator = (
        "|----------"
        "|----------------------------------------"
        "|------------------------------|"
    )

    rows = []
    for loc in locations:
        row = (
            "| "
            f"{sanitize(loc.name)} "
            "| "
            f"{sanitize(loc.description)} "
            "| "
            f"{sanitize(loc.notes)} "
            "|"
        )
        rows.append(row)

    table = "\n".join([header, separator] + rows)

    return table
