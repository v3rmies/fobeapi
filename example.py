import fobeapi
cookie = "yourFobeCookie"
userid = 2
onlineStatus = fobeapi.is_online(userid, cookie)
print(onlineStatus)
