from django.urls import path

from apps.views.branch import BranchOneListView, BranchDeleteView

urlpatterns = [
    path('brinch_user', BranchOneListView.as_view()),
    path('branch_delete/<int:pk>', BranchDeleteView.as_view()),

]
