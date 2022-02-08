from Instagram import Instagram
import os

EMAIL = "ksetty12@gmail.com"
PASSW = os.environ.get("INSTA_PASS")
target = "https://www.instagram.com/selenagomez/"

inst = Instagram()
inst.login(EMAIL, PASSW)
inst.followers(target)