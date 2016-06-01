document.addEventListener('DOMContentLoaded', function () {
  var bricks = Bricks({
    container: '.container',
    packed: 'data-packed',
    sizes: [
      { columns: 1, gutter: 16 },
      { mq: '856px', columns: 2, gutter: 8 },
      { mq: '1248px', columns: 3, gutter: 16 },
    ],
  })
  bricks.resize(true).pack()
  var images = document.querySelectorAll('img')
  for (var i = 0; i < images.length; i++) {
    images[i].addEventListener('load', function(e) {
      bricks.pack()
    })
  }
})

