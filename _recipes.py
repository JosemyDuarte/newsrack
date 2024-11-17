# Copyright (c) 2022 https://github.com/ping/
#
# This software is released under the GNU General Public License v3.0
# https://opensource.org/licenses/GPL-3.0

# --------------------------------------------------------------------
# This file defines default recipes distributed with newsrack.
# To customise your own instance, do not modify this file.
# Add your recipes to _recipes_custom.py instead and new recipe source
# files to recipes_custom/.
# --------------------------------------------------------------------

from typing import List

from _recipe_utils import (
    CoverOptions,
    Recipe,
    first_n_days_of_month,
    last_n_days_of_month,
    onlyat_hours,
    onlyon_days,
    onlyon_weekdays,
)

# Only mobi work as periodicals on the Kindle
# Notes:
#   - When epub is converted to mobi periodicals:
#       - masthead is lost
#       - mobi retains periodical support but has the non-functional
#         calibre generated nav, e.g. Next Section, Main, etc
#       - article summary/description is lost
#   - When mobi periodical is converted to epub:
#       - epub loses the calibre generated nav, e.g. Next Section, Main, etc
#         but full toc is retained
#   - Recipe can be defined twice with different src_ext, will work except
#     for potential throttling and time/bandwidth taken

categories_sort: List[str] = ["News", "Magazines", "Online Magazines", "Arts & Culture"]

# Keep this list in alphabetical order
recipes: List[Recipe] = [
    Recipe(
        recipe="fivebooks",
        slug="fivebooks",
        src_ext="mobi",
        target_ext=["epub"],
        category="Arts & Culture",
        enable_on=onlyon_weekdays([0, 1, 2, 3, 4]),
        cover_options=CoverOptions(
            logo_path_or_url="https://fivebooks.com/app/themes/five-books/assets/images/logo.png"
        ),
        tags=["literature", "books"],
    ),
    Recipe(
        recipe="ft",
        slug="ft-online",
        src_ext="mobi",
        target_ext=["epub"],
        category="News",
        tags=["business"],
        cover_options=CoverOptions(
            logo_path_or_url="https://www.ft.com/partnercontent/content-hub/static/media/ft-horiz-new-black.215c1169.png"
        ),
    ),

    Recipe(
        recipe="lithub",
        slug="lithub",
        src_ext="mobi",
        target_ext=["epub"],
        category="Arts & Culture",
        enable_on=onlyon_weekdays([0, 1, 2, 3, 4], -5)
        and onlyat_hours(list(range(10, 17)), -5),
        cover_options=CoverOptions(
            logo_path_or_url="https://s26162.pcdn.co/wp-content/themes/rigel/images/social_logo.png"
        ),
        tags=["literature", "books"],
    ),
    Recipe(
        recipe="mit-tech-review",
        slug="mit-tech-review-feed",
        src_ext="mobi",
        target_ext=["epub"],
        category="Online Magazines",
        enable_on=onlyon_weekdays([0, 1, 2, 3, 4, 5], -4),
        tags=["technology"],
        cover_options=CoverOptions(
            text_colour="#444444",
            logo_path_or_url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/MIT_Technology_Review_modern_logo.svg/1024px-MIT_Technology_Review_modern_logo.svg.png",
        ),
    ),
    Recipe(
        recipe="mit-tech-review-magazine",
        slug="mit-tech-review-magazine",
        src_ext="mobi",
        target_ext=["epub"],
        category="Magazines",
        overwrite_cover=False,
        enable_on=first_n_days_of_month(7, -5) or last_n_days_of_month(7, -5),
        tags=["technology"],
    ),
    Recipe(
        recipe="mollywhite-newsletter",
        slug="mollywhite-newsletter",
        src_ext="mobi",
        target_ext=["epub"],
        category="Blogs/Newsletters",
        tags=["technology"],
        cover_options=CoverOptions(
            logo_path_or_url="https://substackcdn.com/image/fetch/w_256,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F3b6a58dc-123a-492b-a1e2-b46138add2b9_856x856.png"
        ),
    ),
    Recipe(
        recipe="natesilver",
        slug="natesilver",
        src_ext="mobi",
        target_ext=["epub"],
        category="Blogs/Newsletters",
        tags=["commentary"],
        cover_options=CoverOptions(
            logo_path_or_url="https://substackcdn.com/image/fetch/w_256,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9798f361-e880-406c-9ed4-29229df02c27_256x256.png"
        ),
    ),
    Recipe(
        recipe="vox",
        slug="vox",
        src_ext="mobi",
        target_ext=["epub"],
        category="Online Magazines",
        cover_options=CoverOptions(
            logo_path_or_url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Vox_logo.svg/300px-Vox_logo.svg.png"
        ),
    ),
    Recipe(
        recipe="wired",
        slug="wired",
        src_ext="mobi",
        target_ext=["epub"],
        overwrite_cover=True,
        category="Online Magazines",
        tags=["technology"],
        enable_on=(first_n_days_of_month(7) or last_n_days_of_month(7))
        and onlyat_hours(list(range(10, 18))),
        cover_options=CoverOptions(
            logo_path_or_url="https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Wired_logo.svg/1024px-Wired_logo.svg.png"
        ),
    ),
]
