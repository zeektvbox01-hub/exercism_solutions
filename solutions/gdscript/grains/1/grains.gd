const NUMBER_OF_SQUARES = 63

func square(num: int):
	if 1 > num or num > NUMBER_OF_SQUARES:
		return null
	return 2 ** (num - 1)


func total():
	return 2 ** NUMBER_OF_SQUARES - 1
