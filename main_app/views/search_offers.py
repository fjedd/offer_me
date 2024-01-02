from typing import Any, Dict

from django.db.models import Q, QuerySet

from ..models import JobOffer
from .offers import OffersView


class SearchOffersView(OffersView):
    def get_context_data(self) -> Dict[str, Any]:
        query: str = self.request.GET.get("q")
        if query:
            offers_list: QuerySet = JobOffer.objects.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )
        else:
            offers_list: QuerySet = JobOffer.objects.none()  # type: ignore

        context: Dict[str, Any] = {
            "job_offers": offers_list,
            "keyword": query,
            "offers_count": offers_list.count(),
        }
        return context
