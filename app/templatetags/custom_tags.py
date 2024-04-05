from django import template

register = template.Library()


@register.simple_tag
def get_page_href(request) -> str:
    query: str = request.GET.get("q", "")
    href: str = f"q={query}&" if query else ""
    return href
