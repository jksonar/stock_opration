from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.StocksFormView, name='order_url'),
    path('all_stocks/', views.showView, name='show_url'),
    path('showfundstocks/<str:s_fname>/', views.fundStockView, name='show_fund_stock_url'),
    path('showfundtypestocks/<str:s_ftype>/', views.fundStockTypeView, name='show_fund_type_stock_url'),
    path('showfundname/', views.showFundView, name='show_fund_name_url'),
    path('showfundtype/', views.showFundTypeView, name='show_fund_type_url'),
    path('up/<int:f_id>', views.updateView, name= 'update_url'),
    path('del/<int:f_id>', views.deleteView, name= 'delete_url'),
]