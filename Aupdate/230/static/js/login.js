var __showtime = 0;

function ShowTip(t, e) {
    var n = $("#loading");
    if (0 == n.length) {
        n = $('<div id="loading"><table><tr><td><img id="loadingimage" src="./img/1.png" alt="loading.." /></td><td id="loadingtxt">Loading content, please wait..</td></tr></table></div>'), $("body").append(n)
    }
    $("#loadingtxt").text(t);
    var r = 2e3;
    "ok" == e ? $("#loadingimage").attr("src", "./img/1.png") : "loading" == e ? ($("#loadingimage").attr("src", "./img/2.gif"), r = 1e4) : "w" == e ? $("#loadingimage").attr("src", "/img/4.png") : $("#loadingimage").attr("src", "./res/3.png"), clearTimeout(__showtime), n.show();
    __showtime = setTimeout(function () {
        n.hide()
    }, r)
}

function btnlogin() {
    u = "/login.do", ShowTip("正在获取数据", "ok", 2e3);
    var t = {};
    t.u = $("#Username").val(), t.p = $("#Password").val(), t.opt = "login", t.opt = "login", t = JSON.stringify(t), $.ajax({
        type: "post",
        url: u,
        data: t,
        dataType: "json",
        contentType: "json",
        success: function (t) {
            0 == t.s ? (window.location.href = "/config.html?randomNum=" + t.randomNum) : ShowTip(t.errmsg, "w")
        },
        error: function (t) {
            //console.log(t)
            alert("网络异常")
        }
    })
}


function RefreshPage() {
    location.href = document.location.href
}
