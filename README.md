SQL dump. Run migrations first

```sql
INSERT INTO `booking_hotel` (`id`, `name`, `city_id`, `nr_rooms`, `price`) VALUES
(1, 'Thon', 1, 452, 980),
(2, 'Scandic', 2, 98, 875),
(3, 'Radisson Blu Royal Hotel', 3, 271, 1198),
(4, 'Clarion', 4, 251, 780),
(5, 'Thon', 4, 412, 2199);
```
```sql
INSERT INTO `booking_city` (`id`, `name`) VALUES
(1, 'Oslo'),
(2, 'Bergen'),
(3, 'Stavanger'),
(4, 'Tromsø');
```
- - - -

Issues:
Had a more less complex query that I could not for the life of me manage to convert into a Django querySet.
You can find the raw query and the failed atempt at the querySet in booking/views.py at line 54 and below.

- - - -

First time ever coding in Python and using Django

Time spendt: ~7hrs
