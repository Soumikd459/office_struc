

#Scenario: Retrieve all users who registered within the last week.



'''from django.utils import timezone
from myapp.models import User

users_last_week = User.objects.filter(date_registered__gte=timezone.now() - timezone.timedelta(days=7))
 
 date_registered__gte is not a variable; it's a lookup expression used in Django QuerySet filtering.

•	date_registered: This is the field name in the Django model//   
 we should use __gte (greater than or equal to) to find users who registered on or after one week ago.// If we used __lte (less than or equal to), it would retrieve users who registered before or exactly one week ago. 
 '''

last_wk = users.objects.filter(date_registered__gte = timezone.now() - timezone.timedelta(days = 7))

Scenario-2: Count the total number of products in the database.

from app.models import products
total_no_of_prod = Products.objects.count() 

Scenario-3: Retrieve the details of the latest purchase made by a specific user.
User_id = 1
latest_purchase = Purchase.objects.filter(user_id = User_id ) .latest('timestamp')

Scenario-4: Retrieve all users with a specific role (e.g., "admin").

users_roles = users.objects.filter(users_role = admin)

**Scenario-5: Calculate the total revenue generated from all purchases. **


total_revenue = Purchase.objects.aggregate(total_revenue=models.Sum('amount'))['total_revenue']

Scenario-6: Retrieve all products sorted by their price in descending order.

products_price = Products.objects.order_by('-price')

Scenario-7: Retrieve all users who have not made any purchases yet.

users_not_purchase = Users.objects.filter(purchase__isnull = True)

Scenario-8: Retrieve all active users who have made a purchase in the last month.


from django.utils import timezone
from myapp.models import User, Purchase

active_users = User.objects.filter(is_active=True, purchase__timestamp__gte=timezone.now() - timezone.timedelta(days=30)).distinct()


Scenario-9: Calculate the total revenue generated from purchases made by users in a specific city.


from myapp.models import Purchase
if profile and purchase is 2 diff table then following Query

city = "New York"  # Example city
total_revenue = Purchase.objects.filter(user__profile__city=city).aggregate(total_revenue=models.Sum('amount'))['total_revenue']

['total_revenue']: Extracts the value associated with the total_revenue key from the dictionary returned by the aggregate method.

#user__profile__city=city: Uses double underscores (__) to follow relationships across models. This condition means that the query will only include purchases where the associated user's profile's city is "New York"

# if only Purchase model is avl.
city = "New York"  # Example city
total_revenue = Purchase.objects.filter(city=city).aggregate(total_revenue=models.Sum('amount'))['total_revenue']

**********************
