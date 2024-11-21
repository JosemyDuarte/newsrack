from typing import List

from _recipe_utils import Recipe

# Define the categories display order, optional
categories_sort: List[str] = []

# Define your custom recipes list here
# Example: https://github.com/ping/newsrack-fork-test/blob/custom/_recipes_custom.py

recipes: List[Recipe] = [
    Recipe(
        recipe="hackernews",
        slug="hackernews",
        category="technology",
        src_ext="mobi",
        target_ext=["epub"],
        tags=["software", "news"],
    ),
    Recipe(
        recipe="theverge",
        slug="theverge",
        category="technology",
        src_ext="mobi",
        target_ext=["epub"],
        tags=["news"],
    ),
    Recipe(
        recipe="substack",
        slug="substack",
        category="newsletter",
        src_ext="mobi",
        target_ext=["epub"],
        tags=["weekly", "growth"],
    ),
]