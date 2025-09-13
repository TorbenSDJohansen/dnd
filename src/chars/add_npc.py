from dataclasses import dataclass

import pandas as pd


@dataclass
class NPC:
    name: str
    description: str
    race: str
    primary_location: str
    relationships: str


def add_char_from_excel_entry(entry: pd.Series) -> NPC:
    char = NPC(
        name=str(entry.Name) if pd.notna(entry.Name) else "",
        description=str(entry.Description) if pd.notna(entry.Description) else "",
        race=str(entry.Race) if pd.notna(entry.Race) else "",
        primary_location=str(entry['Primary location']) if pd.notna(entry['Primary location']) else "",
        relationships=str(entry.Relationships) if pd.notna(entry.Relationships) else "",
    )

    return char


def get_characters_from_excel(file_path: str) -> list[NPC]:
    df = pd.read_excel(file_path, sheet_name='Characters')
    characters = [add_char_from_excel_entry(row) for _, row in df.iterrows()]

    return characters


def sanitize(value: str) -> str:
    # Replace line breaks and excessive whitespace with a single space
    return " ".join(str(value).split())


def make_markdown_table(characters: list[NPC]) -> str:
    header = (
        "| Name     "
        "| Description                            "
        "| Race    "
        "| Primary location "
        "| Relationships                |"
    )
    separator = (
        "|----------"
        "|----------------------------------------"
        "|---------"
        "|------------------"
        "|------------------------------|"
    )

    rows = []
    for char in characters:
        row = (
            "| "
            f"{sanitize(char.name)} "
            "| "
            f"{sanitize(char.description)} "
            "| "
            f"{sanitize(char.race)} "
            "| "
            f"{sanitize(char.primary_location)} "
            "| "
            f"{sanitize(char.relationships)} "
            "|"
        )
        rows.append(row)

    table = "\n".join([header, separator] + rows)

    return table


def write_table(table: str, output_file: str) -> None:
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(table)
