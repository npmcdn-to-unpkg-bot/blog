---
publish_date: '2014-09-23'
title: Quick random bytes in Go
---

I wanted to generate random IDs for some database entries I was storing:

```
import (
  "math/rand"
  "time"
)

var r = rand.New(rand.NewSource(time.Now().UnixNano()))

func GenID() string {
  i := 100000 + r.Intn(900000)
  return fmt.Sprintf("%x", i)
}
```

Obviously, we can do better. I suck at math so I’ll just trust this package
some Googler wrote:

```
import "github.com/dustin/randbo"

func GenID(l int) string {
  p := make([]byte, l)
  randbo.New().Read(p)
  return fmt.Sprintf("%x", p)
}
```
