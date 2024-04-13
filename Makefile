lint:
	black . && flake8 --count && mypy --exclude tests . && pylint config account room_booking
