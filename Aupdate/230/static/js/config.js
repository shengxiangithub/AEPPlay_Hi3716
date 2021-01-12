
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

function G4_set(t) {
    var e = !1, n = !0;
    "1" == t && (n = !(e = !0)), $("#G41").prop("checked", e), $("#G42").prop("checked", n)
}

function G4_read() {
    return $("#G41").prop("checked") ? "1" : "2"
}

function logout() {
    ShowTip("正在注销", "loading", 2e3), window.location.href = "login.html"
}

function btnsave() {
    u = "/btnsave.do", ShowTip("正在保存数据", "loading", 2e3);
    var t = {};
    t.ip = $("#tx_ip").val(), t.ipmask = $("#tx_ipmask").val(), t.gateway = $("#tx_gateway").val(), t.dns1=$("#tx_dns1").val(),t.dns2=$("#tx_dns2").val(),
            t.mac = $("#tx_mac").val(), t.g4en = G4_read(), t.mqttep = $("#tx_mqtt_addr").val(), t.mqttpass = $("#tx_mqtt_pass").val(), t.despass = $("#tx_des_pass").val(), t.productid = $("#tx_productid").val(), t.apnname = $("#tx_apn_name").val(), t.apnuser = $("#tx_apn_user").val(), t.apnpass = $("#tx_apn_pass").val(), t.sn = $("#tx_logic").val(), t = JSON.stringify(t), $.ajax({
        type: "post",
        url: u,
        data: t,
        dataType: "json",
        contentType: "json",
        success: function (t) {
            var e = t.s;
            0 == e ? ShowTip("保存数据成功", "ok", 2e3) : 2018 == e ? (window.location.href = "/login.html") : ShowTip(t.c, "w")
        },
        error: function (t) {
            console.log(t), ShowTip("未知错误", "w", 2e3)
        }
    })
}


function btnquery() {
    //todo
    u = "/btnquery.do", ShowTip("正在获取数据", "loading", 2e3);
    var t = {opt: "q"};
    t = JSON.stringify(t), $.ajax({
        type: "post",
        url: u,
        data: t,
        dataType: "json",
        contentType: "json",
        success: function (t) {
            var e = t.s;
            0 == e ? (ShowTip("获取数据成功", "ok", 2e3), $("#tx_ip").val(t.ip), $("#tx_ipmask").val(t.ipmask), $("#tx_gateway").val(t.gateway),
                $("#tx_dns1").val(t.dns1),$("#tx_dns2").val(t.dns2),
                $("#tx_mac").val(t.mac), G4_set(t.g4en), $("#tx_mqtt_addr").val(t.mqttep), $("#tx_mqtt_pass").val(t.mqttpass), $("#tx_des_pass").val(t.despass), $("#tx_productid").val(t.productid), $("#tx_logic").val(t.sn), $("#tx_apn_name").val(t.apnname), $("#tx_apn_user").val(t.apnuser), $("#tx_apn_pass").val(t.apnpass), $("#tx_ver").text(t.ver)) : 2018 == e ? window.location.href = "/login.html" : ShowTip(t.c, "w")
        },
        error: function (t) {
            console.log(t), ShowTip("未知错误", "w", 2e3)
        }
    })
}

function btnreboot() {
    u = "/btnreboot.do", ShowTip("正在提交命令", "loading", 2e3);
    var t = {opt: "reboot"};
    t = JSON.stringify(t), $.ajax({
        type: "post",
        url: u,
        data: t,
        dataType: "json",
        contentType: "json",
        success: function (t) {
            var e = t.s;
            0 == e ? ShowTip("命令成功下发,请稍后", "ok", 2e3) : ShowTip("命令下发失败，请重试", "ok", 2e3)
        },
        error: function (t) {
            console.log(t), ShowTip("未知错误", "w", 2e3)
        }
    })
}


function getQueryVariable(variable) {
    var query = window.location.search.substring(1);
    var vars = query.split("&");
    for (var i = 0; i < vars.length; i++) {
        var pair = vars[i].split("=");
        if (pair[0] == variable) {
            return pair[1];
        }
    }
    return (false);
}


window.onload = function () {
    randomNum = getQueryVariable("randomNum");
    //alert(randomNum);
    var t = {"num": randomNum};
    t = JSON.stringify(t)
    $.ajax({
        type: "post",
        url: "/config.do",
        data: t,
        dataType: "json",
        contentType: "json",
        success: function (t) {
            0 == t.s ? btnquery() : window.location.href = "/login.html";
        },
        error: function (t) {
            //console.log(t)
            alert("网络异常");
        }
    })
}
