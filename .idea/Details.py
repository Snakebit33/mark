class Details(object):
    username = ('markselezenev@gmail.com')
    password = ('12345678')
    website = ('https://www.imdb.com/chart/top?ref_=nv_mv_250_6')

    Sort = ('sort')
    URvalue = ('nv:descending')
    Movie1 =('.//tbody[contains(@class,"lister-list")]/tr[1]/td[2]/a[1]')
    Movie2 = ('.//tbody[contains(@class,"lister-list")]/tr[2]/td[2]/a[1]')
    Movie3 = ('.//tbody[contains(@class,"lister-list")]/tr[3]/td[2]/a[1]')
    Number = ('.//div[contains(@class,"imdbRating")]/a[1]/span[1]')

    Lusername = ('ap_email')
    Lpassword = ('ap_password')
    Login = ('signInSubmit')
    Sighin = ('Sign in')
    Sighin2 = ('Sign in with IMDb')

    Watchlist =('.//tbody[contains(@class,"lister-list")]/tr[1]/td[5]/div[1]/div[1]')
    title = ('Click to remove from watchlist')
    title2 = ('Click to add to watchlist')
    Movie = ('.//tbody[contains(@class,"lister-list")]/tr[1]/td[2]/a[1]')
    Wbutton = ('navWatchlistMenu')
    list =('Top Rated Movies')