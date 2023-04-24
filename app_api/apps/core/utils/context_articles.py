def get_context_from_content(articles: list) -> list:
    context = []
    for _ in articles:
        if _['author'] and _['title'] and _['description']:
            context.append(dict(
                title=_['title'],
                author=_['author'],
                description=_['description'],
            ))

    return context
