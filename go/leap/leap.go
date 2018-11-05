package leap

// IsLeapYear should take in an year as an integer and return true or false if
// that year is a leap year.
func IsLeapYear(y int) bool {
	return y%4 == 0 && (y%100 != 0 || (y%100 == 0 && y%400 == 0))
}
