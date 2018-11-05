package gigasecond

import "time"

// AddGigasecond accept a time and return a time 1 gigasecond from the time
// submitted.
func AddGigasecond(t time.Time) time.Time {
	return t.Add(time.Duration(1e18))
}
