# Helpers to generate opds xml - extremely minimal
from datetime import datetime

extension_contenttype_map = {
    ".epub": "application/epub+zip",
    ".mobi": "application/x-mobipocket-ebook",
    ".azw": "application/x-mobipocket-ebook",
    ".azw3": "application/x-mobi8-ebook",
    ".pdf": "application/pdf",
}


def simple_tag(doc_root, tag, value=None, attributes=None):
    new_tag = doc_root.createElement(tag)
    if value:
        new_tag.appendChild(doc_root.createTextNode(value))
    if attributes:
        for k, v in attributes.items():
            new_tag.setAttribute(k, v)
    return new_tag


def init_feed(doc, publish_site, feed_id, title):
    feed = simple_tag(
        doc,
        "feed",
        attributes={
            "xmlns": "http://www.w3.org/2005/Atom",
            "xmlns:dc": "http://purl.org/dc/terms/",
            "xmlns:opds": "http://opds-spec.org/2010/catalog",
        },
    )
    doc.appendChild(feed)
    feed.appendChild(simple_tag(doc, "id", feed_id))
    feed.appendChild(simple_tag(doc, "title", title))
    feed.appendChild(simple_tag(doc, "updated", f"{datetime.now():%Y-%m-%dT%H:%M:%SZ}"))
    feed_author = doc.createElement("author")
    feed_author.appendChild(simple_tag(doc, "name", publish_site))
    feed_author.appendChild(simple_tag(doc, "uri", publish_site))
    feed.appendChild(feed_author)
    return feed