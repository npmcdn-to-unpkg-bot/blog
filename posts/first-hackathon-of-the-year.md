---
publish_date: '2014-05-11'
title: First hackathon of the year
---

I love going to hackathons. They’re like slumber party tournaments. I actually
like hackathons that let you code during daytime more but that’s for another
blog post.

(Oh just got an idea. HACKATHON IN A CAMP!)

Anways, our entry to yesterday’s Tech Camp Hackathon at Globe Labs was
[KUWAGO](http://kuwago.marksteve.com/).

Don’t mind the units and values. They’re just random sample data :P The app
basically shows a dashboard that LGUs can monitor, for them to make decisions
in disaster situations. The idea is that the dashboard will be able to pull
from several normalized APIs and render visualizations that are concise and
easy to digest. There are 3 panels for every monitored value. First one is a
time-series graph that shows you the trend of the value monitored. This is
useful for answering questions like “Is it getting any worse?” or “How much
time do we have before we ask people to evacuate?”. Second panel shows the
current value and the threshold value. Last one shows an
evaluation/recommendation based from the difference of the current value from
the threshold value.

Most data available from other monitoring sites show raw values that are not
usually enough to make out the situation. In our project, there’s an
assumption that the values returned by the queried APIs are enough to make
meaningful deductions. So data coming has to be processed such that they can
give a better picture of the situation.

Also, if you’ve checked our entry out, you’ll notice that the values are
updated every 3 seconds. This was to show that it was realtime. This kind of
measurements are usually measured every X minutes/hours. We sped it up for
presentation.

So we had Friday night until Saturday noon to build this. My awesome partner
[Kat Padi](http://katpadi.ph/) did the dummy REST APIs in PHP while I worked
on the frontend using React and jQuery. (I just realized that React was really
good for prototyping things.) It was a relatively easy simple app so Kat was
able to go back her apartment near the venue and I was able to sleep with the
beanbags there at around 3am. Added the finishing touches after breakfast and
we were done.

One of the things I’ve learned from the other hackathons I’ve been too is to
plan for the smallest feature set you’d be happy with and make it as polished
looking as you can. Another one is to use the tools you’re already comfortable
with. Don’t go playing around with some tech that seems to be the perfect fit
for what you’re building if you have nil experience about it. Use something
you know well. This was Kat’s first hackathon so I was telling her about these
tips sounding like an old veteran :P

[![BnQox5iCMAAlQux.jpg](https://svbtleusercontent.com/jvtgzayqigndla_small.jpg
)](https://svbtleusercontent.com/jvtgzayqigndla.jpg)
[![BnQoyJOCMAAs4Yx.jpg](https://svbtleusercontent.com/dwkwc3kjvjeq2a_small.jpg
)](https://svbtleusercontent.com/dwkwc3kjvjeq2a.jpg)

Both of us presented our entry. Kat did the intro and overview while I talked
about the details and our motivation. Got a couple of questions from the
judges which we fortunately didn’t have issues answering. Then we waited
patiently for judging…

In 3rd place was “Fans of katpadi” (Yep. My partner had a team named after
her). They built ERPAT which did building permit assessment and tracking.

In 2nd place was “DE”. My colleagues at Insync, Justin and Ted, built a mobile
app and API that enables surveyors to quickly assess structural integrity of
buildings.

And we won first place! Moom Manes! (Was also our team name. Haha.)

[![2014-05-10 17.59.13.jpg](https://svbtleusercontent.com/cuul4cggmw8bq_small.
jpg)](https://svbtleusercontent.com/cuul4cggmw8bq.jpg)

Got a grant from USAID and some good goodies from GDG and Globe Labs. Another
fun hackathon experience. There will be more for this year but this was
definitely an awesome first one.

[![BnQ73icCcAAQ1_w.jpg](https://svbtleusercontent.com/ywbt4omfrpw5ja_small.jpg
)](https://svbtleusercontent.com/ywbt4omfrpw5ja.jpg)

_Credits to @globelabs for all photos except for the one with just me and Kat_
