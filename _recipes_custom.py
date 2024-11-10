from typing import List

from _recipe_utils import (
    Recipe,
    CoverOptions,
)

# Define the categories display order, optional
categories_sort: List[str] = []

# Define your custom recipes list here
# Example: https://github.com/ping/newsrack-fork-test/blob/custom/_recipes_custom.py

recipes: List[Recipe] = [
     Recipe(
        recipe="substack",
        slug="substack",
        src_ext="mobi",
        target_ext=["epub"],
        category="Blogs/Newsletters",
        tags=["commentary"],
     ),
]
