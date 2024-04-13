lint:
	black . && flake8 --count && mypy . && pylint config account room_booking
