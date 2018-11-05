package gigasecond

// import path for the time package from the standard library
import (
	"math"
	"time"
)

// AddGigasecond accept a time and return a time 1 gigasecond from the time
// submitted.
func AddGigasecond(t time.Time) time.Time {
	return t.Add(time.Duration(math.Pow10(18)))
}
