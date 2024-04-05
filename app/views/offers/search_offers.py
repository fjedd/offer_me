from typing import Any, Dict

from django.db.models import Q, QuerySet

from app.models import JobOffer

from .offers import OffersView


class SearchOffersView(OffersView):
    query: str = ""
    offers_list: QuerySet = None

    def get_queryset(self) -> QuerySet[Any]:
        self.query: str = self.request.GET.get("q")
        if self.query:
            self.offers_list: QuerySet = JobOffer.objects.filter(
                Q(title__icontains=self.query)
                | Q(description__icontains=self.query)
                | Q(author__username__icontains=self.query)
                | Q(is_remote__icontains=self.query)
                | Q(company__icontains=self.query)
                | Q(location__icontains=self.query)
            )
        else:
            self.offers_list: QuerySet = JobOffer.objects.none()
        return self.offers_list

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        context["keyword"] = self.query
        context["offers_count"] = self.offers_list.count()
        return context
