SQL dump. Run migrations first

INSERT INTO `booking_hotel` (`id`, `name`, `city_id`, `nr_rooms`, `price`) VALUES
(1, 'Thon', 1, 452, 980),
(2, 'Scandic', 2, 98, 875),
(3, 'Radisson Blu Royal Hotel', 3, 271, 1198),
(4, 'Clarion', 4, 251, 780),
(5, 'Thon', 4, 412, 2199);

INSERT INTO `booking_city` (`id`, `name`) VALUES
(1, 'Oslo'),
(2, 'Bergen'),
(3, 'Stavanger'),
(4, 'Tromsø');

- - - -

Time spendt: 6hr 12min