---
publish_date: '2014-01-23'
title: Backing up Docker volumes
---

I remembered this morning how [Linode](https://www.linode.com/) now supports
Docker with their latest default kernel. OC-ness urges kicked in so I decided
to replace the custom kernel I was using with the new `3.12.6` one. Soon after
I rebooted my vm, I ssh’d back to it and ran `docker ps`. My mouth was wide
open as I stared at an empty list. Even `docker images` was displaying
nothing. Docker somehow broke after I switched to the new kernel. But wait, I
had backup! I previously did a `docker export` on my `ghost-mysql` container
so it should be fine. First I cleared out `/var/lib/docker` and re-installed
docker. Then, I ran `docker import` and checked its filesystem. Nope.
`/var/lib/mysql/ghost` wasn’t there. I headed to `#docker` looking for answers
and some good soul told me about how volumes are exempted from the container’s
filesystem when exported. He also gave me a tip: link the volume to the
container and tar it up. Which kinda looks like this if you do it from the
docker cli:

    
    
    #!/bin/bash
    sudo docker run -rm -i -volumes-from ghost-mysql ubuntu tar -cz /var/lib/mysql > ~/backups/ghost-mysql-`date +%s`.tgz
    

Good thing I suck at blogging and only have three measly posts. Also,
[Cloudflare](https://www.cloudflare.com/) was kind enough to cache my pages so
it was easy to bring them back up again. And now I know how to properly backup
my container volumes. All’s well that ends well.