$docsify.plugins = [].concat(function (i) {
    var e = Docsify.dom;
    i.mounted(function (i) {
        var n = e.create("div");
        n.id = "ad-container";
        var t = e.getNode("#main");
        n.style = "width: " + t.clientWidth + "px; margin: 0 auto 20px; ", e.appendTo(e.find(".content"), n)
    }),
    i.afterEach(function (i) {
        // var text1="广告位："
        return i
        // + text1
        + '<script>google_sl_win = window.parent; google_iframe_start_time = new Date().getTime(); google_async_iframe_id = "aswift_0";</script>'
        + "<script>window.parent.google_sa_impl({ iframeWin: window, pubWin: window.parent, vars: window.parent['google_sv_map']['aswift_0'] });</script>"
        + '<iframe frameborder="1" width="'
        + e.getNode("#main").clientWidth
        + '" height="93"'
        + ' id="google_ads_frame1" name="google_ads_frame1" sandbox="allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" frameborder="0" src="https://googleads.g.doubleclick.net/pagead/ads?client=ca-pub-1076724771190722&amp;output=html&amp;h=103&amp;slotname=3967051353&amp;adk=959199999&amp;adf=1842464052&amp;w='
        + e.getNode("#main").clientWidth
        + '&amp;lmt=1584646796&amp;rafmt=11&amp;psa=1&amp;guci=2.2.0.0.2.2.0.0&amp;format=1010x103&amp;url=https%3A%2F%2Fblog.csdn.net%2Fu011467553%2Farticle%2Fdetails%2F103889411&amp;flash=29.0.0&amp;wgl=1&amp;adsid=ChAI8LDM8wUQ3L3swaaA2tN3EkgA2qGmH11FgjjBT3MU5m53gBeAmprA10UbjqGP0h9ZjHTP-ueEud8uXS--0P4uXVGa3MsBNg6RFwFn4U5txNvJtXHimEfqFgQ&amp;dt=1584646794732&amp;bpp=49&amp;bdt=2435&amp;fdt=1826&amp;idt=1827&amp;shv=r20200316&amp;cbv=r20190131&amp;ptt=9&amp;saldr=aa&amp;abxe=1&amp;cookie=ID%3D404359d0ddae9a5d%3AT%3D1580188789%3AS%3DALNI_MZ8Fbj6d_HK8byvFJ6m4L1Ti3HYQA&amp;crv=1&amp;correlator=6176698164524&amp;frm=20&amp;pv=2&amp;ga_vid=660360905.1584646797&amp;ga_sid=1584646797&amp;ga_hid=2102603062&amp;ga_fc=0&amp;iag=0&amp;icsg=550838643330&amp;dssz=37&amp;mdo=0&amp;mso=8&amp;u_tz=480&amp;u_his=1&amp;u_java=0&amp;u_h=1080&amp;u_w=1920&amp;u_ah=1030&amp;u_aw=1920&amp;u_cd=24&amp;u_nplug=16&amp;u_nmime=33&amp;adx=387&amp;ady=5037&amp;biw=1519&amp;bih=361&amp;scr_x=0&amp;scr_y=4912&amp;eid=410075105%2C423550201&amp;oid=2&amp;pg_h=8942&amp;pvsid=3647494960823883&amp;pem=45&amp;ref=https%3A%2F%2Fblog.csdn.net%2Fu011467553&amp;rx=0&amp;eae=0&amp;fc=896&amp;brdim=0%2C0%2C0%2C0%2C1920%2C0%2C1920%2C1030%2C1536%2C361&amp;vis=1&amp;rsz=%7C%7CpeE%7C&amp;abl=CS&amp;pfx=0&amp;fu=152&amp;bc=31&amp;jar=2020-03-14-02&amp;ifi=1&amp;uci=a!1&amp;fsb=1&amp;xpc=5MCKKpRz7z&amp;p=https%3A//blog.csdn.net&amp;dtd=1879" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allowfullscreen="true" data-google-container-id="a!1" data-google-query-id="CID5-Kqlp-gCFZlxYAodRsAFWQ" data-load-complete="true"></iframe>'
        // return i + text1 + '<iframe src="./.js/own/test_ad.html" id="iframe" src="index.html" frameborder="0"  style="border: 0px;"></iframe>'
    })
}, $docsify.plugins);