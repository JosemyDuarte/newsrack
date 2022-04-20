from collections import namedtuple

Receipe = namedtuple(
    "Recipe",
    ["recipe", "name", "slug", "src_ext", "target_ext", "timeout", "overwrite_cover"],
)
default_recipe_timeout = 120

# the azw3 formats don't open well in the kindle (stuck, cannot return to library)
recipes = [
    Receipe(
        recipe="channelnewsasia",
        name="ChannelNewsAsia",
        slug="channelnewsasia",
        src_ext="mobi",
        target_ext=[],
        timeout=default_recipe_timeout,
        overwrite_cover=True,
    ),
    Receipe(
        recipe="thediplomat",
        name="The Diplomat",
        slug="the-diplomat",
        src_ext="mobi",
        target_ext=[],
        timeout=default_recipe_timeout,
        overwrite_cover=True,
    ),
    Receipe(
        recipe="economist",
        name="The Economist",
        slug="economist",
        src_ext="mobi",
        target_ext=[],
        timeout=300,
        overwrite_cover=True,
    ),
    Receipe(
        recipe="ft",
        name="Financial Times",
        slug="ft",
        src_ext="mobi",
        target_ext=[],
        timeout=default_recipe_timeout,
        overwrite_cover=True,
    ),
    Receipe(
        recipe="fivebooks",
        name="Five Books",
        slug="fivebooks",
        src_ext="mobi",
        target_ext=[],
        timeout=default_recipe_timeout,
        overwrite_cover=True,
    ),
    Receipe(
        recipe="guardian",
        name="The Guardian",
        slug="guardian",
        src_ext="mobi",
        target_ext=[],
        timeout=default_recipe_timeout,
        overwrite_cover=True,
    ),
    Receipe(
        recipe="japan-times",
        name="Japan Times",
        slug="japan-times",
        src_ext="mobi",
        target_ext=[],
        timeout=default_recipe_timeout,
        overwrite_cover=True,
    ),
    Receipe(
        recipe="joongangdaily",
        name="Joongang Daily",
        slug="joongang-daily",
        src_ext="mobi",
        target_ext=[],
        timeout=default_recipe_timeout,
        overwrite_cover=True,
    ),
    Receipe(
        recipe="korea-herald",
        name="Korea Herald",
        slug="korea-herald",
        src_ext="mobi",
        target_ext=[],
        timeout=default_recipe_timeout,
        overwrite_cover=True,
    ),
    Receipe(
        recipe="london-review",
        name="London Review of Books",
        slug="lrb",
        src_ext="mobi",
        target_ext=[],
        timeout=default_recipe_timeout,
        overwrite_cover=False,
    ),
    Receipe(
        recipe="nytimes-global",
        name="NY Times Global",
        slug="nytimes-global",
        src_ext="mobi",
        target_ext=[],
        timeout=default_recipe_timeout,
        overwrite_cover=True,
    ),
    Receipe(
        recipe="nytimes-books",
        name="New York Times Books",
        slug="nytimes-books",
        src_ext="mobi",
        target_ext=[],
        timeout=default_recipe_timeout,
        overwrite_cover=True,
    ),
    Receipe(
        recipe="politico-magazine",
        name="POLITICO Magazine",
        slug="politico-magazine",
        src_ext="mobi",
        target_ext=[],
        timeout=default_recipe_timeout,
        overwrite_cover=True,
    ),
    Receipe(
        recipe="scmp",
        name="South China Morning Post",
        slug="scmp",
        src_ext="mobi",
        target_ext=[],
        timeout=default_recipe_timeout,
        overwrite_cover=True,
    ),
    Receipe(
        recipe="wapo",
        name="The Washington Post",
        slug="wapo",
        src_ext="mobi",
        target_ext=[],
        timeout=600,
        overwrite_cover=True,
    ),
]
