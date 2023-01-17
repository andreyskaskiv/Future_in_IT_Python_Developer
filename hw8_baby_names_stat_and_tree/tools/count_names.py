from collections import Counter
from typing import Dict, Any


def count_names(data_base_table: Dict[int, Dict], sex_name, first_items: int = 5) -> list[tuple[Any, int]]:
    """Count names"""
    count = Counter()
    for year, sex in data_base_table.items():
        count.update(sex[sex_name])

    return count.most_common(first_items)
