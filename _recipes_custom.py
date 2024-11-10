from typing import List

from _recipe_utils import Recipe

# Define the categories display order, optional
categories_sort: List[str] = []

# Define your custom recipes list here
# Example: https://github.com/ping/newsrack-fork-test/blob/custom/_recipes_custom.py

recipes: List[Recipe] = [
     Recipe(
        recipe="weskao-newsletter",
        slug="weskao-newsletter",
        src_ext="mobi",
        target_ext=["epub"],
        category="Blogs/Newsletters",
        tags=["commentary"],
        cover_options=CoverOptions(
            logo_path_or_url="https://substackcdn.com/image/fetch/w_96,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1b53bd7d-121d-45b5-8b63-77c9cc08ffbd_1280x1280.png"
        )
     ),
]
